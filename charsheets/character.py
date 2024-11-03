""" Class to define a character"""

import sys
from string import ascii_uppercase
from typing import Any, Type

from charsheets.constants import Skill, Armour, WeaponType, Stat, Feat, Ability
from charsheets.char_class import CharClass
from charsheets.ability_score import AbilityScore
from charsheets.skill import CharacterSkill
from charsheets.weapon import Weapon
from charsheets.feat import get_feat, BaseFeat
from charsheets.ability import get_ability, BaseAbility
from charsheets.spells import Spells


#############################################################################
class Character:
    def __init__(self, pcm):
        self.pcm = pcm
        self.char_class: CharClass = CharClass(pcm.char_class)  # type: ignore
        self.level: int = self.pcm.level  # type: ignore
        self.species = self.pcm.species
        self.stats = {
            Stat.STRENGTH: AbilityScore(pcm.strength),
            Stat.DEXTERITY: AbilityScore(pcm.dexterity),
            Stat.CONSTITUTION: AbilityScore(pcm.constitution),
            Stat.INTELLIGENCE: AbilityScore(pcm.intelligence),
            Stat.WISDOM: AbilityScore(pcm.wisdom),
            Stat.CHARISMA: AbilityScore(pcm.charisma),
        }
        self.set_class_proficiency()
        self.skills: dict[Skill, CharacterSkill] = self.fill_skills(pcm.skill_proficiencies)
        self.armour: Armour = self.pcm.armour
        self.shield: bool = getattr(self.pcm, "shield", False)
        self.equipment: list[str] = getattr(self.pcm, "equipment", [])
        self.weapons: dict[WeaponType, Weapon] = self.get_weapons(self.pcm.weapons)
        self.feats = self.get_feats(self.pcm.feats)
        self.abilities = self.get_abilities(self.pcm.abilities)
        self.hp: int = 0
        self.background = self.pcm.origin
        self.speed: int = 30

    #########################################################################
    def get_feats(self, pcm_traits: set[Feat]) -> dict[Feat, Type[BaseFeat]]:
        result = {}
        for feat in pcm_traits:
            result[feat] = get_feat(feat)
        return result

    #########################################################################
    def get_abilities(self, pcm_abilities: set[Ability]) -> dict[Ability, Type[BaseAbility]]:
        result = {}
        for ability in pcm_abilities:
            result[ability] = get_ability(ability)
        return result

    #########################################################################
    @property
    def hit_dice(self) -> str:
        return f"{self.level}d{self.char_class.hit_dice}"

    #########################################################################
    @property
    def spell_save_dc(self) -> int:
        return 8 + self.spell_attack_bonus

    #########################################################################
    @property
    def perception(self):
        return 10 + self.stats[Stat.WISDOM].modifier

    #########################################################################
    @property
    def spell_attack_bonus(self) -> int:
        bonus = self.proficiency_bonus
        bonus += self.stats[self.spell_casting_ability].modifier
        return bonus

    #########################################################################
    @property
    def spell_casting_ability(self) -> Stat:
        return self.char_class.spell_casting_ability

    #########################################################################
    def spell_slots(self, spell_level: int):
        return self.char_class.spell_slots(self.level)[spell_level - 1]  # -1 to 0 index

    #########################################################################
    @property
    def initiative(self) -> int:
        return self.stats[Stat.DEXTERITY].modifier + self.check_modifiers("initiative_bonus")

    #########################################################################
    @property
    def proficiency_bonus(self) -> int:
        return int((self.level - 1) / 4) + 2

    #########################################################################
    @property
    def ac(self) -> int:
        ac = 10
        if self.armour == Armour.LEATHER:
            ac = 11 + self.stats[Stat.DEXTERITY].modifier
        if self.shield:
            ac += 2
        return ac

    #########################################################################
    def spells(self, spell_level: int) -> list[tuple[str, Spells]]:
        ans = []
        if self.spell_slots(spell_level):
            for num, spell in enumerate(self.char_class.spells(spell_level)):
                ans.append((ascii_uppercase[num], spell))
        return ans

    #########################################################################
    def ranged_atk_bonus(self) -> int:
        return self.check_modifiers("ranged_atk_bonus")

    #########################################################################
    def melee_atk_bonus(self) -> int:
        return self.check_modifiers("melee_atk_bonus")

    #########################################################################
    def check_modifiers(self, modifier: str) -> int:
        """Check everything that can modify a value"""
        bonus = 0
        for feat in self.feats.values():
            if hasattr(feat, modifier):
                bonus += getattr(feat, modifier)(self)
        for ability in self.abilities.values():
            if hasattr(ability, modifier):
                bonus += getattr(ability, modifier)(self)
        return bonus

    #########################################################################
    def set_class_proficiency(self) -> None:
        for stat in Stat:
            self.stats[stat].proficient = int(self.char_class.stat_proficiency(stat))

    #########################################################################
    def __getattr__(self, item: str) -> Any:
        """Guess what they are asking for"""
        # Try a skill
        try:
            skill = Skill(item.lower())
            return self.skills[skill]
        except ValueError:
            pass

        # Try Stat
        try:
            return self.stats[Stat(item.lower())]
        except ValueError:
            pass

        # Try anything mentioned in the pcm
        try:
            ans = getattr(self.pcm, item)
            return ans
        except AttributeError:
            pass

        print(f"DBG Unknown __getattr__({item=})", file=sys.stderr)
        return "unknown"

    #############################################################################
    def fill_skills(self, proficiencies: set[Skill]) -> dict[Skill, CharacterSkill]:
        skills = {}
        p = proficiencies
        pb = self.proficiency_bonus
        for skill in (Skill.ATHLETICS,):
            skills[skill] = CharacterSkill(self.stats[Stat.STRENGTH], pb, skill in p)
        for skill in (Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND, Skill.STEALTH):
            skills[skill] = CharacterSkill(self.stats[Stat.DEXTERITY], pb, skill in p)

        for skill in (Skill.ARCANA, Skill.HISTORY, Skill.INVESTIGATION, Skill.NATURE, Skill.RELIGION):
            skills[skill] = CharacterSkill(self.stats[Stat.INTELLIGENCE], pb, skill in p)

        for skill in (Skill.ANIMAL_HANDLING, Skill.INSIGHT, Skill.MEDICINE, Skill.PERCEPTION, Skill.SURVIVAL):
            skills[skill] = CharacterSkill(self.stats[Stat.WISDOM], pb, skill in p)

        for skill in (Skill.DECEPTION, Skill.INTIMIDATION, Skill.PERFORMANCE, Skill.PERSUASION):
            skills[skill] = CharacterSkill(self.stats[Stat.CHARISMA], pb, skill in p)

        return skills

    #############################################################################
    def get_weapons(self, weapons: set[WeaponType]) -> dict[WeaponType, Weapon]:
        tmp = {}
        for weapon_name in weapons:
            tmp[weapon_name] = Weapon(weapon_name, self)
        return tmp

    # EOF

""" Class to define a character"""

import sys
from typing import Any

from charsheets.constants import Skill, Armour, WeaponType, Stat, Feat
from charsheets.char_class import CharClass
from charsheets.ability_score import Ability
from charsheets.skill import CharacterSkill
from charsheets.weapon import Weapon
from charsheets.feat import get_feat


#############################################################################
class Character:
    def __init__(self, pcm):
        self.pcm = pcm
        self.char_class: CharClass = CharClass(pcm.char_class)  # type: ignore
        self.level: int = self.pcm.level  # type: ignore
        self.species = self.pcm.species
        self.stats = {
            Stat.STRENGTH: Ability(pcm.strength),
            Stat.DEXTERITY: Ability(pcm.dexterity),
            Stat.CONSTITUTION: Ability(pcm.constitution),
            Stat.INTELLIGENCE: Ability(pcm.intelligence),
            Stat.WISDOM: Ability(pcm.wisdom),
            Stat.CHARISMA: Ability(pcm.charisma),
        }
        self.set_class_proficiency()
        self.skills: dict[Skill, CharacterSkill] = self.fill_skills(pcm.skill_proficiencies)
        self.armour: Armour = self.pcm.armour
        self.shield: bool = getattr(self.pcm, "shield", False)
        self.equipment: list[str] = getattr(self.pcm, "equipment", [])
        self.weapons: dict[WeaponType, Weapon] = self.get_weapons(self.pcm.weapons)
        self.feats = self.get_feats(self.pcm.feats)
        self.hp: int = 0
        self.speed: int = 30

    #########################################################################
    def get_feats(self, pcm_traits: set[Feat]):
        result = {}
        for feat in pcm_traits:
            result[feat] = get_feat(feat)
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

""" Class to define a character"""

import sys
from string import ascii_uppercase
from typing import Any, Type, Optional

from charsheets.exception import UnhandledException
from charsheets.constants import Skill, Armour, WeaponType, Stat, Feat, Ability, Proficiencies, CharSubclassName
from charsheets.char_class import char_class_picker
from charsheets.ability_score import AbilityScore
from charsheets.skill import CharacterSkill
from charsheets.weapon import Weapon
from charsheets.feat import get_feat, BaseFeat
from charsheets.ability import get_ability, BaseAbility
from charsheets.spells import Spells
from charsheets.species import Species


#############################################################################
class Character:
    def __init__(self, pcm):
        self.pcm = pcm
        self.char_class: CharClass = char_class_picker(pcm.char_class, getattr(pcm, "char_subclass", CharSubclassName.NONE))  # type: ignore
        self.level: int = self.pcm.level  # type: ignore
        self.species = Species(self.pcm.species)
        self.stats = {
            Stat.STRENGTH: AbilityScore(pcm.strength),
            Stat.DEXTERITY: AbilityScore(pcm.dexterity),
            Stat.CONSTITUTION: AbilityScore(pcm.constitution),
            Stat.INTELLIGENCE: AbilityScore(pcm.intelligence),
            Stat.WISDOM: AbilityScore(pcm.wisdom),
            Stat.CHARISMA: AbilityScore(pcm.charisma),
        }
        self.set_saving_throw_proficiency()
        self.skills: dict[Skill, CharacterSkill] = self.fill_skills(getattr(pcm, "skill_proficiencies", set()))  # type: ignore
        self.armour: Armour = getattr(self.pcm, "armour", None)  # type: ignore
        self.shield: bool = getattr(self.pcm, "shield", False)
        self.equipment: list[str] = getattr(self.pcm, "equipment", [])
        self.weapons: dict[WeaponType, Weapon] = self.get_weapons(getattr(pcm, "weapons", set()))
        self.feats = self.get_feats(getattr(pcm, "feats", set()))
        self.abilities = self.get_abilities(getattr(self.pcm, "abilities", set()))
        self.hp: int = self.pcm.hp
        self.background = self.pcm.origin
        self.speed: int = 30

    #########################################################################
    @property
    def class_name(self) -> str:
        return self.char_class.name()

    #########################################################################
    def get_feats(self, pcm_traits: set[Feat]) -> dict[Feat, Type[BaseFeat]]:
        result = {}
        for feat in pcm_traits:
            result[feat] = get_feat(feat)
        return result

    #########################################################################
    def get_abilities(self, pcm_abilities: set[Ability]) -> dict[Ability, Type[BaseAbility]]:
        result = {}
        ability_list: set[Ability] = set()
        ability_list |= pcm_abilities
        ability_list |= self.char_class.class_abilities(self.level)
        ability_list |= self.species.species_abilities()
        for ability in ability_list:
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
    def spell_casting_ability(self) -> Optional[Stat]:
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
        match self.armour:
            case Armour.PADDED:
                ac = 11 + self.stats[Stat.DEXTERITY].modifier
            case Armour.LEATHER:
                ac = 11 + self.stats[Stat.DEXTERITY].modifier
            case Armour.STUDDED:
                ac = 12 + self.stats[Stat.DEXTERITY].modifier
            case Armour.SCALE:
                ac = 14 + max(2, self.stats[Stat.DEXTERITY].modifier)
            case None:
                ac = 10 + self.stats[Stat.DEXTERITY].modifier
            case _:
                raise UnhandledException(f"Unhandled armour {self.armour} in character.ac()")
        if self.shield:
            ac += 2
        return ac

    #########################################################################
    def half_spell_sheet(self) -> bool:
        """If we only have spells up to level 6 use a half sheet, otherwise we use a full sheet."""
        if self.spell_slots(6) == 0:
            return True
        return False

    #########################################################################
    def spells(self, spell_level: int) -> list[tuple[str, str]]:
        ans = []
        if self.spell_slots(spell_level) or spell_level == 0:
            for num, spell in enumerate(self.char_class.spells(spell_level)[: self.spell_display_limits(spell_level)]):
                ans.append((ascii_uppercase[num], spell.name))
        return ans

    #########################################################################
    def overflow_spells(self, spell_level: int) -> list[tuple[str, str]]:
        ans = [("A", "---- Overflow Spells ----")]
        count = 0
        limit = self.spell_display_limits(spell_level)
        for num in range(limit):
            try:
                ans.append((ascii_uppercase[num + 1], self.char_class.spells(spell_level)[num + limit].name))
                count += 1
            except IndexError:
                ans.append((ascii_uppercase[num + 1], ""))
        if count == 0:  # If no spells don't display overflow tag
            ans[0] = ("A", "")
        return ans

    #########################################################################
    def spell_display_limits(self, level: int) -> int:
        """How many spells we can display per level"""
        limits = {
            True: {0: 11, 1: 25, 2: 19, 3: 19, 4: 19, 5: 19},
            False: {0: 8, 1: 13, 2: 13, 3: 13, 4: 13, 5: 9, 6: 9, 7: 9, 8: 7, 9: 7},
        }
        return limits[self.half_spell_sheet()][level]

    #########################################################################
    def has_overflow_spells(self) -> bool:
        """Do we have more than a single page of spells"""

        for level in range(0, 10):
            if len(self.char_class.spells(level)) > self.spell_display_limits(level):
                return True
        return False

    #########################################################################
    def ranged_atk_bonus(self) -> int:
        return self.check_modifiers("ranged_atk_bonus")

    #########################################################################
    def melee_atk_bonus(self) -> int:
        return self.check_modifiers("melee_atk_bonus")

    #########################################################################
    def ranged_dmg_bonus(self) -> int:
        return self.check_modifiers("ranged_dmg_bonus")

    #########################################################################
    def melee_dmg_bonus(self) -> int:
        return self.check_modifiers("melee_dmg_bonus")

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
    def weapon_proficiencies(self) -> set[Proficiencies]:
        return self.char_class.weapon_proficiency()

    #########################################################################
    def armour_proficiencies(self) -> set[Proficiencies]:
        return self.char_class.armour_proficiency()

    #########################################################################
    def set_saving_throw_proficiency(self) -> None:
        for stat in Stat:
            self.stats[stat].proficient = int(self.char_class.saving_throw_proficiency(stat))

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
        tmp[WeaponType.UNARMED] = Weapon(WeaponType.UNARMED, self)
        return tmp

    # EOF

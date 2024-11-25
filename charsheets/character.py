""" Class to define a character"""

import sys
from string import ascii_uppercase
from typing import Any, Type, Optional

from charsheets.ability_score import AbilityScore

from charsheets.constants import Skill, Armour, Stat, Feat, Proficiencies, CharSpecies, Weapon, Origin, SKILL_STAT_MAP, Ability
from charsheets.exception import UnhandledException
from charsheets.origin import origin_picker
from charsheets.skill import CharacterSkill
from charsheets.reason import Reason
from charsheets.species import Species
from charsheets.weapon import BaseWeapon, weapon_picker


#############################################################################
class Character:
    def __init__(self, name: str, origin: Origin, species: CharSpecies, skill1: Skill, skill2: Skill, **kwargs: Any):
        self.name = name
        self.player_name = "<Undefined>"
        self.level = 1
        self.origin = origin_picker(origin)
        self.species = Species(species)
        self.hp = self.hit_dice
        self.stats = {
            Stat.STRENGTH: AbilityScore(kwargs.get("strength", 0)),
            Stat.DEXTERITY: AbilityScore(kwargs.get("dexterity", 0)),
            Stat.CONSTITUTION: AbilityScore(kwargs.get("constitution", 0)),
            Stat.INTELLIGENCE: AbilityScore(kwargs.get("intelligence", 0)),
            Stat.WISDOM: AbilityScore(kwargs.get("wisdom", 0)),
            Stat.CHARISMA: AbilityScore(kwargs.get("charisma", 0)),
        }
        self.extras: dict[str, Any] = {}
        self.feats: set[Feat] = set()
        self.armour = Armour.NONE
        self.shield = False
        self.weapons: set[BaseWeapon] = set()
        self.weight = 0
        self.capacity = 0
        self.class_skills: set[Skill] = {skill1, skill2}
        self.skills: dict[Skill, CharacterSkill] = self.fill_skills()
        self.feats.add(self.origin.origin_feat)
        self.languages: set[str] = set()
        self.abilities: set[Ability] = set()
        self.equipment: list[str] = []
        self.set_saving_throw_proficiency()

    #########################################################################
    def add_weapon(self, weapon: Weapon):
        self.weapons.add(weapon_picker(weapon, self))

    #########################################################################
    def add_equipment(self, *items):
        if isinstance(items, str):
            self.equipment.append(items)
        else:
            self.equipment.extend(items)

    #########################################################################
    @property
    def class_name(self) -> str:
        return self.__class__.__name__

    #########################################################################
    @property
    def hit_dice(self) -> int:
        raise NotImplemented

    #########################################################################
    def add_level(self, hp=0):
        self.hp += max(1, hp + self.stats[Stat.CONSTITUTION].modifier)
        self.level += 1

    #########################################################################
    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    #########################################################################
    def __getattr__(self, item: str) -> Any:
        """Guess what they are asking for"""
        if item in self.extras:
            return self.extras[item]
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

        print(f"DBG Unknown __getattr__({item=})", file=sys.stderr)
        return "unknown"

    #########################################################################
    @property
    def speed(self) -> int:
        if self.species.char_species == CharSpecies.GOLIATH:
            return 35

        return 30

    #########################################################################
    @property
    def max_hit_dice(self) -> str:
        return f"{self.level}d{self.hit_dice}"

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
        if self.spell_casting_ability:
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
    def initiative(self) -> Reason:
        result = Reason("dex", self.stats[Stat.DEXTERITY].modifier)
        result.extend(self.check_modifiers("initiative_bonus"))
        return result

    #########################################################################
    @property
    def proficiency_bonus(self) -> int:
        return int((self.level - 1) / 4) + 2

    #########################################################################
    @property
    def ac(self) -> Reason:
        result = Reason()
        match self.armour:
            case Armour.PADDED:
                result.add("padded", 11)
                result.add("dex_modifier", self.stats[Stat.DEXTERITY].modifier)
            case Armour.LEATHER:
                result.add("leather", 11)
                result.add("dex_modifier", self.stats[Stat.DEXTERITY].modifier)
            case Armour.STUDDED:
                result.add("studded", 12)
                result.add("dex_modifier", self.stats[Stat.DEXTERITY].modifier)
            case Armour.SCALE:
                result.add("scale", 14)
                result.add("dex_modifier", max(2, self.stats[Stat.DEXTERITY].modifier))
            case Armour.RING:
                result.add("ring", 14)
            case Armour.CHAIN:
                result.add("chain", 16)
            case Armour.SPLINT:
                result.add("splint", 17)
            case Armour.PLATE:
                result.add("planet", 168)
            case Armour.NONE:
                result.add("none", 14)
                result.add("dex mod", self.stats[Stat.DEXTERITY].modifier)
            case _:
                raise UnhandledException(f"Unhandled armour {self.armour} in character.ac()")
        if self.shield:
            result.add("shield", 2)
        result.extend(self.check_modifiers("ac_bonus"))
        return result

    #########################################################################
    def max_spell_level(self, char_level: int) -> int:
        return self.char_class.max_spell_level(char_level)

    #########################################################################
    def half_spell_sheet(self) -> bool:
        """If we only have spells up to level 6 use a half sheet, otherwise we use a full sheet."""
        if self.spell_slots(6) == 0:
            return True
        return False

    #########################################################################
    def spells(self, spell_level: int) -> list[tuple[str, str]]:
        ans = []
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
            True: {0: 11, 1: 25, 2: 19, 3: 19, 4: 19, 5: 19, 6: 0, 7: 0, 8: 0, 9: 0},
            False: {0: 8, 1: 13, 2: 13, 3: 13, 4: 13, 5: 9, 6: 9, 7: 9, 8: 7, 9: 7},
        }
        return limits[self.half_spell_sheet()][level]

    #########################################################################
    def has_overflow_spells(self) -> bool:
        """Do we have more than a single page of spells"""

        for spell_level in range(0, 10):
            if len(self.char_class.spells(spell_level)) > self.spell_display_limits(spell_level):
                return True
        return False

    #########################################################################
    def ranged_atk_bonus(self) -> Reason:
        result = Reason("prof_bonus", self.proficiency_bonus)
        result.add("dex mod", self.dexterity.modifier)
        return result

    #########################################################################
    def melee_atk_bonus(self) -> Reason:
        result = Reason("prof_bonus", self.proficiency_bonus)
        result.add("str mod", self.strength.modifier)
        return result

    #########################################################################
    def ranged_dmg_bonus(self) -> Reason:
        return Reason("dex mod", self.dexterity.modifier)

    #########################################################################
    def melee_dmg_bonus(self) -> Reason:
        return Reason("str mod", self.strength.modifier)

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        """Check everything that can modify a value"""
        result = Reason()
        for feat in self.feats:
            if hasattr(feat, modifier):
                result.add(f"feat {feat}", getattr(feat, modifier)(self))
        for ability in self.abilities:
            if hasattr(ability, modifier):
                result.add(f"ability {ability}", getattr(ability, modifier)(self))
        return result

    #########################################################################
    def weapon_proficiencies(self) -> set[Proficiencies]:
        return self.weapon_proficiency()

    #########################################################################
    def armour_proficiencies(self) -> set[Proficiencies]:
        return self.armour_proficiency()

    #########################################################################
    def set_saving_throw_proficiency(self) -> None:
        for stat in Stat:
            self.stats[stat].proficient = int(self.saving_throw_proficiency(stat))

    #############################################################################
    @property
    def other_proficiencies(self) -> list[str]:
        proficiencies = self.extras.get("other_proficiencies", [])
        proficiencies.append(self.origin.tool_proficiency)
        return proficiencies

    #############################################################################
    def fill_skills(self) -> dict[Skill, CharacterSkill]:
        skills = {}
        origin_proficiencies = self.origin.proficiencies
        p = self.class_skills | origin_proficiencies
        pb = self.proficiency_bonus

        for skill, stat in SKILL_STAT_MAP.items():
            if skill in p:
                if skill in origin_proficiencies:
                    origin = f"{self.origin}"
                if skill in self.class_skills:
                    origin = f"{self.class_name}"
            else:
                origin = ""
            skills[skill] = CharacterSkill(self.stats[stat], pb, int(skill in p), origin)

        return skills

    # EOF

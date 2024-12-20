""" Class to define a character"""

import sys
from string import ascii_uppercase
from typing import Any, Optional

from charsheets.ability_score import AbilityScore

from charsheets.constants import (
    Skill,
    Ability,
    Armour,
    Stat,
    Feat,
    Proficiencies,
    Weapon,
    Origin,
    SKILL_STAT_MAP,
    DamageType,
    Movements,
)
from charsheets.attack import Attack
from charsheets.exception import UnhandledException
from charsheets.origin import origin_picker
from charsheets.skill import CharacterSkill
from charsheets.reason import Reason
from charsheets.species import Species
from charsheets.spells import Spells, SPELL_LEVELS
from charsheets.weapon import BaseWeapon, weapon_picker
from charsheets.ability import BaseAbility, get_ability
from charsheets.feat import get_feat, BaseFeat


#############################################################################
class Character:
    def __init__(self, name: str, origin: Origin, species: Species, skill1: Skill, skill2: Skill, **kwargs: Any):
        self.name = name
        self._class_name = ""
        self.player_name = "<Undefined>"
        self.level = 1
        self.origin = origin_picker(origin)
        self.species = species
        self.species.character = self  # type: ignore
        self.stats = {
            Stat.STRENGTH: AbilityScore(self, kwargs.get("strength", 0)),  # type: ignore
            Stat.DEXTERITY: AbilityScore(self, kwargs.get("dexterity", 0)),  # type: ignore
            Stat.CONSTITUTION: AbilityScore(self, kwargs.get("constitution", 0)),  # type: ignore
            Stat.INTELLIGENCE: AbilityScore(self, kwargs.get("intelligence", 0)),  # type: ignore
            Stat.WISDOM: AbilityScore(self, kwargs.get("wisdom", 0)),  # type: ignore
            Stat.CHARISMA: AbilityScore(self, kwargs.get("charisma", 0)),  # type: ignore
        }
        self._hp: list[int] = []
        self.extras: dict[str, Any] = {}
        self.feats_list: set[Feat] = set()
        self.armour = Armour.NONE
        self.shield = False
        self.weapons: set[BaseWeapon] = {weapon_picker(Weapon.UNARMED, self)}  # type: ignore
        self._class_skills: set[Skill] = {skill1, skill2}
        self.feats_list.add(self.origin.origin_feat)
        self.languages: set[str] = set()
        self.equipment: list[str] = []
        self.set_saving_throw_proficiency()
        self._known_spells: set[Spells] = set()
        self._damage_resistances: set[DamageType] = set()
        self._prepared_spells: set[Spells] = set()
        self._attacks: set[Attack] = set()
        self._abilities: set[Ability] = set()

    #########################################################################
    @property
    def hp(self) -> int:
        return self.hit_dice + sum(self._hp) + self.level * self.stats[Stat.CONSTITUTION].modifier

    #########################################################################
    @property
    def class_special(self) -> str:
        return ""

    #############################################################################
    def class_abilities(self) -> set[Ability]:  # pragma: no coverage
        raise NotImplemented

    #########################################################################
    @property
    def additional_attacks(self) -> set[Attack]:
        return self._attacks | self.check_set_modifiers("mod_add_attack")

    #########################################################################
    def add_ability(self, new_ability: Ability):
        self._abilities.add(new_ability)

    #########################################################################
    @property
    def abilities(self) -> set[BaseAbility]:
        abils = set()
        abils |= self.class_abilities()
        abils |= self.species.species_abilities()
        abils |= self._abilities
        real_abils = set(get_ability(_) for _ in abils)
        return real_abils

    #########################################################################
    @property
    def feats(self) -> set[BaseFeat]:
        """Return a set of the actual Feats (not the labels)"""
        return set(get_feat(_) for _ in self.feats_list)

    #########################################################################
    @property
    def damage_resistances(self) -> set[DamageType]:
        return self._damage_resistances | self.check_set_modifiers("mod_add_damage_resistances")

    #########################################################################
    def add_damage_resistance(self, dmg_type: DamageType):
        self._damage_resistances.add(dmg_type)

    #########################################################################
    def add_weapon(self, weapon: Weapon):
        self.weapons.add(weapon_picker(weapon, self))  # type: ignore

    #########################################################################
    def add_equipment(self, *items):
        if isinstance(items, str):
            self.equipment.append(items)
        else:
            self.equipment.extend(items)

    #########################################################################
    @property
    def class_name(self) -> str:
        if self._class_name:
            return self._class_name
        return self.__class__.__name__

    #########################################################################
    @property
    def hit_dice(self) -> int:  # pragma: no coverage
        raise NotImplemented

    #########################################################################
    def add_level(self, hp=0):
        self._hp.append(hp)
        self.level += 1

    #########################################################################
    def __repr__(self):
        return f"{self.class_name}: {self.name}"

    #########################################################################
    def __getattr__(self, item: str) -> Any:
        """Guess what they are asking for"""
        if item in self.extras:
            return self.extras[item]
        # Try a skill
        try:
            skill = Skill(item.lower())
            return self.lookup_skill(skill)
        except ValueError:
            pass

        # Try Stat
        try:
            return self.stats[Stat(item.lower())]
        except ValueError:
            pass

        # print(f"DBG Unknown __getattr__({item=})", file=sys.stderr)
        return "unknown"

    #########################################################################
    @property
    def movements(self) -> dict[Movements, Reason]:
        moves = {
            Movements.SPEED: Reason("Species", self.species.speed),
            Movements.FLY: self.check_modifiers("mod_fly_movement"),
            Movements.SWIM: self.check_modifiers("mod_swim_movement"),
        }
        return moves

    #########################################################################
    @property
    def speed(self) -> Reason:
        return self.movements[Movements.SPEED]

    #########################################################################
    @property
    def fly_speed(self) -> Reason:
        return self.movements[Movements.FLY]

    #########################################################################
    @property
    def swim_speed(self) -> Reason:
        return self.movements[Movements.SWIM]

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
        bonus = 0
        if self.spell_casting_ability:
            bonus = self.proficiency_bonus + self.stats[self.spell_casting_ability].modifier
        return bonus

    #########################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:  # pragma: no coverage
        raise NotImplemented

    #########################################################################
    def spell_slots(self, spell_level: int) -> int:
        """How many spell slots we have for the spell_level"""
        # Override on spell caster classes
        return 0

    #########################################################################
    @property
    def initiative(self) -> Reason:
        result = Reason("dex", self.stats[Stat.DEXTERITY].modifier)
        result.extend(self.check_modifiers("mod_initiative_bonus"))
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
            case Armour.HIDE:
                result.add("hide", 12)
                result.add("dex_modifier", min(2, self.stats[Stat.DEXTERITY].modifier))
            case Armour.CHAIN:
                result.add("chain", 13)
                result.add("dex_modifier", min(2, self.stats[Stat.DEXTERITY].modifier))
            case Armour.SCALE:
                result.add("scale", 14)
                result.add("dex_modifier", min(2, self.stats[Stat.DEXTERITY].modifier))
            case Armour.BREASTPLATE:
                result.add("breastplate", 14)
                result.add("dex_modifier", min(2, self.stats[Stat.DEXTERITY].modifier))
            case Armour.HALFPLATE:
                result.add("halfplate", 15)
                result.add("dex_modifier", min(2, self.stats[Stat.DEXTERITY].modifier))
            case Armour.SCALE:
                result.add("scale", 14)
                result.add("dex_modifier", min(2, self.stats[Stat.DEXTERITY].modifier))
            case Armour.RING:
                result.add("ring", 14)
            case Armour.CHAIN:
                result.add("chain", 16)
            case Armour.SPLINT:
                result.add("splint", 17)
            case Armour.PLATE:
                result.add("plate", 18)
            case Armour.NONE:
                result.add("none", 10)
                result.add("dex mod", self.stats[Stat.DEXTERITY].modifier)
            case _:
                raise UnhandledException(f"Unhandled armour {self.armour} in character.ac()")
        if self.shield:
            result.add("shield", 2)
        result.extend(self.check_modifiers("mod_ac_bonus"))
        return result

    #########################################################################
    def max_spell_level(self) -> int:
        return self.max_spell_level()

    #########################################################################
    def half_spell_sheet(self) -> bool:
        """If we only have spells up to level 6 use a half sheet, otherwise we use a full sheet."""
        if self.spell_slots(6) == 0:
            return True
        return False

    #########################################################################
    def level_spells(self, spell_level: int) -> list[tuple[str, bool, str]]:
        """List of spells of spell_level (and an A-Z prefix) known - for display purposes"""
        ans = []
        for num, spell in enumerate(self.spells_of_level(spell_level)[: self.spell_display_limits(spell_level)]):
            prepared = spell in self.prepared_spells
            ans.append((ascii_uppercase[num], prepared, spell.name.title()))
        return ans

    #########################################################################
    def overflow_level_spells(self, spell_level: int) -> list[tuple[str, bool, str]]:
        ans = [("A", False, "---- Overflow Spells ----")]
        count = 0
        limit = self.spell_display_limits(spell_level)
        for num in range(limit):
            try:
                spell = self.spells_of_level(spell_level)[num + limit]
                prepared = spell in self.prepared_spells
                ans.append((ascii_uppercase[num + 1], prepared, spell.name.title()))
                count += 1
            except IndexError:
                ans.append((ascii_uppercase[num + 1], False, ""))
        if count == 0:  # If no spells don't display overflow tag
            ans[0] = ("A", False, "")
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
            if len(self.spells_of_level(spell_level)) > self.spell_display_limits(spell_level):
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
        # print(f"DBG character.check_modifiers {modifier=}", file=sys.stderr)

        result = Reason()
        # Feat modifiers
        for feat in self.feats:
            if hasattr(feat, modifier):
                result.add(f"feat {feat}", getattr(feat, modifier)(self))
        # Ability modifiers
        for ability in self.abilities:
            if hasattr(ability, modifier):
                result.add(f"ability {ability.tag}", getattr(ability, modifier)(self=ability, character=self))
        # Character class modifier
        if hasattr(self, modifier) and callable(getattr(self, modifier)):
            result.extend(getattr(self, modifier)(self))
        # Species modifier
        if hasattr(self.species, modifier):
            result.extend(getattr(self.species, modifier)(self))
        return result

    #########################################################################
    def check_set_modifiers(self, modifier: str) -> set[Any]:
        """Check everything that can modify a set"""
        # print(f"DBG character.check_set_modifiers {modifier=}", file=sys.stderr)

        result = set()
        # Feat modifiers
        for feat in self.feats:
            if hasattr(feat, modifier):
                result |= getattr(feat, modifier)(character=self)
        # Ability modifiers
        for ability in self.abilities:
            if hasattr(ability, modifier):
                # print(f"DBG {ability=} {modifier=} {getattr(ability, modifier)=}", file=sys.stderr)
                result |= getattr(ability, modifier)(self=ability, character=self)
        # Character class modifier
        if hasattr(self, modifier) and callable(getattr(self, modifier)):
            # print(f"DBG {self=} {modifier=} {getattr(self, modifier)=}", file=sys.stderr)
            result |= getattr(self, modifier)(character=self)
        # Species modifier
        if hasattr(self.species, modifier):
            result |= getattr(self.species, modifier)(character=self)
        return result

    #########################################################################
    def weapon_proficiencies(self) -> set[Proficiencies]:
        return self.weapon_proficiency() | self.check_set_modifiers("mod_weapon_proficiency")

    #########################################################################
    def armour_proficiencies(self) -> set[Proficiencies]:
        return self.armour_proficiency() | self.check_set_modifiers("mod_armour_proficiency")

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
    def spells_of_level(self, spell_level: int) -> list[Spells]:
        """Return list of spells known at spell_level"""
        result = []
        for spell in self.known_spells:
            if SPELL_LEVELS[spell] == spell_level:
                result.append(spell)
        return result

    #############################################################################
    def learn_spell(self, *spells: Spells):
        self._known_spells |= set(spells)

    #############################################################################
    @property
    def known_spells(self) -> set[Spells]:
        """What spells the character knows"""
        return (
            self._known_spells
            | self.check_set_modifiers("mod_add_known_spells")
            | self.check_set_modifiers("mod_add_prepared_spells")  # All prepared spells must be known
        )

    #############################################################################
    def prepare_spells(self, *spells: Spells):
        self._known_spells |= set(spells)
        self._prepared_spells |= set(spells)

    #############################################################################
    @property
    def prepared_spells(self) -> set[Spells]:
        """What spells the character has prepared"""
        return self._prepared_spells | self.check_set_modifiers("mod_add_prepared_spells")

    #############################################################################
    @property
    def skills(self) -> set[Skill]:
        return self._class_skills | self.origin.proficiencies | self.check_set_modifiers("mod_skills")

    #############################################################################
    def lookup_skill(self, skill: Skill) -> CharacterSkill:
        pb = self.proficiency_bonus
        proficient = int(skill in self.skills)

        origin = ""
        if skill in self.origin.proficiencies:
            origin = f"{self.origin}"
        if skill in self._class_skills:
            origin = f"{self.class_name}"
        return CharacterSkill(skill, self, proficient, origin)  # type: ignore

    #############################################################################
    def mod_add_attack(self, character: "Character") -> set[Attack]:
        return set()

    #############################################################################
    def mod_add_damage_resistances(self, character: "Character") -> set[DamageType]:
        return set()

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> set[Spells]:
        return set()

    #############################################################################
    def mod_add_prepared_spells(self, character: "Character") -> set[Spells]:
        return set()

    # EOF

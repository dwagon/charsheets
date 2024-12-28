""" Class to define a character"""

from string import ascii_uppercase
from typing import Any, Optional

from charsheets.ability import BaseAbility, get_ability
from charsheets.ability_score import AbilityScore
from charsheets.attack import Attack
from charsheets.constants import Skill, Ability, Armour, Stat, Feat, Proficiency, Weapon, DamageType, Movements, Mod, Tool
from charsheets.exception import UnhandledException
from charsheets.feats.base_feat import BaseFeat
from charsheets.origins.base_origin import BaseOrigin
from charsheets.reason import Reason
from charsheets.skill import CharacterSkill
from charsheets.species import Species
from charsheets.spells import Spells, SPELL_LEVELS
from charsheets.weapon import BaseWeapon, weapon_picker


#############################################################################
class Character:
    def __init__(self, name: str, origin: BaseOrigin, species: Species, skill1: Skill, skill2: Skill, **kwargs: Any):
        self.name = name
        self._class_name = ""
        self.player_name = "<Undefined>"
        self.level = 1
        self.origin = origin
        self.species = species
        self.species.character = self  # type: ignore
        self.stats = {
            Stat.STRENGTH: AbilityScore(Stat.STRENGTH, self, kwargs.get("strength", 0)),  # type: ignore
            Stat.DEXTERITY: AbilityScore(Stat.DEXTERITY, self, kwargs.get("dexterity", 0)),  # type: ignore
            Stat.CONSTITUTION: AbilityScore(Stat.CONSTITUTION, self, kwargs.get("constitution", 0)),  # type: ignore
            Stat.INTELLIGENCE: AbilityScore(Stat.INTELLIGENCE, self, kwargs.get("intelligence", 0)),  # type: ignore
            Stat.WISDOM: AbilityScore(Stat.WISDOM, self, kwargs.get("wisdom", 0)),  # type: ignore
            Stat.CHARISMA: AbilityScore(Stat.CHARISMA, self, kwargs.get("charisma", 0)),  # type: ignore
        }
        self._hp: list[Reason] = []
        self.extras: dict[str, Any] = {}

        self.armour = Armour.NONE
        self.shield = False
        self.weapons: set[BaseWeapon] = {weapon_picker(Weapon.UNARMED, self)}  # type: ignore
        self._class_skills: set[Skill] = {skill1, skill2}
        self.languages: set[str] = set()
        self.equipment: list[str] = []
        self.set_saving_throw_proficiency()
        self._known_spells: set[Spells] = set()
        self._damage_resistances: Reason[DamageType] = Reason()
        self._prepared_spells: set[Spells] = set()
        self._abilities: set[Ability] = set()
        self.feats: dict[Feat, BaseFeat] = {self.origin.origin_feat.tag: self.origin.origin_feat(self)}

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiency]:
        raise NotImplementedError

    #############################################################################
    def armour_proficiency(self) -> set[Proficiency]:
        raise NotImplementedError

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        raise NotImplementedError

    #########################################################################
    @property
    def hp(self) -> Reason:
        hp_track = Reason("Level 1", self.hit_dice)
        hp_track.add("CON bonus", self.level * self.stats[Stat.CONSTITUTION].modifier)
        hp_track.extend(self.check_modifiers(Mod.MOD_HP_BONUS))
        for lvl in self._hp:
            hp_track.extend(lvl)
        return hp_track

    #########################################################################
    @property
    def class_special(self) -> str:
        return ""

    #############################################################################
    def add_feat(self, feat: BaseFeat):
        self.feats[feat.tag] = feat

    #############################################################################
    def class_abilities(self) -> set[Ability]:  # pragma: no coverage
        raise NotImplementedError

    #########################################################################
    @property
    def additional_attacks(self) -> set[Attack]:
        return self.check_set_modifiers(Mod.MOD_ADD_ATTACK)

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
    def damage_resistances(self) -> Reason[DamageType]:
        return self.check_modifiers(Mod.MOD_ADD_DAMAGE_RESISTANCES) | self._damage_resistances

    #########################################################################
    def add_damage_resistance(self, dmg_type: Reason[DamageType]):
        self._damage_resistances |= dmg_type

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
        raise NotImplementedError

    #########################################################################
    def __repr__(self):
        return f"{self.class_name}: {self.name}"

    #########################################################################
    def __getattr__(self, item: str) -> Any:
        """Guess what they are asking for"""
        # Something static in extras
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
        # raise AttributeError(f"{item} not found")
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
        raise NotImplementedError

    #########################################################################
    def spell_slots(self, spell_level: int) -> int:
        """How many spell slots we have for the spell_level"""
        # Override on spell caster classes
        return 0

    #########################################################################
    @property
    def initiative(self) -> Reason:
        result = Reason("dex", self.stats[Stat.DEXTERITY].modifier)
        result.extend(self.check_modifiers(Mod.MOD_INITIATIVE_BONUS))
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

        for spell_level in range(10):
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
    def _handle_modifier_result(self, value: Any, label: str) -> Reason:
        """Change how a result is stored based on the type"""
        result = Reason()
        if isinstance(value, Reason):
            result.extend(value)
        elif isinstance(value, int):
            result.add(label, value)
        else:
            raise UnhandledException(f"character.check_modifiers({label=}) returning unhandled type ({type(value)}) {value=}")
        return result

    #########################################################################
    def _has_modifier(self, obj: Any, modifier: str) -> bool:
        return hasattr(obj, modifier) and callable(getattr(obj, modifier))

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        """Check everything that can modify a value"""

        result = Reason()
        # Feat modifiers
        for name, feat in self.feats.items():
            if self._has_modifier(feat, modifier):
                value = getattr(feat, modifier)(self)
                result.extend(self._handle_modifier_result(value, f"feat {name}"))

        # Origin modifiers
        if self._has_modifier(self.origin, modifier):
            value = getattr(self.origin, modifier)(character=self)
            result.extend(self._handle_modifier_result(value, f"Origin {self.origin.tag}"))

        # Ability modifiers
        for ability in self.abilities:
            if self._has_modifier(ability, modifier):
                value = getattr(ability, modifier)(self=ability, character=self)
                result.extend(self._handle_modifier_result(value, f"ability {ability.tag}"))

        # Character class modifier
        if self._has_modifier(self, modifier):
            value = getattr(self, modifier)(self)
            result.extend(self._handle_modifier_result(value, f"class {modifier}"))

        # Species modifier
        if self._has_modifier(self.species, modifier):
            value = getattr(self.species, modifier)(self)
            result.extend(self._handle_modifier_result(value, f"species {modifier}"))
        return result

    #########################################################################
    def check_set_modifiers(self, modifier: str) -> set[Any]:
        """Check everything that can modify a set"""
        # print(f"DBG character.check_set_modifiers {modifier=}", file=sys.stderr)

        result = set()
        # Feat modifiers
        for name, feat in self.feats.items():
            if self._has_modifier(feat, modifier):
                result |= getattr(feat, modifier)(character=self)

        # Origin modifiers
        if self._has_modifier(self.origin, modifier):
            result |= getattr(self.origin, modifier)(character=self)

        # Ability modifiers
        for ability in self.abilities:
            if self._has_modifier(ability, modifier):
                # print(f"DBG {ability=} {modifier=} {getattr(ability, modifier)=}", file=sys.stderr)
                result |= getattr(ability, modifier)(self=ability, character=self)
        # Character class modifier
        if self._has_modifier(self, modifier):
            # print(f"DBG {self=} {modifier=} {getattr(self, modifier)=}", file=sys.stderr)
            result |= getattr(self, modifier)(character=self)
        # Species modifier
        if self._has_modifier(self.species, modifier):
            result |= getattr(self.species, modifier)(character=self)
        return result

    #########################################################################
    def weapon_proficiencies(self) -> set[Proficiency]:
        return self.weapon_proficiency() | self.check_set_modifiers(Mod.MOD_WEAPON_PROFICIENCY)

    #########################################################################
    def armour_proficiencies(self) -> set[Proficiency]:
        return self.armour_proficiency() | self.check_set_modifiers(Mod.MOD_ARMOUR_PROFICIENCY)

    #########################################################################
    def set_saving_throw_proficiency(self) -> None:
        for stat in Stat:  # type: ignore
            self.stats[stat].proficient = int(self.saving_throw_proficiency(stat))

    #############################################################################
    @property
    def tool_proficiencies(self) -> set[Tool]:
        """What tools the character is proficient with"""
        return self.check_set_modifiers(Mod.MOD_ADD_TOOL_PROFICIENCY)

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
        """What skills the character is proficient in"""
        return self._class_skills | self.origin.proficiencies | self.check_set_modifiers(Mod.MOD_ADD_SKILL_PROFICIENCY)

    #############################################################################
    def lookup_skill(self, skill: Skill) -> CharacterSkill:
        proficient = int(skill in self.skills)

        origin = ""
        if skill in self.origin.proficiencies:
            origin = f"{self.origin}"
        elif skill in self._class_skills:
            origin = f"{self.class_name}"
        elif skill in self.check_set_modifiers(Mod.MOD_ADD_SKILL_PROFICIENCY):
            origin = "something"
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

    #############################################################################
    def level2(self, **kwargs: Any):
        self.level = 2
        self._add_level(self.level, **kwargs)

    #############################################################################
    def level3(self, **kwargs: Any):
        self.level = 3
        self._add_level(self.level, **kwargs)

    #############################################################################
    def level4(self, **kwargs: Any):
        self.level = 4
        self._add_level(self.level, **kwargs)

    #########################################################################
    def _add_level(self, level: int, **kwargs):
        self._hp.append(Reason(f"level {level}", kwargs["hp"]))
        if "feat" in kwargs:
            self.add_feat(kwargs["feat"])

    # EOF

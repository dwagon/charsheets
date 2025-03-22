"""Class to define a character"""

import sys
from string import ascii_uppercase
from typing import Any, Optional

from charsheets.ability_score import AbilityScore
from charsheets.armour import Unarmoured
from charsheets.armour.base_armour import BaseArmour
from charsheets.attack import Attack
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Skill, Feature, Stat, Proficiency, DamageType, Mod, Tool, Sense, Language, CharacterClass
from charsheets.exception import UnhandledException, InvalidOption, NotDefined
from charsheets.features.base_feature import BaseFeature
from charsheets.origins.base_origin import BaseOrigin
from charsheets.reason import Reason
from charsheets.skill import CharacterSkill
from charsheets.species.base_species import BaseSpecies
from charsheets.spell import Spell, SPELL_DETAILS, spell_school, spell_flags, spell_name
from charsheets.weapons import Unarmed
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Character:
    def __init__(
        self,
        name: str,
        origin: BaseOrigin,
        species: BaseSpecies,
        **kwargs: Any,
    ):
        self.name = name
        self._class_name = ""
        self._levels: dict[str, int] = {}  # What level for each class we are
        self.class_levels: dict[int, BaseClass] = {}  # Charclass instances
        self.player_name = "<Undefined>"
        self.level = 0  # Total level
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
        self.extras: dict[str, Any] = {}
        self._skills: dict[Skill, CharacterSkill] = self.initialise_skills()
        self._hp: list[Reason] = []
        self._base_skill_proficiencies: set[Skill]
        self.armour: BaseArmour
        self.shield: Optional[BaseArmour] = None
        self.weapons: list[BaseWeapon] = []
        self._languages: Reason[Language] = Reason("Common", Language.COMMON)
        self.equipment: list[str] = []
        self._known_spells: Reason[Spell] = Reason()
        self._damage_resistances: Reason[DamageType] = Reason()
        self._prepared_spells: Reason[Spell] = Reason()
        self._features: set[BaseFeature] = set()
        self._extra_attacks: list[str] = []
        self._weapon_proficiencies: Reason[Proficiency] = Reason()
        self._armor_proficiencies: Reason[Proficiency] = Reason()
        self.add_weapon(Unarmed())
        self.wear_armour(Unarmoured())
        if isinstance(self.origin.origin_feat, BaseFeature):
            self.add_feature(self.origin.origin_feat)
        else:
            self.add_feature(self.origin.origin_feat())

    #############################################################################
    @property
    def class_description(self) -> str:
        """Return a class description for all the subclasses"""
        ans: list[str] = []
        for cls, lvl in self._levels.items():
            ans.append(f"{cls.title()}: {lvl}")
        return ", ".join(ans)

    #############################################################################
    def initialise_skills(self) -> dict[Skill, CharacterSkill]:
        skills: dict[Skill, CharacterSkill] = {skill: CharacterSkill(skill, self) for skill in Skill}
        return skills

    #############################################################################
    def has_feature(self, feature: Feature) -> bool:
        """Does the character have the feature with the tag {feature}"""
        return any(abil.tag == feature for abil in self.features)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:  # pragma: no coverage
        raise NotImplementedError

    #########################################################################
    @property
    def extra_attacks(self) -> list[str]:
        ans = self._extra_attacks[:]
        for reason in self.check_modifiers(Mod.MOD_EXTRA_ATTACK):
            ans.append(reason.value)
        return ans

    #########################################################################
    @property
    def senses(self) -> Reason[Sense]:
        return Reason("Basic", Sense.NORMAL) | self.check_modifiers(Mod.MOD_ADD_SENSE)

    #########################################################################
    @property
    def hp(self) -> Reason:
        hp_track = Reason("CON bonus", self.level * self.stats[Stat.CONSTITUTION].modifier)
        hp_track.extend(self.check_modifiers(Mod.MOD_HP_BONUS))
        for lvl in self._hp:
            hp_track.extend(lvl)
        return hp_track

    #########################################################################
    def add_languages(self, *languages: Language):
        self._languages.extend(Reason("Set", *languages))

    #########################################################################
    @property
    def languages(self) -> Reason[Language]:
        return self.check_modifiers(Mod.MOD_ADD_LANGUAGE) | self._languages

    #########################################################################
    @property
    def class_special(self) -> str:
        return ""

    #########################################################################
    def display_features(self, numerator: int = 1, denominator: int = 1, show_hidden=False, hidden_only=False):
        """Return features for output purposes"""
        # Select the sort of objects we want to return
        all_things = sorted(list(self.features), key=lambda x: x.tag.name)
        if show_hidden:
            displayable = all_things
        elif hidden_only:
            displayable = [_ for _ in all_things if _.hide]
        else:
            displayable = [_ for _ in all_things if not _.hide]

        first_element, last_element = display_selection(len(displayable), numerator, denominator)
        yield from displayable[first_element:last_element]

    #############################################################################
    def find_feature(self, feature: Feature) -> BaseFeature:
        for feat in self.features:
            if feat.tag == feature:
                return feat
        raise NotDefined(f"{feature} not present")

    #########################################################################
    @property
    def additional_attacks(self) -> Reason[Attack]:
        return self.check_modifiers(Mod.MOD_ADD_ATTACK)

    #########################################################################
    def add_feature(self, new_feature: BaseFeature):
        new_feature.add_owner(self)
        self._features.add(new_feature)

    #########################################################################
    @property
    def features(self) -> set[BaseFeature]:
        abils = self._features.copy()
        abils |= self.species.species_feature()
        for abil in abils:
            abil.add_owner(self)
        return abils

    #########################################################################
    @property
    def damage_resistances(self) -> Reason[DamageType]:
        return self.check_modifiers(Mod.MOD_ADD_DAMAGE_RESISTANCES) | self._damage_resistances

    #########################################################################
    def add_damage_resistance(self, dmg_type: Reason[DamageType]):
        self._damage_resistances |= dmg_type

    #########################################################################
    def add_weapon(self, weapon: BaseWeapon) -> None:
        weapon.wielder = self
        self.weapons.append(weapon)

    #########################################################################
    def wear_armour(self, armour: BaseArmour) -> None:
        armour.wearer = self
        self.armour = armour

    #########################################################################
    def wear_shield(self, shield: BaseArmour) -> None:
        shield.wearer = self
        self.shield = shield

    #########################################################################
    def add_equipment(self, *items):
        if isinstance(items, str):
            self.equipment.append(items)
        else:
            self.equipment.extend(items)

    #########################################################################
    def __repr__(self):
        return f"{self.name}"

    #########################################################################
    def __getattr__(self, item: str) -> Any:
        """Guess what they are asking for"""
        # Something static in extras
        # print(f"DBG  __getattr__({item=})")
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

        # print(f"DBG Unknown __getattr__({item=})", file=sys.stderr)
        raise AttributeError(f"{item} not found")
        # return "unknown"

    #########################################################################
    @property
    def speed(self) -> Reason[int]:
        speeds = [self.species.speed]
        speeds.extend(link.value for link in self.check_modifiers(Mod.MOD_SET_MOVEMENT_SPEED))
        return Reason("Species", max(speeds)) | self.check_modifiers(Mod.MOD_ADD_MOVEMENT_SPEED)

    #########################################################################
    @property
    def fly_speed(self) -> Reason[int]:
        return self.check_modifiers("mod_fly_movement")

    #########################################################################
    @property
    def swim_speed(self) -> Reason[int]:
        return self.check_modifiers("mod_swim_movement")

    #########################################################################
    @property
    def max_hit_dice(self) -> str:
        dice: dict[int, int] = {}
        for chclass in self.class_levels.values():
            dice[chclass.hit_dice] = dice.get(chclass.hit_dice, 0) + 1
        ans: list[str] = []
        for sides, num in dice.items():
            ans.append(f"{num}d{sides}")
        return " + ".join(ans)

    #########################################################################
    @property
    def spell_save_dc(self) -> int:
        return 8 + self.spell_attack_bonus

    #########################################################################
    @property
    def passive_perception(self):
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
        return None
        #   raise NotImplementedError

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
    def ac(self) -> Reason[int]:
        result = self.armour.armour_class()
        if self.shield:
            result.extend(self.shield.armour_class())
        result.extend(self.check_modifiers(Mod.MOD_AC_BONUS))
        return result

    #########################################################################
    def half_spell_sheet(self) -> bool:
        """If we only have spells up to level 6 use a half sheet, otherwise we use a full sheet."""
        return self.spell_slots(6) == 0

    #########################################################################
    def spell_display_range(self, spell_level: int, overflow=False) -> tuple[int, int]:
        if overflow:
            start_limit = self.spell_display_limits(spell_level)
            end_limit = 999
        else:
            start_limit = 0
            end_limit = self.spell_display_limits(spell_level)
        return start_limit, end_limit

    #########################################################################
    def level_spells(self, spell_level: int, overflow=False) -> list[tuple[str, bool, str, str, str, str]]:
        """List of known spells of spell_level (and an A-Z prefix) - for display purposes
        Spell Index A-Z; Spell Prepared {bool}; Spell Name; Spell School; Spell Flags
        """
        ans = []
        if overflow:
            ans.append(("A", False, "---- Overflow Spells ----", "", "", ""))
        start_limit, end_limit = self.spell_display_range(spell_level, overflow)
        if spell_level and self.spell_slots(spell_level) == 0:
            return []
        spells = self.spells_of_level(spell_level)[start_limit:end_limit]

        for num, spell in enumerate(spells, start=len(ans)):
            ans.append(
                (
                    ascii_uppercase[num],
                    spell[0] in self.prepared_spells,
                    spell_name(spell[0]),
                    spell_school(spell[0]),
                    spell_flags(spell[0]),
                    spell[1].reason,
                )
            )
        if overflow and len(ans) == 1:  # Just the overflow label
            ans = []
        for num in range(len(ans), self.spell_display_limits(spell_level)):
            ans.append((ascii_uppercase[num], False, "", "", "", ""))

        return ans

    #########################################################################
    def spell_display_limits(self, level: int) -> int:
        """How many spells we can display per level"""
        if self.half_spell_sheet():
            return {0: 11, 1: 26, 2: 19, 3: 19, 4: 19, 5: 19, 6: 0, 7: 0, 8: 0, 9: 0}[level]
        return {0: 8, 1: 13, 2: 13, 3: 13, 4: 13, 5: 9, 6: 9, 7: 9, 8: 7, 9: 7}[level]

    #########################################################################
    def has_overflow_spells(self) -> bool:
        """Do we have more than a single page of spells"""

        for spell_level in range(10):
            if (
                len(self.spells_of_level(spell_level)) > self.spell_display_limits(spell_level)
                and self.spell_slots(spell_level) != 0
            ):
                return True
        return False

    #########################################################################
    def ranged_atk_bonus(self) -> Reason:
        result = Reason("prof_bonus", self.proficiency_bonus)
        result.add("dex mod", self.stats[Stat.DEXTERITY].modifier)
        return result

    #########################################################################
    def melee_atk_bonus(self) -> Reason:
        result = Reason("prof_bonus", self.proficiency_bonus)
        result.add("str mod", self.stats[Stat.STRENGTH].modifier)
        return result

    #########################################################################
    def ranged_dmg_bonus(self) -> Reason:
        return Reason("dex mod", self.stats[Stat.DEXTERITY].modifier)

    #########################################################################
    def melee_dmg_bonus(self) -> Reason:
        return Reason("str mod", self.stats[Stat.STRENGTH].modifier)

    #########################################################################
    def _handle_modifier_result(self, value: Any, label: str) -> Reason:
        """Change how a result is stored based on the type"""
        result = Reason[Any]()
        if isinstance(value, Reason):
            result.extend(value)
        elif isinstance(value, int):
            result.add(label, value)
        else:  # pragma: no coverage
            raise UnhandledException(f"character.check_modifiers({label=}) returning unhandled type ({type(value)}) {value=}")
        return result

    #########################################################################
    def _has_modifier(self, obj: Any, modifier: str) -> bool:
        return hasattr(obj, modifier) and callable(getattr(obj, modifier))

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        """Check everything that can modify a value"""

        result = Reason[Any]()
        # Origin modifiers
        if self._has_modifier(self.origin, modifier):
            value = getattr(self.origin, modifier)(character=self)
            result.extend(self._handle_modifier_result(value, f"Origin {self.origin.tag}"))

        # Feature modifiers
        for feature in self.features:
            if self._has_modifier(feature, modifier):
                value = getattr(feature, modifier)(character=self)
                result.extend(self._handle_modifier_result(value, f"feature {feature.tag}"))

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
    def weapon_proficiencies(self) -> Reason[Proficiency]:
        return self.check_modifiers(Mod.MOD_WEAPON_PROFICIENCY) | self._weapon_proficiencies

    #########################################################################
    def add_weapon_proficiency(self, proficiency: Reason[Proficiency]):
        self._weapon_proficiencies |= proficiency

    #########################################################################
    def add_armor_proficiency(self, proficiency: Reason[Proficiency]):
        self._armor_proficiencies |= proficiency

    #########################################################################
    def armour_proficiencies(self) -> set[Proficiency]:
        return self.check_modifiers(Mod.MOD_ARMOUR_PROFICIENCY) | self._armor_proficiencies

    #########################################################################
    def set_saving_throw_proficiency(self, *stats: Stat) -> None:
        for stat in stats:  # type: ignore
            self.stats[stat].proficient = 1

    #############################################################################
    @property
    def tool_proficiencies(self) -> Reason[Tool]:
        """What tools the character is proficient with"""
        return self.check_modifiers(Mod.MOD_ADD_TOOL_PROFICIENCY)

    #############################################################################
    def spells_of_level(self, spell_level: int) -> list[tuple[Spell, Reason[Spell]]]:
        """Return list of (unique) spells known at spell_level"""
        return sorted(
            {(_.value, _) for _ in self.known_spells if SPELL_DETAILS[_.value].level == spell_level}, key=lambda x: spell_name(x[0])
        )

    #############################################################################
    def learn_spell(self, *spells: Spell):
        learnt = Reason[Spell]()
        for spell in spells:
            learnt |= Reason("Learnt", spell)
        self._known_spells |= learnt

    #############################################################################
    @property
    def known_spells(self) -> Reason[Spell]:
        """What spells the character knows"""
        known = self._known_spells.copy()
        for spell in self.check_modifiers(Mod.MOD_ADD_KNOWN_SPELLS):
            if spell.value not in known:
                known.add(spell.reason, spell.value)
        for spell in self.check_modifiers(Mod.MOD_ADD_PREPARED_SPELLS):  # All prepared spells must be known
            if spell.value not in known:
                known.add(spell.reason, spell.value)
        return known

    #############################################################################
    def prepare_spells(self, *spells: Spell):
        for spell in set(spells):
            if spell not in self._known_spells:
                self._known_spells |= Reason("Prepared", spell)
            if spell not in self._prepared_spells:
                self._prepared_spells |= Reason("Prepared", spell)

    #############################################################################
    @property
    def prepared_spells(self) -> Reason[Spell]:
        """What spells the character has prepared"""
        return self.check_modifiers(Mod.MOD_ADD_PREPARED_SPELLS) | self._prepared_spells

    #############################################################################
    @property
    def skills(self) -> dict[Skill, CharacterSkill]:
        """Return skills"""
        proficiency = self.check_modifiers(Mod.MOD_ADD_SKILL_PROFICIENCY)
        expertise = self.check_modifiers(Mod.MOD_ADD_SKILL_EXPERTISE)

        skills = self._skills.copy()
        for skill in skills:
            if skill in proficiency or skill in expertise:
                skills[skill].proficient = True
                if skill in expertise:
                    skills[skill].expert = True
                for mod in proficiency:
                    if mod.value == skill:
                        skills[skill].origin = mod.reason
        return skills

    #############################################################################
    def is_expert(self, skill: Skill) -> bool:
        return self.skills[skill].expert

    #############################################################################
    def is_proficient(self, skill: Skill) -> bool:
        return self.skills[skill].proficient

    #############################################################################
    def mod_add_attack(self, character: "Character") -> Reason[Attack]:
        return Reason()

    #############################################################################
    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason()

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason()

    #############################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason()

    #############################################################################
    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason()

    #############################################################################
    def mod_set_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason()

    #############################################################################
    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason[Sense]()

    #########################################################################
    @property
    def rogue(self) -> Optional[BaseClass]:
        return self.highest_level(CharacterClass.ROGUE)

    #########################################################################
    def highest_level(self, charclass: CharacterClass) -> Optional[BaseClass]:
        """Return the highest level instance obtained of a character class or subclass"""
        max_level = 0
        bc = None
        for lvl, cls in self.class_levels.items():
            if cls.is_subclass(charclass) and lvl > max_level:
                max_level = lvl
                bc = cls
        return bc

    #########################################################################
    def add_level(self, charclass: BaseClass):
        self.level += 1
        class_name = charclass._base_class
        charclass.character = self
        self._levels[class_name] = self._levels.get(class_name, 0) + 1
        print(f"DBG: {self._levels=}", file=sys.stderr)
        self.class_levels[self.level] = charclass

        charclass.level = self._levels[class_name]
        charclass.add_level(self._levels[class_name])


#############################################################################
def display_selection(number_of_items: int = 1, numerator: int = 1, denominator: int = 1) -> tuple[int, int]:
    # Pick which chunk to return (part {numerator} of {denominator})
    chunk_size = number_of_items // denominator
    first_element = (numerator - 1) * chunk_size
    if numerator == denominator:  # Handle rounding errors
        last_element = number_of_items
    else:
        last_element = numerator * chunk_size

    return first_element, last_element


# EOF

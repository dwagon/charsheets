"""Class to define a character"""

import sys
import traceback
from collections import Counter
from string import ascii_uppercase
from typing import Any, Optional, cast

from charsheets.ability_score import AbilityScore
from charsheets.armour import Unarmoured
from charsheets.armour.base_armour import BaseArmour
from charsheets.attack import Attack
from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.classes import Wizard, Warlock, Sorcerer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Skill, Feature, Stat, Proficiency, DamageType, Mod, Tool, Sense, Language, CharacterClass, Weapon
from charsheets.exception import UnhandledException, NotDefined
from charsheets.features.base_feature import BaseFeature
from charsheets.origins.base_origin import BaseOrigin
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason
from charsheets.skill import CharacterSkill
from charsheets.species.base_species import BaseSpecies
from charsheets.spell import Spell, SPELL_DETAILS, spell_school, spell_flags, spell_name
from charsheets.spells.base_spell import BaseSpell
from charsheets.weapons import Unarmed
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class BaseCharacter:
    def __init__(
        self,
        name: str,
        strength: int,
        dexterity: int,
        constitution: int,
        intelligence: int,
        wisdom: int,
        charisma: int,
        **kwargs: Any,
    ):
        self.name = name
        self._class_name = ""
        self._levels: dict[str, int] = {}  # What level for each class we are
        self.class_levels: dict[int, BaseClass] = {}  # Charclass instances
        self.level = 0  # Total level

        self.stats = {
            Stat.STRENGTH: AbilityScore(Stat.STRENGTH, self, strength),  # type: ignore
            Stat.DEXTERITY: AbilityScore(Stat.DEXTERITY, self, dexterity),  # type: ignore
            Stat.CONSTITUTION: AbilityScore(Stat.CONSTITUTION, self, constitution),  # type: ignore
            Stat.INTELLIGENCE: AbilityScore(Stat.INTELLIGENCE, self, intelligence),  # type: ignore
            Stat.WISDOM: AbilityScore(Stat.WISDOM, self, wisdom),  # type: ignore
            Stat.CHARISMA: AbilityScore(Stat.CHARISMA, self, charisma),  # type: ignore
        }
        self._extras: dict[str, Any] = kwargs.copy()
        self.specials: dict[CharacterClass, Any] = {}  # Things each class can have e.g. metamagic, invocations, etc.
        self._skills: dict[Skill, CharacterSkill] = self.initialise_skills()
        self.hp_track: list[Reason] = []
        self._base_skill_proficiencies: set[Skill]
        self.armour: BaseArmour
        self.shield: Optional[BaseArmour] = None
        self.weapons: list[BaseWeapon] = []
        self.equipment: list[str] = []
        self.treasure: list[str] = []
        self._known_spells: Reason[Spell] = Reason()
        self._damage_resistances: Reason[DamageType] = Reason()
        self._prepared_spells: Reason[Spell] = Reason()
        self._features: set[BaseFeature] = set()
        self._extra_attacks: list[str] = []
        self._spell_attacks: list[BaseSpell] = []
        self._weapon_proficiencies: Reason[Proficiency] = Reason("Base", cast(Proficiency, Proficiency.SIMPLE_WEAPONS))
        self._specific_weapon_proficiencies: Reason[Weapon] = Reason()
        self._armor_proficiencies: Reason[Proficiency] = Reason()
        self.add_weapon(Unarmed())
        self.wear_armour(Unarmoured())

    #############################################################################
    @property
    def class_description(self) -> str:
        """Return a class description for all the subclasses"""
        base_levels = Counter[CharacterClass]()
        class_names: dict[CharacterClass, str] = {}

        for cls in self.class_levels.values():
            base_levels[cls._base_class] += 1
            class_names[cls._base_class] = cls.class_name

        for cls in self.class_levels.values():
            if hasattr(cls, "_sub_class"):
                class_names[cls._base_class] = cls.class_name

        ans: list[str] = [f"{class_names[level]}: {base_levels[level]}" for level in base_levels]
        return ", ".join(ans)

    #############################################################################
    def initialise_skills(self) -> dict[Skill, CharacterSkill]:
        skills: dict[Skill, CharacterSkill] = {skill: CharacterSkill(skill, self) for skill in Skill}  # type: ignore
        return skills

    #############################################################################
    def has_feature(self, feature: Feature) -> bool:
        """Does the character have the feature with the tag {feature}"""
        return any(abil.tag == feature for abil in self.features)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:  # pragma: no coverage
        return bool(self.stats[stat].proficient)

    #########################################################################
    @property
    def extras(self) -> dict[str, Any]:
        return self._extras

    @extras.setter
    def extras(self, values: dict[str, str]):
        self._extras.update(values)

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
        return self.check_modifiers(Mod.MOD_ADD_SENSE)

    #########################################################################
    @property
    def hp(self) -> Reason:
        hp_reason = Reason("CON bonus", self.level * self.stats[Stat.CONSTITUTION].modifier)
        hp_reason.extend(self.check_modifiers(Mod.MOD_HP_BONUS))
        for lvl in self.hp_track:
            hp_reason.extend(lvl)
        return hp_reason

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
        try:
            ans: dict[CharacterClass, str] = {
                CharacterClass.BARBARIAN: self.barbarian.class_special if self.barbarian else "",
                CharacterClass.BARD: self.bard.class_special if self.bard else "",
                CharacterClass.CLERIC: self.cleric.class_special if self.cleric else "",
                CharacterClass.DRUID: self.druid.class_special if self.druid else "",
                CharacterClass.FIGHTER: self.fighter.class_special if self.fighter else "",
                CharacterClass.MONK: self.monk.class_special if self.monk else "",
                CharacterClass.PALADIN: self.paladin.class_special if self.paladin else "",
                CharacterClass.RANGER: self.ranger.class_special if self.ranger else "",
                CharacterClass.ROGUE: self.rogue.class_special if self.rogue else "",
                CharacterClass.SORCERER: self.sorcerer.class_special if self.sorcerer else "",
                CharacterClass.WARLOCK: self.warlock.class_special if self.warlock else "",
                CharacterClass.WIZARD: self.wizard.class_special if self.wizard else "",
            }
            return "\n".join([_ for _ in ans.values() if _])
        except Exception as exc:  # pragma: no coverage
            print(f"Class Special Failure: {exc=}", file=sys.stderr)
            raise

    #########################################################################
    def display_features(self, numerator: int = 1, denominator: int = 1, show_hidden=False, hidden_only=False):
        """Return features for output purposes"""
        # Select the sort of objects we want to return
        all_things = sorted(list(self.features), key=lambda x: x.tag.value)
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
        new_feature.add_owner(self)  # type: ignore
        self._features.add(new_feature)

    #########################################################################
    def remove_feature(self, old_feature: BaseFeature):
        self._features.remove(old_feature)

    #########################################################################
    @property
    def features(self) -> set[BaseFeature]:
        abils = self._features.copy()
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
        weapon.wielder = self  # type: ignore
        self.weapons.append(weapon)

    #########################################################################
    def wear_armour(self, armour: BaseArmour) -> None:
        assert isinstance(armour, BaseArmour)
        armour.wearer = self  # type: ignore
        self.armour = armour

    #########################################################################
    def wear_shield(self, shield: BaseArmour) -> None:
        shield.wearer = self  # type: ignore
        self.shield = shield

    #########################################################################
    def add_equipment(self, *items):
        if isinstance(items, str):
            self.equipment.append(items)
        else:
            self.equipment.extend(items)

    #########################################################################
    def add_treasure(self, *items):
        if isinstance(items, str):
            self.treasure.append(items)
        else:
            self.treasure.extend(items)

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

    #########################################################################
    @property
    def speed(self) -> Reason[int]:
        speeds = [self.base_speed]
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
    def spell_casting_ability(self) -> Optional[Stat]:
        casting_stat: Counter[Stat] = Counter()
        for chclass in self.class_levels.values():
            if max_cls := self.highest_level(chclass._base_class):
                if sca := max_cls.spell_casting_ability:
                    casting_stat[sca] += 1
        return casting_stat.most_common(1)[0][0] if casting_stat else None

    #########################################################################
    def spell_slots(self, spell_level: int) -> int:
        """How many spell slots we have for the spell_level"""
        # TODO - handle wierd multi-classing spell slots rules
        slots = {}
        for chclass in self.class_levels.values():
            if max_cls := self.highest_level(chclass._base_class):
                slots[chclass._base_class] = max_cls.spell_slots(spell_level)
        return sum(slots[_] for _ in slots)

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
    def has_modifier(self, obj: Any, modifier: str) -> bool:
        return hasattr(obj, modifier) and callable(getattr(obj, modifier))

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        """Check everything that can modify a value"""

        result = Reason[Any]()

        # Feature modifiers
        for feature in self.features:
            if self.has_modifier(feature, modifier):
                value = getattr(feature, modifier)(character=self)
                result.extend(self._handle_modifier_result(value, f"feature {feature.tag}"))

        # Character modifier
        if self.has_modifier(self, modifier):
            value = getattr(self, modifier)(self)
            result.extend(self._handle_modifier_result(value, f"class {modifier}"))

        # Class modifier
        for charclass in self.class_levels.values():
            if value := charclass.check_modifiers(modifier):
                ans = self._handle_modifier_result(value, f"class {modifier}")
                result.extend(ans)

        return result

    #########################################################################
    def weapon_proficiencies(self) -> Reason[Proficiency]:
        """Proficiency in a class of weapons (2024)"""
        return self.check_modifiers(Mod.MOD_WEAPON_PROFICIENCY) | self._weapon_proficiencies

    #########################################################################
    def specific_weapon_proficiencies(self) -> Reason[Proficiency]:
        """Unique proficiencies on specific weapons, not classes of weapons (2014)"""
        profs = Reason[Proficiency]()
        mods = self._specific_weapon_proficiencies | self.check_modifiers(Mod.MOD_SPECIFIC_WEAPON_PROFICIENCY)
        for link in mods:
            if link.value not in profs:
                profs.add(link.reason, link.value)
        return profs

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
        try:
            return self.check_modifiers(Mod.MOD_ADD_PREPARED_SPELLS) | self._prepared_spells
        except Exception as exc:  # pragma: no coverage
            print(f"Prepared Spell Failure: {exc=}", file=sys.stderr)
            raise

    #############################################################################
    @property
    def skills(self) -> dict[Skill, CharacterSkill]:
        """Return skills"""
        _skills = self._skills.copy()

        try:
            proficiency = self.check_modifiers(Mod.MOD_ADD_SKILL_PROFICIENCY)
            expertise = self.check_modifiers(Mod.MOD_ADD_SKILL_EXPERTISE)

            for skill in _skills:
                if skill in proficiency or skill in expertise:
                    for mod in proficiency:
                        if mod.value == skill:
                            _skills[skill].origin = mod.reason
                            _skills[skill].proficient = True
                    for mod in expertise:
                        if mod.value == skill:
                            _skills[skill].origin = mod.reason
                            _skills[skill].expert = True
        except Exception as exc:
            print(f"Exception '{exc}' in skills", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
        return _skills

    #############################################################################
    def add_spell_details(self, spell: BaseSpell):
        spell.caster = self  # type: ignore
        self._spell_attacks.append(spell)

    #############################################################################
    @property
    def spell_attacks(self) -> list[Attack]:
        """Return a list of attacks that are spells for display purposes"""
        attacks: list[Attack] = []
        for spell in self._spell_attacks:
            attacks.append(spell.to_attack())
        return attacks

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
    def barbarian(self) -> Optional[Barbarian]:
        return cast(Barbarian, self.highest_level(CharacterClass.BARBARIAN))

    #########################################################################
    @property
    def bard(self) -> Optional[Bard]:
        return cast(Bard, self.highest_level(CharacterClass.BARD))

    #########################################################################
    @property
    def cleric(self) -> Optional[Cleric]:
        return cast(Cleric, self.highest_level(CharacterClass.CLERIC))

    #########################################################################
    @property
    def druid(self) -> Optional[Druid]:
        return cast(Druid, self.highest_level(CharacterClass.DRUID))

    #########################################################################
    @property
    def fighter(self) -> Optional[Fighter]:
        return cast(Fighter, self.highest_level(CharacterClass.FIGHTER))

    #########################################################################
    @property
    def monk(self) -> Optional[Monk]:
        return cast(Monk, self.highest_level(CharacterClass.MONK))

    #########################################################################
    @property
    def paladin(self) -> Optional[Paladin]:
        return cast(Paladin, self.highest_level(CharacterClass.PALADIN))

    #########################################################################
    @property
    def ranger(self) -> Optional[Ranger]:
        return cast(Ranger, self.highest_level(CharacterClass.RANGER))

    #########################################################################
    @property
    def rogue(self) -> Optional[Rogue]:
        return cast(Rogue, self.highest_level(CharacterClass.ROGUE))

    #########################################################################
    @property
    def sorcerer(self) -> Optional[Sorcerer]:
        return cast(Sorcerer, self.highest_level(CharacterClass.SORCERER))

    #########################################################################
    @property
    def warlock(self) -> Optional[Warlock]:
        return cast(Warlock, self.highest_level(CharacterClass.WARLOCK))

    #########################################################################
    @property
    def wizard(self) -> Optional[Wizard]:
        return cast(Wizard, self.highest_level(CharacterClass.WIZARD))

    #########################################################################
    def highest_level(self, char_class: CharacterClass) -> Optional[BaseClass]:
        """Return the highest level instance obtained of a character class or subclass"""
        max_level = 0
        bc = None
        for lvl, cls in self.class_levels.items():
            if cls.is_subclass(char_class) and lvl > max_level:
                max_level = lvl
                bc = cls
        return bc

    #########################################################################
    def add_level(self, charclass: BaseClass):
        self.level += 1
        class_name = charclass._base_class
        charclass.character = self  # type: ignore
        self._levels[class_name] = self._levels.get(class_name, 0) + 1
        self.class_levels[self.level] = charclass

        charclass.level = self._levels[class_name]
        charclass.add_level(self._levels[class_name])

    #########################################################################
    def spell_damage_bonus(self, spell: Spell) -> int:
        """Return modifiers to spell damage"""
        bonus = 0
        classes: set[CharacterClass] = {cls._base_class for cls in self.class_levels.values()}
        for char_class in classes:
            if max_level := self.highest_level(char_class):
                bonus += max_level.spell_damage_bonus(spell)
        return bonus

    #########################################################################
    def spell_notes(self, spell: Spell) -> str:
        """Return notes on the attack spell"""
        bonus = ""
        classes: set[CharacterClass] = {cls._base_class for cls in self.class_levels.values()}
        for char_class in classes:
            if max_level := self.highest_level(char_class):
                bonus += max_level.spell_notes(spell)
        return bonus

    #########################################################################
    def spell_range(self, spell: Spell) -> int:
        """Return notes on the attack spell"""
        bonus = 0
        classes: set[CharacterClass] = {cls._base_class for cls in self.class_levels.values()}
        for char_class in classes:
            if max_level := self.highest_level(char_class):
                bonus += max_level.spell_range(spell)
        return bonus


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


#############################################################################
class Character2014(BaseCharacter):
    def __init__(
        self,
        name: str,
        background: BaseBackground,
        race: BaseRace,
        **kwargs: Any,
    ):
        self._languages: Reason[Language] = Reason("Initial", Language.COMMON)
        self.race = race
        self.race.character = self  # type: ignore
        self.background = background
        super().__init__(name, **kwargs)

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        """Check everything that can modify a value"""

        result = Reason[Any]()
        # Race modifier
        if self.has_modifier(self.race, modifier):
            value = getattr(self.race, modifier)(self)
            result.extend(self._handle_modifier_result(value, f"Race {modifier}"))

        # Background modifier
        if self.has_modifier(self.background, modifier):
            value = getattr(self.background, modifier)(self)
            result.extend(self._handle_modifier_result(value, f"Background {modifier}"))

        result.extend(super().check_modifiers(modifier))
        return result

    #########################################################################
    @property
    def features(self) -> set[BaseFeature]:
        abils = super().features
        try:
            abils |= self.race.race_feature()
            for abil in abils:
                abil.add_owner(self)  # type: ignore
        except Exception:
            traceback.print_exc(file=sys.stderr)
        return abils

    #########################################################################
    @property
    def base_speed(self) -> int:
        return self.race.speed


#############################################################################
class Character(BaseCharacter):
    def __init__(
        self,
        name: str,
        origin: BaseOrigin,
        species: BaseSpecies,
        language1: Language,
        language2: Language,
        **kwargs: Any,
    ):
        self.origin = origin
        self.species = species
        self.species.character = self  # type: ignore
        self._languages: Reason[Language] = Reason("Initial", Language.COMMON, language1, language2)
        super().__init__(name, **kwargs)
        if isinstance(self.origin.origin_feat, BaseFeature):
            self.add_feature(self.origin.origin_feat)
        else:
            self.add_feature(self.origin.origin_feat())

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        """Check everything that can modify a value"""

        result = Reason[Any]()
        # Origin modifiers
        if self.has_modifier(self.origin, modifier):
            value = getattr(self.origin, modifier)(character=self)
            result.extend(self._handle_modifier_result(value, f"Origin {self.origin.tag}"))

        # Species modifier
        if self.has_modifier(self.species, modifier):
            value = getattr(self.species, modifier)(self)
            result.extend(self._handle_modifier_result(value, f"species {modifier}"))

        result.extend(super().check_modifiers(modifier))
        return result

    #########################################################################
    @property
    def base_speed(self) -> int:
        return self.species.speed

    #########################################################################
    @property
    def features(self) -> set[BaseFeature]:
        abils = self.species.species_feature()
        abils |= super().features
        for abil in abils:
            abil.add_owner(self)  # type: ignore
        return abils


# EOF

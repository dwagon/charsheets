""" Class to define a character"""

from string import ascii_uppercase
from typing import Any, Optional

from charsheets.abilities.base_ability import BaseAbility
from charsheets.ability_score import AbilityScore
from charsheets.armour import Unarmoured
from charsheets.armour.base_armour import BaseArmour
from charsheets.attack import Attack
from charsheets.constants import Skill, Ability, Stat, Feat, Proficiency, DamageType, Movements, Mod, Tool, Sense
from charsheets.exception import UnhandledException, InvalidOption
from charsheets.feats.base_feat import BaseFeat
from charsheets.origins.base_origin import BaseOrigin
from charsheets.reason import Reason
from charsheets.skill import CharacterSkill
from charsheets.species.base_species import BaseSpecies
from charsheets.spells import Spells, SPELL_LEVELS
from charsheets.util import safe
from charsheets.weapons import Unarmed
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Character:
    def __init__(self, name: str, origin: BaseOrigin, species: BaseSpecies, skill1: Skill, skill2: Skill, **kwargs: Any):
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
        self._base_skill_proficiencies: set[Skill]
        self.armour: Optional[BaseArmour] = None
        self.shield = False
        self.weapons: list[BaseWeapon] = []
        self._class_skills: Reason[Skill] = Reason(self.class_name, skill1, skill2)
        self.languages: set[str] = set()
        self.equipment: list[str] = []
        self.set_saving_throw_proficiency()
        self._known_spells: Reason[Spells] = Reason()
        self._damage_resistances: Reason[DamageType] = Reason()
        self._prepared_spells: Reason[Spells] = Reason()
        self._abilities: set[BaseAbility] = set()
        self.feats: dict[Feat, BaseFeat] = {self.origin.origin_feat.tag: self.origin.origin_feat(self)}
        self.add_weapon(Unarmed())
        self.wear_armour(Unarmoured())
        self._validation(skill1, skill2)

    #############################################################################
    def _validation(self, skill1: Skill, skill2: Skill):
        """Ensure valid options have been selected"""
        if skill1 not in self._base_skill_proficiencies:
            raise InvalidOption(f"{skill1} not in {self.class_name}'s skill proficiencies: {self._base_skill_proficiencies}")
        if skill2 not in self._base_skill_proficiencies:
            raise InvalidOption(f"{skill2} not in {self.class_name}'s skill proficiencies: {self._base_skill_proficiencies}")
        if skill1 == skill2:
            raise InvalidOption(f"{skill1} and {skill2} are the same")

    #############################################################################
    def has_ability(self, ability: Ability) -> bool:
        """Does the character have the ability with the tag {ability}"""
        return any(abil.tag == ability for abil in self.abilities)

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        raise NotImplementedError

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        raise NotImplementedError

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        raise NotImplementedError

    #########################################################################
    @property
    def senses(self) -> Reason[Sense]:
        return Reason("Basic", Sense.NORMAL) | self.check_modifiers(Mod.MOD_ADD_SENSE)

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
    def class_abilities(self) -> set[BaseAbility]:  # pragma: no coverage
        raise NotImplementedError

    #########################################################################
    @property
    def additional_attacks(self) -> Reason[Attack]:
        return self.check_modifiers(Mod.MOD_ADD_ATTACK)

    #########################################################################
    def add_ability(self, new_ability: BaseAbility):
        self._abilities.add(new_ability)

    #########################################################################
    @property
    def abilities(self) -> set[BaseAbility]:
        abils = self._abilities.copy()
        abils |= self.class_abilities()
        abils |= self.species.species_abilities()
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
        speeds = [self.species.speed]
        speeds.extend(link.value for link in self.check_modifiers(Mod.MOD_SET_MOVEMENT_SPEED))
        moves = {
            Movements.SPEED: Reason("Species", max(speeds)) | self.check_modifiers(Mod.MOD_ADD_MOVEMENT_SPEED),
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
    def ac(self) -> Reason[int]:
        result = self.armour.armour_class()
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
            ans.append((ascii_uppercase[num], prepared, safe(spell.name).title()))
        return ans

    #########################################################################
    def overflow_level_spells(self, spell_level: int) -> list[tuple[str, bool, str]]:
        ans = [("A", False, "---- Overflow Spells ----")]
        limit = self.spell_display_limits(spell_level)
        spell_count = 0
        for spell_num in range(limit - 1):
            tag = ascii_uppercase[spell_num + 1]  # +1 for space for overflow message
            try:
                spell = self.spells_of_level(spell_level)[spell_num + limit]
                prepared = spell in self.prepared_spells
                ans.append((tag, prepared, safe(spell.name).title()))
                spell_count += 1
            except IndexError:
                ans.append((tag, False, ""))

        if spell_count == 0:  # If no spells don't display overflow tag
            ans[0] = ("A", False, "")
        return ans

    #########################################################################
    def spell_display_limits(self, level: int) -> int:
        """How many spells we can display per level"""
        if self.half_spell_sheet():
            return {0: 12, 1: 26, 2: 19, 3: 19, 4: 19, 5: 19, 6: 0, 7: 0, 8: 0, 9: 0}[level]
        return {0: 8, 1: 13, 2: 13, 3: 13, 4: 13, 5: 9, 6: 9, 7: 9, 8: 7, 9: 7}[level]

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
        result = Reason[Any]()
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

        result = Reason[Any]()
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
                value = getattr(ability, modifier)(character=self)
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
    def weapon_proficiencies(self) -> Reason[Proficiency]:
        return self.check_modifiers(Mod.MOD_WEAPON_PROFICIENCY) | self.weapon_proficiency()

    #########################################################################
    def armour_proficiencies(self) -> set[Proficiency]:
        return self.check_modifiers(Mod.MOD_ARMOUR_PROFICIENCY) | self.armour_proficiency()

    #########################################################################
    def set_saving_throw_proficiency(self) -> None:
        for stat in Stat:  # type: ignore
            self.stats[stat].proficient = int(self.saving_throw_proficiency(stat))

    #############################################################################
    @property
    def tool_proficiencies(self) -> Reason[Tool]:
        """What tools the character is proficient with"""
        return self.check_modifiers(Mod.MOD_ADD_TOOL_PROFICIENCY)

    #############################################################################
    def spells_of_level(self, spell_level: int) -> list[Spells]:
        """Return list of (unique) spells known at spell_level"""
        return sorted({_.value for _ in self.known_spells if SPELL_LEVELS[_.value] == spell_level})

    #############################################################################
    def learn_spell(self, *spells: Spells):
        learnt = Reason[Spells]()
        for spell in spells:
            learnt |= Reason("Learnt", spell)
        self._known_spells |= learnt

    #############################################################################
    @property
    def known_spells(self) -> Reason[Spells]:
        """What spells the character knows"""
        return (
            self._known_spells
            | self.check_modifiers(Mod.MOD_ADD_KNOWN_SPELLS)
            | self.check_modifiers(Mod.MOD_ADD_PREPARED_SPELLS)  # All prepared spells must be known
        )

    #############################################################################
    def prepare_spells(self, *spells: Spells):
        for spell in set(spells):
            if spell not in self._known_spells:
                self._known_spells |= Reason("Prepared", spell)
        for spell in set(spells):
            self._prepared_spells |= Reason("Prepared", spell)

    #############################################################################
    @property
    def prepared_spells(self) -> Reason[Spells]:
        """What spells the character has prepared"""
        return self.check_modifiers(Mod.MOD_ADD_PREPARED_SPELLS) | self._prepared_spells

    #############################################################################
    @property
    def skills(self) -> Reason[Skill]:
        """What skills the character is proficient in"""
        return self._class_skills | self.check_modifiers(Mod.MOD_ADD_SKILL_PROFICIENCY)

    #############################################################################
    def lookup_skill(self, skill: Skill) -> CharacterSkill:
        origin = ""

        for _ in self.skills:
            if _.value == skill:
                origin = _.reason
        proficient = int(skill in self.skills)
        return CharacterSkill(skill, self, proficient, origin)

    #############################################################################
    def mod_add_attack(self, character: "Character") -> Reason[Attack]:
        return Reason()

    #############################################################################
    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason()

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
        return Reason()

    #############################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
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
        if "feat" not in kwargs:
            raise InvalidOption("Level 4 should specify a feat")
        self._add_level(self.level, **kwargs)

    #############################################################################
    def level5(self, **kwargs: Any):
        self.level = 5
        self._add_level(self.level, **kwargs)

    #########################################################################
    def _add_level(self, level: int, **kwargs):
        self._hp.append(Reason(f"level {level}", kwargs["hp"]))
        if "feat" in kwargs:
            self.add_feat(kwargs["feat"])
        if "ability" in kwargs:
            self.add_ability(kwargs["ability"])

    # EOF

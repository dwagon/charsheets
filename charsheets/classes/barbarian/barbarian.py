from typing import Optional, cast

from aenum import extend_enum

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature
from charsheets.features import WeaponMastery, ExtraAttack
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason


extend_enum(Feature, "BRUTAL_STRIKE", "Brutal Strike")
extend_enum(Feature, "DANGER_SENSE", "Danger Sense")
extend_enum(Feature, "FAST_MOVEMENT", "Fast Movement")
extend_enum(Feature, "FERAL_INSTINCT", "Feral Instinct")
extend_enum(Feature, "IMPROVED_BRUTAL_STRIKE", "Improved Brutal Strike")
extend_enum(Feature, "INSTINCTIVE_POUNCE", "Instinctive Pounce")
extend_enum(Feature, "PRIMAL_KNOWLEDGE", "Primal Knowledge")
extend_enum(Feature, "RAGE", "Rage")
extend_enum(Feature, "RECKLESS_ATTACK", "Reckless Attack")
extend_enum(Feature, "RELENTLESS_RAGE", "Relentless Rage")
extend_enum(Feature, "UNARMORED_DEFENSE_BARBARIAN", "Unarmored Defense")


#################################################################################
class Barbarian(Character):
    _base_skill_proficiencies = {
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INTIMIDATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 12

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    @property
    def rage_dmg_bonus(self) -> int:
        if self.level >= 16:
            return 4
        elif self.level >= 9:
            return 3
        return 2

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"""Rage Damage Bonus: {self.rage_dmg_bonus}

        Number of Rages: {self.num_rages}"""

    #############################################################################
    @property
    def num_rages(self) -> int:
        if self.level >= 17:
            return 6
        if self.level >= 12:
            return 5
        if self.level >= 6:
            return 4
        if self.level >= 3:
            return 3
        return 2

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason(
            "Barbarian",
            cast(Proficiency, Proficiency.SIMPLE_WEAPONS),
            cast(Proficiency, Proficiency.MARTIAL_WEAPONS),
        )

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason(
            "Barbarian",
            cast(Proficiency, Proficiency.SHIELDS),
            cast(Proficiency, Proficiency.LIGHT_ARMOUR),
            cast(Proficiency, Proficiency.MEDIUM_ARMOUR),
        )

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {UnarmoredDefenseBarbarian()}
        abilities.add(WeaponMastery())
        abilities.add(Rage())
        if self.level >= 2:
            abilities.add(DangerSense())
            abilities.add(RecklessAttack())
        if self.level >= 5:
            abilities.add(ExtraAttack())
            abilities.add(FastMovement())
        if self.level >= 7:
            abilities.add(FeralInstinct())
            abilities.add(InstinctivePounce())
        if self.level >= 9:
            abilities.add(BrutalStrike())
        if self.level >= 11:
            abilities.add(RelentlessRage())
        if self.level >= 13:
            abilities.add(ImprovedBrutalStrike())
        return abilities

    #############################################################################
    def spell_slots(self, level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


#############################################################################
class ImprovedBrutalStrike(BaseFeature):
    tag = Feature.IMPROVED_BRUTAL_STRIKE
    _desc = """You have honed new ways to attack furiously. The following effects are now among your Brutal Strike 
    options.

    Staggering Blow. The target has Disadvantage on the next saving throw it makes, and it can't make Opportunity 
    Attacks until the start of your next turn.

    Sundering Blow. Before the start of your next turn, the next attack roll made by another creature against the 
    target gains a +5 bonus to the roll. An attack roll can gain only one Sundering Blow bonus."""


#############################################################################
class UnarmoredDefenseBarbarian(BaseFeature):
    tag = Feature.UNARMORED_DEFENSE_BARBARIAN
    _desc = """While you aren't wearing any armor, your base Armor Class equals 10 plus your Constitution and Dexterity 
    modifiers. You can use a Shield and still gain this benefit."""


#############################################################################
class Rage(BaseFeature):
    tag = Feature.RAGE
    _desc = """Damage Resistance
    Rage Damage
    Strength Advantage"""


#############################################################################
class DangerSense(BaseFeature):
    tag = Feature.DANGER_SENSE
    _desc = """You gain an uncanny sense of when things aren't as they should be, giving you an edge when you 
    dodge perils. You have Advantage on Dexterity saving throws unless you have the Incapacitated condition."""


#############################################################################
class RecklessAttack(BaseFeature):
    tag = Feature.RECKLESS_ATTACK
    _desc = """When you make your first attack roll on your turn, you can decide to attack recklessly. Doing so
    gives you Advantage on attack rolls using Strength until the start of your next turn, but attack rolls against
    you have Advantage during that time."""


#############################################################################
class PrimalKnowledge(BaseFeature):
    tag = Feature.PRIMAL_KNOWLEDGE
    _desc = """You gain proficiency in one skill of your choice."""
    hide = True

    def __init__(self, skill: Skill):
        super().__init__()
        self.skill = skill

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Primal Knowledge", self.skill)


#############################################################################
class FastMovement(BaseFeature):
    tag = Feature.FAST_MOVEMENT
    _desc = """Your speed increases by 10 feet while you aren't wearing Heavy Armor."""

    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        # TODO - check for heavy armor and hide
        return Reason("Fast Movement", 10)


#############################################################################
class FeralInstinct(BaseFeature):
    tag = Feature.FERAL_INSTINCT
    _desc = """Your instincts are so honed that you have Advantage on Initiative rolls."""


#############################################################################
class InstinctivePounce(BaseFeature):
    tag = Feature.INSTINCTIVE_POUNCE
    _desc = """As part of the Bonus Action you take to enter your Rage, you can move up to half your Speed."""


#############################################################################
class BrutalStrike(BaseFeature):
    tag = Feature.BRUTAL_STRIKE
    _desc = """If you use Reckless Attack, you can forgo any Advantage on one Strength-based attack roll of your 
    choice on your turn. The chosen attack roll mustn’t have Disadvantage. If the chosen attack roll hits, 
    the target takes an extra 1d10 damage of the same type dealt by the weapon or Unarmed Strike, and you can cause 
    one Brutal Strike effect of your choice. You have the following effect options.

    Forceful Blow. The target is pushed 15 feet straight away from you. You can then move up to half your Speed 
    straight toward the target without provoking Opportunity Attacks.

    Hamstring Blow. The target’s Speed is reduced by 15 feet until the start of your next turn. A target can be 
    affected by only one Hamstring Blow at a time—the most recent one."""


#############################################################################
class RelentlessRage(BaseFeature):
    tag = Feature.RELENTLESS_RAGE
    _desc = """If you drop to O Hit Points while your Rage is active and don't die outright, you can make a DC 10 
    Constitution saving throw. If you succeed, your Hit Points instead change to a number equal to twice your 
    Barbarian level.

    Each time you use this feature after the first, the DC increases by 5. When you finish a Short or Long Rest, 
    the DC resets to 10."""


# EOF

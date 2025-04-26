from typing import Optional, cast, Any, TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, CharacterClass, Recovery
from charsheets.features import WeaponMastery, ExtraAttack
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "BRUTAL_STRIKE", "Brutal Strike")
extend_enum(Feature, "DANGER_SENSE", "Danger Sense")
extend_enum(Feature, "FAST_MOVEMENT", "Fast Movement")
extend_enum(Feature, "FERAL_INSTINCT", "Feral Instinct")
extend_enum(Feature, "IMPROVED_BRUTAL_STRIKE_L13", "Improved Brutal Strike")
extend_enum(Feature, "IMPROVED_BRUTAL_STRIKE_L17", "Improved Brutal Strike")
extend_enum(Feature, "INDOMITABLE_MIGHT", "Indomitable Might")
extend_enum(Feature, "INSTINCTIVE_POUNCE", "Instinctive Pounce")
extend_enum(Feature, "PERSISTENT_RAGE", "Persistent Rage")
extend_enum(Feature, "PRIMAL_CHAMPION", "Primal Champion")
extend_enum(Feature, "PRIMAL_KNOWLEDGE", "Primal Knowledge")
extend_enum(Feature, "RAGE", "Rage")
extend_enum(Feature, "RECKLESS_ATTACK", "Reckless Attack")
extend_enum(Feature, "RELENTLESS_RAGE", "Relentless Rage")
extend_enum(Feature, "UNARMORED_DEFENSE_BARBARIAN", "Unarmored Defense")


#################################################################################
class Barbarian(BaseClass):
    _base_skill_proficiencies = {
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INTIMIDATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    }

    _base_class = CharacterClass.BARBARIAN
    _class_name = "Barbarian"

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
        assert self.character is not None
        barb_level = self.character.highest_level(CharacterClass.BARBARIAN)
        if barb_level is None:  # pragma: no coverage
            return 0
        if barb_level.level >= 16:
            return 4
        elif barb_level.level >= 9:
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
        assert self.character is not None
        barb_level = self.character.highest_level(CharacterClass.BARBARIAN)
        if barb_level is None:  # pragma: no coverage
            return 0
        if barb_level.level >= 17:
            return 6
        if barb_level.level >= 12:
            return 5
        if barb_level.level >= 6:
            return 4
        if barb_level.level >= 3:
            return 3
        return 2

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.set_saving_throw_proficiency(Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(UnarmoredDefenseBarbarian())
        self.add_feature(WeaponMastery())
        self.add_feature(Rage())
        self.character.add_weapon_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.add_armor_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.SHIELDS)))

    #############################################################################
    def level2(self, **kwargs: Any):
        self.add_feature(DangerSense())
        self.add_feature(RecklessAttack())

    #############################################################################
    def level5(self, **kwargs: Any):
        self.add_feature(ExtraAttack())
        self.add_feature(FastMovement())

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(FeralInstinct())
        self.add_feature(InstinctivePounce())

    #############################################################################
    def level9(self, **kwargs: Any):
        self.add_feature(BrutalStrike())

    #############################################################################
    def level11(self, **kwargs: Any):
        self.add_feature(RelentlessRage())

    #############################################################################
    def level13(self, **kwargs: Any):
        self.add_feature(ImprovedBrutalStrike13())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(PersistentRage())

    #############################################################################
    def level17(self, **kwargs: Any):
        self.add_feature(ImprovedBrutalStrike17())

    #############################################################################
    def level18(self, **kwargs: Any):
        self.add_feature(IndomitableMight())

    #############################################################################
    def level20(self, **kwargs: Any):
        self.add_feature(PrimalChampion())

    #############################################################################
    def spell_slots(self, level: int) -> int:
        return 0


#############################################################################
class ImprovedBrutalStrike17(BaseFeature):
    tag = Feature.IMPROVED_BRUTAL_STRIKE_L17
    hide = True


#############################################################################
class ImprovedBrutalStrike13(BaseFeature):
    tag = Feature.IMPROVED_BRUTAL_STRIKE_L13

    @property
    def desc(self) -> str:
        return """The following effects are now among your Brutal Strike options.

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
    recovery = Recovery.PARTIAL

    @property
    def desc(self) -> str:
        assert self.owner.barbarian is not None

        return f"""You can enter it as a Bonus Action if you aren't wearing Heavy armor.

        While active, your Rage follows the rules below. 
        
        Damage Resistance. You have Resistance to Bludgeoning, Piercing, and Slashing damage. 
        
        Rage Damage. When you make an attack using Strength - with either a weapon or an Unarmed Strike - and deal 
        damage to the target, add {self.owner.barbarian.rage_dmg_bonus} damage.
        
        Strength Advantage. You have Advantage on Strength checks and Strength saving throws. 
        
        No Concentration or Spells. You can't maintain Concentration, and you can't cast spells. 
        
        Duration. The Rage lasts until the end of your next turn, and it ends early if you don Heavy armor or have 
        the Incapacitated condition. If your Rage is still active on your next turn, you can extend the Rage for 
        another round by doing one of the following:

        Make an attack roll against an enemy.
        Force an enemy to make a saving throw. 
        Take a Bonus Action to extend your Rage. 
        
        Each time the Rage is extended, it lasts until the end of your next turn. You can maintain 
        a Rage for up to 10 minutes."""

    @property
    def goes(self) -> int:
        assert self.owner.barbarian is not None
        return self.owner.barbarian.num_rages


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

    @property
    def desc(self) -> str:
        assert self.owner.barbarian is not None
        dmg = 2 if self.owner.barbarian.level >= 17 else 1  # Lvl 17 Improved Brutal Strike
        num = "two" if self.owner.barbarian.level >= 17 else "one"  # Lvl 17 Improved Brutal Strike

        return f"""If you use Reckless Attack, you can forgo any Advantage on one Strength-based attack roll of your 
    choice on your turn. The chosen attack roll mustn’t have Disadvantage. If the chosen attack roll hits, 
    the target takes an extra {dmg}d10 damage of the same type dealt by the weapon or Unarmed Strike, and you can cause 
    {num} Brutal Strike effect of your choice. You have the following effect options.

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


#############################################################################
class PersistentRage(BaseFeature):
    tag = Feature.PERSISTENT_RAGE
    recovery = Recovery.LONG_REST
    _desc = """When you roll Initiative, you can regain all expended uses of Rage. After you regain uses of Rage in 
    this way, you can't do so again until you finish a Long Rest.

    In addition, your Rage is so fierce that it now lasts for 10 minutes without you needing to do anything to extend 
    it from round to round. Your Rage ends early if you have the Unconscious condition (not just the Incapacitated 
    condition) or don Heavy armor."""


#############################################################################
class IndomitableMight(BaseFeature):
    tag = Feature.INDOMITABLE_MIGHT
    _desc = """If your total for a Strength check or Strength saving throw is less than your Strength score, you can
            use that score in place of the total."""


#############################################################################
class PrimalChampion(BaseFeature):
    tag = Feature.PRIMAL_CHAMPION
    _desc = """You embody primal power. Your Strength and Constitution scores increase by 4, to a maximum of 25."""


# EOF

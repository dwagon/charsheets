from typing import Optional, Any, cast, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.weapons.base_weapon import BaseWeapon

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "FIGHTING_STYLE_FIGHTER14", "Fighting Style")
extend_enum(Feature, "SECOND_WIND14", "Second Wind")


#################################################################################
class FightingStyle(BaseFeature):
    pass


#############################################################################
class Archery(FightingStyle):
    tag = Feature.ARCHERY
    desc = """You gain a +2 bonus to attack rolls you make with Ranged weapons."""
    hide = True

    def mod_ranged_atk_bonus(self, _: BaseWeapon, character: "BaseCharacter"):
        return 2


#############################################################################
class Defense(FightingStyle):
    tag = Feature.DEFENSE
    desc = """While you're wearing armour, you gain a +1 bonus to AC."""
    hide = True

    def mod_ac_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Defense", 1)


#############################################################################
class Dueling(FightingStyle):
    tag = Feature.DUELING
    desc = """When you're holding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage 
    rolls with that weapon."""


#############################################################################
class GreatWeaponFighting(FightingStyle):
    tag = Feature.GREAT_WEAPON_FIGHTING
    desc = """When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding 
    with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon 
    must have the two-handed or versatile property for you to gain this benefit."""


#############################################################################
class Protection(FightingStyle):
    tag = Feature.PROTECTION
    desc = """When a creature you can see attacks a target other than you that is within 5 feet of you, you can use 
    your reaction to impose disadvantage on the attack roll. You must be wielding a shield."""


#############################################################################
class TwoWeaponFighting(FightingStyle):
    tag = Feature.TWO_WEAPON_FIGHTING
    desc = """When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second 
    attack."""


#################################################################################
class Fighter(BaseClass):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    }
    _base_class = CharacterClass.FIGHTER
    _class_name = "Fighter"

    #################################################################################
    def __init__(self, **kwargs: Any):
        self.fighting_styles: list[BaseFeature] = []
        super().__init__(**kwargs)

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.SIMPLE_WEAPONS)))
        self.character.add_weapon_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.SHIELDS)))
        self.add_feature(SecondWind())
        self.add_feature(FightingStyleFighter())
        if "style" not in kwargs:
            raise InvalidOption("Level 1 fighters get a Fighting Style. 'style=...'")
        assert isinstance(kwargs["style"], FightingStyle)
        self.add_feature(kwargs["style"])

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0


#############################################################################
class FightingStyleFighter(BaseFeature):
    tag = Feature.FIGHTING_STYLE_FIGHTER
    hide = True
    _desc = """You adopt a particular style of fighting as your speciality"""


#############################################################################
class SecondWind(BaseFeature):
    tag = Feature.SECOND_WIND14
    recovery = Recovery.SHORT_REST
    _goes = 1
    _desc = """As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter Level."""


# EOF

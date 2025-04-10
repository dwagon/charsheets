from typing import Optional, Any, cast

from aenum import extend_enum

from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features import WeaponMastery, ExtraAttack
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

extend_enum(Feature, "ACTION_SURGE", "Action Surge")
extend_enum(Feature, "FIGHTING_STYLE_FIGHTER", "Fighting Style")
extend_enum(Feature, "INDOMITABLE", "Indomitable")
extend_enum(Feature, "SECOND_WIND", "Second Wind")
extend_enum(Feature, "STUDIED_ATTACKS", "Studied Attacks")
extend_enum(Feature, "TACTICAL_MASTER", "Tactical Master")
extend_enum(Feature, "TACTICAL_MIND", "Tactical Mind")
extend_enum(Feature, "TACTICAL_SHIFT", "Tactical Shift")


#################################################################################
class Fighter(BaseClass):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.PERSUASION,
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
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.set_saving_throw_proficiency(Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Fighter", cast(Proficiency, Proficiency.SHIELDS)))
        self.add_feature(WeaponMastery(self.num_weapon_mastery))
        self.add_feature(ActionSurge())
        self.add_feature(SecondWind())
        self.add_feature(FightingStyleFighter())
        if "style" not in kwargs:
            raise InvalidOption("Level 1 fighters get a Fighting Style. 'style=...'")

    #############################################################################
    def every_level(self, **kwargs: Any):
        if style := kwargs.get("add_style"):
            self.add_style(style)
        if style := kwargs.get("style"):
            self.add_style(style)
        if style := kwargs.get("remove_style"):
            self.remove_style(style)

    #########################################################################
    def add_style(self, style: BaseFeature):
        assert self.character is not None
        style.owner = self.character
        self.fighting_styles.append(style)
        self.add_feature(style)

    #########################################################################
    def remove_style(self, style: BaseFeature):
        assert self.character is not None
        remove_tag = style.tag
        for fighting_style in self.fighting_styles[:]:
            if fighting_style.tag == remove_tag:
                self.fighting_styles.remove(fighting_style)
                break
        for feature in self.character.features:
            if feature.tag == remove_tag:
                self.character.remove_feature(feature)
                break
        else:
            raise InvalidOption(f"Trying to remove a style {style} that doesn't exist")

    #############################################################################
    def level2(self, **kwargs: Any):
        self.add_feature(TacticalMind())

    #############################################################################
    def level5(self, **kwargs: Any):
        self.add_feature(ExtraAttack())
        self.add_feature(TacticalShift())

    #############################################################################
    def level6(self, **kwargs: Any):
        if "feat" not in kwargs:
            raise InvalidOption("Level 6 fighter should specify a feat")

    #############################################################################
    def level9(self, **kwargs: Any):
        self.add_feature(Indomitable())
        self.add_feature(TacticalMaster())

    #############################################################################
    def level11(self, **kwargs: Any):
        assert self.character is not None
        for feature in self.character.features:
            if feature.tag == Feature.EXTRA_ATTACK:
                feature = cast(ExtraAttack, feature)
                feature.number_str = "three times"
                break

    #############################################################################
    def level13(self, **kwargs: Any):
        self.add_feature(StudiedAttacks())

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    @property
    def num_weapon_mastery(self) -> int:
        if self.level >= 16:
            return 6
        elif self.level >= 10:
            return 5
        elif self.level >= 4:
            return 4
        return 3

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


#############################################################################
class FightingStyleFighter(BaseFeature):
    tag = Feature.FIGHTING_STYLE_FIGHTER
    hide = True
    _desc = """You have honed your martial prowess and gain a Fighting Style feat of your choice.
    
    Whenever you gain a Fighter level, you can replace the feat you chose with a different Fighting Style feat."""


#############################################################################
class StudiedAttacks(BaseFeature):
    tag = Feature.STUDIED_ATTACKS
    _desc = """If you make an attack roll against a creature and miss, you have Advantage on your next attack roll 
    against that creature before the end of your next turn."""


############################################################################
class ActionSurge(BaseFeature):
    tag = Feature.ACTION_SURGE
    recovery = Recovery.SHORT_REST
    goes = 1
    _desc = """You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional
    action, except the Magic action."""


#############################################################################
class SecondWind(BaseFeature):
    tag = Feature.SECOND_WIND
    recovery = Recovery.PARTIAL

    @property
    def goes(self) -> int:
        if self.owner.level >= 10:
            return 4
        elif self.owner.level >= 4:
            return 3
        return 2

    @property
    def desc(self) -> str:
        return """You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action,
        you can use it to regain Hit Points equal to 1d10 plus your Fighter Level."""


############################################################################
class TacticalMind(BaseFeature):
    tag = Feature.TACTICAL_MIND
    _desc = """You have a mind for tactics on and off the battlefield. When you fail an ability check you can expend
     a use of your Second Wind to push yourself toward success. Rather than regaining Hit Points, you roll 1d10 and add
     the number rolled to the ability check, potentially turning it into a success. If the check still fails, this use
     of Second Wind isn't expended.
    """


############################################################################
class TacticalShift(BaseFeature):
    tag = Feature.TACTICAL_SHIFT
    _desc = """Whenever you activate your Second Wind with a Bonus Action, you can move up to half your Speed without
    provoking Opportunity Attacks."""


############################################################################
class Indomitable(BaseFeature):
    tag = Feature.INDOMITABLE
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        if self.owner.level >= 17:
            return 3
        elif self.owner.level >= 13:
            return 2
        return 1

    @property
    def desc(self) -> str:
        return f"""If you fail a saving throw, you can reroll it with a bonus of {self.owner.fighter.level}. You must use the 
        new roll."""


############################################################################
class TacticalMaster(BaseFeature):
    tag = Feature.TACTICAL_MASTER
    _desc = """When you attack with a weapon whose mastery property you can use, you can replace that property with 
    the Push, Sap, or Slow property for that attack."""


# EOF

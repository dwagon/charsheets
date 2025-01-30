from typing import Optional, Any

from charsheets.features import WeaponMastery, ExtraAttack
from charsheets.features.base_feature import BaseFeature
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature
from charsheets.exception import InvalidOption
from charsheets.reason import Reason


#################################################################################
class Fighter(Character):
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

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    def fighting_style(self, style: BaseFeature):
        self.add_feature(style)

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.LIGHT_ARMOUR, Proficiency.MEDIUM_ARMOUR, Proficiency.HEAVY_ARMOUR, Proficiency.SHIELDS)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {WeaponMastery(self.num_weapon_mastery), ActionSurge(), SecondWind(), FightingStyleFighter()}

        if self.level >= 2:
            abilities.add(TacticalMind())
        if self.level >= 5:
            abilities.add(ExtraAttack())
            abilities.add(TacticalShift())
        return abilities

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
    def level6(self, **kwargs: Any):
        if "feat" not in kwargs:
            raise InvalidOption("Level 6 fighter should specify a feat")
        self._add_level(6, **kwargs)


#############################################################################
class FightingStyleFighter(BaseFeature):
    tag = Feature.FIGHTING_STYLE_FIGHTER
    _desc = """You have honed your martial prowess and gain a Fighting Style feat of your choice.
    
    Whenever you gain a Fighter level, you can replace the feat you chose with a different Fighting Style feat."""


############################################################################
class ActionSurge(BaseFeature):
    tag = Feature.ACTION_SURGE
    goes = 1
    _desc = """You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional
    action, except the Magic action.

    Once you use this feature, you can't do so again until you finish a Short or Long Rest.
    """


#############################################################################
class SecondWind(BaseFeature):
    tag = Feature.SECOND_WIND

    @property
    def goes(self) -> int:
        if self.owner.level >= 10:
            return 4
        elif self.owner.level >= 4:
            return 3
        return 2

    @property
    def desc(self) -> str:
        return f"""You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action,
        you can use it to regain Hit Points equal to 1d10 plus your Fighter Level.

        You can use this feature {self.goes} times. You regain one expended use when you finish a Short Rest, and 
        you regain all expended uses when you finish a Long Rest.
        """


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


# EOF

from enum import StrEnum, auto
from typing import Any, cast

from charsheets.abilities import CombatSuperiority, StudentOfWar
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.fighter import Fighter
from charsheets.constants import Tool, Skill
from charsheets.exception import InvalidOption


#############################################################################
class BattleManeuver(StrEnum):
    AMBUSH = auto()
    BAIT_AND_SWITCH = auto()
    COMMANDERS_STRIKE = auto()
    COMMANDING_PRESENCE = auto()
    DISARMING_ATTACK = auto()
    DISTRACTING_STRIKE = auto()
    EVASIVE_FOOTWORK = auto()
    FEINTING_ATTACK = auto()
    GOADING_ATTACK = auto()
    LUNGING_ATTACK = auto()
    MANEUVERING_ATTACK = auto()
    MENACING_ATTACK = auto()
    NONE = auto()
    PARRY = auto()
    PRECISION_ATTACK = auto()
    PUSHING_ATTACK = auto()
    RALLY = auto()
    RIPOSTE = auto()
    SWEEPING_ATTACK = auto()
    TACTICAL_ASSESSMENT = auto()
    TRIP_ATTACK = auto()


#############################################################################
class BaseManeuver:
    _desc = "Unspecified"
    tag: BattleManeuver = BattleManeuver.NONE

    #############################################################################
    @property
    def desc(self) -> str:
        return self._desc


#############################################################################
class Ambush(BaseManeuver):
    tag = BattleManeuver.AMBUSH
    _desc = """Ambush"""


#############################################################################
class BaitAndSwitch(BaseManeuver):
    tag = BattleManeuver.BAIT_AND_SWITCH
    _desc = """Bait and Switch"""


#############################################################################
class CommandersStrike(BaseManeuver):
    tag = BattleManeuver.COMMANDERS_STRIKE
    _desc = """Commander's Strike"""


#############################################################################
class CommandingPresence(BaseManeuver):
    tag = BattleManeuver.COMMANDING_PRESENCE
    _desc = """Commanding Presence"""


#############################################################################
class DisarmingAttack(BaseManeuver):
    tag = BattleManeuver.DISARMING_ATTACK
    _desc = """Disarming Attack"""


#############################################################################
class DistractingStrike(BaseManeuver):
    tag = BattleManeuver.DISTRACTING_STRIKE
    _desc = """Distracting Strike"""


#############################################################################
class EvasiveFootwork(BaseManeuver):
    tag = BattleManeuver.EVASIVE_FOOTWORK
    _desc = """Evasive Footwork"""


#############################################################################
class FeintingAttack(BaseManeuver):
    tag = BattleManeuver.FEINTING_ATTACK
    _desc = """Feinting Attack"""


#############################################################################
class GoadingAttack(BaseManeuver):
    tag = BattleManeuver.GOADING_ATTACK
    _desc = """Goading Attack"""


#############################################################################
class LungingAttack(BaseManeuver):
    tag = BattleManeuver.LUNGING_ATTACK
    _desc = """Lunging Attack"""


#############################################################################
class ManeuveringAttack(BaseManeuver):
    tag = BattleManeuver.MANEUVERING_ATTACK
    _desc = """Maneuvering Attack"""


#############################################################################
class MenacingAttack(BaseManeuver):
    tag = BattleManeuver.MENACING_ATTACK
    _desc = """Menacing Attack"""


#############################################################################
class Parry(BaseManeuver):
    tag = BattleManeuver.PARRY
    _desc = """Parry"""


#############################################################################
class PrecisionAttack(BaseManeuver):
    tag = BattleManeuver.PRECISION_ATTACK
    _desc = """Precision Attack"""


#############################################################################
class PushingAttack(BaseManeuver):
    tag = BattleManeuver.PUSHING_ATTACK
    _desc = """Pushing Attack"""


#############################################################################
class Rally(BaseManeuver):
    tag = BattleManeuver.RALLY
    _desc = """Rally"""


#############################################################################
class Riposte(BaseManeuver):
    tag = BattleManeuver.RIPOSTE
    _desc = """Riposte"""


#############################################################################
class SweepingAttack(BaseManeuver):
    tag = BattleManeuver.SWEEPING_ATTACK
    _desc = """Sweeping Attack"""


#############################################################################
class TacticalAssessment(BaseManeuver):
    tag = BattleManeuver.TACTICAL_ASSESSMENT
    _desc = """Tactical Assessment"""


#############################################################################
class TripAttack(BaseManeuver):
    tag = BattleManeuver.TRIP_ATTACK
    _desc = """Trip Attack"""


#################################################################################
class FighterBattleMaster(Fighter):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._class_name = "Battle Master"
        self.maneuvers: set[BaseManeuver] = set()
        if "student_tool" in kwargs:
            self._tool = cast(Tool, kwargs.get("student_tool"))
        else:
            raise InvalidOption("Battle Master need to define a tool for Student of War")
        if "student_skill" in kwargs:
            self._skill = cast(Skill, kwargs.get("student_skill"))
        else:
            raise InvalidOption("Battle Master need to define a skill for Student of War")

    #############################################################################
    @property
    def superiority_dice(self) -> int:
        if self.level >= 15:
            return 6
        elif self.level >= 7:
            return 5
        return 4

    #############################################################################
    def add_maneuver(self, *maneuvers: BaseManeuver) -> None:
        for maneuver in maneuvers:
            self.maneuvers.add(maneuver)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {CombatSuperiority(), StudentOfWar(self._tool, self._skill)}
        return abilities

    #############################################################################
    @property
    def class_special(self) -> str:
        ans = f"Superiority Dice: {self.superiority_dice}\n\n"
        for maneuver in self.maneuvers:
            ans += maneuver.desc
            ans += "\n\n"
        return ans


# EOF

from enum import StrEnum, auto
from typing import Any

from charsheets.classes.fighter import Fighter
from charsheets.constants import Ability, CharSubclassName
from charsheets.util import do_import


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

    @property
    def desc(self) -> str:
        if hasattr(self, "dynamic_desc"):
            return getattr(self, "dynamic_desc")()
        else:
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


#############################################################################
MANEUVER_MAP: dict[BattleManeuver, BaseManeuver] = {
    BattleManeuver.AMBUSH: Ambush(),
    BattleManeuver.BAIT_AND_SWITCH: BaitAndSwitch(),
    BattleManeuver.COMMANDERS_STRIKE: CommandersStrike(),
    BattleManeuver.COMMANDING_PRESENCE: CommandingPresence(),
    BattleManeuver.DISARMING_ATTACK: DisarmingAttack(),
    BattleManeuver.DISTRACTING_STRIKE: DistractingStrike(),
    BattleManeuver.EVASIVE_FOOTWORK: EvasiveFootwork(),
    BattleManeuver.FEINTING_ATTACK: FeintingAttack(),
    BattleManeuver.GOADING_ATTACK: GoadingAttack(),
    BattleManeuver.LUNGING_ATTACK: LungingAttack(),
    BattleManeuver.MANEUVERING_ATTACK: ManeuveringAttack(),
    BattleManeuver.MENACING_ATTACK: MenacingAttack(),
    BattleManeuver.PARRY: Parry(),
    BattleManeuver.PRECISION_ATTACK: PrecisionAttack(),
    BattleManeuver.PUSHING_ATTACK: PushingAttack(),
    BattleManeuver.RALLY: Rally(),
    BattleManeuver.RIPOSTE: Riposte(),
    BattleManeuver.SWEEPING_ATTACK: SweepingAttack(),
    BattleManeuver.TACTICAL_ASSESSMENT: TacticalAssessment(),
    BattleManeuver.TRIP_ATTACK: TripAttack(),
}


#################################################################################
class BattleMaster(Fighter):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.set_sub_class(CharSubclassName.BATTLE_MASTER)
        self.superiority_dice: int = self.num_superiority_dice()
        self.maneuvers: set[BattleManeuver] = {BattleManeuver.NONE}

    #############################################################################
    def num_superiority_dice(self) -> int:
        if self.level >= 15:
            return 6
        elif self.level >= 7:
            return 5
        return 4

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.COMBAT_SUPERIORITY, Ability.STUDENT_OF_WAR}
        return abilities

    #############################################################################
    @property
    def class_special(self) -> str:
        ans = f"Superiority Dice: {self.superiority_dice}\n"
        for maneuver in self.maneuvers:
            ans += MANEUVER_MAP[maneuver].desc
            ans += "\n"
        return ans


# EOF

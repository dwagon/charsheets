from enum import StrEnum, auto
from typing import Any, cast
from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.fighter import Fighter
from charsheets.constants import Tool, Skill, Ability, ARTISAN_TOOLS
from charsheets.exception import InvalidOption
from charsheets.reason import Reason
from charsheets.util import safe

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


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
    _desc = """When you make a Dexterity (Stealth) check or an Initiative roll, you can expend one Superiority Die 
    and add teh die to the roll, unless you have the Incapacitated condition."""


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
    _desc = """As a Bonus Action, you can expend one Superiority Die to feint, choosing one creature within 5 feet of 
    yourself as your target. You have Advantage on your next attack roll against that target this turn. If that 
    attack hits, add the Superiority Die to the attack's damage roll."""


#############################################################################
class GoadingAttack(BaseManeuver):
    tag = BattleManeuver.GOADING_ATTACK
    _desc = """When you hit a creature with an attack roll, you can expend one Superiority die to attempt to goad the 
    target into attacking you. Add the Superiority Die to the attack's damage roll. The target must succeed on a 
    Wisdom saving throw or have Disadvantage on attack rolls against targets other than you until the end of your 
    next turn."""


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
    _desc = """When a creature misses you with a melee attack roll, you can take a Reaction and expend one 
    Superiority Die to make a melee attack roll with a weapon or an Unarmed Strike against the creature. If you hit, 
    add the Superiority Die to the attack's damage."""


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
    def num_superiority_dice(self) -> int:
        if self.level >= 15:
            return 6
        elif self.level >= 7:
            return 5
        return 4

    #############################################################################
    @property
    def type_superiority_dice(self) -> str:
        if self.level >= 18:  # Ultimate Combat Superiority
            return "d12"
        if self.level >= 10:  # Improved Combat Superiority
            return "d10"
        return "d8"

    #############################################################################
    def add_maneuver(self, *maneuvers: BaseManeuver) -> None:
        for maneuver in maneuvers:
            self.maneuvers.add(maneuver)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {CombatSuperiority(), StudentOfWar(self._tool, self._skill)}
        if self.level >= 7:
            abilities |= {KnowYourEnemy()}
        return abilities

    #############################################################################
    @property
    def class_special(self) -> str:
        ans = f"Superiority Dice: {self.num_superiority_dice}{self.type_superiority_dice}\n\n"
        for maneuver in self.maneuvers:
            ans += f"{safe(maneuver.tag).title()}: {maneuver.desc}\n\n"
        return ans


############################################################################
class CombatSuperiority(BaseAbility):
    tag = Ability.COMBAT_SUPERIORITY

    @property
    def goes(self) -> int:
        return self.owner.num_superiority_dice

    @property
    def desc(self) -> str:
        return f"""Your experience on the battlefield has redefined your fighting techniques. You learn maneuvers that
    are fueled by special dice called Superiority Dice.

    Superiority Dice. You have {self.owner.num_superiority_dice} Superiority Dice, which are 
    {self.owner.type_superiority_dice}. A Superiority Die is expended when you use it. You regain all expended
    Superiority Dice when you finish a Short or Long Rest.

    Saving Throws. If a maneuver requires a saving throw, the DC equals 8 plus your Strength or Dexterity modifier 
    (your choice) and Proficiency Bonus."""


############################################################################
class StudentOfWar(BaseAbility):
    tag = Ability.STUDENT_OF_WAR
    _desc = """You gain proficiency with one type of Artisan's Tools of your choice, and you gain proficiency in
    one skill of your choice from the skills available to Fighters at level 1."""
    hide = True

    def __init__(self, tool: Tool, skill: Skill):
        self._tool = tool
        self._skill = skill

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        if self._skill not in character._base_skill_proficiencies:
            raise InvalidOption(f"Student of War: {self._skill} not a valid choice: {character._base_skill_proficiencies}")
        return Reason("Student of War", self._skill)

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        if self._tool not in ARTISAN_TOOLS:
            raise InvalidOption(f"Student of War: {self._tool} not a valid choice: {ARTISAN_TOOLS}")
        return Reason("Student of War", self._tool)


############################################################################
class KnowYourEnemy(BaseAbility):
    tag = Ability.KNOW_YOUR_ENEMY
    _goes = 1
    _desc = """As a Bonus Action, you can discern certain strengths and weaknesses of a creature you can see within 
    30 feet of yourself; you know whether that creature has any Immunities, Resistances, or Vulnerabilities, 
    and if the creature has any, you known what they are.
    
    Once you use this feature, you can't do so again until you finish a Long Rest. You can also restore a use of the 
    feature by expending one Superiority Dice (no action required)."""


# EOF

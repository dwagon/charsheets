from enum import StrEnum, auto
from typing import Any, Iterable
from typing import TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes.fighter import Fighter
from charsheets.constants import Tool, Skill, Feature, ARTISAN_TOOLS, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.util import safe

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "COMBAT_SUPERIORITY", "Combat Superiority")
extend_enum(Feature, "KNOW_YOUR_ENEMY", "Know your Enemy")
extend_enum(Feature, "RELENTLESS", "Relentless")
extend_enum(Feature, "STUDENT_OF_WAR", "Student of War")


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
    and add the die to the roll, unless you have the Incapacitated condition."""


#############################################################################
class BaitAndSwitch(BaseManeuver):
    tag = BattleManeuver.BAIT_AND_SWITCH
    _desc = """When you're within 5 feet of a creature on your turn, you can expend one Superiority 
    Die and switch places with that creature, provided you spend at least 5 feet of movement and the creature is 
    willing and doesn't have the Incapacitated condition. This movement doesn't provoke Opportunity Attacks.

    Roll the Superiority Die. Until the start of your next turn, you or the other creature (your choice) gains a 
    bonus to AC equal to the number rolled."""


#############################################################################
class CommandersStrike(BaseManeuver):
    tag = BattleManeuver.COMMANDERS_STRIKE
    _desc = """When you take the Attack action on your turn, you can replace one of your attacks to direct one of 
    your companions to strike. When you do so, choose a willing creature who can see or hear you and expend one 
    Superiority Die. That creature can immediately use its Reaction to make one attack with a weapon or an Unarmed 
    Strike, adding the Superiority Die to the attack's damage roll on a hit."""


#############################################################################
class CommandingPresence(BaseManeuver):
    tag = BattleManeuver.COMMANDING_PRESENCE
    _desc = """When you make a Charisma (Intimidation, Performance, or Persuasion) check, you can expend one 
            Superiority Die and add that die to the roll."""


#############################################################################
class DisarmingAttack(BaseManeuver):
    tag = BattleManeuver.DISARMING_ATTACK
    _desc = """When you hit a creature with an attack roll, you can expend one Superiority Die to attempt to disarm 
    the target. Add the Superiority Die roll to the attack's damage roll. The target must succeed on a Strength 
    saving throw or drop one object of your choice that it's holding, with the object landing in its space."""


#############################################################################
class DistractingStrike(BaseManeuver):
    tag = BattleManeuver.DISTRACTING_STRIKE
    _desc = """When you hit a creature with an attack roll, you can expend one Superiority Die to distract the 
    target. Add the Superiority Die roll to the attack's damage roll. The next attack roll against the target by an 
    attacker other than you has Advantage if the attack is made before the start of your next turn."""


#############################################################################
class EvasiveFootwork(BaseManeuver):
    tag = BattleManeuver.EVASIVE_FOOTWORK
    _desc = """As a Bonus Action, you can expend one Superiority Die and take the Disengage action. You also roll the 
    die and add the number rolled to your AC until the start of your next turn."""


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
    _desc = """As a Bonus Action, you can expend one Superiority Die and take the Dash action. If you move at least 5 
    feet in a straight line immediately before hitting with a melee attack as part of the Attack action on this turn, 
    you can add the Superiority Die to the attack's damage roll."""


#############################################################################
class ManeuveringAttack(BaseManeuver):
    tag = BattleManeuver.MANEUVERING_ATTACK
    _desc = """When you hit a creature with an attack roll, you can expend one Superiority Die to maneuver one of 
    your comrades into another position. Add the Superiority Die roll to the attack's damage roll, and choose a 
    willing creature who can see or hear you. That creature can use its Reaction to move up to half its Speed without 
    provoking an Opportunity Attack from the target of your attack."""


#############################################################################
class MenacingAttack(BaseManeuver):
    tag = BattleManeuver.MENACING_ATTACK
    _desc = """When you hit a creature with an attack roll, you can expend one Superiority Die to attempt to frighten 
    the target. Add the Superiority Die to the attack's damage roll. The target must succeed on a Wisdom saving throw 
    or have the Frightened condition until the end of your next turn. Parry."""


#############################################################################
class Parry(BaseManeuver):
    tag = BattleManeuver.PARRY
    _desc = """When another creature damages you with a melee attack roll, you can take a Reaction and expend one 
    Superiority Die to reduce the damage by the number you roll on your Superiority Die plus your Strength or 
    Dexterity modifier (your choice)."""


#############################################################################
class PrecisionAttack(BaseManeuver):
    tag = BattleManeuver.PRECISION_ATTACK
    _desc = """When you miss with an attack roll, you can expend one Superiority Die, roll that die, and add it to 
    the attack roll, potentially causing the attack to hit."""


#############################################################################
class PushingAttack(BaseManeuver):
    tag = BattleManeuver.PUSHING_ATTACK
    _desc = """When you hit a creature with an attack roll using a weapon or an Unarmed Strike, you can expend one 
    Superiority Die to attempt to drive the target back. Add the Superiority Die to the attack's damage roll. If the 
    target is Large or smaller, it must succeed on a Strength saving throw or be pushed up to 15 feet directly away 
    from you."""


#############################################################################
class Rally(BaseManeuver):
    tag = BattleManeuver.RALLY
    _desc = """As a Bonus Action, you can expend one Superiority Die to bolster the resolve of a companion. Choose an 
    ally of yours within 30 feet of yourself who can see or hear you. That creature gains Temporary Hit Points equal 
    to the Superiority Die roll plus half your Fighter level (round down)."""


#############################################################################
class Riposte(BaseManeuver):
    tag = BattleManeuver.RIPOSTE
    _desc = """When a creature misses you with a melee attack roll, you can take a Reaction and expend one 
    Superiority Die to make a melee attack roll with a weapon or an Unarmed Strike against the creature. If you hit, 
    add the Superiority Die to the attack's damage."""


#############################################################################
class SweepingAttack(BaseManeuver):
    tag = BattleManeuver.SWEEPING_ATTACK
    _desc = """When you hit a creature with a melee attack roll using a weapon or an Unarmed Strike, you can expend 
    one Superiority Die to attempt to damage another creature. Choose another creature within 5 feet of the original 
    target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to 
    the number you roll on your Superiority Die. The damage is of the same type dealt by the original attack."""


#############################################################################
class TacticalAssessment(BaseManeuver):
    tag = BattleManeuver.TACTICAL_ASSESSMENT
    _desc = """When you make an Intelligence (History or Investigation) check or a Wisdom (Insight) check, 
    you can expend one Superiority Die and add that die to the ability check."""


#############################################################################
class TripAttack(BaseManeuver):
    tag = BattleManeuver.TRIP_ATTACK
    _desc = """When you hit a creature with an attack roll using a weapon or an Unarmed Strike, you can expend one 
    Superiority Die and add the die to the attack's damage roll. If the target is Large or smaller, it must succeed 
    on a Strength saving throw or have the Prone condition"""


#################################################################################
class FighterBattleMaster(Fighter):
    _class_name = "Battle Master"
    _sub_class = CharacterClass.FIGHTER

    #############################################################################
    def level3(self, **kwargs: Any):
        assert self.character is not None
        if not isinstance(kwargs.get("student"), StudentOfWar):
            raise InvalidOption("Need to specify Student of War with 'student=StudentOfWar()'")
        self.add_feature(CombatSuperiority())
        self.add_feature(kwargs["student"])
        self.character.specials[CharacterClass.FIGHTER] = set()

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(KnowYourEnemy())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(Relentless())

    #############################################################################
    def every_level(self, **kwargs: Any):
        if maneuvers := kwargs.get("add_maneuver"):
            if not isinstance(maneuvers, Iterable):
                maneuvers = [maneuvers]
            for maneuver in maneuvers:
                self.add_maneuver(maneuver)
        if maneuvers := kwargs.get("remove_maneuver"):
            if not isinstance(maneuvers, Iterable):
                maneuvers = [maneuvers]
            for maneuver in maneuvers:
                self.remove_maneuver(maneuver)
        super().every_level(**kwargs)

    #############################################################################
    def add_maneuver(self, maneuver: BaseManeuver) -> None:
        assert self.character is not None

        self.character.specials[CharacterClass.FIGHTER].add(maneuver)

    #############################################################################
    def remove_maneuver(self, maneuver: BaseManeuver) -> None:
        assert self.character is not None
        remove_tag = maneuver.tag
        for man in self.character.specials[CharacterClass.FIGHTER]:
            if man.tag == remove_tag:
                self.character.specials[CharacterClass.FIGHTER].remove(man)
                break
        else:
            raise InvalidOption(f"Failed to find {remove_tag} to remove")

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
    @property
    def class_special(self) -> str:
        assert self.character is not None
        ans = f"Superiority Dice: {self.num_superiority_dice}{self.type_superiority_dice}\n\n"
        for maneuver in sorted(self.character.specials[CharacterClass.FIGHTER], key=lambda x: x.tag):
            ans += f"{safe(maneuver.tag).title()}: {maneuver.desc}\n\n"
        return ans


############################################################################
class CombatSuperiority(BaseFeature):
    tag = Feature.COMBAT_SUPERIORITY
    recovery = Recovery.SHORT_REST

    @property
    def goes(self) -> int:
        assert self.owner.fighter is not None
        return self.owner.fighter.num_superiority_dice

    @property
    def desc(self) -> str:
        assert self.owner.fighter is not None
        return f"""Your experience on the battlefield has redefined your fighting techniques. You learn maneuvers that
    are fueled by special dice called Superiority Dice.

    Superiority Dice. You have {self.owner.fighter.num_superiority_dice} Superiority Dice, which are 
    {self.owner.fighter.type_superiority_dice}. A Superiority Die is expended when you use it.

    Saving Throws. If a maneuver requires a saving throw, the DC equals 8 plus your Strength or Dexterity modifier 
    (your choice) and Proficiency Bonus."""


############################################################################
class StudentOfWar(BaseFeature):
    tag = Feature.STUDENT_OF_WAR
    _desc = """You gain proficiency with one type of Artisan's Tools of your choice, and you gain proficiency in
    one skill of your choice from the skills available to Fighters at level 1."""
    hide = True

    def __init__(self, tool: Tool, skill: Skill):
        self._sw_tool = tool
        self._sw_skill = skill

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        assert character.fighter is not None
        if self._sw_skill not in character.fighter._base_skill_proficiencies:
            raise InvalidOption(f"Student of War: {self._sw_skill} not a valid choice: {character._base_skill_proficiencies}")
        return Reason("Student of War", self._sw_skill)

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        if self._sw_tool not in ARTISAN_TOOLS:
            raise InvalidOption(f"Student of War: {self._sw_tool} not a valid choice: {ARTISAN_TOOLS}")
        return Reason("Student of War", self._sw_tool)


############################################################################
class KnowYourEnemy(BaseFeature):
    tag = Feature.KNOW_YOUR_ENEMY
    _goes = 1
    recovery = Recovery.LONG_REST
    _desc = """As a Bonus Action, you can discern certain strengths and weaknesses of a creature you can see within 
    30 feet of yourself; you know whether that creature has any Immunities, Resistances, or Vulnerabilities, 
    and if the creature has any, you known what they are.
    
    You can also restore a use of the feature by expending one Superiority Dice (no action required)."""


############################################################################
class Relentless(BaseFeature):
    tag = Feature.RELENTLESS

    _desc = """Once per turn, when you use a maneuver, you can roll 1d8 and use the number rolled instead of 
    expending a Superiority Die."""


# EOF

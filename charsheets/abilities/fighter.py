from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Tool, Skill, ARTISAN_TOOLS
from charsheets.reason import Reason
from charsheets.exception import InvalidOption

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class FightingStyle(BaseAbility):
    tag = Ability.FIGHTING_STYLE
    _desc = """You gain a Fighting Style fear of your choice. Instead of choosing one of those feats you can choose the
    option below.

    Druidic Warrior. You learn two Druid cantrips of your choice. The chosen cantrips count as Ranger spells for you,
    and Wisdom is your spellcasting ability for them. Whenever you gain a Ranger level, you can replace one of these
    cantrips with another Druid cantrip."""


#############################################################################
class SecondWind(BaseAbility):
    tag = Ability.SECOND_WIND
    _desc = """You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action,
    you can use it to regain Hit Points equal to 1d10 plus your Fighter Level.

    You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all
    expended uses when you finish a Long Rest.
    """

    @property
    def goes(self) -> int:
        if self.owner.level >= 10:
            return 4
        elif self.owner.level >= 4:
            return 3
        return 2


############################################################################
class ActionSurge(BaseAbility):
    tag = Ability.ACTION_SURGE
    goes = 1
    _desc = """You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional
    action, except the Magic action.

    Once you use this feature, you can't do so again until you finish a Short or Long Rest.
    """


############################################################################
class TacticalMind(BaseAbility):
    tag = Ability.TACTICAL_MIND
    _desc = """You have a mind for tactics on and off the battlefield. When you fail an ability check you can expend
     a use of your Second Wind to push yourself toward success. Rather than regaining Hit Points, you roll 1d10 and add
     the number tolled to the ability check, potentially turning it into a success. If the check still fails, this use
     of Second Wind isn't expended.
    """


############################################################################
class CombatSuperiority(BaseAbility):
    tag = Ability.COMBAT_SUPERIORITY

    @property
    def goes(self) -> int:
        return self.owner.superiority_dice

    @property
    def desc(self) -> str:
        return f"""Your experience on the battlefield has redefined your fighting techniques. You learn maneuvers that
    are fueled by special dice called Superiority Dice.

    Superiority Dice. You have {self.owner.superiority_dice} Superiority Dice, which are d8s. A Superiority Die is
    expended when you use it. You regain all expended Superiority Dice when you finish a Short or Long Rest.

    Saving Throws. If a maneuver requires a saving throw, the DC equals 8 plus your Strength or Dexterity modifier (
    your choice) and Proficiency Bonus."""


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
class WarBond(BaseAbility):
    tag = Ability.WAR_BOND
    _desc = """You learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual
    over the course of 1 hour, which can be done during a Short Rest.

    Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you have the Incapacitated
    condition. You can summon that weapon as a Bonus Action, causing it to teleport instantly to your hand."""


############################################################################
class PsionicPowerFighter(BaseAbility):
    tag = Ability.PSIONIC_POWER_FIGHTER

    @property
    def desc(self) -> str:
        int_mod = self.owner.intelligence.modifier
        bonus = max(1, int_mod)
        return f"""You harbor a wellspring of psionic energy within yourself.

    You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them
    when you finish a Long Rest.

    Protective Field. When you or another creature you can see within 30 feet of you takes damage, you can take a 
    Reaction to expend one Psionic Energy Die, roll the die, and reduce the damage taken by the number rolled plus 
    {bonus}, as you create a momentary shield of telekinetic force.

    Psionic Strike. You can propel your weapons with psionic force. Once on each of your turns, immediately after you 
    hit a target within 30 feet of yourself with an attack and deal damage to it with a weapon, you can expend one 
    Psionic Energy Die, rolling it and dealing Force damage to the target equal to the number rolled plus
    {int_mod}.

    Telekinetic Movement. You can move an object or a creature with your mind. As a Magic action, choose one target 
    you can see within 30 feet of yourself; the target must be a loose object that is Large or smaller or one willing 
    creature other than you. You transport the target up to 30 feet to an unoccupied space you can see. 
    Alternatively, if that target is a Tiny object, you can transport it to or from your hand.
    
    Once you take this action, you can't do so again until you finish a Short or Long Rest unless you expend a 
    Psionic Energy Die (no action required) to restore your use of it."""


############################################################################
class TacticalShift(BaseAbility):
    tag = Ability.TACTICAL_SHIFT
    _desc = """Whenever you activate your Second Wind with a Bonus Action, you can move up to half your Speed without
    provoking Opportunity Attacks."""


############################################################################
class ImprovedCritical(BaseAbility):
    tag = Ability.IMPROVED_CRITICAL
    _desc = """Your attack rolls with weapons and Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on
    the d20"""


############################################################################
class RemarkableAthlete(BaseAbility):
    tag = Ability.REMARKABLE_ATHLETE
    _desc = """Thanks to your athleticism, you have Advantage on Initiative rolls and Strength(Athletics) checks.

    In addition, immediately after you score a Critical Hit, you can move up to half your Speed without provoking
    Opportunity Attacks."""


# EOF

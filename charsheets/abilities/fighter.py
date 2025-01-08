from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability


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


#############################################################################
class WeaponMastery(BaseAbility):
    tag = Ability.WEAPON_MASTERY
    _desc = """Your training with weapons allows you to use the mastery properties of two kinds of weapons of your
    choice with which you have proficiency.Whenever you finish a Long Rest, you can change the kinds of weapons
    you choose."""


############################################################################
class ActionSurge(BaseAbility):
    tag = Ability.ACTION_SURGE
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
    _desc = """Your experience on the battlefield has redefined your fighting techniques. 
    You learn maneuvers that are fueled by special dice called Superiority Dice.
    
    Maneuvers.
    
    Superiority Dice. You have four Superiority Dice, which are d8s. A Superiority Die is expended when you use it.
    You regain all expended Superiority Dice when you finish a Short or Long Rest.
    
    Saving Throws."""


############################################################################
class StudentOfWar(BaseAbility):
    tag = Ability.STUDENT_OF_WAR
    _desc = """You gain proficiency with one type of Artisan's Tools of your choice, and you gain proficiency in
    one skill of your choice from the skills available to Fighters at level 1."""


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
    _desc = """You harbor a wellspring of psionic energy within yourself.
    
    You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them
    when you finish a Long Rest. 
    
    Protective Field.
    
    Psionic Strike.
    
    Telekinetic Movement.
    """


############################################################################
class TacticalShift(BaseAbility):
    tag = Ability.TACTICAL_SHIFT
    _desc = """Whenever you activate your Second Wind with a Bonus Action, you can move up to half your Speed without 
    provoking Opportunity Attacks."""


# EOF

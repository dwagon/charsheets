from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityFightingStyle(BaseAbility):
    tag = Ability.FIGHTING_STYLE
    desc = """You gain a Fighting Style fear of your choice. Instead of choosing one of those feats you can choose the
    option below.
    
    Druidic Warrior. You learn two Druid cantrips of your choice. The chosen cantrips count as Ranger spells for you,
    and Wisdom is your spellcasting ability for them. Whenever you gain a Ranger level, you can replace one of these
    cantrips with another Druid cantrip."""


#############################################################################
class AbilitySecondWind(BaseAbility):
    tag = Ability.SECOND_WIND
    desc = """You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action,
    you can use it to regain Hit Points equal to 1d10 plus your Fighter Level.
    
    You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all
    expended uses when you finish a Long Rest.
    """


#############################################################################
class AbilityWeaponMastery(BaseAbility):
    tag = Ability.WEAPON_MASTERY
    desc = """Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency.
     Whenever you finish a Long Rest, you can change the kinds of weapons you choose."""


############################################################################
class AbilityActionSurge(BaseAbility):
    tag = Ability.ACTION_SURGE
    desc = """You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional
    action, except the Magic action.

    Once you use this feature, you can't do so again until you finish a Short or Long Rest.
    """


############################################################################
class AbilityTacticalMind(BaseAbility):
    tag = Ability.TACTICAL_MIND
    desc = """You have a mind for tactics on and off the battlefield. When you fail an ability check you can expend
     a use of your Second Wind to push yourself toward success. Rather than regaining Hit Points, you roll 1d10 and add
     the number tolled to the ability check, potentially turning it into a success. If the check still fails, this use
     of Second Wind isn't expended.
    """


# EOF

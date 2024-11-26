from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityDivineOrder(BaseAbility):
    tag = Ability.DIVINE_ORDER
    desc = """You have dedicated yourself to one of the following sacred roles:Protector, Thaumaturge"""


#############################################################################
class AbilityChannelDivinity(BaseAbility):
    tag = Ability.CHANNEL_DIVINITY
    desc = """You can channel divine energy.
    
    Divine Spark. As a Magic action, you point your Holy Symbol at another creature you can see within 30 feet of
    yourself and focus divine energy at it. Roll 1d8 and add your Wisdom modifier. You either restore Hot Points to
    the creature equal to that total or force the creature to Make a Constitution saving throw. On a failed save, the
    creature takes Necrotic or Radiant damage (your choice) equal to that total. On a successful save, the creature
    takes half as much damage.
    
    Turn Undead. As a Magic action, you present your Hold Symbol and censure Undead creatures. Each Undead of your
    choice within 30 feet of you must make a Wisdom saving throw. If the creature fails its save, it has the Frightened
    and Incapacitated condition for 1 minute. For that duration, it tries to mave as far from you as it can on its turns. 
    This effect ends early on the creature if it takes any damage, f you have the Incapacitated condition, or if you die
    """


# EOF

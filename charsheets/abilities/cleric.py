from charsheets.ability import BaseAbility
from charsheets.constants import Ability


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
    and Incapacitated condition for 1 minute. For that duration, it tries to mave as far from you as it can on its
    turns. This effect ends early on the creature if it takes any damage, f you have the Incapacitated condition,
    or if you die
    """


#############################################################################
class AbilityDiscipleOfLife(BaseAbility):
    tag = Ability.DISCIPLE_OF_LIFE
    desc = """When a spell you cast with a spell slot restores Hit Points to a creature, that creature regains
    additional Hit Points on the turn you cast the spell. The additional Hit Points equal 2 plus the spell
    slot’s level."""


#############################################################################
class AbilityLifeDomainSpells(BaseAbility):
    tag = Ability.LIFE_DOMAIN_SPELLS
    desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Life Domain Spells table, you thereafter always have the listed spells prepared."""


#############################################################################
class AbilityPreserveLife(BaseAbility):
    tag = Ability.PRESERVE_LIFE
    desc = """As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to evoke healing
    energy that can restore a number of Hit Points equal to five times your Cleric level. Choose Bloodied creatures
    within 30 feet of yourself (which can include you), and divide those Hit Points among them. This feature can
    restore a creature to no more than half its Hit Point maximum."""


# EOF

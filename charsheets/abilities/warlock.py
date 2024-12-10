from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityEldritchInvocation(BaseAbility):
    tag = Ability.ELDRITCH_INVOCATIONS
    desc = """You have unearthed Eldritch Invocations, pieces of forbidden knowledge that imbue you with an abiding
    magical ability or other lessons."""


#############################################################################
class AbilityPactMagic(BaseAbility):
    tag = Ability.PACT_MAGIC
    desc = """You know two Warlock cantrips"""


#############################################################################
class AbilityMagicalCunning(BaseAbility):
    tag = Ability.MAGICAL_CUNNING
    desc = """You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell
    slots but no more than a numer equal to half your maximum (round up). Once you use this feature, you can't do so
    again until you finish a Long Rest."""


#############################################################################
class AbilityStepsOfTheFey(BaseAbility):
    tag = Ability.STEPS_OF_THE_FEY
    desc = """Your patron grants you the ability to move between the boundaries of the planes. You can cast
    Misty Step without expending a spell slot a number of times equal to your Charisma modifier (min once), and 
    you regain all expended uses when you finish a Long Rest.
    
    In addition, whenever you cast that spell, you can choose one of the following additional effects.
    
    Refreshing Step. Immediately after you teleport, you or one creature you can see within 10 feet of yourself
    gains 1d10 Temporary Hit Points.
    
    Taunting Step. Creatures within 5 feet of the space you left must succeed on a Wisdom saving throw against your
    spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your
    next turn."""


#############################################################################
class AbilityHealingLight(BaseAbility):
    tag = Ability.HEALING_LIGHT
    desc = """You gain the ability to channel celestial energy to heal wounds. You have a pool of d6s to fuel this
    healing. The number of dice in the pool equals 1 plus your Warlock level.
    
    As a Bonus Action, you can heal yourself or one creature you can see within 60 feet of yourself, expending dice
    from the pool. The maximum number of dice you can expend at once equals your Charisma modifier (minimum of one die).
    Roll the dice you expend, and restore a number of Hit Points equal to the roll's total. Your pool regains all
    expended dice when you finish a Long Rest.
    """


#############################################################################
class AbilityDarkOnesBlessing(BaseAbility):
    tag = Ability.DARK_ONES_BLESSING
    desc = """When you reduce an enemy to 0 Hit Points, you gain Temporary Hit Points equal to your Charisma
    modifier plus your Warlock level (minimum of 1 Temporary Hit Point). You also gain this benefit if someone else
    reduces an enemy within 10 feet of you to 0 Hit Points.
    """


#############################################################################
class AbilityPsychicSpells(BaseAbility):
    tag = Ability.PSYCHIC_SPELLS
    desc = """When you cast a Warlock spell that deals damage, you can change its damage type to Psychic. In addition,
    when you cast a Warlock spell that is an Enchantment or Illusion, you can do so without Verbal or Somatic
    components."""


# EOF

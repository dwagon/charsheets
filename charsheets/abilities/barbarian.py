from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityRage(BaseAbility):
    tag = Ability.RAGE
    desc = """Damage Resistance
    Rage Damage
    Strength Advantage"""


#############################################################################
class AbilityUnarmoredDefense(BaseAbility):
    tag = Ability.UNARMORED_DEFENSE
    desc = """While you aren't wearing any armor, your base Armor Class equals 10 plus your Constitution and Dexterity 
    modifiers. You can use a Shield and still gain this benefit."""


#############################################################################
class AbilityDangerSense(BaseAbility):
    tag = Ability.DANGER_SENSE
    desc = """You gain an uncanny sense of when things aren't as they should be, giving you an edge when you 
    dodge perils. You have Advantage on Dexterity saving throws unless you have the Incapacitated condition."""


#############################################################################
class AbilityRecklessAttack(BaseAbility):
    tag = Ability.RECKLESS_ATTACK
    desc = """You can throw aside all concern for defense to attack with increased ferocity.
    When you make your first attack roll on your turn, you can decide to attack recklessly. Doing so gives you 
    Advantage on attack rolls using Strength until the start of your next turn, but attack rolls against you have 
    Advantage during that time."""


#############################################################################
class AbilityPrimalKnowledge(BaseAbility):
    tag = Ability.PRIMAL_KNOWLEDGE
    desc = """You gain proficiency in one skill of your choice."""


# EOF

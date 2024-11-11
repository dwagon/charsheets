from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityHuntersPrey(BaseAbility):
    tag = Ability.HUNTERS_PREY
    desc = """You gain one of the following. Whenever you finish a Long Rest you can replace the option.
    
    Colossus Slayer. Your tenacity can wear down even the most resilient foes. When you hit a creature with a weapon,
    the weapon deals an extra 1d8 damage to the target if its missing any of its Hit Points. You can deal this extra 
    damage only once per turn.
    
    Horde Breaker. Once on each of your turns when you make an attack with a weapon, you can make another attack with 
    the same weapon against a different creature that is within 5 feet of the original target, that is within the 
    weapon's range, and you haven't attacked this turn.
    """


#############################################################################
class AbilityHuntersLore(BaseAbility):
    tag = Ability.HUNTERS_LORE
    desc = """You can call on the forces of nature to reveal certain strengths and weaknesses of your prey.
    While a creature is marked by your Hunter’s Mark, you know whether that creature has any
    Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are."""


# EOF

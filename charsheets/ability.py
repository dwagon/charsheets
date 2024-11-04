""" Abilities"""

from charsheets.constants import Ability


#############################################################################
class BaseAbility:
    desc = "Unspecified"


#############################################################################
class AbilityDeftExplorer(BaseAbility):
    desc = """Thanks to your travels, you gain the following benefits.
    
    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.
    
    Languages. You know two languages of your choice"""


#############################################################################
class AbilityColossusSlayer(BaseAbility):
    desc = """Your tenacity can wear down even the most resilient foes.
    When you hit a creature with a weapon, the weapon deals an extra 1d8 damage to the target if it’s missing any
    of its Hit Points. You can deal this extra damage only once per turn."""


#############################################################################
class AbilityHuntersLore(BaseAbility):
    desc = """You can call on the forces of nature to reveal certain strengths and weaknesses of your prey.
    While a creature is marked by your Hunter’s Mark, you know whether that creature has any
    Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are."""


#############################################################################
class AbilityUnarmoredDefense(BaseAbility):
    desc = """While you aren't weaing any armor, your base Armor Class equals 10 plus your Constitution and Dexterity 
    modifiers. You can use a Shield and still gain this benefit."""


#############################################################################
class AbilityDangerSense(BaseAbility):
    desc = """You gain an uncanny sense of when things aren't as they should be, giving you an edge when you 
    dodge perils. You have Advantage on Dexterity saving throws unless you have the Incapacitated condition."""


#############################################################################
ability_mapping = {
    Ability.DANGER_SENSE: AbilityDangerSense,
    Ability.UNARMORED_DEFENSE: AbilityUnarmoredDefense,
    Ability.DEFT_EXPLORER: AbilityDeftExplorer,
    Ability.COLOSSUS_SLAYER: AbilityColossusSlayer,
    Ability.HUNTERS_LORE: AbilityHuntersLore,
}


#############################################################################
def get_ability(ability: Ability):
    try:
        return ability_mapping[ability]
    except KeyError:
        return f"Unknown ability {ability}"


# EOF

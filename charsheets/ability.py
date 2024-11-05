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
class AbilityResourceful(BaseAbility):
    desc = """You gain Heroic Inspiration whenever you finish a Long Rest."""


#############################################################################
class AbilitySkilful(BaseAbility):
    desc = """You gain proficiency in one skill of your choice."""


#############################################################################
class AbilityDarkvision120(BaseAbility):
    desc = """You have Darkvision with a range of 120 feet"""


#############################################################################
class AbilityDwarvenResilience(BaseAbility):
    desc = """You have Resistance to Poison damage. You also have Advantage on saving throws you make to avoid or
    end the Poisoned condition,."""


#############################################################################
class AbilityDwarvenToughness(BaseAbility):
    desc = """Your Hit Point maximum increases by 1, and it increases by 1 again whenever you gain a level."""


#############################################################################
class AbilityStonecunning(BaseAbility):
    desc = """As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes.
    You must be on a stone surface or touching a stone surface to use this Tremorsense. 
    The stone can be natural or worked. You can use this Bonus Action a number of times equal to your Proficiency Bonus,
     and you regain expended uses when you finish a Long Rest."""


#############################################################################
class AbilityRage(BaseAbility):
    desc = """Damage Resistance
    Rage Damage
    Strength Advantage"""


#############################################################################
class AbilityRecklessAttack(BaseAbility):
    desc = """You can throw aside all concern for defense to attack with increased ferocity.
    When you make your first attack roll on your tuen, you can decide to attack recklessly. Doing so gives you 
    Advantage on attack rolls using Strength until the start of your next turn, but attack rolls against you have 
    Advantage during that time."""


#############################################################################
class AbilityPrimalKnowledge(BaseAbility):
    desc = """You gain proficiency in one skill of your choice."""


#############################################################################
class AbilityDruidic(BaseAbility):
    desc = """You know Druidic, the secret language of Druids."""


#############################################################################
class AbilityPrimalOrder(BaseAbility):
    desc = """You have dedicated yourself to one of the following sacred roles: Magician, Warden."""


#############################################################################
class AbilityWildShape(BaseAbility):
    desc = """The power of nature allows you to assume the form of an animal.
    As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature."""


#############################################################################
class AbilityWildCompanion(BaseAbility):
    desc = """You can summon a nature spirit that assumes an animal form to aid you. As a Magic action,
    you can expend a spell slot or a use of Wild Shape to cast the Find Familiar spell without Material components.
    When you cast the spell in this way, the familiar is Fey and disappears when you finish a long rest."""


#############################################################################
ability_mapping = {
    Ability.DANGER_SENSE: AbilityDangerSense,
    Ability.UNARMORED_DEFENSE: AbilityUnarmoredDefense,
    Ability.DEFT_EXPLORER: AbilityDeftExplorer,
    Ability.COLOSSUS_SLAYER: AbilityColossusSlayer,
    Ability.HUNTERS_LORE: AbilityHuntersLore,
    Ability.RESOURCEFUL: AbilityResourceful,
    Ability.SKILLFUL: AbilitySkilful,
    Ability.DARKVISION120: AbilityDarkvision120,
    Ability.DWARVEN_RESILIANCE: AbilityDwarvenResilience,
    Ability.DWARVEN_TOUGHNESS: AbilityDwarvenToughness,
    Ability.RECKLESS_ATTACK: AbilityRecklessAttack,
    Ability.STONE_CUNNING: AbilityStonecunning,
    Ability.PRIMAL_KNOWLEDGE: AbilityPrimalKnowledge,
}


#############################################################################
def get_ability(ability: Ability):
    try:
        return ability_mapping[ability]
    except KeyError:
        return f"Unknown ability {ability}"


# EOF

from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityRitualAdept(BaseAbility):
    tag = Ability.RITUAL_ADEPT
    desc = """You can cast any spell as a Ritual if that spell has the Ritual tag and the spell is in your spellbook.
    You needn't have the spell prepared, but you must read from the book to cast a spell in this way."""


#############################################################################
class AbilityArcaneRecovery(BaseAbility):
    tag = Ability.ARCANE_RECOVERY
    desc = """You can regain some of your magical energy by studying your spellbook. When you finish a Short Rest,
    you can choose expeded spell slots to recover. The spell slots can have a combined level equal to no more than half
    your Wizard level (round up), and none of the slots can be level 6 or higher.
    
    Once you use this feature, you can't do so again until you finish a Long Rest"""


#############################################################################
class AbilityScholar(BaseAbility):
    tag = Ability.SCHOLAR
    desc = """While studying magic, you also specialized in another field of study. Choose on of the following skills
    in which you have proficiency: Arcana, History, Investigation, Medicine, Nature, or Religion. You have Expertise
    in the chosen skill."""


# EOF

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
    you can choose expended spell slots to recover. The spell slots can have a combined level equal to no more than half
    your Wizard level (round up), and none of the slots can be level 6 or higher.
    
    Once you use this feature, you can't do so again until you finish a Long Rest"""


#############################################################################
class AbilityScholar(BaseAbility):
    tag = Ability.SCHOLAR
    desc = """While studying magic, you also specialized in another field of study. Choose on of the following skills
    in which you have proficiency: Arcana, History, Investigation, Medicine, Nature, or Religion. You have Expertise
    in the chosen skill."""


#############################################################################
class AbilityAbjurationSavant(BaseAbility):
    tag = Ability.ABJURATION_SAVANT
    desc = """Choose two Wizard spells from the Abjuration school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Abjuration school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class AbilityArcaneWard(BaseAbility):
    tag = Ability.ARCANE_WARD
    desc = """You can weave magic around yourself for protection. When you cast an Abjuration spell with a spell slot, 
    you can simultaneously use a strand of the spell’s magic to create a magical ward on yourself that lasts until 
    you finish a Long Rest. The ward has a Hit Point maximum equal to twice your Wizard level plus your Intelligence 
    modifier. Whenever you take damage, the ward takes the damage instead, and if you have any Resistances or 
    Vulnerabilities, apply them before reducing the ward’s Hit Points. If the damage reduces the ward to 0 Hit 
    Points, you take any remaining damage. While the ward has O Hit Points, it can’t absorb damage, but its magic 
    remains.

    Whenever you cast an Abjuration spell with a spell slot, the ward regains a number of Hit Points equal to twice 
    the level of the spell slot. Alternatively, as a Bonus Action, you can expend a spell slot, and the ward 
    regains a number of Hit Points equal to twice the level of the spell slot expended. Once you create the ward, 
    you can’t create it again until you finish a Long Rest."""


#############################################################################
class AbilityDivinationSavant(BaseAbility):
    tag = Ability.DIVINATION_SAVANT
    desc = """Choose two Wizard spells from the Divination school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Divination school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class AbilityPortent(BaseAbility):
    tag = Ability.PORTENT
    desc = """Glimpses of the future begin to press on your awareness. Whenever you finish a Long Rest, roll two d20s 
    and record the numbers rolled. You can replace any D20 Test made by you or a creature that you can see with one 
    of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only 
    once per turn.
    
    Each foretelling roll can be used only once. When you finish a Long Rest, you lose any unused foretelling rolls."""


#############################################################################
class AbilityEvocationSavant(BaseAbility):
    tag = Ability.EVOCATION_SAVANT
    desc = """Choose two Wizard spells from the Evocation school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Evocation school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class AbilityPotentCantrip(BaseAbility):
    tag = Ability.POTENT_CANTRIP
    desc = """Your damaging cantrips affect even creatures that avoid the brunt of the effect. When you cast a can‑ 
    trip at a creature and you miss with the attack roll or the target succeeds on a saving throw against the 
    cantrip, the target takes half the cantrip’s damage (if any) but suffers no additional effect from the cantrip."""


#############################################################################
class AbilityIllusionSavant(BaseAbility):
    tag = Ability.ILLUSION_SAVANT
    desc = """Choose two Wizard spells from the Illusion school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Illusion school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class AbilityImprovedIllusions(BaseAbility):
    tag = Ability.IMPROVED_ILLUSIONS
    desc = """You can cast Illusion spells without providing Verbal components, and if an Illusion spell you cast has 
    a range 10+ feet, the range is increased by 60 feet.
    
    You also know the Minor Illusion cantrip. If you already know it, you learn a different Wizard cantrip of your 
    choice. The cantrip doesn't count against your number of cantrips known. You can create both a sound and an image 
    with a single casting of Minor Illusion, and you can cast it as a Bonus Action."""


# EOF

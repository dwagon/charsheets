from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityFavoredEnemy(BaseAbility):
    tag = Ability.FAVOURED_ENEMY
    desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot
    and you regain all expended uses of this ability when you finish a Long Rest.
    """


#############################################################################
class AbilityDeftExplorer(BaseAbility):
    tag = Ability.DEFT_EXPLORER
    desc = """Thanks to your travels, you gain the following benefits.

    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.

    Languages. You know two languages of your choice"""


#############################################################################
class AbilityPrimalCompanion(BaseAbility):
    tag = Ability.PRIMAL_COMPANION
    desc = """You magically summon a primal beast, which draws strength from your bond with nature."""


#############################################################################
class AbilityDreadfulStrikes(BaseAbility):
    tag = Ability.DREADFUL_STRIKES
    desc = """You can augment your weapon strikes with mind-scarring magic drawn from the murky hollows of the
    Fey wild. When you hit a creature with a weapon, you can deal an extra 1d4 Psychic damage to the target,
    which can take this extra damage only once per turn."""


#############################################################################
class AbilityOtherworldlyGlamour(BaseAbility):
    tag = Ability.OTHERWORLDLY_GLAMOUR
    desc = """Whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier (min +1).
    You also gain proficiency in one of these skills of your choice: Deception, Performance or Persuasion"""


#############################################################################
class AbilityFeywildGifts(BaseAbility):
    tag = Ability.FEYWILD_GIFTS
    desc = """You possess a fey blessing."""


#############################################################################
class AbilityDreadAmbusher(BaseAbility):
    tag = Ability.DREAD_AMBUSHER
    desc = """You have mastered the art of creating fearsome ambushes, granting you the following benefits.
    
    Ambusher's Leap
    
    Dreadful Strike
    
    Initiative Bonus. When you roll Initiative, you can add your Wisdom modifier to the roll."""


#############################################################################
class AbilityUmbralSight(BaseAbility):
    tag = Ability.UMBRAL_SIGHT
    desc = """You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 60
    feet.
    
    You are also adept at evading creatures that rely on Darkvision. While entirely in Darkness, you have the
    Invisible condition to any creture that relies on Darkvision to see you in that Darkness."""


# EOF

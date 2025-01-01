from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class FavoredEnemy(BaseAbility):
    tag = Ability.FAVOURED_ENEMY
    _desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot
    and you regain all expended uses of this ability when you finish a Long Rest.
    """


#############################################################################
class DeftExplorer(BaseAbility):
    tag = Ability.DEFT_EXPLORER
    _desc = """Thanks to your travels, you gain the following benefits.

    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.

    Languages. You know two languages of your choice"""


#############################################################################
class PrimalCompanion(BaseAbility):
    tag = Ability.PRIMAL_COMPANION
    _desc = """You magically summon a primal beast, which draws strength from your bond with nature."""


#############################################################################
class DreadfulStrikes(BaseAbility):
    tag = Ability.DREADFUL_STRIKES
    _desc = """You can augment your weapon strikes with mind-scarring magic drawn from the murky hollows of the
    Fey wild. When you hit a creature with a weapon, you can deal an extra 1d4 Psychic damage to the target,
    which can take this extra damage only once per turn."""


#############################################################################
class OtherworldlyGlamour(BaseAbility):
    tag = Ability.OTHERWORLDLY_GLAMOUR
    _desc = """Whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier (min +1).
    You also gain proficiency in one of these skills of your choice: Deception, Performance or Persuasion"""


#############################################################################
class FeywildGifts(BaseAbility):
    tag = Ability.FEYWILD_GIFTS
    _desc = """You possess a fey blessing."""


#############################################################################
class DreadAmbusher(BaseAbility):
    tag = Ability.DREAD_AMBUSHER
    _desc = """You have mastered the art of creating fearsome ambushes, granting you the following benefits.
    
    Ambusher's Leap
    
    Dreadful Strike
    
    Initiative Bonus. When you roll Initiative, you can add your Wisdom modifier to the roll."""


#############################################################################
class UmbralSight(BaseAbility):
    tag = Ability.UMBRAL_SIGHT
    _desc = """You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 60
    feet.
    
    You are also adept at evading creatures that rely on Darkvision. While entirely in Darkness, you have the
    Invisible condition to any creture that relies on Darkvision to see you in that Darkness."""


# EOF

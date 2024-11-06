""" Feats"""

from typing import TYPE_CHECKING
from charsheets.constants import Feat
from charsheets.exception import UnhandledException

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class BaseFeat:
    pass


#############################################################################
class FeatArchery(BaseFeat):
    desc = """You gain a +2 bonus to attack rolls you make with Ranged weapons."""

    @classmethod
    def ranged_atk_bonus(cls, character: "Character"):
        return 2


#############################################################################
class FeatAlert(BaseFeat):
    desc = """You gain the following benefits.

Initiative Proficiency. When you roll Initiative, you can add your Proficiency Bonus to the roll.

Initiative Swap. Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing
ally in the same combat. You can’t make this swap if you or the ally has the Incapacitated condition."""

    @classmethod
    def initiative_bonus(cls, character: "Character"):
        return character.proficiency_bonus


#############################################################################
class FeatHealer(BaseFeat):
    desc = """You gain the following benefits.

Battle Medic. If you have a Healer's Kit, you can expend one use of it and tend to a creature within 5 feet of
yourself as a Utilize action. That creature can expend on of its Hit Point Dice, and you then roll that die.
The creature regains a number of Hit Points equal to the roll plus your Proficiency Bonus.

Healing Rerolls. Whenever you roll a die to determine the number of Hit Points you restore with a spell or with this
feat's Battle Medic benefit, you can reroll the die if it rolls a 1, and you must use the new roll."""


#############################################################################
class FeatCrafter(BaseFeat):
    desc = """You gain the following benefits.

Tool Proficiency.

Discount. Whenever you buy a nonmagical item, you receive a 20 percent discount on it.

Fast Crafting. When you finish a Long Rest, you can craft one piece of gear."""


#############################################################################
class FeatLucky(BaseFeat):
    desc = """You gain the following benefits.
    
    Luck Points. 
    
    Advantage.
    
    Disadvantage."""


#############################################################################
class FeatMagicInitiate(BaseFeat):
    desc = """You gain the following benefits.
    
    Two Cantrips.
    
    Level 1 Spell.
    
    Spell Change.
    """


#############################################################################
class FeatMusician(BaseFeat):
    desc = """You gain the following benefits.
    
    Intrument Training.
    
    Encouraging Song."""


#############################################################################
class FeatSavageAttacker(BaseFeat):
    desc = """You've trained to deal particularly damaging strikes."""


#############################################################################
class FeatSkilled(BaseFeat):
    desc = """You gain proficiency in any combination of three skills or tools of your choice."""


#############################################################################
class FeatTavernBrawler(BaseFeat):
    desc = """You gain the following benefits.
    
    Enhanced Unarmed Strike.
    
    Damage Rerolls.
    
    Improvised Weaponry.
    
    Push."""


#############################################################################
class FeatTough(BaseFeat):
    desc = """Your Hit Point maximum increases by an amount equal to twice your character level when you gain this feat.
     Whenever you gain a character level thereafter, your Hit Point maxium increases by an additional 2 Hit Points"""


#############################################################################
feat_mapping = {
    Feat.ALERT: FeatAlert,
    Feat.CRAFTER: FeatCrafter,
    Feat.HEALER: FeatHealer,
    Feat.LUCKY: FeatLucky,
    Feat.MAGIC_INITIATE: FeatMagicInitiate,
    Feat.MUSICIAN: FeatMusician,
    Feat.SAVAGE_ATTACKER: FeatSavageAttacker,
    Feat.SKILLED: FeatSkilled,
    Feat.TAVERN_BRAWLER: FeatTavernBrawler,
    Feat.TOUGH: FeatTough,
}


#############################################################################
def get_feat(feat: Feat):
    try:
        return feat_mapping[feat]
    except KeyError:
        raise UnhandledException(f"Unknown feat {feat}")

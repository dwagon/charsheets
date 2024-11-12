from typing import TYPE_CHECKING

from charsheets.feat import BaseFeat
from charsheets.constants import Feat


if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class FeatAlert(BaseFeat):
    tag = Feat.ALERT
    desc = """You gain the following benefits.

Initiative Proficiency. When you roll Initiative, you can add your Proficiency Bonus to the roll.

Initiative Swap. Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing
ally in the same combat. You can’t make this swap if you or the ally has the Incapacitated condition."""

    @classmethod
    def initiative_bonus(cls, character: "Character"):
        return character.proficiency_bonus


#############################################################################
class FeatCrafter(BaseFeat):
    tag = Feat.CRAFTER
    desc = """You gain the following benefits.

Tool Proficiency.

Discount. Whenever you buy a nonmagical item, you receive a 20 percent discount on it.

Fast Crafting. When you finish a Long Rest, you can craft one piece of gear."""


#############################################################################
class FeatHealer(BaseFeat):
    tag = Feat.HEALER
    desc = """You gain the following benefits.

Battle Medic. If you have a Healer's Kit, you can expend one use of it and tend to a creature within 5 feet of
yourself as a Utilize action. That creature can expend on of its Hit Point Dice, and you then roll that die.
The creature regains a number of Hit Points equal to the roll plus your Proficiency Bonus.

Healing Rerolls. Whenever you roll a die to determine the number of Hit Points you restore with a spell or with this
feat's Battle Medic benefit, you can reroll the die if it rolls a 1, and you must use the new roll."""


#############################################################################
class FeatLucky(BaseFeat):
    tag = Feat.LUCKY
    desc = """You gain the following benefits.

    Luck Points. 

    Advantage.

    Disadvantage."""


#############################################################################
class FeatMagicInitiateCleric(BaseFeat):
    tag = Feat.MAGIC_INITIATE_CLERIC
    desc = """You gain the following benefits.

    Two Cantrips.

    Level 1 Spell.

    Spell Change.
    """


#############################################################################
class FeatMagicInitiateDruid(BaseFeat):
    tag = Feat.MAGIC_INITIATE_DRUID
    desc = """You gain the following benefits.

    Two Cantrips.

    Level 1 Spell.

    Spell Change.
    """


#############################################################################
class FeatMagicInitiateWizard(BaseFeat):
    tag = Feat.MAGIC_INITIATE_WIZARD
    desc = """You gain the following benefits.

    Two Cantrips.

    Level 1 Spell.

    Spell Change.
    """


#############################################################################
class FeatMusician(BaseFeat):
    tag = Feat.MUSICIAN
    desc = """You gain the following benefits.
    
    Instrument Training. You gain proficiency with three Musical Instruments of your choice.
    
    Encouraging Song. As you finish a Short or Long Rest, you can play a song on a Musical Instrument with which you
    have proficiency and give Heroic Inspiration to allies who hear the song. The number of allies you can affect in
    this way equals your Proficiency Bonus.
    """


#############################################################################
class FeatSavageAttacker(BaseFeat):
    tag = Feat.SAVAGE_ATTACKER
    desc = """You've trained to deal particularly damaging strikes."""


#############################################################################
class FeatSkilled(BaseFeat):
    tag = Feat.SKILLED
    desc = """You gain proficiency in any combination of three skills or tools of your choice."""


#############################################################################
class FeatTavernBrawler(BaseFeat):
    tag = Feat.TAVERN_BRAWLER
    desc = """You gain the following benefits.

    Enhanced Unarmed Strike.

    Damage Rerolls.

    Improvised Weaponry.

    Push."""


#############################################################################
class FeatTough(BaseFeat):
    tag = Feat.TOUGH
    desc = """Your Hit Point maximum increases by an amount equal to twice your character level when you gain this feat.
     Whenever you gain a character level thereafter, your Hit Point maxium increases by an additional 2 Hit Points"""


# EOF

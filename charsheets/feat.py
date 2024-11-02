""" Feats"""

from typing import TYPE_CHECKING
from charsheets.constants import Feat

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class BaseFeat:
    pass


#############################################################################
class FeatArchery(BaseFeat):
    desc = """Fighting Style Feat (Prerequisite: Fighting Style Feature)
You gain a +2 bonus to attack rolls you make with Ranged weapons."""

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
feat_mapping = {Feat.ALERT: FeatAlert, Feat.ARCHERY: FeatArchery, Feat.HEALER: FeatHealer}


#############################################################################
def get_feat(feat: Feat):
    try:
        return feat_mapping[feat]
    except KeyError:
        return f"Unknown feat {feat}"

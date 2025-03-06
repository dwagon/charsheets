from aenum import extend_enum

from charsheets.classes.rogue import Rogue
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class RogueThief(Rogue):
    #############################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Thief"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {FastHands(), SecondStoryWork()}
        if self.level >= 9:
            abilities |= {SupremeSneak()}
        abilities |= super().class_features()

        return abilities


extend_enum(Feature, "FAST_HANDS", "Fast Hands")
extend_enum(Feature, "SECOND_STORY_WORK", "Second Story Work")
extend_enum(Feature, "SUPREME_SNEAK", "Supreme Sneak")


#############################################################################
class FastHands(BaseFeature):
    tag = Feature.FAST_HANDS
    _desc = """As a Bonus Action, you can do one of the following.

    Sleight of Hand. Make a Dexterity (Sleight of Hand) check to pick a lock or disarm a trap with Thieves' Tools or 
    to pick a pocket.

    Use an Object. Take the Utilize action, or take the Magic action to use a magic item that requires that action."""


#############################################################################
class SecondStoryWork(BaseFeature):
    tag = Feature.SECOND_STORY_WORK
    _desc = """Climber. You gain a Climb Speed equal to your Speed. 

    Jumper. You can determine your jump distance using your Dexterity rather than your Strength."""


#############################################################################
class SupremeSneak(BaseFeature):
    tag = Feature.SUPREME_SNEAK
    _desc = """You gain the following Cunning Strike option.
    
    Stealth Attack (Cost: 1d6). If you have the Hide Action's Invisible condition, this attack doesn't end that 
    condition on you if you end the turn behind Three-Quarter Cover or Total Cover."""


# EOF

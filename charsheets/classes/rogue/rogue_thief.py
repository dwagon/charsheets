from charsheets.features.base_feature import BaseFeature
from charsheets.classes.rogue import Rogue
from charsheets.constants import Feature


#################################################################################
class RogueThief(Rogue):
    #############################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Rogue (Thief)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {FastHands(), SecondStoryWork()}
        abilities |= super().class_features()
        return abilities


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
    _desc = """You've trained to get into especially hard-to-reach places, granting you these benefits. 

    Climber. You gain a Climb Speed equal to your Speed. 

    Jumper. You can determine your jump distance using your Dexterity rather than your Strength."""


# EOF

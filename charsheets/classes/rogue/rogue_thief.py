from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.rogue import Rogue
from charsheets.constants import Ability


#################################################################################
class RogueThief(Rogue):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {FastHands(), SecondStoryWork()}
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class FastHands(BaseAbility):
    tag = Ability.FAST_HANDS
    _desc = """As a Bonus Action, you can do one of the following.

    Sleight of Hand. Make a Dexterity (Sleight of Hand) check to pick a lock or disarm a trap with Thieves' Tools or 
    to pick a pocket.

    Use an Object. Take the Utilize action, or take the Magic action to use a magic item that requires that action."""


#############################################################################
class SecondStoryWork(BaseAbility):
    tag = Ability.SECOND_STORY_WORK
    _desc = """You've trained to get into especially hard-to-reach places, granting you these benefits. 

    Climber. You gain a Climb Speed equal to your Speed. 

    Jumper. You can determine your jump distance using your Dexterity rather than your Strength."""


# EOF

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk
from charsheets.constants import Ability


#################################################################################
class MonkWarriorOfTheOpenHand(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of the Open Hand)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {OpenHandTechnique()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(WholenessOfBody())
        return abilities


#############################################################################
class OpenHandTechnique(BaseAbility):
    tag = Ability.OPEN_HAND_TECHNIQUE
    _desc = """Whenever you hit a creature with an attack granted by your Flurry of Blows, you can impose one of the 
    following effects on that target. 

    Addle. The target can’t make Opportunity Attacks until the start of its next turn. 

    Push. The target must succeed on a Strength saving throw or be pushed up to 15 feet away from you. 

    Topple. The target must succeed on a Dexterity saving throw or have the Prone condition."""


#############################################################################
class WholenessOfBody(BaseAbility):
    tag = Ability.WHOLENESS_OF_BODY

    _desc = """You gain the ability to heal yourself. As a Bonus Action, you can roll your Martial Arts die. You 
    regain a number of Hit Points equal to the number rolled plus your Wisdom modifier (minimum of 1 Hit Point 
    regained).

    You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all 
    expended uses when you finish a Long Rest."""


# EOF

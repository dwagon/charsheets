from charsheets.abilities import FastHands, SecondStoryWork
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.rogue import Rogue


#################################################################################
class RogueThief(Rogue):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {FastHands(), SecondStoryWork()}
        abilities |= super().class_abilities()
        return abilities


# EOF

from charsheets.abilities import Assassinate, AssassinsTools
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.rogue import Rogue


#################################################################################
class RogueAssassin(Rogue):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Assassinate(), AssassinsTools()}
        abilities |= super().class_abilities()
        return abilities


# EOF

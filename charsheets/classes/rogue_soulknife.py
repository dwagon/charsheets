from charsheets.abilities import PsionicPowerRogue, PsychicBlades
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.rogue import Rogue


#################################################################################
class RogueSoulknife(Rogue):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PsionicPowerRogue(), PsychicBlades()}
        abilities |= super().class_abilities()
        return abilities


# EOF

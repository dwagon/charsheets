from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability


#################################################################################
class LightDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.RADIANCE_OF_THE_DAWN, Ability.LIGHT_DOMAIN_SPELLS, Ability.WARDING_FLARE}
        return abilities


# EOF

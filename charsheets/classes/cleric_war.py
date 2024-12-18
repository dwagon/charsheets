from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability


#################################################################################
class WarDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.GUIDED_STRIKE, Ability.WAR_DOMAIN_SPELLS, Ability.WAR_PRIEST}
        return abilities


# EOF

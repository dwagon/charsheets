from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability


#################################################################################
class LifeDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.DISCIPLE_OF_LIFE, Ability.LIFE_DOMAIN_SPELLS, Ability.PRESERVE_LIFE}
        return abilities


# EOF

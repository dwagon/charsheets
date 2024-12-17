from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability


#################################################################################
class LifeDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.LIFE_DOMAIN_SPELLS, Ability.DISCIPLE_OF_LIFE, Ability.PRESERVE_LIFE}
        return abilities


# EOF

from charsheets.abilities import LifeDomainSpells, DiscipleOfLife, PreserveLife
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric


#################################################################################
class ClericLifeDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {LifeDomainSpells(), DiscipleOfLife(), PreserveLife()}
        return abilities


# EOF

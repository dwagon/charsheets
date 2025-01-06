from charsheets.abilities import GuidedStrike, WarDomainSpells, WarPriest
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric


#################################################################################
class ClericWarDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {GuidedStrike(), WarDomainSpells(), WarPriest()}
        abilities |= super().class_abilities()
        return abilities


# EOF

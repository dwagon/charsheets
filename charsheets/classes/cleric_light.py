from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability
from charsheets.abilities import RadianceOfTheDawn, LightDomainSpells, WardingFlare


#################################################################################
class ClericLightDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {RadianceOfTheDawn(), LightDomainSpells(), WardingFlare()}
        return abilities


# EOF

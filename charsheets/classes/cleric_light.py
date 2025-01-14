from charsheets.abilities import RadianceOfTheDawn, LightDomainSpells, WardingFlare, ImprovedWardingFlare
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric


#################################################################################
class ClericLightDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (Light Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {RadianceOfTheDawn(), LightDomainSpells(), WardingFlare()}
        if self.level >= 6:
            abilities |= {ImprovedWardingFlare()}
        return abilities


# EOF

from charsheets.abilities import GuidedStrike, WarDomainSpells, WarPriest, WarGodsBlessing
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric


#################################################################################
class ClericWarDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (War Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {GuidedStrike(), WarDomainSpells(), WarPriest()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {WarGodsBlessing()}
        return abilities


# EOF

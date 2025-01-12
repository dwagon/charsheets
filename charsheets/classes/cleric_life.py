from charsheets.abilities import LifeDomainSpells, DiscipleOfLife, PreserveLife, BlessedHealer
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric


#################################################################################
class ClericLifeDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (Life Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {LifeDomainSpells(), DiscipleOfLife(), PreserveLife()}
        if self.level >= 6:
            abilities |= {BlessedHealer()}
        return abilities


# EOF

from charsheets.abilities import ImprovedCritical, RemarkableAthlete
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.fighter import Fighter


#################################################################################
class FighterChampion(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Champion"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ImprovedCritical(), RemarkableAthlete()}
        abilities |= super().class_abilities()
        return abilities


# EOF

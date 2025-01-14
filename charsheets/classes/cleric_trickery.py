from charsheets.abilities import BlessingOfTheTrickster, InvokeDuplicity, TrickeryDomainSpells, TrickstersTransposition
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric


#################################################################################
class ClericTrickeryDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (Trickery Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {BlessingOfTheTrickster(), InvokeDuplicity(), TrickeryDomainSpells()}
        if self.level >= 6:
            abilities |= {TrickstersTransposition()}
        return abilities


# EOF

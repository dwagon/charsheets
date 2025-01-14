from charsheets.abilities import NaturesWrath
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.spells import Spells


#################################################################################
class PaladinOathOfAncients(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of the Ancients)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {NaturesWrath()}
        abilities |= super().class_abilities()
        if self.level >= 3:
            self.prepare_spells(Spells.ENSNARING_STRIKE, Spells.SPEAK_WITH_ANIMALS)
        if self.level >= 5:
            self.prepare_spells(Spells.MISTY_STEP, Spells.MOONBEAM)
        return abilities


# EOF

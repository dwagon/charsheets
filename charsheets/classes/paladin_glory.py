from charsheets.abilities import PeerlessAthlete, InspiringSmite
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.spells import Spells


#################################################################################
class PaladinOathOfGlory(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Glory)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PeerlessAthlete(), InspiringSmite()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spells.GUIDING_BOLT, Spells.HEROISM)
        if self.level >= 5:
            self.prepare_spells(Spells.ENHANCE_ABILITY, Spells.MAGIC_WEAPON)
        return abilities


# EOF

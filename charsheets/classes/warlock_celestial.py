from charsheets.abilities import HealingLight, RadiantSoul
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class WarlockCelestial(Warlock):
    _class_name = "Warlock (Celestial Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {HealingLight()}
        abilities |= super().class_abilities()
        self.prepare_spells(
            Spells.AID,
            Spells.CURE_WOUNDS,
            Spells.GUIDING_BOLT,
            Spells.LESSER_RESTORATION,
            Spells.LIGHT,
            Spells.SACRED_FLAME,
        )
        if self.level >= 5:
            self.prepare_spells(Spells.DAYLIGHT, Spells.REVIVIFY)
        if self.level >= 6:
            abilities |= {RadiantSoul()}
        return abilities


# EOF

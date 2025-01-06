from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells
from charsheets.abilities import HealingLight


#################################################################################
class WarlockCelestial(Warlock):
    _class_name = "Warlock (Celestial Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        self.prepare_spells(
            Spells.AID,
            Spells.CURE_WOUNDS,
            Spells.GUIDING_BOLT,
            Spells.LESSER_RESTORATION,
            Spells.LIGHT,
            Spells.SACRED_FLAME,
        )
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {HealingLight()}
        return abilities


# EOF

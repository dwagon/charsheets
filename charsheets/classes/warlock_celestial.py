from charsheets.constants import Ability
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class CelestialWarlock(Warlock):
    _class_name = "Warlock (Celestial Patron)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        self.prepare_spells(
            Spells.AID,
            Spells.CURE_WOUNDS,
            Spells.GUIDING_BOLT,
            Spells.LESSER_RESTORATION,
            Spells.LIGHT,
            Spells.SACRED_FLAME,
        )
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.HEALING_LIGHT}
        return abilities


# EOF

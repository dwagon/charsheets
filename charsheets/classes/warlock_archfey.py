from charsheets.classes.warlock import Warlock
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class ArchFeyWarlock(Warlock):
    _class_name = "Warlock (Archfey Patron)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        self.prepare_spells(Spells.CALM_EMOTIONS, Spells.FAERIE_FIRE, Spells.MISTY_STEP, Spells.PHANTASMAL_FORCE, Spells.SLEEP)

        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.STEPS_OF_THE_FEY}
        return abilities


# EOF

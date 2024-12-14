from charsheets.classes.warlock import Warlock
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class OldOneWarlock(Warlock):
    _class_name = "Warlock (Great Old One Patron)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        self.prepare_spells(
            Spells.DETECT_THOUGHTS,
            Spells.DISSONANT_WHISPERS,
            Spells.PHANTASMAL_FORCE,
            Spells.TASHAS_HIDEOUS_LAUGHTER,
        )
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.PSYCHIC_SPELLS}
        return abilities


# EOF

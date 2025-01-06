from charsheets.abilities import PsychicSpells
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class WarlockOldOne(Warlock):
    _class_name = "Warlock (Great Old One Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        self.prepare_spells(
            Spells.DETECT_THOUGHTS,
            Spells.DISSONANT_WHISPERS,
            Spells.PHANTASMAL_FORCE,
            Spells.TASHAS_HIDEOUS_LAUGHTER,
        )
        abilities: set[BaseAbility] = {PsychicSpells()}
        abilities |= super().class_abilities()
        return abilities


# EOF

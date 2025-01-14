from charsheets.abilities import PsychicSpells, ClairvoyantCombatant
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class WarlockOldOne(Warlock):
    _class_name = "Warlock (Great Old One Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PsychicSpells()}
        abilities |= super().class_abilities()

        self.prepare_spells(
            Spells.DETECT_THOUGHTS,
            Spells.DISSONANT_WHISPERS,
            Spells.PHANTASMAL_FORCE,
            Spells.TASHAS_HIDEOUS_LAUGHTER,
        )
        if self.level >= 5:
            self.prepare_spells(Spells.CLAIRVOYANCE, Spells.HUNGER_OF_HADAR)
        if self.level >= 6:
            abilities |= {ClairvoyantCombatant()}
        return abilities


# EOF

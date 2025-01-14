from charsheets.abilities import AberrantSorcery, TelepathicSpeech, PsionicSorcery, PsychicDefenses
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer
from charsheets.spells import Spells


#################################################################################
class SorcererAberrant(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Aberrant Sorceror"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {AberrantSorcery(), TelepathicSpeech()}
        abilities |= super().class_abilities()
        self.prepare_spells(
            Spells.ARMS_OF_HADAR, Spells.CALM_EMOTIONS, Spells.DETECT_THOUGHTS, Spells.DISSONANT_WHISPERS, Spells.MIND_SLIVER
        )
        if self.level >= 5:
            self.prepare_spells(Spells.HUNGER_OF_HADAR, Spells.SENDING)
        if self.level >= 6:
            abilities |= {PsionicSorcery(), PsychicDefenses()}

        return abilities


# EOF

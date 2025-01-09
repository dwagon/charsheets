from charsheets.abilities import AberrantSorcery, PsionicSpells, TelepathicSpeech
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer


#################################################################################
class SorcererAberrant(Sorcerer):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {AberrantSorcery(), PsionicSpells(), TelepathicSpeech()}
        abilities |= super().class_abilities()

        return abilities


# EOF

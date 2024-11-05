from charsheets.constants import CharSpecies, Ability
from charsheets.exception import UnhandledException


#############################################################################
class Species:
    def __init__(self, char_species: CharSpecies):
        self.char_species = char_species

    #########################################################################
    def species_abilities(self) -> set[Ability]:
        match self.char_species:
            case CharSpecies.DWARF:
                return {Ability.DARKVISION120, Ability.DWARVEN_RESILIANCE, Ability.DWARVEN_TOUGHNESS, Ability.STONE_CUNNING}
            case CharSpecies.ELF:
                return {Ability.DARKVISION60}
            case CharSpecies.HUMAN:
                return {Ability.RESOURCEFUL, Ability.SKILLFUL}
            case _:
                raise UnhandledException(f"Unhandled {self.char_species} in species_abilities()")

    #########################################################################
    @property
    def name(self) -> str:
        return self.char_species.title()

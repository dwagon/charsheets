from typing import TYPE_CHECKING
from charsheets.constants import CharSpecies, Ability
from charsheets.exception import UnhandledException

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class Species:
    def __init__(self, char_species: CharSpecies, character: "Character"):
        self.char_species = char_species
        self.character = character

    #########################################################################
    def species_abilities(self) -> set[Ability]:
        match self.char_species:
            case CharSpecies.AASIMAR:
                results = {Ability.CELESTIAL_RESISTANCE, Ability.DARKVISION60, Ability.HEALING_HANDS, Ability.LIGHT_BEARER}
                if self.character.level >= 3:
                    results.add(Ability.CELESTIAL_REVELATION)
                return results
            case CharSpecies.DWARF:
                return {Ability.DARKVISION120, Ability.DWARVEN_RESILIANCE, Ability.DWARVEN_TOUGHNESS, Ability.STONE_CUNNING}
            case CharSpecies.ELF:
                return {Ability.DARKVISION60}
            case CharSpecies.GOLIATH:
                return set()
            case CharSpecies.HALFLING:
                return {Ability.BRAVE, Ability.HALFLING_NIMBLENESS, Ability.LUCK, Ability.NATURALLY_STEALTHY}
            case CharSpecies.HUMAN:
                return {Ability.RESOURCEFUL, Ability.SKILLFUL}
            case _:
                raise UnhandledException(f"Unhandled {self.char_species} in species_abilities()")

    #########################################################################
    @property
    def name(self) -> str:
        return self.char_species.title()

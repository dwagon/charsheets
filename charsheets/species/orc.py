from charsheets.constants import Ability
from charsheets.species import Species


#############################################################################
class Orc(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        results = {Ability.CELESTIAL_RESISTANCE, Ability.DARKVISION60, Ability.HEALING_HANDS, Ability.LIGHT_BEARER}
        if self.character.level >= 3:
            results.add(Ability.CELESTIAL_REVELATION)
        return results


# EOF

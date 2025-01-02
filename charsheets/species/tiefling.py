from charsheets.abilities import Darkvision60
from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.species.base_species import BaseSpecies


#############################################################################
class Tiefling(BaseSpecies):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        results: set[BaseAbility] = {FiendishLegacy(), Darkvision60(), OtherworldlyPresence()}
        return results


#############################################################################
class FiendishLegacy(BaseAbility):
    tag = Ability.FIENDISH_LEGACY
    _desc = """As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus.
    The creature regains a number of Hit Points equal to the total rolled. Once you use this trait, you can't use
    it again until you finish a Long Rest."""


#############################################################################
class OtherworldlyPresence(BaseAbility):
    tag = Ability.OTHERWORLDLY_PRESENCE
    _desc = """As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus.
    The creature regains a number of Hit Points equal to the total rolled. Once you use this trait, you can't use
    it again until you finish a Long Rest."""


# EOF

from typing import TYPE_CHECKING

from charsheets.abilities import Darkvision60
from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, DamageType
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spells import Spells

if TYPE_CHECKING:
    from charsheets.character import Character  # pragma: no coverage


#############################################################################
class Aasimar(BaseSpecies):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        results: set[BaseAbility] = {CelestialResistance(), Darkvision60(), HealingHands(), LightBearer()}
        if self.character.level >= 3:
            results.add(CelestialRevelation())
        return results


#############################################################################
class HealingHands(BaseAbility):
    tag = Ability.HEALING_HANDS
    _desc = """As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus.
    The creature regains a number of Hit Points equal to the total rolled. Once you use this trait, you can't use
    it again until you finish a Long Rest."""


#############################################################################
class LightBearer(BaseAbility):
    tag = Ability.LIGHT_BEARER
    _desc = """You know the Light cantrip. Charisma is your spellcasting ability for it."""

    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Light Bearer", Spells.LIGHT)


#############################################################################
class CelestialResistance(BaseAbility):
    tag = Ability.CELESTIAL_RESISTANCE
    _desc = """You have Resistance to Necrotic damage and Radiant damage."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Celestial Resistance", DamageType.NECROTIC) | Reason("Celestial Resistance", DamageType.RADIANT)


#############################################################################
class CelestialRevelation(BaseAbility):
    tag = Ability.CELESTIAL_REVELATION
    _desc = """TODO"""


# EOF

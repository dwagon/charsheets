from typing import TYPE_CHECKING

from charsheets.ability import BaseAbility
from charsheets.constants import Ability, DamageType
from charsheets.reason import Reason
from charsheets.species import Species
from charsheets.spells import Spells

if TYPE_CHECKING:
    from charsheets.character import Character  # pragma: no coverage


#############################################################################
class Aasimar(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        results = {Ability.CELESTIAL_RESISTANCE, Ability.DARKVISION60, Ability.HEALING_HANDS, Ability.LIGHT_BEARER}
        if self.character.level >= 3:
            results.add(Ability.CELESTIAL_REVELATION)
        return results


#############################################################################
class AbilityHealingHands(BaseAbility):
    tag = Ability.HEALING_HANDS
    desc = """As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus.
    The creature regains a number of Hit Points equal to the total rolled. Once you use this trait, you can't use
    it again until you finish a Long Rest."""


#############################################################################
class AbilityLightBearer(BaseAbility):
    tag = Ability.LIGHT_BEARER
    desc = """You know the Light cantrip. Charisma is your spellcasting ability for it."""

    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Light Bearer", Spells.LIGHT)


#############################################################################
class AbilityCelestialResistance(BaseAbility):
    tag = Ability.CELESTIAL_RESISTANCE
    desc = """You have Resistance to Necrotic damage and Radiant damage."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Celestial Resistance", DamageType.NECROTIC) | Reason("Celestial Resistance", DamageType.RADIANT)


#############################################################################
class AbilityCelestialRevelation(BaseAbility):
    tag = Ability.CELESTIAL_REVELATION
    desc = """TODO"""


# EOF

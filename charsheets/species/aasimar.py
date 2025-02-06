from typing import TYPE_CHECKING

from charsheets.constants import Feature, DamageType
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spell import Spell

if TYPE_CHECKING:
    from charsheets.character import Character  # pragma: no coverage


#############################################################################
class Aasimar(BaseSpecies):
    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        results: set[BaseFeature] = {CelestialResistance(), Darkvision60(), HealingHands(), LightBearer()}
        if self.character.level >= 3:
            results.add(CelestialRevelation())
        return results


#############################################################################
class HealingHands(BaseFeature):
    tag = Feature.HEALING_HANDS
    goes = 1
    _desc = """As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus.
    The creature regains a number of Hit Points equal to the total rolled. Once you use this trait, you can't use
    it again until you finish a Long Rest."""


#############################################################################
class LightBearer(BaseFeature):
    tag = Feature.LIGHT_BEARER
    _desc = """You know the Light cantrip. Charisma is your spellcasting ability for it."""
    hide = True

    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Light Bearer", Spell.LIGHT)


#############################################################################
class CelestialResistance(BaseFeature):
    tag = Feature.CELESTIAL_RESISTANCE
    _desc = """You have Resistance to Necrotic damage and Radiant damage."""
    hide = True

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Celestial Resistance", DamageType.NECROTIC) | Reason("Celestial Resistance", DamageType.RADIANT)


#############################################################################
class CelestialRevelation(BaseFeature):
    tag = Feature.CELESTIAL_REVELATION
    goes = 1
    _desc = """WYou can transform as a Bonus Action using one of the options below
    (choose the option each time you transform). The transformation lasts for 1 minute or until you end it (no action 
    required). Once you transform, you can’t do so again until you finish a Long Rest.

    Once on each of your turns before the transformation ends, you can deal extra damage to one target when you deal 
    damage to it with an attack or a spell. The extra damage equals your Proficiency Bonus, and the extra damage’s 
    type is either Necrotic for Necrotic Shroud or Radiant for Heavenly Wings and Inner Radiance.

    Here are the transformation options:

    Heavenly Wings. Two spectral wings sprout from your back temporarily. Until the transformation ends, you have a 
    Fly Speed equal to your Speed.

    Inner Radiance. Searing light temporarily radiates from your eyes and mouth. For the duration, you shed Bright 
    Light in a 10-foot radius and Dim Light for an additional 10 feet, and at the end of each of your turns, 
    each creature within 10 feet of you takes Radiant damage equal to your Proficiency Bonus.

    Necrotic Shroud. Your eyes briefly become pools of darkness, and flightless wings sprout from your back 
    temporarily. Creatures other than your allies within 10 feet of you must succeed on a Charisma saving throw (DC8 
    plus your Charisma modifier and Proficiency Bonus) or have the Frightened condition until the end of your next 
    turn."""


# EOF

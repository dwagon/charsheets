from typing import TYPE_CHECKING
from charsheets.ability import BaseAbility
from charsheets.constants import Ability, DamageType
from charsheets.spells import Spells

if TYPE_CHECKING:
    from charsheets.character import Character


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

    def mod_add_known_spells(self, character: "Character") -> set[Spells]:
        return {Spells.LIGHT}


#############################################################################
class AbilityCelestialResistance(BaseAbility):
    tag = Ability.CELESTIAL_RESISTANCE
    desc = """You have Resistance to Necrotic damage and Radiant damage."""

    def mod_add_damage_resistances(self, character: "Character") -> set[DamageType]:
        return {DamageType.NECROTIC, DamageType.RADIANT}


# EOF

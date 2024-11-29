from charsheets.ability import BaseAbility
from charsheets.constants import Ability, DamageType
from charsheets.spells import Spells


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

    def add_known_spells(self) -> set[Spells]:
        return {Spells.LIGHT}


#############################################################################
class AbilityCelestialResistance(BaseAbility):
    tag = Ability.CELESTIAL_RESISTANCE
    desc = """You have Resistance to Necrotic damage and Radiant damage."""

    def add_damage_resistances(self) -> set[DamageType]:
        return {DamageType.NECROTIC, DamageType.RADIANT}


# EOF

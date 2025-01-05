from enum import StrEnum, auto
from typing import TYPE_CHECKING

from charsheets.abilities import Darkvision60
from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, DamageType
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spells import Spells
from charsheets.exception import UnhandledException

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Legacy(StrEnum):
    ABYSSAL = auto()
    CHTHONIC = auto()
    INFERNAL = auto()


#############################################################################
class Tiefling(BaseSpecies):
    #########################################################################
    def __init__(self, legacy: Legacy):
        super().__init__()
        self.legacy = legacy

    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        results: set[BaseAbility] = {FiendishLegacy(), Darkvision60(), OtherworldlyPresence()}
        return results


#############################################################################
class FiendishLegacy(BaseAbility):
    tag = Ability.FIENDISH_LEGACY
    _desc = """You are the recipient of a legacy that grants you supernatural abilities.
    
    You can cast it once without a spell slot, and you regain the ability to cast it in that way 
    when you finish a Long Rest. You can also cast the spell using any spell slots you have of the appropriate level. 
    Intelligence, Wisdom, or Charisma is your spellcasting ability for the spells you cast with this trait (choose 
    the ability when you select the legacy)."""

    #########################################################################
    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        match character.species.legacy:
            case Legacy.ABYSSAL:
                return Reason("Fiendish Legacy", DamageType.POISON)
            case Legacy.CHTHONIC:
                return Reason("Fiendish Legacy", DamageType.NECROTIC)
            case Legacy.INFERNAL:
                return Reason("Fiendish Legacy", DamageType.FIRE)
        raise UnhandledException(f"Fiendish Legacy - unhandled legacy {character.species.legacy}")  # pragma: no coverage

    #########################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason[Spells]()
        match character.species.legacy:
            case Legacy.ABYSSAL:
                spells.add("Fiendish Legacy", Spells.POISON_SPRAY)
                if character.level >= 3:
                    spells.add("Fiendish Legacy", Spells.RAY_OF_SICKNESS)
                if character.level >= 5:
                    spells.add("Fiendish Legacy", Spells.HOLD_PERSON)
            case Legacy.CHTHONIC:
                spells.add("Fiendish Legacy", Spells.CHILL_TOUCH)
                if character.level >= 3:
                    spells.add("Fiendish Legacy", Spells.FALSE_LIFE)
                if character.level >= 5:
                    spells.add("Fiendish Legacy", Spells.RAY_OF_ENFEEBLEMENT)
            case Legacy.INFERNAL:
                spells.add("Fiendish Legacy", Spells.FIRE_BOLT)
                if character.level >= 3:
                    spells.add("Fiendish Legacy", Spells.HELLISH_REBUKE)
                if character.level >= 5:
                    spells.add("Fiendish Legacy", Spells.DARKNESS)
        return spells


#############################################################################
class OtherworldlyPresence(BaseAbility):
    tag = Ability.OTHERWORLDLY_PRESENCE
    _desc = """You know the Thaumaturgy cantrip. When you cast it with this trait, the spell uses the same 
    spellcasting ability you use for your Fiendish Legacy trait."""

    #########################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Otherworldly Presence", Spells.THAUMATURGY)


# EOF

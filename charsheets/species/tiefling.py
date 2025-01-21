from enum import StrEnum, auto
from typing import TYPE_CHECKING, cast

from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.constants import Feature, DamageType
from charsheets.exception import UnhandledException
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spell import Spell

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
    def species_feature(self) -> set[BaseFeature]:
        results: set[BaseFeature] = {FiendishLegacy(), Darkvision60(), OtherworldlyPresence()}
        return results


#############################################################################
class FiendishLegacy(BaseFeature):
    tag = Feature.FIENDISH_LEGACY
    _desc = """You are the recipient of a legacy that grants you supernatural features.
    
    You can cast it once without a spell slot, and you regain the ability to cast it in that way 
    when you finish a Long Rest. You can also cast the spell using any spell slots you have of the appropriate level. 
    Intelligence, Wisdom, or Charisma is your spellcasting ability for the spells you cast with this trait (choose 
    the ability when you select the legacy)."""

    #########################################################################
    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        character.species = cast(Tiefling, character.species)
        match character.species.legacy:
            case Legacy.ABYSSAL:
                return Reason("Fiendish Legacy", DamageType.POISON)
            case Legacy.CHTHONIC:
                return Reason("Fiendish Legacy", DamageType.NECROTIC)
            case Legacy.INFERNAL:
                return Reason("Fiendish Legacy", DamageType.FIRE)
        raise UnhandledException(f"Fiendish Legacy - unhandled legacy {character.species.legacy}")  # pragma: no coverage

    #########################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason[Spell]()
        character.species = cast(Tiefling, character.species)
        match character.species.legacy:
            case Legacy.ABYSSAL:
                spells.add("Fiendish Legacy", Spell.POISON_SPRAY)
                if character.level >= 3:
                    spells.add("Fiendish Legacy", Spell.RAY_OF_SICKNESS)
                if character.level >= 5:
                    spells.add("Fiendish Legacy", Spell.HOLD_PERSON)
            case Legacy.CHTHONIC:
                spells.add("Fiendish Legacy", Spell.CHILL_TOUCH)
                if character.level >= 3:
                    spells.add("Fiendish Legacy", Spell.FALSE_LIFE)
                if character.level >= 5:
                    spells.add("Fiendish Legacy", Spell.RAY_OF_ENFEEBLEMENT)
            case Legacy.INFERNAL:
                spells.add("Fiendish Legacy", Spell.FIRE_BOLT)
                if character.level >= 3:
                    spells.add("Fiendish Legacy", Spell.HELLISH_REBUKE)
                if character.level >= 5:
                    spells.add("Fiendish Legacy", Spell.DARKNESS)
        return spells


#############################################################################
class OtherworldlyPresence(BaseFeature):
    tag = Feature.OTHERWORLDLY_PRESENCE
    _desc = """You know the Thaumaturgy cantrip. When you cast it with this trait, the spell uses the same 
    spellcasting ability you use for your Fiendish Legacy trait."""

    #########################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Otherworldly Presence", Spell.THAUMATURGY)


# EOF

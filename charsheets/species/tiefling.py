from enum import StrEnum, auto
from typing import TYPE_CHECKING, cast

from aenum import extend_enum
from charsheets.constants import Feature, DamageType, Stat, Recovery, SpellNotes
from charsheets.exception import UnhandledException, InvalidOption
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spell import Spell, spell_name

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "FIENDISH_LEGACY", "Fiendish Legacy")
extend_enum(Feature, "OTHERWORLDLY_PRESENCE", "Otherworldly Presence")


#############################################################################
class Legacy(StrEnum):
    ABYSSAL = auto()
    CHTHONIC = auto()
    INFERNAL = auto()


#############################################################################
class Tiefling(BaseSpecies):
    #########################################################################
    def __init__(self, legacy: Legacy, spellcast_stat: Stat):
        super().__init__()
        self.legacy = legacy
        self.spellcast_stat = spellcast_stat

    #########################################################################
    @property
    def name(self) -> str:
        return f"{self.legacy.name.title()} Tiefling"

    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        results: set[BaseFeature] = {FiendishLegacy(self.spellcast_stat), Darkvision60(), OtherworldlyPresence()}
        return results


#############################################################################
class FiendishLegacy(BaseFeature):
    tag = Feature.FIENDISH_LEGACY
    goes = 1
    recovery = Recovery.LONG_REST

    def __init__(self, spellcast_stat: Stat):
        super().__init__()
        self.spellcast_stat = spellcast_stat

    @property
    def desc(self) -> str:
        spells = [f"'{spell_name(_.value)}'" for _ in self.mod_add_prepared_spells(self.owner)]
        return f"""You can cast {', '.join(spells)} once without a spell slot. You can also cast the spell
        using any spell slots you have of the appropriate level. {self.spellcast_stat.name.title()} is your 
        spellcasting ability for the spells you cast with this trait."""

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
            case _:  # pragma: no coverage
                raise InvalidOption(f"Bad legacy: {character.species.legacy}")
        for spell_link in spells:
            character.add_spell_note(spell_link.value, SpellNotes.STAT, self.spellcast_stat)
        return spells


#############################################################################
class OtherworldlyPresence(BaseFeature):
    tag = Feature.OTHERWORLDLY_PRESENCE

    #########################################################################

    @property
    def desc(self) -> str:
        species = cast(Tiefling, self.owner.species)
        return f"""You know the 'Thaumaturgy' cantrip. When you cast it with this trait,
                the spell uses {species.spellcast_stat.name.title()}."""

    #########################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        species = cast(Tiefling, self.owner.species)
        character.add_spell_note(Spell.THAUMATURGY, SpellNotes.STAT, species.spellcast_stat)
        return Reason("Otherworldly Presence", Spell.THAUMATURGY)


# EOF

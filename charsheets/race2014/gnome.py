from typing import TYPE_CHECKING, cast

from aenum import extend_enum
from charsheets.constants import Language, Feature, Tool
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "GNOMISH_CUNNING14", "Gnomish Cunning")
extend_enum(Feature, "NATURAL_ILLUSIONIST14", "Natural Illusionist")
extend_enum(Feature, "SPEAK_WITH_SMALL_BEASTS14", "Speak with Small Beasts")
extend_enum(Feature, "ARTIFICERS_LORE14", "Artificer's Lore")
extend_enum(Feature, "TINKER14", "Tinker")


#############################################################################
class Gnome(BaseRace):
    #########################################################################
    def __init__(self):
        super().__init__()
        self.speed = 25

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {Darkvision60(), GnomishCunning()}

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Gnome", Language.GNOMISH)

    #########################################################################
    def mod_stat_int(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Gnome", 2)


#############################################################################
class ForestGnome(Gnome):
    #########################################################################
    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Forest Gnome", 1)

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        feats = super().race_feature()
        feats.add(NaturalIllusionist())
        feats.add(SpeakWithSmallBeasts())
        return feats


#############################################################################
class RockGnome(Gnome):

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        feats = super().race_feature()
        feats.add(ArtificersLore())
        feats.add(Tinker())
        return feats

    #########################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Rock Gnome", 1)


#############################################################################
class GnomishCunning(BaseFeature):
    tag = Feature.GNOMISH_CUNNING14
    _desc = """You have advantage on all Intelligence, Wisdom, and Charisma saving throws
    against magic."""


#############################################################################
class NaturalIllusionist(BaseFeature):
    tag = Feature.NATURAL_ILLUSIONIST14
    _desc = """You know the 'Minor Illusionist' cantrip. Intelligence is your spellcasting
    ability for it."""

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Forest Gnome", Spell.MINOR_ILLUSION)


#############################################################################
class SpeakWithSmallBeasts(BaseFeature):
    tag = Feature.SPEAK_WITH_SMALL_BEASTS14
    _desc = """Through sounds and gestures, you can communicate simple ideas with Small or
    smaller beasts."""


#############################################################################
class ArtificersLore(BaseFeature):
    tag = Feature.ARTIFICERS_LORE14
    _desc = """Whenever you ake an Intelligence (History) check related to magic items, alchemical
    objects, or technological devices, you can add twice your proficiency bonus, instead of any
    proficiency bonus normally apply."""


#############################################################################
class Tinker(BaseFeature):
    tag = Feature.TINKER14
    _desc = """Using Tinkerer's Tools you can spend 1 hour and 10gp worth of materials to 
    construct a Tiny clockwork device."""

    def mod_add_tool_proficiency(self, character: "BaseCharacter") -> Reason[Tool]:
        return Reason("Tinker", cast(Tool, Tool.TINKERS_TOOLS))


# EOF

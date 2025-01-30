from enum import StrEnum, auto
from typing import TYPE_CHECKING, cast

from charsheets.features import Darkvision60, Darkvision120
from charsheets.features.base_feature import BaseFeature
from charsheets.constants import Feature, Skill
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spell import Spell
from charsheets.exception import InvalidOption

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Lineages(StrEnum):
    DROW = auto()
    HIGH_ELF = auto()
    WOOD_ELF = auto()


#############################################################################
class Elf(BaseSpecies):
    #########################################################################
    def __init__(self, lineage: Lineages, keen_sense: Skill) -> None:
        super().__init__()
        self.lineage = lineage
        self.keen_sense = keen_sense
        if keen_sense not in (Skill.INSIGHT, Skill.PERCEPTION, Skill.SURVIVAL):
            raise InvalidOption(f"Keen Sense must be one on Insight, Perception or Survival - not {keen_sense}")

    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        abils = {FeyAncestry(), KeenSenses(), Trance()}
        match self.lineage:
            case Lineages.DROW:
                abils.add(Darkvision120())
            case Lineages.HIGH_ELF:
                abils.add(Darkvision60())
            case Lineages.WOOD_ELF:
                abils.add(Darkvision60())
        return abils

    #############################################################################
    @property
    def name(self) -> str:
        match self.lineage:
            case Lineages.DROW:
                return "Drow"
            case Lineages.HIGH_ELF:
                return "High Elf"
            case Lineages.WOOD_ELF:
                return "Wood Elf"

    #############################################################################
    def mod_set_movement_speed(self, character: "Character") -> Reason[int]:
        if self.lineage == Lineages.WOOD_ELF:
            return Reason("Wood Elf", 35)
        return Reason()

    #########################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason[Spell]()
        match self.lineage:
            case Lineages.DROW:
                spells |= Reason("Drow", Spell.DANCING_LIGHTS)
                if character.level >= 3:
                    spells |= Reason("Drow", Spell.FAERIE_FIRE)
                if character.level >= 5:
                    spells |= Reason("Drow", Spell.DARKNESS)
            case Lineages.HIGH_ELF:
                spells |= Reason("High Elf", Spell.PRESTIGITATION)
                if character.level >= 3:
                    spells |= Reason("High Elf", Spell.DETECT_MAGIC)
                if character.level >= 5:
                    spells |= Reason("High Elf", Spell.MISTY_STEP)
            case Lineages.WOOD_ELF:
                spells |= Reason("Wood Elf", Spell.DRUIDCRAFT)
                if character.level >= 3:
                    spells |= Reason("Wood Elf", Spell.LONGSTRIDER)
                if character.level >= 5:
                    spells |= Reason("Wood Elf", Spell.PASS_WITHOUT_TRACE)
        return spells


#############################################################################
class FeyAncestry(BaseFeature):
    tag = Feature.FEY_ANCESTRY
    _desc = """You have Advantage on saving throws you make to avoid or end the Charmed throws you make to avoid or 
    end the Charmed condition."""


#############################################################################
class KeenSenses(BaseFeature):
    tag = Feature.KEEN_SENSES
    _desc = """You have proficiency in the Insight, Perception, or Survival skill."""
    hide = True

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        character.species = cast(Elf, character.species)
        return Reason("Keen Senses", character.species.keen_sense)


#############################################################################
class Trance(BaseFeature):
    tag = Feature.TRANCE
    _desc = """You don’t need to sleep, and magic can’t put you to sleep. You can finish a Long Rest in 4 hours if 
    you spend those hours in a trancelike meditation, during which you retain consciousness."""


""
# EOF

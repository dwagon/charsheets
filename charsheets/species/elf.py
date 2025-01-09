from enum import StrEnum, auto
from typing import TYPE_CHECKING

from charsheets.abilities import Darkvision60, Darkvision120
from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spells import Spells

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
    def __init__(self, lineage: Lineages) -> None:
        super().__init__()
        self.lineage = lineage

    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
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
    def mod_set_movement_speed(self, character: "Character") -> Reason[int]:
        if self.lineage == Lineages.WOOD_ELF:
            return Reason("Wood Elf", 35)
        return Reason()

    #########################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason[Spells]()
        match self.lineage:
            case Lineages.DROW:
                spells |= Reason("Drow", Spells.DANCING_LIGHTS)
                if character.level >= 3:
                    spells |= Reason("Drow", Spells.FAERIE_FIRE)
                if character.level >= 5:
                    spells |= Reason("Drow", Spells.DARKNESS)
            case Lineages.HIGH_ELF:
                spells |= Reason("High Elf", Spells.PRESTIGITATION)
                if character.level >= 3:
                    spells |= Reason("High Elf", Spells.DETECT_MAGIC)
                if character.level >= 5:
                    spells |= Reason("High Elf", Spells.MISTY_STEP)
            case Lineages.WOOD_ELF:
                spells |= Reason("Wood Elf", Spells.DRUIDCRAFT)
                if character.level >= 3:
                    spells |= Reason("Wood Elf", Spells.LONGSTRIDER)
                if character.level >= 5:
                    spells |= Reason("Wood Elf", Spells.PASS_WITHOUT_TRACE)
        return spells


#############################################################################
class FeyAncestry(BaseAbility):
    tag = Ability.FEY_ANCESTRY
    _desc = """You have Advantage on saving throws you make to avoid or end the Charmed throws you make to avoid or 
    end the Charmed condition."""


#############################################################################
class KeenSenses(BaseAbility):
    tag = Ability.KEEN_SENSES
    _desc = """You have proficiency in the Insight, Perception, or Survival skill."""


#############################################################################
class Trance(BaseAbility):
    tag = Ability.TRANCE
    _desc = """You don’t need to sleep, and magic can’t put you to sleep. You can finish a Long Rest in 4 hours if 
    you spend those hours in a trancelike meditation, during which you retain consciousness."""


""
# EOF

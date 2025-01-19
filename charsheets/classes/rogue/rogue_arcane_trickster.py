from typing import Optional

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.rogue import Rogue
from charsheets.constants import Stat, Ability
from charsheets.spells import Spells


#################################################################################
class RogueArcaneTrickster(Rogue):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {MageHandLegerdemain()}
        abilities |= super().class_abilities()
        self.learn_spell(Spells.MAGE_HAND)
        self._class_name = "Arcane Trickster"
        return abilities

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            6: [3, 0, 0, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        if self.level >= 19:
            return 4
        elif self.level >= 13:
            return 3
        elif self.level >= 7:
            return 2
        return 1


#############################################################################
class MageHandLegerdemain(BaseAbility):
    tag = Ability.MAGE_HAND_LEGERDERMAIN
    _desc = """When you cast Mage Hand, you can cast it as a Bonus Action, and you can make the spectral hand 
    Invisible. You can control the hand as a Bonus Action, and through it, you can make Dexterity (Sleight of Hand) 
    checks."""


# EOF

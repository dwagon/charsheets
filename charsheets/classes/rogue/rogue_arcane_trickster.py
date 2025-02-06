from typing import Optional

from charsheets.classes.rogue import Rogue
from charsheets.constants import Stat, Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.spell import Spell


#################################################################################
class RogueArcaneTrickster(Rogue):
    #############################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Arcane Trickster"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        features: set[BaseFeature] = {MageHandLegerdemain()}
        features |= super().class_features()
        self.learn_spell(Spell.MAGE_HAND)
        if self.level >= 9:
            features |= {MagicalAmbush()}
        return features

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
            7: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            8: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            9: [4, 2, 0, 0, 0, 0, 0, 0, 0],
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
class MageHandLegerdemain(BaseFeature):
    tag = Feature.MAGE_HAND_LEGERDERMAIN
    _desc = """When you cast Mage Hand, you can cast it as a Bonus Action, and you can make the spectral hand 
    Invisible. You can control the hand as a Bonus Action, and through it, you can make Dexterity (Sleight of Hand) 
    checks."""


#############################################################################
class MagicalAmbush(BaseFeature):
    tag = Feature.MAGICAL_AMBUSH
    _desc = """If you have the Invisible condition when you cast a spell on a creature, it has Disadvantage on any
    saving throw it makes against the spell on the same turn."""


# EOF

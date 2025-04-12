from typing import Optional, Any

from aenum import extend_enum

from charsheets.classes.rogue import Rogue
from charsheets.constants import Stat, Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.spell import Spell

extend_enum(Feature, "MAGE_HAND_LEGERDERMAIN", "Mage Hand Legerdermain")
extend_enum(Feature, "MAGICAL_AMBUSH", "Magical Ambush")
extend_enum(Feature, "VERSATILE_TRICKSTER", "Versatile Trickster")


#################################################################################
class RogueArcaneTrickster(Rogue):
    _class_name = "Arcane Trickster"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(MageHandLegerdemain())
        self.character.learn_spell(Spell.MAGE_HAND)
        super().level3(**kwargs)

    ##############################################################################
    def level9(self, **kwargs: Any):
        self.add_feature(MagicalAmbush())

    ##############################################################################
    def level13(self, **kwargs: Any):
        self.add_feature(VersatileTrickster())

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
            10: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            11: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            12: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            13: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            14: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            15: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            16: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            17: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            18: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            19: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            20: [4, 3, 3, 1, 0, 0, 0, 0, 0],
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
    _desc = """When you cast 'Mage Hand', you can cast it as a Bonus Action, and you can make the spectral hand 
    Invisible. You can control the hand as a Bonus Action, and through it, you can make Dexterity (Sleight of Hand) 
    checks."""


#############################################################################
class MagicalAmbush(BaseFeature):
    tag = Feature.MAGICAL_AMBUSH
    _desc = """If you have the Invisible condition when you cast a spell on a creature, it has Disadvantage on any
    saving throw it makes against the spell on the same turn."""


#############################################################################
class VersatileTrickster(BaseFeature):
    tag = Feature.VERSATILE_TRICKSTER
    _desc = """You gain the ability to distract targets with your 'Mage Hand'. When you use the Trip option of your 
    Cunning Strike on a creature, you can also use that option on another creature within 5 feet of the spectral 
    hand."""


# EOF

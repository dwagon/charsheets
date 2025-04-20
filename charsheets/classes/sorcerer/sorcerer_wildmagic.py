from typing import TYPE_CHECKING, Any

from aenum import extend_enum

if TYPE_CHECKING:  # pragma: no coverage
    pass

from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature


extend_enum(Feature, "BEND_LUCK", "Bend Luck")
extend_enum(Feature, "CONTROLLED_CHAOS", "Controlled Chaos")
extend_enum(Feature, "TAMED_SURGE", "Tamed Surge")
extend_enum(Feature, "TIDES_OF_CHAOS", "Tides of Chaos")
extend_enum(Feature, "WILD_MAGIC_SURGE", "Wild Magic Surge")


#################################################################################
class SorcererWildMagic(Sorcerer):
    _class_name = "Wild Magic Sorcerer"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(WildMagicSurge())
        self.add_feature(TidesOfChaos())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(BendLuck())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(ControlledChaos())

    #############################################################################
    def level18(self, **kwargs: Any):
        self.add_feature(TamedSurge())


#############################################################################
class WildMagicSurge(BaseFeature):
    tag = Feature.WILD_MAGIC_SURGE
    _desc = """Once per turn, you can roll 1d20 immediately after you cast a Sorceror spell with a spell slot. If you 
    roll a 20, roll on the Wild Magic Surge table to create a magical effect. If the magical effect is a spell, 
    it is too wild to be affected by your Metamagic."""


#############################################################################
class TidesOfChaos(BaseFeature):
    tag = Feature.TIDES_OF_CHAOS
    _desc = """You can manipulate chaos itself to give yourself Advantage on one D20 Test before you roll the d20. 
    Once you do so, you must cast a Sorcerer spell with a spell slot or finish a Long Rest before you can use 
    this feature again. If you do cast a Sorcerer spell with a spell slot before you finish a Long Rest, 
    you automatically roll on the Wild Magic Surge table."""


#############################################################################
class BendLuck(BaseFeature):
    tag = Feature.BEND_LUCK
    _desc = """You have the ability to twist fate using your wild magic. Immediately after another creature you can 
    see rolls the d20 for a D20 Test, you can take a Reaction and spend 1 Sorcery Point to roll 1d4 and apply the 
    number rolled as a bonus or penalty (your choice) to the d20 roll."""


#############################################################################
class ControlledChaos(BaseFeature):
    tag = Feature.CONTROLLED_CHAOS
    _desc = """You gain a modicum of control over the surges of your wild magic. Whenever you roll on the Wild Magic 
    Surge table, you can roll twice and use either number."""


#############################################################################
class TamedSurge(BaseFeature):
    tag = Feature.TAMED_SURGE
    recovery = Recovery.LONG_REST
    _desc = """Immediately after you cast a Sorcerer spell with a spell slot, you can create an effect of your choice 
    from the Wild Magic Surge table instead of rolling on that table. You can choose any effect in the table except 
    for the final row, and if the chosen effect involves a roll, you must make it."""


# EOF

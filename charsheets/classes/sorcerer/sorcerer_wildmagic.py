from charsheets.features.base_feature import BaseFeature
from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Feature


#################################################################################
class SorcererWildMagic(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Wild Magic Sorceror"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {WildMagicSurge(), TidesOfChaos()}
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {BendLuck()}

        return abilities


#############################################################################
class WildMagicSurge(BaseFeature):
    tag = Feature.WILD_MAGIC_SURGE
    _desc = """Your spellcasting can unleash surges of untamed magic. Once per turn, you can roll 1d20 immediately 
    after you cast a Sorceror spell with a spell slot. If you roll a 20, roll on the Wild Magic Surge table to create 
    a magical effect. If the magical effect is a spell, it is too wild to be affected by your Metamagic."""


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


# EOF

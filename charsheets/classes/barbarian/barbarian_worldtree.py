from aenum import extend_enum

from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class BarbarianPathOfTheWorldTree(Barbarian):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Barbarian (Path of the World Tree)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        features: set[BaseFeature] = {VitalityOfTheTree()}
        if self.level >= 6:
            features.add(BranchesOfTheTree())
        if self.level >= 10:
            features.add(BatteringRoots())
        features |= super().class_features()
        return features


extend_enum(Feature, "VITALITY_OF_THE_TREE", "Vitality of the Tree")
extend_enum(Feature, "BRANCHES_OF_THE_TREE", "Branches of the Tree")
extend_enum(Feature, "BATTERING_ROOTS", "Battering Roots")


#############################################################################
class VitalityOfTheTree(BaseFeature):
    tag = Feature.VITALITY_OF_THE_TREE

    @property
    def desc(self) -> str:
        return f"""Your Rage taps into the life force of the World Tree. You gain the following benefits.

    Vitality Surge. When you activate your Rage, you gain {self.owner.level} Temporary Hit Points.

    Life-Giving Force. At the start of each of your turns while your Rage is active, you can choose another
    creature within 10 feet of yourself to gain Temporary Hit Points. To determine the number of Temporary Hit
    Points, roll {self.owner.rage_dmg_bonus}d6s, and add them together. If any of these
    Temporary Hit Points remain when your Rage ends, they vanish."""


#############################################################################
class BranchesOfTheTree(BaseFeature):
    tag = Feature.BRANCHES_OF_THE_TREE
    _desc = """ """

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.strength.modifier + self.owner.proficiency_bonus
        return f"""Whenever a creature you can see starts its turn within 30 feet of you while your Rage is active, 
        you can take a Reaction to summon spectral branches of the World Tree around it. The target must succeed on a 
        Strength saving thrown (DC {dc}) or be teleported to an unoccupied space you can see within 5 feet of 
        yourself or in the nearest unoccupied space you can see. After the target teleports, you can reduce its Speed 
        to 0 until the end of the current turn."""


#############################################################################
class BatteringRoots(BaseFeature):
    tag = Feature.BATTERING_ROOTS
    _desc = """During your turn, your reach is 10 feet greater with any Melee weapon that has the Heavy or Versatile 
    property, as tendrils of the World Tree extend from you. When you hit with such a weapon on your turn, 
    you can activate the Push or Topple mastery property in addition to a different mastery property you're using 
    with that weapon."""


# EOF

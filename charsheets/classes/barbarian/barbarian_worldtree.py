from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Ability


#################################################################################
class BarbarianPathOfTheWorldTree(Barbarian):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Barbarian (Path of the World Tree)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {VitalityOfTheTree()}
        if self.level >= 6:
            abilities.add(BranchesOfTheTree())
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class VitalityOfTheTree(BaseAbility):
    tag = Ability.VITALITY_OF_THE_TREE

    @property
    def desc(self) -> str:
        return f"""Your Rage taps into the life force of the World Tree. You gain the following benefits.

    Vitality Surge. When you activate your Rage, you gain {self.owner.level} Temporary Hit Points.

    Life-Giving Force. At the start of each of your turns while your Rage is active, you can choose another
    creature within 10 feet of yourself to gain Temporary Hit Points. To determine the number of Temporary Hit
    Points, roll {self.owner.rage_dmg_bonus}d6s, and add them together. If any of these
    Temporary Hit Points remain when your Rage ends, they vanish."""


#############################################################################
class BranchesOfTheTree(BaseAbility):
    tag = Ability.BRANCHES_OF_THE_TREE
    _desc = """ """

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.strength.modifier + self.owner.proficiency_bonus
        return f"""Whenever a creature you can see starts its turn within 30 feet of you while your Rage is active, 
        you can take a Reaction to summon spectral branches of the World Tree around it. The target must succeed on a 
        Strength saving thrown (DC {dc}) or be teleported to an unoccupied space you can see within 5 feet of 
        yourself or in the nearest unoccupied space you can see. After the target teleports, you can reduce its Speed 
        to 0 until the end of the current turn."""


# EOF

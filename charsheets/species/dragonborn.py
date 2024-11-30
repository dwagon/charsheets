from typing import TYPE_CHECKING
from enum import StrEnum, auto

from charsheets.constants import Ability, DamageType
from charsheets.species import Species
from charsheets.ability import BaseAbility


#############################################################################
class Ancestor(StrEnum):
    BLACK = auto()
    BLUE = auto()
    BRASS = auto()
    BRONZE = auto()
    COPPER = auto()
    GOLD = auto()
    GREEN = auto()
    RED = auto()
    SILVER = auto()
    WHITE = auto()


#############################################################################
class Dragonborn(Species):
    #########################################################################
    def __init__(self, ancestor: Ancestor):
        super().__init__()
        self.ancestor = ancestor

    #########################################################################
    def species_abilities(self) -> set[Ability]:
        results = {Ability.BREATH_WEAPON, Ability.DARKVISION60}
        if self.character.level >= 5:
            results.add(Ability.DRACONIC_FLIGHT)
        return results

    #########################################################################
    @property
    def name(self) -> str:
        return f"{self.ancestor.title()} Dragonborn"

    #########################################################################
    def add_damage_resistances(self) -> set[DamageType]:
        match self.ancestor:
            case Ancestor.BLACK:
                return {DamageType.ACID}
            case Ancestor.BLUE:
                return {DamageType.LIGHTNING}
            case Ancestor.BRASS:
                return {DamageType.FIRE}
            case Ancestor.BRONZE:
                return {DamageType.LIGHTNING}
            case Ancestor.COPPER:
                return {DamageType.ACID}
            case Ancestor.GOLD:
                return {DamageType.FIRE}
            case Ancestor.GREEN:
                return {DamageType.POISON}
            case Ancestor.RED:
                return {DamageType.FIRE}
            case Ancestor.SILVER:
                return {DamageType.COLD}
            case Ancestor.WHITE:
                return {DamageType.COLD}
        return set()


#############################################################################
class AbilityBreathWeapon(BaseAbility):
    tag = Ability.BREATH_WEAPON
    desc = """Stuff"""


# EOF

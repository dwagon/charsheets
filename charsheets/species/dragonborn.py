from enum import StrEnum, auto
from typing import TYPE_CHECKING
from charsheets.ability import BaseAbility
from charsheets.attack import Attack
from charsheets.constants import Ability, DamageType, Movements
from charsheets.species import Species
from charsheets.exception import UnhandledException
from charsheets.reason import Reason, SignedReason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


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
    def mod_add_damage_resistances(self, character: "Character") -> set[DamageType]:
        return {damage_type(self.ancestor)}


#############################################################################
class AbilityDraconicFlight(BaseAbility):
    tag = Ability.DRACONIC_FLIGHT
    desc = """ When you reach character level 5, you can channel draconic magic to give yourself temporary flight. 
    As a Bonus Action, you sprout spectral wings on your back that last for 10 minutes or until you retract the
    wings (no action required) or have the Incapacitated condition. During that time, you have a Fly Speed equal 
    to your Speed. Your wings appear to be made of the same energy as your Breath Weapon. Once you use this trait,
    you can’t use it again until you finish a Long Rest."""

    def mod_fly_movement(self, character: "Character") -> Reason:
        return Reason("Draconic Flight", character.movements[Movements.SPEED].value)


#############################################################################
class AbilityBreathWeapon(BaseAbility):
    tag = Ability.BREATH_WEAPON
    desc = """Dragonborn breath weapon"""

    def mod_add_attack(self, character: "Character") -> set[Attack]:
        if character.level >= 17:
            dmg_dice = "4d10"
        elif character.level >= 11:
            dmg_dice = "3d10"
        elif character.level >= 5:
            dmg_dice = "2d10"
        else:
            dmg_dice = "1d10"

        return {
            Attack(
                f"{character.species.ancestor.title()} breath weapon",
                atk_bonus=SignedReason("None", 0),
                dmg_dice=dmg_dice,
                dmg_bonus=SignedReason("None", 0),
                dmg_type=damage_type(character.species.ancestor),
            )
        }


#########################################################################
def damage_type(ancestor: Ancestor) -> DamageType:
    match ancestor:
        case Ancestor.BLACK:
            return DamageType.ACID
        case Ancestor.BLUE:
            return DamageType.LIGHTNING
        case Ancestor.BRASS:
            return DamageType.FIRE
        case Ancestor.BRONZE:
            return DamageType.LIGHTNING
        case Ancestor.COPPER:
            return DamageType.ACID
        case Ancestor.GOLD:
            return DamageType.FIRE
        case Ancestor.GREEN:
            return DamageType.POISON
        case Ancestor.RED:
            return DamageType.FIRE
        case Ancestor.SILVER:
            return DamageType.COLD
        case Ancestor.WHITE:
            return DamageType.COLD
    raise UnhandledException(f"Unhandled dragonborn ancestor {ancestor}")


# EOF

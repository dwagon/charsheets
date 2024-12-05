""" Abilities"""

from typing import TYPE_CHECKING
from pathlib import Path
from charsheets.constants import Ability, DamageType
from charsheets.exception import UnhandledException
from charsheets.util import import_generic
from charsheets.spells import Spells
from charsheets.attack import Attack
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class BaseAbility:
    desc = "Unspecified"
    tag: Ability = Ability.NONE

    def mod_add_prepared_spells(self, character: "Character") -> set[Spells]:
        return set()

    def mod_add_attack(self, character: "Character") -> set[Attack]:
        return set()

    def mod_add_damage_resistances(self, character: "Character") -> set[DamageType]:
        return set()

    def mod_swim_movement(self, character: "Character") -> int:
        return 0

    def mod_fly_movement(self, character: "Character") -> int:
        return 0


#############################################################################
ABILITY_MAPPING: dict[Ability, BaseAbility] = import_generic(class_prefix="Ability", path=Path("abilities"))
ABILITY_MAPPING.update(import_generic(class_prefix="Ability", path=Path("species")))


#############################################################################
def get_ability(ability: Ability):
    try:
        return ABILITY_MAPPING[ability]
    except KeyError as e:
        raise UnhandledException(f"Unknown ability {ability}") from e


# EOF

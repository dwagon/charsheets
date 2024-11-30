""" Abilities"""

from charsheets.constants import Ability
from charsheets.exception import UnhandledException
from charsheets.util import import_generic


#############################################################################
class BaseAbility:
    desc = "Unspecified"


#############################################################################
ABILITY_MAPPING: dict[Ability, BaseAbility] = import_generic(class_prefix="Ability", path="abilities")
ABILITY_MAPPING.update(import_generic(class_prefix="Ability", path="species"))


#############################################################################
def get_ability(ability: Ability):
    try:
        return ABILITY_MAPPING[ability]
    except KeyError as e:
        raise UnhandledException(f"Unknown ability {ability}") from e


# EOF

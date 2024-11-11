""" Abilities"""

import glob
import importlib.util

from charsheets.constants import Ability
from charsheets.exception import UnhandledException


#############################################################################
class BaseAbility:
    desc = "Unspecified"


#############################################################################
def import_abilities() -> dict[Ability, type[BaseAbility]]:
    abilities: dict[Ability, type[BaseAbility]] = {}
    files = glob.glob("charsheets/abilities/*.py")
    for py_file_name in files:
        file_name = py_file_name.replace(".py", "")
        module_name = file_name.replace("/", ".")
        spec = importlib.util.spec_from_file_location(module_name, py_file_name)
        if not spec:
            raise ImportError(f"import_abilities: Couldn't load spec from {py_file_name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore
        classes = dir(module)
        for class_name in classes:
            if class_name.startswith("Ability") and class_name != "Ability":
                klass = getattr(module, class_name)
                abilities[getattr(klass, "tag")] = klass
    return abilities


#############################################################################
ABILITY_MAPPING = import_abilities()


#############################################################################
def get_ability(ability: Ability):
    try:
        return ABILITY_MAPPING[ability]
    except KeyError as e:
        raise UnhandledException(f"Unknown ability {ability}") from e


# EOF

from typing import Type

from charsheets.constants import Origin, Feat, Skill
from charsheets.exception import UnhandledException
from charsheets.util import import_generic


#################################################################################
class BaseOrigin:
    tag = Origin.NONE
    proficiencies: set[Skill] = set()
    origin_feat = Feat.NONE

    #############################################################################
    def __repr__(self):
        return f"{self.tag.name.title()}"


#############################################################################
ORIGIN_MAPPING: dict[Origin, Type[BaseOrigin]] = import_generic(class_prefix="Origin", path="origins")


#################################################################################
def origin_picker(origin: Origin) -> BaseOrigin:
    try:
        return ORIGIN_MAPPING[origin]()
    except KeyError as e:
        raise UnhandledException(f"Unknown origin {origin}") from e


# EOF

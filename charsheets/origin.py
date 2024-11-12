from typing import Type

from charsheets.constants import Origin, Feat
from charsheets.exception import UnhandledException
from charsheets.util import import_generic


#################################################################################
class BaseOrigin:

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        raise NotImplemented


#############################################################################
ORIGIN_MAPPING: dict[Origin, Type[BaseOrigin]] = import_generic(class_prefix="Origin", path="origins")


#################################################################################
def origin_picker(origin: Origin) -> BaseOrigin:
    try:
        return ORIGIN_MAPPING[origin]()
    except KeyError as e:
        raise UnhandledException(f"Unknown origin {origin}") from e


# EOF

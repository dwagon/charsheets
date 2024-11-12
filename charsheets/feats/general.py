from typing import TYPE_CHECKING

from charsheets.feat import BaseFeat
from charsheets.constants import Feat

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class FeatActor(BaseFeat):
    tag = Feat.ACTOR
    desc = """You gain the following benefits.
    
    Impersonation.
    
    Mimicry."""


# EOF

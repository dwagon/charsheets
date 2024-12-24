""" Feats"""

from pathlib import Path

from charsheets.constants import Feat

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseFeat:
    tag = Feat.NONE


#############################################################################
FEAT_MAPPING: dict[Feat, BaseFeat] = import_generic(class_prefix="Feat", path=Path("feats"))


#############################################################################
def get_feat(feat: Feat):
    try:
        return FEAT_MAPPING[feat]
    except KeyError:
        raise UnhandledException(f"Unknown feat {feat}")

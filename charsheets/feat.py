""" Feats"""

from charsheets.constants import Feat
from charsheets.exception import UnhandledException
from charsheets.util import import_generic


#############################################################################
class BaseFeat:
    pass


#############################################################################
FEAT_MAPPING: dict[Feat, BaseFeat] = import_generic(class_prefix="Feat", path="feats")


#############################################################################
def get_feat(feat: Feat):
    try:
        return FEAT_MAPPING[feat]
    except KeyError:
        raise UnhandledException(f"Unknown feat {feat}")

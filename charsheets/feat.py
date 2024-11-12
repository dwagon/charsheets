""" Feats"""

import glob
import importlib.util

from charsheets.constants import Feat, CharClassName
from charsheets.exception import UnhandledException


#############################################################################
class BaseFeat:
    pass


#############################################################################
def import_feats() -> dict[Feat, type[BaseFeat]]:
    feats: dict[Feat, type[BaseFeat]] = {}
    files = glob.glob("charsheets/feats/*.py")
    for py_file_name in files:
        file_name = py_file_name.replace(".py", "")
        module_name = file_name.replace("/", ".")
        spec = importlib.util.spec_from_file_location(module_name, py_file_name)
        if not spec:
            raise ImportError(f"import_feats: Couldn't load spec from {py_file_name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore
        classes = dir(module)
        for class_name in classes:
            if class_name.startswith("Feat") and class_name != "Feat":
                klass = getattr(module, class_name)
                feats[getattr(klass, "tag")] = klass
    return feats


#############################################################################
FEAT_MAPPING = import_feats()


#############################################################################
def get_feat(feat: Feat):
    try:
        return FEAT_MAPPING[feat]
    except KeyError:
        raise UnhandledException(f"Unknown feat {feat}")

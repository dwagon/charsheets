import glob
import importlib.util
import os.path
from typing import Any


#############################################################################
# import_generic(class_prefix="Feat", path="feats")


#############################################################################
def import_generic(class_prefix: str, path: str) -> dict[Any, Any]:
    feats: dict[Any, Any] = {}
    files = glob.glob(os.path.join("charsheets", path, "*.py"))
    for py_file_name in files:
        file_name = py_file_name.replace(".py", "")
        module_name = file_name.replace("/", ".")
        spec = importlib.util.spec_from_file_location(module_name, py_file_name)
        if not spec:
            raise ImportError(f"import_generic: Couldn't load spec from {py_file_name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore
        classes = dir(module)
        for class_name in classes:
            if class_name.startswith(class_prefix) and class_name != class_prefix:
                klass = getattr(module, class_name)
                feats[getattr(klass, "tag")] = klass
    return feats

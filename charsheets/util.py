import glob
import importlib.util
import sys
from pathlib import Path
from typing import Any


#############################################################################
def import_generic(class_prefix: str, path: Path) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    paths = [path, Path(path).joinpath("homebrew")]
    for dir in paths:
        base_dir = Path("charsheets").joinpath(dir)

        files = base_dir.glob("*.py")
        for py_file_name in files:
            ans = do_import(py_file_name, class_prefix)
            result.update(ans)
    return result


#############################################################################
def do_import(file_name: Path, class_prefix) -> dict[Any, Any]:
    """Import classes from a specific file {file_name}"""
    result: dict[Any, Any] = {}
    file_stem = file_name.stem
    module_name = file_stem.replace("/", ".")
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    if not spec:
        raise ImportError(f"import_generic: Couldn't load spec from {file_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    classes = dir(module)
    for class_name in classes:
        if class_name.startswith(class_prefix) and class_name != class_prefix:
            klass = getattr(module, class_name)
            try:
                result[getattr(klass, "tag")] = klass
            except AttributeError:
                pass  # No tag - not a useful class
    return result


#############################################################################
def safe(instr: str) -> str:
    """Make it safe for outputting"""
    return instr.replace("_", " ")


# EOF

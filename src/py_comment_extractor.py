from pathlib import Path
import importlib.util
from types import ModuleType


def import_module(module_path: str) -> ModuleType:
    module_path = Path(module_path)
    spec = importlib.util.spec_from_file_location(module_path.name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def module_docstring(module_path:str) -> str:
    return import_module(module_path).__doc__

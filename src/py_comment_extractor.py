"""Extracts comments from python files"""
from pathlib import Path
import importlib.util
from types import ModuleType
import os
import logging
INIT_FILE = '__init__.py'


def import_module(module_path: str) -> ModuleType:
    module_path = Path(module_path)
    spec = importlib.util.spec_from_file_location(
        module_path.name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    logging.debug(module)
    return module


def module_docstring(module_path: str) -> str:
    logging.debug(module_path)
    try:
        return import_module(module_path).__doc__ or ''
    except Exception:  # pylint: disable=broad-except
        return ''


def package_docstring(package_path: str)->str:
    """Returns the packages docstring, extracted by its `__init__.py` file"""
    logging.debug(package_path)
    if os.path.isdir(package_path) and INIT_FILE in os.listdir(package_path):
        return module_docstring(os.path.join(package_path, INIT_FILE))
    return ''

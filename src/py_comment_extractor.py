"""Extracts comments from python files"""
from pathlib import Path
import importlib.util
from types import ModuleType
from typing import Any
import os
import logging
INIT_FILE = '__init__.py'


def import_module(module_path: os.PathLike) -> ModuleType:
    module_pathlib_path = Path(module_path)
    spec:Any = importlib.util.spec_from_file_location(
        module_pathlib_path.name, str(module_pathlib_path))
    module:Any = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    logging.debug(module)
    return module


def module_docstring(module_path: os.PathLike) -> str:
    logging.debug(module_path)
    try:
        return import_module(module_path).__doc__ or ''
    except Exception:  # pylint: disable=broad-except
        return ''


def package_docstring(package_path: Path)->str:
    """Returns the packages docstring, extracted by its `__init__.py` file"""
    logging.debug(package_path)
    init_file =package_path/ INIT_FILE
    if package_path.is_dir() and init_file.exists():
        return module_docstring(init_file)
    return ''

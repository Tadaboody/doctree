"""Test file for the python comment extractor"""
from pathlib import Path

import pytest

from src.py_comment_extractor import module_docstring, package_docstring

FILE_DIR = Path(__file__).parent
FILE_PATH = Path(__file__)

def test_module_docstring():
    assert __doc__ == module_docstring(FILE_PATH)


def test_non_module_docstring():
    assert module_docstring(FILE_DIR / '.coveragerc.ini') == ''


@pytest.mark.parametrize("path,doc",
                         [(FILE_DIR/'test_dir'/'package',
                           "Example python package"),
                          (FILE_DIR.parent/'src',
                           "Creates project structure files with built-in documentation")
                          ])
def test_package_docstring(path: Path, doc: str):
    assert package_docstring(path) == doc

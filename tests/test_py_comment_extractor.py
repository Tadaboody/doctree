"""Test file for the python comment extractor"""
import os

from src.py_comment_extractor import import_module, module_docstring

FILE_PATH = os.path.abspath(__file__)
import os
FILE_DIR = os.path.abspath(os.path.dirname(__file__))


def test_import_module():
    this_module = import_module(FILE_PATH)
    assert 'test_import_module' in dir(this_module)

def test_module_docstring():
    assert __doc__ == module_docstring(FILE_PATH)
    
def test_non_module_docstring():
    assert module_docstring(os.path.join(FILE_DIR,'.coveragerc.ini')) == ''
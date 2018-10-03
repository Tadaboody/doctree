"""Test file for the python comment extractor"""
import os

from src.py_comment_extractor import import_module

FILE_PATH = os.path.abspath(__file__)


def test_import_module():
    this_module = import_module(FILE_PATH)
    assert 'test_import_module' in dir(this_module)

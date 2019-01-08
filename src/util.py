"""Misc util functions"""
import os
from contextlib import contextmanager


@contextmanager
def cd(path: os.PathLike):
    """Context manager that sets the cwd to be `path`"""
    old_path = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(old_path)

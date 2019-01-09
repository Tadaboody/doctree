"""The main tree script"""
import os
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable, Iterator, Set, Tuple,Union

from src.py_comment_extractor import docstring


DEFAULT_IGNORE = ('__pycache__', '.git', '__init__.py')

SPACE = ' '
PathType = Union[os.PathLike,str]

def _path_depth(path:Path)->int:
    return len(path.parents) - 1 
def _with_dirs(paths:Iterable[os.PathLike]) -> Iterator[Path]:
    """Yields `paths` with the dirs as they appear"""
    known_dirs:Set[Path] = { Path('.') }
    path:Path
    for path in ( Path(path) for path in paths ):
        yield from set(path.parents) - known_dirs
        known_dirs = known_dirs.union(set( path.parents ))
        yield path

@contextmanager
def _cd(path:PathType)->Iterator[None]:
    old_path = Path.cwd()
    os.chdir(path)
    yield
    os.chdir(old_path)

def tree_dir(starting_dir: PathType='.', ignored_globs=DEFAULT_IGNORE) -> Iterator[Tuple[Path, str, int]]:
    """
    Yields the lines of git repo at `starting_dir`, their depth in the tree, and their docstring
    params:
        starting_dir: the directory you start in
        ignored_globs: glob patterns that should be ignored in iteration
        max_depth: The maximum depth to go into the file tree
    returns: a tuple of (path,docstring,depth)
    """
    with _cd(starting_dir):
        out = subprocess.check_output(('git', 'ls-files')).decode()
        path:Path
        for path in _with_dirs(out.splitlines()):
            doc = docstring(path)
            doc = f'  # {doc}' if doc else ''
            yield path, doc, _path_depth(path)


def depth_seperator(indent_char: str, depth: int, is_dir: bool) -> str:
    """Returns the prefix to display a node of `depth`"""
    return  indent_char+ indent_char*depth 

def doctree(starting_dir: str,indent_char:str=SPACE*2) -> Iterator[str]:
    """Prints the doctree in a markdown-tolerant way"""
    file:Path
    for file, doc, depth in tree_dir(starting_dir):
        if file.is_dir():
            yield ''
            if doc:
                yield depth_seperator(indent_char,depth-1,file.is_dir()) +doc
            yield depth_seperator(indent_char,depth,file.is_dir()) + file.name
        else:
            yield depth_seperator(indent_char, depth, file.is_dir()) + file.name + doc

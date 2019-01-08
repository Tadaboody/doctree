"""The main tree script"""
import os
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable, Iterator, Set, Tuple

from src.py_comment_extractor import docstring

BACKSLASH = '\\'

DEFAULT_IGNORE = ('__pycache__', '.git', '__init__.py')

def path_depth(path:Path)->int:
    return len(path.parents) - 1 
def with_dirs(paths:Iterable[os.PathLike]) -> Iterator[Path]:
    """Yields `paths` with the dirs as they appear"""
    known_dirs:Set[Path] = { Path('.') }
    path:Path
    for path in ( Path(path) for path in paths ):
        yield from set(path.parents) - known_dirs
        known_dirs = known_dirs.union(set( path.parents ))
        yield path
@contextmanager
def cd(path:Path):
    old_path = Path.cwd()
    os.chdir(path)
    yield
    os.chdir(old_path)

def tree_dir(starting_dir: Path='.', ignored_globs=DEFAULT_IGNORE, max_depth=None) -> Iterator[Tuple[Path, str, int]]:
    """
    params:
        starting_dir: the directory you start in
        ignored_globs: glob patterns that should be ignored in iteration
        max_depth: The maximum depth to go into the file tree
    returns: a tuple of (path,docstring,depth)
    """
    with cd(starting_dir):
        out = subprocess.check_output(('git', 'ls-files')).decode()
        for path in ( path for path in with_dirs(out.splitlines()) if (not max_depth or path_depth(path) <=max_depth ) ):
            doc = docstring(path)
            doc = f'  # {doc}' if doc else ''
            yield path, doc, path_depth(path)


def depth_seperator(indent_char: str, depth: int, is_dir: bool) -> str:
    """Returns the prefix to display a node of `depth`"""
    return f"{indent_char}{f' {indent_char}'*depth}{BACKSLASH if is_dir else ''}"


def doctree(starting_dir: str, max_depth: int = None):
    """Prints the doctree in a markdown-tolerant way"""
    for file, doc, depth in tree_dir(Path(starting_dir), max_depth=max_depth):
        yield depth_seperator('|', depth, file.is_dir()) + file.name + doc

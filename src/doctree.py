"""The main tree script"""
from functools import partial
from pathlib import Path
from typing import Tuple, Generator

from src.git_ignored_files import git_ignored_files
from src.py_comment_extractor import docstring
from src.dfs import dfs, safe_iterdir

BACKSLASH = '\\'


def ignored(filename: Path, starting_dir: Path, ignored_globs: Tuple[Path, ...]):
    """Check if a file is ignored by the user"""
    if filename == starting_dir:
        return False
    path_ignored = git_ignored_files(
        starting_dir) + ignored_globs
    return any(filename.match(str(path)) for path in path_ignored)


DEFAULT_IGNORE = ('__pycache__', '.git', '__init__.py')


def tree_dir(starting_dir: Path, ignored_globs=DEFAULT_IGNORE, max_depth=None) -> Generator[Tuple[Path, str, int], None, None]:
    """
    params:
        starting_dir: the directory you start in
        ignored_globs: glob patterns that should be ignored in iteration
        max_depth: The maximum depth to go into the file tree
    returns: a tuple of (path,docstring,depth)
    """

    item: Path
    ignored_in_tree = partial(
        ignored, starting_dir=starting_dir, ignored_globs=ignored_globs)
    dfs_walk = dfs(Path(starting_dir), safe_iterdir,
                   predicate=ignored_in_tree, max_depth=max_depth)
    for item, depth in dfs_walk:
        # item is all the things in the directory that does not ignored
        full_path = Path.resolve(item)
        doc = docstring(full_path)
        doc = f'  # {doc}' if doc else ''
        yield item, doc, depth


def depth_seperator(indent_char: str, depth: int, is_dir: bool) -> str:
    """Returns the prefix to display a node of `depth`"""
    return f"{indent_char}{f' {indent_char}'*depth}{BACKSLASH if is_dir else ''}"


def doctree(starting_dir: str, max_depth: int = None):
    """Prints the doctree in a markdown-tolerant way"""
    for file, doc, depth in tree_dir(Path(starting_dir), max_depth=max_depth):
        yield depth_seperator('|', depth, file.is_dir()) + file.name + doc

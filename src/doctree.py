"""The main tree script"""
import glob
from pathlib import Path
from typing import Iterator, Tuple

from src.git_ignored_files import git_ignored_files
from src.py_comment_extractor import module_docstring, package_docstring
from src.dfs import dfs, safe_iterdir

BACKSLASH = '\\'
SLASH = '/'

def tree_dir(starting_dir: Path, ignored_globs=('__pycache__', '.git', '__init__.py'))->Iterator[Tuple[str, int]]:
    """
    params:
        starting_dir: the directory you start in
        ignored_globs: glob patterns that should be ignored in iteration
    returns: The documantion string
    """

    def ignored(filename: Path):
        """Check if a file is ignored by the user"""
        if filename == starting_dir:
            return False
        path_ignored = git_ignored_files(
            starting_dir) + ignored_globs 
        return any(filename.match(str(path)) for path in path_ignored)

    item: Path
    for item, depth in ((path, _) for path, _ in dfs(Path(starting_dir), safe_iterdir, ignored)):
        # item is all the things in the directory that does not ignored
        full_path = Path.resolve(item)
        docstring = module_docstring(full_path) + package_docstring(full_path)
        doc = f'  # {module_docstring(full_path)}' if docstring else ''
        yield item, doc, depth


def depth_seperator(indent_char: str, depth: int, is_dir: bool)->str:
    """Returns the prefix to display a node of `depth`"""
    return f"{indent_char}{f' {indent_char}'*depth}{BACKSLASH if is_dir else ''}"


def print_doctree(starting_dir: str):
    """Prints the doctree in a markdown-tolerant way"""
    for file, doc, depth in tree_dir(Path(starting_dir)):
        print(depth_seperator('|', depth, file.is_dir()) + file.name + doc)


if __name__ == '__main__':
    print_doctree('.')

"""The main tree script"""
import glob
import os
from pathlib import Path
from typing import Iterator

from src.git_ignored_files import git_ignored_files,cd
from src.py_comment_extractor import module_docstring,package_docstring

BACKSLASH = '\\'


fnmatch = glob.fnmatch.fnmatch # can't import for some reason


def tree_dir(starting_dir: Path, max_depth: int=None, indent_char: str='|', ignored_globs=('.git', '__init__.py','.vscode'))-> str:

    def rec_tree_dir(current_dir: str, depth) -> Iterator[str]:
        if max_depth and depth > max_depth:
            return
        def ignored(file):
            ignore_patterns = ignored_globs + git_ignored_files(current_dir) + git_ignored_files(starting_dir)
            return any(fnmatch(file, pattern) or fnmatch(os.path.join(current_dir, file), pattern) or fnmatch(os.path.abspath(file), pattern)
                       for pattern in ignore_patterns)

        non_ignored_files = (file for file in os.listdir(current_dir) if not ignored(file))
        
        for file in non_ignored_files:
            full_path = os.path.join(current_dir, file)
            isdir = os.path.isdir(full_path)
            docstring = module_docstring(full_path) + package_docstring(full_path)
            doc = f'  # {module_docstring(full_path)}' if docstring else ''
            yield depth_seperator(indent_char, depth) + (BACKSLASH if isdir else '') + file + doc
            if isdir:
                yield from rec_tree_dir(current_dir=full_path, depth=depth+1)
                yield f"{depth_seperator(indent_char,depth)}/"
            
    with cd(starting_dir):
        return '\n'.join(rec_tree_dir(starting_dir, 0))


def depth_seperator(indent_char: str, depth: int)->str:
    return f"{indent_char}{f' {indent_char}'*depth}"


if __name__ == '__main__':
    print(tree_dir('.', max_depth=2))

"""The main tree script"""
import glob
import os
from pathlib import Path
from typing import Iterator

from src.py_comment_extractor import module_docstring

BACKSLASH = '\\'


fnmatch = glob.fnmatch.fnmatch # can't import for some reason


def tree_dir(starting_dir: Path, max_depth: int=None, indent_char: str='|', ignored_globs=('.git', 'venv','*cache*'))-> str:

    def rec_tree_dir(current_dir: Path, depth) -> Iterator[str]:
        if max_depth and depth > max_depth:
            return
        non_ignored_files = (file for file in os.listdir(current_dir) if not any(
            fnmatch(file, pattern) for pattern in ignored_globs))
        
        for file in non_ignored_files:
            full_path = os.path.join(current_dir, file)
            isdir = os.path.isdir(full_path)
            docstring = module_docstring(full_path)
            doc = f'  # {module_docstring(full_path)}' if not isdir and docstring else ''
            yield depth_seperator(indent_char, depth) + (BACKSLASH if isdir else '') + file + doc
            if isdir:
                yield from rec_tree_dir(current_dir=os.path.join(current_dir, file), depth=depth+1)
                yield f"{depth_seperator(indent_char,depth)}/"
    return '\n'.join(rec_tree_dir(starting_dir, 0))


def depth_seperator(indent_char: str, depth: int)->str:
    return f"{indent_char}{f' {indent_char}'*depth}"


if __name__ == '__main__':
    print(tree_dir('.', max_depth=2))

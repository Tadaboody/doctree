"""The main tree script"""
import glob
import os
from pathlib import Path
from typing import Iterator

from src.git_ignored_files import git_ignored_files,cd
from src.py_comment_extractor import module_docstring,package_docstring

BACKSLASH = '\\'
SLASH = '/'

fnmatch = glob.fnmatch.fnmatch # can't import for some reason

def ignored(filename: str, starting_dir: Path, ignored_globs=('.git', '__init__.py','.vscode')):
    """
    manage the ignore files (.gitignore and ignored_globals) for this path.
    """
    path_ignored = git_ignored_files(starting_dir) + ignored_globs  # check if need to add git_ignored_files(starting_dir)

    return any(fnmatch(filename, path) for path in path_ignored)


def tree_dir(starting_dir: Path, indent_char: str="|", times_indented:int=1):
    """
    params:
        startding_dir: the directory you start in
    returns: The documantion string
    """
    out = dict()
    my_dirs_docs = dict()
    not_ignored_files = (Path(this_dir_not_ignored_file) for this_dir_not_ignored_file in Path(starting_dir).glob('*') if not ignored(this_dir_not_ignored_file, starting_dir))
    for item in not_ignored_files:
        # item is all the things in the directory that does not ignored
        full_path = Path.resolve(item)
        docstring = module_docstring(full_path) + package_docstring(full_path)
        doc = f'  # {module_docstring(full_path)}' if docstring else ''
        if not full_path.is_dir():
            out[item.name] = indent_char*times_indented + item.name + doc
        else:
            my_dirs_docs[item.name] = item.name + doc
    for o in out:
        print(out[o])
    return my_dirs_docs


def depth_seperator(indent_char: str, depth: int)->str:
    return f"{indent_char}{f' {indent_char}'*depth}"


def run(start, times=1):
    dirs = tree_dir(start, times_indented=times)
    indent_char = "|"
    for _dir in dirs:
        print(indent_char*times + BACKSLASH)
        print(indent_char*(1 + times) + dirs[_dir])
        run(_dir, times=times+1)
    print(indent_char*(times-1) + SLASH)

if __name__ == '__main__':
    print('.')
    run('.')

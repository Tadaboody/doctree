"""Outputs files ignored by git"""
from typing import Tuple
from subprocess import check_output,CalledProcessError
import os
from src.util import cd


def git_ignored_files(repo_path:str='.')->Tuple[str]:
    """Files ignored by the git repository in `repo_path`, relative to `repo_path`"""
    # in bash:
    # "git status --ignored  --porcelain=v2|grep '!'|awk '{print }'"
    try:
        with cd(repo_path):
            git_output =  check_output(['git', 'status', '--ignored', '--porcelain']).decode("utf-8").splitlines()
            return tuple( os.path.abspath(file.strip('!! ')) for file in git_output
                    if file.startswith('!!') )
    except CalledProcessError:
        return ()

if __name__ == '__main__':
    print(git_ignored_files())
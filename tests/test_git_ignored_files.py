import logging

from src import git_ignored_files
import os
from os.path import join


def test_git_ignored_files():
    FILE_DIR = os.path.abspath(os.path.dirname(__file__))
    repo_path = os.path.join(FILE_DIR, 'test_dir', 'repo')
    ignored_files = git_ignored_files.git_ignored_files( repo_path)
    logging.debug(ignored_files)
    assert join(repo_path, 'ignored') in ignored_files
    assert join(repo_path, '.gitignore') not in ignored_files

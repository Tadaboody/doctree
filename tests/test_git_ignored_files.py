import logging

from src import git_ignored_files


def test_git_ignored_files():
    from pathlib import Path
    FILE_DIR = Path(__file__).parent
    repo_path = FILE_DIR / 'test_dir' / 'repo'
    ignored_files = git_ignored_files.git_ignored_files(repo_path)
    logging.debug(ignored_files)
    assert any(file.match('ignored') for file in ignored_files)
    assert not any(file.match('.gitignore') for file in ignored_files)
    assert not any(file.match('not_ignored') for file in ignored_files)

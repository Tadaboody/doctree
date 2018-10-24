"""Tests for the dfs module"""
from src.dfs import dfs, safe_iterdir
from pathlib import Path


FILE_DIR = Path(__file__).parent
TEST_DIR = FILE_DIR/'test_dir'


def test_dfs():
    INIT_FILE = TEST_DIR/'package'/'__init__.py'
    dfs_walk = list(dfs(TEST_DIR, safe_iterdir))
    assert (INIT_FILE, 2) in dfs_walk
    assert (TEST_DIR/'package', 1) in dfs_walk
    assert (TEST_DIR, 0) in dfs_walk
    assert (TEST_DIR/'..', 0) not in dfs_walk

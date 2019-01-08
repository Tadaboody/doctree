from src import doctree
from pathlib import Path
import logging


def test_all_in_tree():
    """Tests that all of the test_dir is represented in the output string"""
    FILE_DIR = Path(__file__).parent
    test_dir = FILE_DIR/'test_dir'
    output = list(doctree.doctree(test_dir))
    logging.debug(output)
    for test_file in (str(file) for file in test_dir.glob('*')):
        assert any(test_file in line for line in output)

from src import tree_dir,util
from glob import glob

def test_all_in_tree():
    import os
    FILE_DIR = os.path.abspath(os.path.dirname(__file__))
    test_dir = os.path.join(FILE_DIR,'test_dir')
    tree = tree_dir(test_dir)
    with util.cd(test_dir):
        assert(glob('*',recursive=True))
        assert(all(any(g_path in line for line in tree.splitlines())
                   for g_path in glob('*', recursive=True)))

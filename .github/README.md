# DocTree
## Autogenerate a directory tree with documentation built-in

Essentially this project will leverage built-in documentation schemes like python docstrings to create 

## Installation
clone the repository
run ``python setup.py install``
### for development:
run 
```
pip install -e .
pip install -r requirements.txt
```

## Example output (in current version a7f0237):

```
|\
| |\src
| | |dfs.py  # Generic and pythonic implementation of the Depth First Search traversal algorithm
| | |doctree.py  # The main tree script
| | |main.py  # Entry points for command scripts
| | |py_comment_extractor.py  # Extracts comments from python files
| | |util.py  # Misc util functions
| | |git_ignored_files.py  # Outputs files ignored by git
| |\.vscode
| | |settings.json
| |\.github
| | |pre-commit-script.sh
| | |install-pre-commit-script.sh
| | |example_output.md
| | |ISSUE_TEMPLATE.md
| | |README.md
| | |base_README.md
| | |PULL_REQUEST_TEMPLATE.md
| |.env
| |.gitignore
| |setup.py
| |\tests
| | |test_doctree.py
| | |test_py_comment_extractor.py  # Test file for the python comment extractor
| | |test_dfs.py  # Tests for the dfs module
| | |\test_dir
| | | |\package  # 
| | | |\repo
| | | | |.gitignore
| | | | |not_ignored
| | | | |ignored
| | |test_git_ignored_files.py
| | |.coveragerc.ini
| |run_tests_with_coverage.sh
| |requirements.txt
```

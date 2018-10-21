# DocTree
## Autogenerate a directory tree with documentation built-in

Essentially this project will leverage built-in documentation schemes like python docstrings to create 

## Installation
clone the repository
run ``python setup.py install``
### for development:
First, you need to install the program. you can do this by typing the commands below on your terminal: 
```
pip install -e .
pip install -r requirements.txt
```
In order to run the program you need to run ```doctree``` on your terminal.
## Example output (in current version 1b45766):

```
|requirements.txt
|run_tests_with_coverage.sh
|\tests
| |.coveragerc.ini
| |test_git_ignored_files.py
| |\test_dir
| | |\repo
| | |/
| | |\package  # 
| | |/
| |/
| |test_py_comment_extractor.py  # Test file for the python comment extractor
| |test_doctree.py
|/
|setup.py
|.gitignore
|.env
|\.github
| |base_README.md
| |README.md
| |example_output.md
| |install-pre-commit-script.sh
| |pre-commit-script.sh
|/
|\src
| |git_ignored_files.py  # Outputs files ignored by git
| |util.py  # Misc util functions
| |py_comment_extractor.py  # Extracts comments from python files
| |main.py  # Entry points for command scripts
| |doctree.py  # The main tree script
|/
```


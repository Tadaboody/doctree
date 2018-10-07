# DocTree
## Autogenerate a directory tree with documentation built-in

Essentially this project will leverage built-in documentation schemes like python docstrings to create 


### Example output (in current version):

```
|requirements.txt
|run_tests_with_coverage.sh
|\tests
| |.coveragerc.ini
| |test_git_ignored_files.py
| |\test_dir
| | |\repo
| | |/
| |/
| |test_py_comment_extractor.py  # Test file for the python comment extractor
|/
|setup.py
|.gitignore
|.env
|\.github
| |base_README.md
| |README.md
| |example_output.md
| |pre-commit-script.sh
|/
|\build
| |\bdist.macosx-10.13-x86_64
| |/
|/
|\.vscode
| |settings.json
| |\.history
| | |run_tests_with_coverage_20181003165105.sh
| | |.gitignore_20181003170633
| | |doctree_20181003141113.py
| | |run_tests_with_coverage_20181003165725.sh
| | |\tests
| | |/
| | |.env_20181003141734
| | |doctree_20181003141112.py
| | |.gitignore_20181003170626
| | |.env_20181003141747
| | |run_tests_with_coverage_20181003165139.sh
| | |doctree_20181003141140.py
| | |\.github
| | |/
| | |\src
| | |/
| |/
| |\.ropeproject
| | |config.py
| | |objectdb
| |/
|/
|\src
| |git_ignored_files.py  # Outputs files ignored by git
| |util.py  # Misc util functions
| |__init__.py
| |py_comment_extractor.py  # Extracts comments from python files
| |doctree.py  # The main tree script
|/
```

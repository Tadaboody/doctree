# DocTree
## Autogenerate a directory tree with documentation built-in

Essentially this project will leverage built-in documentation schemes like python docstrings to create 


### Example output (in current version 1b45766):

```
|requirements.txt
|\.pytest_cache
|/
|.coverage
|cov.xml
|run_tests_with_coverage.sh
|\tests
| |.coveragerc.ini
| |\__pycache__
| | |test_py_comment_extractor.cpython-36-PYTEST.pyc
| | |test_py_comment_extractor.cpython-36.pyc
| |/
| |test_py_comment_extractor.py
|/
|setup.py
|.gitignore
|.env
|\.github
| |README.md
| |example_output.md
|/
|\venv
|/
|\.vscode
| |settings.json
| |\.history
| |\.ropeproject
|/
|\src
| |__init__.py
| |py_comment_extractor.py
| |\__pycache__
| | |doctree.cpython-36.pyc
| | |py_comment_extractor.cpython-36.pyc
| | |__init__.cpython-36.pyc
| |/
| |doctree.py
|/
```
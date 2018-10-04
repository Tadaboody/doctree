# DocTree
## Autogenerate a directory tree with documentation built-in

Essentially this project will leverage built-in documentation schemes like python docstrings to create 


### Example output (in current version 1b45766):

```
|requirements.txt
|\.pytest_cache
| |README.md
| |.gitignore
| |\v
| | |\cache
| | |/
| |/
|/
|\dist
| |doctree-0.1-py3.6.egg
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
| |test_py_comment_extractor.py  # Test file for the python comment extractor
|/
|\__pycache__
| |setup.cpython-36.pyc
|/
|setup.py
|.gitignore
|\doctree.egg-info
| |PKG-INFO
| |SOURCES.txt
| |top_level.txt
| |dependency_links.txt
|/
|.env
|\.github
| |base_README.md
| |README.md
| |example_output.md
| |package.json
|/
|\venv
| |\bin
| | |pip3.6
| | |pylint
| | |python3
| | |pytest
| | |easy_install
| | |coverage3
| | |python
| | |pip3
| | |easy_install-3.6
| | |activate.fish
| | |doctree
| | |isort
| | |pip
| | |pyreverse
| | |epylint
| | |activate
| | |coverage-3.6
| | |coverage
| | |py.test
| | |symilar
| | |activate.csh
| |/
| |\include
| |/
| |pyvenv.cfg
| |\lib
| | |\python3.6
| | |/
| |/
| |pip-selfcheck.json
|/
|\build
| |\bdist.macosx-10.13-x86_64
| |/
|/
|\.git
| |config
| |\objects
| | |\61
| | |/
| | |\0d
| | |/
| | |\95
| | |/
| | |\59
| | |/
| | |\3e
| | |/
| | |\3b
| | |/
| | |\69
| | |/
| | |\94
| | |/
| | |\02
| | |/
| | |\a4
| | |/
| | |\d9
| | |/
| | |\ac
| | |/
| | |\ad
| | |/
| | |\be
| | |/
| | |\ae
| | |/
| | |\d8
| | |/
| | |\ab
| | |/
| | |\eb
| | |/
| | |\ee
| | |/
| | |\cf
| | |/
| | |\fe
| | |/
| | |\c1
| | |/
| | |\18
| | |/
| | |\4b
| | |/
| | |\pack
| | |/
| | |\1f
| | |/
| | |\19
| | |/
| | |\4c
| | |/
| | |\2a
| | |/
| | |\88
| | |/
| | |\38
| | |/
| | |\info
| | |/
| | |\53
| | |/
| | |\55
| | |/
| | |\0a
| | |/
| | |\d3
| | |/
| | |\a0
| | |/
| | |\a7
| | |/
| | |\de
| | |/
| | |\e6
| | |/
| | |\ff
| | |/
| | |\f6
| | |/
| | |\2d
| | |/
| | |\1b
| | |/
| | |\24
| | |/
| | |\8c
| | |/
| | |\82
| | |/
| | |\8e
| | |/
| |/
| |HEAD
| |\info
| | |exclude
| |/
| |\logs
| | |HEAD
| | |\refs
| | |/
| |/
| |description
| |\hooks
| | |commit-msg.sample
| | |pre-rebase.sample
| | |pre-commit.sample
| | |applypatch-msg.sample
| | |fsmonitor-watchman.sample
| | |pre-receive.sample
| | |prepare-commit-msg.sample
| | |post-update.sample
| | |pre-applypatch.sample
| | |pre-push.sample
| | |update.sample
| |/
| |\refs
| | |\heads
| | |/
| | |\tags
| | |/
| | |\remotes
| | |/
| |/
| |index
| |\branches
| |/
| |COMMIT_EDITMSG
| |FETCH_HEAD
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
| | |\__pycache__
| | |/
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
| | |\__pycache__
| | |/
| |/
|/
|\src
| |__init__.py
| |py_comment_extractor.py
| |\__pycache__
| | |doctree.cpython-36.pyc
| | |py_comment_extractor.cpython-36.pyc
| | |__init__.cpython-36.pyc
| |/
| |doctree.py  # The main tree script
|/
```

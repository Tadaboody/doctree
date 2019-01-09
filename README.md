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

## Example output (in current version 0.1):

```sh
  .env

  .github
    ISSUE_TEMPLATE.md
    PULL_REQUEST_TEMPLATE.md
    README.md
    base_README.md
    example_output.md
    install-pre-commit-script.sh
    pre-commit-script.sh
  .gitignore

  .vscode
    settings.json
  requirements.txt
  run_tests_with_coverage.sh
  setup.py

    # Creates project structure files with built-in documentation
  src
    __init__.py  # Creates project structure files with built-in documentation
    doctree.py  # The main tree script
    main.py  # Entry points for command scripts
    py_comment_extractor.py  # Extracts comments from python files

    # Pytest tests for every doctree module. Run using python setup.py install
  tests
    .coveragerc.ini
    __init__.py  # Pytest tests for every doctree module. Run using python setup.py install

    test_dir

      # Example python package
      package
        __init__.py  # Example python package

      repo
        .gitignore
        ignored
        not_ignored
    test_py_comment_extractor.py  # Test file for the python comment extractor
```
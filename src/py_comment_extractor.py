"""Extracts comments from python files"""
import logging
import os
from pathlib import Path

INIT_FILE = '__init__.py'

def module_docstring(module_path: os.PathLike) -> str:
    import ast
    import inspect
    module_path = Path(module_path)
    try:
        module_ast = ast.parse(module_path.read_text(),filename=module_path.name)
    except SyntaxError:
        return ''
    module_doc = ast.get_docstring(module_ast)
    non_import_body = module_ast.body
    non_import_body = [ node for node in module_ast.body if not isinstance(node, (ast.Import, ast.ImportFrom)) ]
    if not module_doc and len( non_import_body ) == 1 and isinstance(non_import_body[0], (ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef)):
        module_doc = ast.get_docstring(non_import_body[0])
    if not module_doc:
        return ''
    return inspect.cleandoc(module_doc).splitlines()[0]

def package_docstring(package_path: Path) -> str:
    """Returns the packages docstring, extracted by its `__init__.py` file"""
    logging.debug(package_path)
    init_file = package_path / INIT_FILE
    if package_path.is_dir() and init_file.exists():
        return module_docstring(init_file)
    return ''
def docstring(path:Path):
    try:
        return package_docstring(path) if path.is_dir() else module_docstring(path)
    except UnicodeDecodeError: # just in case. probably better to check that path is a python file with `inspect`
        return ''

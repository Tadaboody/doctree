from pathlib import Path
import os
from typing import Iterator


BACKSLASH = '\\'


def tree_dir(starting_dir: Path, max_depth: int=None, indent_char: str='|')-> str:

    def rec_tree_dir(current_dir: Path, depth) -> Iterator[str]:
        if max_depth and depth > max_depth:
            return
        for file in os.listdir(current_dir):
            full_path = os.path.join(current_dir,file)
            isdir = os.path.isdir(full_path)
            yield depth_seperator(indent_char, depth) + (BACKSLASH if isdir else '') + file
            if isdir:
                yield from rec_tree_dir(current_dir=os.path.join(current_dir, file), depth=depth+1)
                yield f"{depth_seperator(indent_char,depth)}/"
    return '\n'.join(rec_tree_dir(starting_dir, 0))

def depth_seperator(indent_char:str,depth:int)->str:
    return f"{indent_char}{f' {indent_char}'*depth}"


print(tree_dir('.',max_depth=3))

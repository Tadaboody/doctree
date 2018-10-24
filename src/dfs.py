"""Generic and pythonic implementation of the Depth First Search traversal algorithm"""
from typing import Callable, List, Iterable, TypeVar, Hashable, Tuple
from pathlib import Path
from collections import namedtuple

DfsVisit = namedtuple('DfsVisit', ['node', 'depth'])
NodeType = TypeVar('NodeType', bound=Hashable)
StackType = TypeVar('StackType')


def iter_top(stack: List[StackType])->Iterable[StackType]:
    """Iterate a stack as long as it is full, yielding the top every time"""
    while stack:
        yield stack.pop()


def dfs(root: NodeType, neighbors_func: Callable[[NodeType], Iterable[NodeType]],
        *,  # Every argument after this has to be a keyword argument
        predicate: Callable[[NodeType], bool]=lambda x: True,
        max_depth: int=None)->Iterable[DfsVisit]:
    """Iterate starting from root, going depth first
    `neighbors_func`: a function that returns an iterable of the nodes neighbors
    returns: A tuple of (item, depth), in order of dfs traversal
        """
    stack = [(root, 0)]
    visited_nodes = set()
    for item, depth in ((item, depth) for item, depth in iter_top(stack)
                        if item not in visited_nodes and not predicate(item)
                        and (max_depth is None or depth <= max_depth)):
        visited_nodes.add(item)
        stack.extend((item, depth+1) for item in neighbors_func(item))
        yield item, depth

# Example usage:


def safe_iterdir(path: Path):
    return path.iterdir() if path.is_dir() else tuple()

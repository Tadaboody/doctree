"""Generic and pythonic implementation of the Depth First Search traversal algorithm"""
from pathlib import Path
from typing import (Any, Callable, Generator,  Hashable, Iterable,
                    List, NamedTuple, Set, TypeVar, Generic, MutableSequence)

NodeType = Path
StackType = TypeVar('StackType', bound=Any)


class DfsVisit(NamedTuple):
    node: NodeType
    depth: int


def iter_top(stack: MutableSequence[StackType])->Iterable[StackType]:
    """Iterate a stack as long as it is full, yielding the top every time"""
    while stack:
        yield stack.pop()


def dfs(root: NodeType, neighbors_func: Callable[[NodeType], Iterable[NodeType]],
        *,  # Every argument after this has to be a keyword argument
        predicate: Callable[[NodeType], bool]=None,
        max_depth: int=None)->Generator[DfsVisit, None, None]:
    """Iterate starting from root, going depth first
    `neighbors_func`: a function that returns an iterable of the nodes neighbors
    returns: A tuple of (item, depth), in order of dfs traversal
        """
    stack: List[DfsVisit] = [DfsVisit(root, 0)]
    visited_nodes: Set[NodeType] = set()
    for item, depth in ((item, depth) for item, depth in iter_top(stack)
                        if item not in visited_nodes
                        and (predicate is None or not predicate(item))
                        and (max_depth is None or depth <= max_depth)):
        visited_nodes.add(item)
        stack.extend(DfsVisit(item, depth+1) for item in neighbors_func(item))
        yield DfsVisit(item, depth)


def safe_iterdir(path: Path):
    return path.iterdir() if path.is_dir() else tuple()


def main():
    root = Path(Path.home()/'Desktop')
    path: Path
    return ('\n'.join(str(path.resolve())
                      for path, depth in dfs(root, safe_iterdir) if path.is_dir()))


if __name__ == '__main__':
    print(main())

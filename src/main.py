"""Entry points for command scripts"""
import click
from src.doctree import doctree
from typing import Optional


@click.command()
@click.argument('starting_dir')
@click.option('--max_depth', default=None, help='Maximum depth of tree')
def cli(starting_dir: str, max_depth: Optional[int]):
    print('\n'.join(doctree(starting_dir, max_depth)))

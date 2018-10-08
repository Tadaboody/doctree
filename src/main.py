"""Entry points for command scripts"""
import click
from src.doctree import tree_dir

@click.command()
@click.argument('starting_dir')
@click.option('--max_depth',default=2,help='Maximum depth of tree (-1 for unlimited)')
def cli(starting_dir,max_depth):
    print(tree_dir(starting_dir=starting_dir, max_depth=max_depth))

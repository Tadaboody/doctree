"""Entry points for command scripts"""
import click
from src.doctree import doctree


@click.command()
@click.argument('starting_dir')
def cli(starting_dir: str='.'):
    print('\n'.join(doctree(starting_dir)))

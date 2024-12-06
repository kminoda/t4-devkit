import click
from .tier4 import Tier4

@click.group()
def cli():
    """T4 DevKit - Tools for working with T4 datasets"""
    pass

@cli.command()
@click.argument('dataset_path', type=click.Path(exists=True))
def visualize(dataset_path):
    """Visualize T4 dataset from the specified path."""
    t4 = Tier4("annotation", dataset_path, verbose=True)
    scene_token = t4.scene[0].token
    t4.render_scene(scene_token)

if __name__ == '__main__':
    cli()
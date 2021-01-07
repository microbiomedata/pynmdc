"""
CLI tools for NMDC
"""
import click
from nmdc import __version__
from nmdc.scripts.gff2json import NMDCGFFLoader


@click.group(help=f"""NMDC Tools v{__version__}.""")
def nmdccli():
    """
    NMDC command line tools.
    """
    pass


@nmdccli.command()
@click.argument('gff', type=click.File('r'))
def gff2json(gff):
    """
    Convert GFF3 to NMDC JSON format.
    """
    converter = NMDCGFFLoader(gff)
    print(converter.get_json())


if __name__ == '__main__':
    nmdccli()

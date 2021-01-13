"""
CLI tools for NMDC
"""
import click
import json
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
@click.option('-of',
              help='output file name for genome feature json',
              required=True,
              type=click.File(mode='w'))
@click.option('-oa',
              help='output file name for functioanl annotation json',
              required=True,
              type=click.File(mode='w'))
def gff2json(gff, of, oa):
    """
    Convert GFF3 to NMDC JSON format.
    """
    INDENT = 2
    converter = NMDCGFFLoader(gff)
    jobj = json.loads(converter.get_json())
    for record in jobj.keys():
        for feature in jobj[record].keys():
            entry = jobj[record][feature]
            gf = entry['genome_feature']
            fa = entry['functional_annotation']
            of.write(json.dumps(gf, indent=INDENT))
            oa.write(json.dumps(fa,  indent=INDENT))


if __name__ == '__main__':
    nmdccli()

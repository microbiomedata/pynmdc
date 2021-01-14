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
    jobj = converter.model
    features = []
    annotations = []
    for record in jobj.keys():
        for feature in jobj[record].keys():
            entry = jobj[record][feature]
            features.append(entry['feature_set'])
            annotations.extend(list(entry['functional_annotation_set'].values()))
            #of.write(json.dumps(gf, indent=INDENT))
            # num_annotations = len(fa)
            # oa.write('[\n')
            # for i, annotation in enumerate(fa.keys(), start=1):
            #     oa.write(json.dumps(fa[annotation], indent=INDENT))
            #     if i < num_annotations:
            #         oa.write(',')
            # oa.write(']\n')
        # for feature in jobj[record].keys():
            # entry = jobj[record][feature]
            # gf = entry['genome_feature']
            # fa = entry['functional_annotation']
            # of.write(json.dumps(gf, indent=INDENT))
            # oa.write(json.dumps(fa,  indent=INDENT))
    of.write(json.dumps({'feature_set': features}, indent=INDENT))
    oa.write(json.dumps({'functional_annotation_set': annotations}, indent=INDENT))


if __name__ == '__main__':
    nmdccli()

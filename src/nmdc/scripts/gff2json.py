"""
Methods to convert NMDC GFF3 to JSON
"""
import os
import json
import obonet
from BCBio import GFF
from nmdc.metadata import schema


class NMDCGenomeFeature(schema.GenomeFeature):
    """
    NMDC GenomeFeature with JSON export functionality
    """
    def __init__(self, seqid, start, end, **kargs):
        super().__init__(seqid, start, end, **kargs)
        assert(isinstance(kargs, dict))
        self.properties = {'seqid': seqid,
                           'start': start,
                           'end': end}
        for k in kargs:
            self.properties.update({k: kargs[k]})

        self.ACCEPTABLE_KEYS = ['id',
                                'cog',
                                'product',
                                'cath_funfam',
                                'ko',
                                'ec_number',
                                'pfam',
                                'superfamily',
                                'source'
                                'score',
                                'phase']

    def __repr__(self):
        repr = f'NMDCGenomeFeature seqid: {self.seqid}.'
        return repr

    def __dict__(self):
        return self.properties

    def get_json(self, indent=2):
        """
        Get JSON dump.
        """
        js = json.dump(self.__dict__(), indent=indent)
        return js

    # def add_product(self, prod):
    #     """
    #     Add annotation type "product"
    #     """
    #     anno_prod = {'product':
    #                  {'subject': 
    #     self.properties['annotations']
        

    def add_annotation(self, adict):
        """
        Add annotation dictionary to GenomeFeature
        """
        if 'annotations' in self.properties.keys():
            old = self.properties['annotations']
            for (k, v) in adict.items():
                if k.lower() in self.ACCEPTABLE_KEYS:
                    if k not in old.keys():
                        old.update({k.lower(): v})
                    else:
                        pass
            self.properties.update({'annotations': old})
        else:
            annotations = {}
            for (k, v) in adict.items():
                if k.lower() in self.ACCEPTABLE_KEYS:
                    annotations.update({k.lower(): v})
                else:
                    pass
            self.properties.update({'annotations': annotations})


class NMDCGFFLoader:
    """
    Load a GFF a file and map its contents to NMDC GenomeFeature
    """
    def __init__(self, gfffh):
        """
        Load a NMDC GFF3 file and convert it to JSON.

        gfffh: GFF file handler ready to read.
        """
        SOOBO = os.path.join(os.path.dirname(schema.__file__),
                             'so-simple.obo')
        sograph = obonet.read_obo(SOOBO)
        sddict = {data.get('name'): id_
                  for id_, data in sograph.nodes(data=True)}

        jd = {}

        for rec in GFF.parse(gfffh):
            rd = {}
            for feature in rec.features:
                feature_id = feature.id
                feature_type = feature.type
                if feature_type in sddict.keys():
                    feature_type_so = sddict[feature_type]
                else:
                    feature_type_so = None
                feature_start = int(feature.location.start)
                feature_end = int(feature.location.end)
                feature_strand = feature.location.strand
                if feature_strand == 1:  # 1 for '+' strand
                    feature_strand = '+'
                elif feature_strand == -1:  # -1 for '-' strand
                    feature_strand = '-'
                elif feature_strand is None:  # None for '' strand
                    feature_strand = ''
                seqid = f'NMDC:{rec.id}'
                nmdc_gf = NMDCGenomeFeature(
                    seqid=seqid,
                    start=feature_start,
                    end=feature_end,
                    strand=feature_strand,
                    type=feature_type_so,
                    encodes=f'NMDC:{feature_id}'
                )
                for (k, v) in feature.qualifiers.items():
                    nmdc_gf.add_annotation({k: v})
                rd.update({feature_id: nmdc_gf.__dict__()})
            jd.update({rec.id: rd})
        self.model = jd

    def get_json(self, indent=2):
        """
        Return data as JSON dump
        """
        return json.dumps(self.model, indent=indent)

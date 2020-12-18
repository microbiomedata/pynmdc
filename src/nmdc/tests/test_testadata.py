import io
import unittest
from BCBio import GFF
from nmdc.metadata.schema import GenomeFeature

class testMetadata(unittest.TestCase):
    def test_GenomeFeature(self):
        """
        Test import GenomeFeature from GFF3 file. The example gff line is from here:
        https://github.com/microbiomedata/nmdc-metadata/issues/184
        """
        gff_str = 'Ga0185794_41\tGeneMark.hmm-2 v1.05\tCDS\t48\t1037\t56.13\t+\t0\tID=Ga0185794_41_48_1037;translation_table=11;start_type=ATG;product=5-methylthioadenosine/S-adenosylhomocysteine deaminase;product_source=KO:K12960;cath_funfam=3.20.20.140;cog=COG0402;ko=KO:K12960;ec_number=EC:3.5.4.28,EC:3.5.4.31;pfam=PF01979;superfamily=51338,51556'
        print(f'Test GenomeFeature...\n\nInput:\n\t{gff_str}\n')

        with io.StringIO() as fh:
            fh.write(gff_str)
            fh.seek(0)
            for rec in GFF.parse(fh):
                for feature in rec.features:
                    feature_id = feature.id
                    feature_type = feature.type  # FIXME
                    feature_start = int(feature.location.start)
                    feature_end = int(feature.location.end)
                    feature_strand = feature.location.strand
                    if feature_strand == 1:
                        feature_strand = '+'
                    elif feature_strand == 0:
                        feature_strand = '-'
                    else:
                        feature_strand = ''
                    print(f'Features from GFF input for {feature.id}:')
                    for qual in feature.qualifiers:
                        print(f'\t{qual} => {feature.qualifiers[qual]}')
                    nmdc_gf = GenomeFeature(
                        seqid=f'NMDC:{rec.id}',  # record id
                        start=feature_start,
                        end=feature_end,
                        strand=feature_strand,
                        # type=feature_type, # FIXME
                        encodes=f'NMDC:{feature_id}'  # feature id # FIXME
                    )
                    self.assertEqual(nmdc_gf.seqid,
                                     'NMDC:Ga0185794_41')
                    self.assertEqual(nmdc_gf.start, 48-1)
                    self.assertEqual(nmdc_gf.end, 1037)
                    self.assertEqual(nmdc_gf.strand, '+')
                    # self.assertEqual(nmdc_gf.type, 'CDS')
                    # self.assertEqual(nmdc_gf.encodes,
                    #                  'NMDC:Ga0185794_41_48_1037')
                    print('\nFrom NMDC GenomeFeature\n')
                    print(f'\t{nmdc_gf}')


if __name__ == '__main__':
    unittest.main()

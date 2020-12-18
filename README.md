# About pynmdc

PyNMDC is a Python package to work with NMDC data.

More about NMDC: https://microbiomedata.org/

## Install (for developers only):
1 git clone git@github.com:microbiomedata/pynmdc.gitc.git

2 Go to the pynmdc package root dir

3 Run this command: `pip install -e .`

4 Run test code: `python src/nmdc/tests/test_testadata.py`


Example output from the test code

Test GenomeFeature...

Input:
	Ga0185794_41	GeneMark.hmm-2 v1.05	CDS	48	1037	56.13	+	0	ID=Ga0185794_41_48_1037;translation_table=11;start_type=ATG;product=5-methylthioadenosine/S-adenosylhomocysteine deaminase;product_source=KO:K12960;cath_funfam=3.20.20.140;cog=COG0402;ko=KO:K12960;ec_number=EC:3.5.4.28,EC:3.5.4.31;pfam=PF01979;superfamily=51338,51556

Features from GFF input for Ga0185794_41_48_1037:
	ID => ['Ga0185794_41_48_1037']
	translation_table => ['11']
	start_type => ['ATG']
	product => ['5-methylthioadenosine/S-adenosylhomocysteine deaminase']
	product_source => ['KO:K12960']
	cath_funfam => ['3.20.20.140']
	cog => ['COG0402']
	ko => ['KO:K12960']
	ec_number => ['EC:3.5.4.28', 'EC:3.5.4.31']
	pfam => ['PF01979']
	superfamily => ['51338', '51556']
	source => ['GeneMark.hmm-2 v1.05']
	score => ['56.13']
	phase => ['0']

From NMDC GenomeFeature

	GenomeFeature(seqid='NMDC:Ga0185794_41', start=47, end=1037, type=None, strand='+', phase=None, encodes=GeneProduct())
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

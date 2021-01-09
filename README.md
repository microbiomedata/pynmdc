# About pynmdc

PyNMDC is a Python package to work with NMDC data.

More about NMDC: https://microbiomedata.org/

## Install (for developers only):
1 `git clone git@github.com:microbiomedata/pynmdc.gitc.git`

2 Go to the pynmdc package root dir
  `cd pynmdc`

3 Run this command to install the package in developer mode
  `pynmdc$ pip install -e .`

4 Test Command line interface:
```
pynmdc$ nmdc --help
Usage: nmdc [OPTIONS] COMMAND [ARGS]...

  NMDC Tools v0.1.

Options:
  --help  Show this message and exit.

Commands:
  gff2json  Convert GFF3 to NMDC JSON format.
```

5. Test the package
   `pynmdc$ python src/nmdc/tests/test_gff2json.py `

   This will test the parsing of GenomeFeature in annotation to JSON.

   The input gff is:
   
```Ga0185794_41	GeneMark.hmm-2 v1.05	CDS	48	1037	56.13	+	0	ID=Ga0185794_41_48_1037;translation_table=11;start_type=ATG;product=5-methylthioadenosine/S-adenosylhomocysteine deaminase;product_source=KO:K12960;cath_funfam=3.20.20.140;cog=COG0402;ko=KO:K12960;ec_number=EC:3.5.4.28,EC:3.5.4.31;pfam=PF01979;superfamily=51338,51556```

   Output in JSON is
   
```javascript
{
  "Ga0185794_41": {
    "Ga0185794_41_48_1037": {
      "seqid": "NMDC:Ga0185794_41",
      "start": 47,
      "end": 1037,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:Ga0185794_41_48_1037",
      "annotations": {
        "product": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": ":['5-methylthioadenosine/S-adenosylhomocysteine deaminase']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "cath_funfam": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": "CATH:['3.20.20.140']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "cog": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": "EGGNOG:['COG0402']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "ko": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": "KEGG.ORTHOLOGY:['KO:K12960']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "ec_number": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": ":['EC:3.5.4.28', 'EC:3.5.4.31']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "pfam": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": "PFAM:['PF01979']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "superfamily": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": "SUPFAM:['51338', '51556']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "phase": {
          "subject": "NMDC:Ga0185794_41_48_1037",
          "has_function": ":['0']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        }
      }
    }
  }
}

```


6 Run gff2json using the MetaG annotation example gff file in test_data :

```
$nmdc gff2json src/nmdc/test_data/MetaG_annotation/1781_100325_functional_annotation_1000.gff 
```

First 100 lines from Output:

```javascript
{
  "1781_100325_scf_1000_c1": {
    "1781_100325_scf_1000_c1_3_1700": {
      "seqid": "NMDC:1781_100325_scf_1000_c1",
      "start": 2,
      "end": 1700,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1000_c1_3_1700",
      "annotations": {
        "product": {
          "subject": "NMDC:1781_100325_scf_1000_c1_3_1700",
          "has_function": ":['PAS domain S-box-containing protein']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "cath_funfam": {
          "subject": "NMDC:1781_100325_scf_1000_c1_3_1700",
          "has_function": "CATH:['3.30.450.20']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "cog": {
          "subject": "NMDC:1781_100325_scf_1000_c1_3_1700",
          "has_function": "EGGNOG:['COG2202']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "pfam": {
          "subject": "NMDC:1781_100325_scf_1000_c1_3_1700",
          "has_function": "PFAM:['GA', 'PA', 'PAS_']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "smart": {
          "subject": "NMDC:1781_100325_scf_1000_c1_3_1700",
          "has_function": "SMART:['55781', '55785']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "superfamily": {
          "subject": "NMDC:1781_100325_scf_1000_c1_3_1700",
          "has_function": "SUPFAM:['SM00086', 'SM00091']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "phase": {
          "subject": "NMDC:1781_100325_scf_1000_c1_3_1700",
          "has_function": ":['0']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        }
      }
    }
  },
  "1781_100325_scf_1001_c1": {
    "1781_100325_scf_1001_c1_82_573": {
      "seqid": "NMDC:1781_100325_scf_1001_c1",
      "start": 81,
      "end": 573,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1001_c1_82_573",
      "annotations": {
        "product": {
          "subject": "NMDC:1781_100325_scf_1001_c1_82_573",
          "has_function": ":['uncharacterized membrane protein']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "cog": {
          "subject": "NMDC:1781_100325_scf_1001_c1_82_573",
          "has_function": "EGGNOG:['COG2237']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "phase": {
          "subject": "NMDC:1781_100325_scf_1001_c1_82_573",
          "has_function": ":['0']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        }
      }
    },
    "1781_100325_scf_1001_c1_859_1671": {
      "seqid": "NMDC:1781_100325_scf_1001_c1",
      "start": 858,
      "end": 1671,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1001_c1_859_1671",
      "annotations": {
        "product": {
          "subject": "NMDC:1781_100325_scf_1001_c1_859_1671",
          "has_function": ":['hypothetical protein']",
          "was_generated_by": "N/A",
          "type": "NMDC:FunctionalAnnotation"
        },
        "phase": {
          "subject": "NMDC:1781_100325_scf_1001_c1_859_1671",
          ....

```
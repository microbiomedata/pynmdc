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
        "id": [
          "Ga0185794_41_48_1037"
        ],
        "product": [
          "5-methylthioadenosine/S-adenosylhomocysteine deaminase"
        ],
        "cath_funfam": [
          "3.20.20.140"
        ],
        "cog": [
          "COG0402"
        ],
        "ko": [
          "KO:K12960"
        ],
        "ec_number": [
          "EC:3.5.4.28",
          "EC:3.5.4.31"
        ],
        "pfam": [
          "PF01979"
        ],
        "superfamily": [
          "51338",
          "51556"
        ],
        "phase": [
          "0"
        ]
      }
    }
  }
}

```


6 Run gff2json using the MetaG annotation example gff file in test_data :

```
$nmdc gff2json src/nmdc/test_data/MetaG_annotation/1781_100325_functional_annotation_1000.gff 
```

Output:

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
        "id": [
          "1781_100325_scf_1000_c1_3_1700"
        ],
        "product": [
          "PAS domain S-box-containing protein"
        ],
        "cath_funfam": [
          "3.30.450.20"
        ],
        "cog": [
          "COG2202"
        ],
        "pfam": [
          "GA",
          "PA",
          "PAS_"
        ],
        "superfamily": [
          "SM00086",
          "SM00091"
        ],
        "phase": [
          "0"
        ]
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
        "id": [
          "1781_100325_scf_1001_c1_82_573"
        ],
        "product": [
          "uncharacterized membrane protein"
        ],
        "cog": [
          "COG2237"
        ],
        "phase": [
          "0"
        ]
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
        "id": [
          "1781_100325_scf_1001_c1_859_1671"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1002_c1": {
    "1781_100325_scf_1002_c1_1_99": {
      "seqid": "NMDC:1781_100325_scf_1002_c1",
      "start": 0,
      "end": 99,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1002_c1_1_99",
      "annotations": {
        "id": [
          "1781_100325_scf_1002_c1_1_99"
        ],
        "product": [
          "large subunit ribosomal protein L18"
        ],
        "ko": [
          "KO:K02881"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1002_c1_96_731": {
      "seqid": "NMDC:1781_100325_scf_1002_c1",
      "start": 95,
      "end": 731,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1002_c1_96_731",
      "annotations": {
        "id": [
          "1781_100325_scf_1002_c1_96_731"
        ],
        "product": [
          "small subunit ribosomal protein S5"
        ],
        "cath_funfam": [
          "3.30.160.20",
          "3.30.230.10"
        ],
        "cog": [
          "COG0098"
        ],
        "ko": [
          "KO:K02988"
        ],
        "pfam": [
          "Ribosomal_S",
          "Ribosomal_S5_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1002_c1_765_1205": {
      "seqid": "NMDC:1781_100325_scf_1002_c1",
      "start": 764,
      "end": 1205,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1002_c1_765_1205",
      "annotations": {
        "id": [
          "1781_100325_scf_1002_c1_765_1205"
        ],
        "product": [
          "large subunit ribosomal protein L30"
        ],
        "cath_funfam": [
          "3.30.1390.20"
        ],
        "cog": [
          "COG1841"
        ],
        "ko": [
          "KO:K02907"
        ],
        "pfam": [
          "Ribosomal_L3"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1002_c1_1207_1629": {
      "seqid": "NMDC:1781_100325_scf_1002_c1",
      "start": 1206,
      "end": 1629,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1002_c1_1207_1629",
      "annotations": {
        "id": [
          "1781_100325_scf_1002_c1_1207_1629"
        ],
        "product": [
          "large subunit ribosomal protein L15"
        ],
        "cath_funfam": [
          "3.100.10.10",
          "4.10.990.10"
        ],
        "cog": [
          "COG0200"
        ],
        "ko": [
          "KO:K02876"
        ],
        "pfam": [
          "Ribosomal_L27"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1002_c1_1626_1700": {
      "seqid": "NMDC:1781_100325_scf_1002_c1",
      "start": 1625,
      "end": 1700,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1002_c1_1626_1700",
      "annotations": {
        "id": [
          "1781_100325_scf_1002_c1_1626_1700"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1003_c1": {
    "1781_100325_scf_1003_c1_1_543": {
      "seqid": "NMDC:1781_100325_scf_1003_c1",
      "start": 0,
      "end": 543,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1003_c1_1_543",
      "annotations": {
        "id": [
          "1781_100325_scf_1003_c1_1_543"
        ],
        "product": [
          "drug/metabolite transporter (DMT)-like permease"
        ],
        "cog": [
          "COG0697"
        ],
        "pfam": [
          "Eam"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1003_c1_597_1697": {
      "seqid": "NMDC:1781_100325_scf_1003_c1",
      "start": 596,
      "end": 1697,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1003_c1_597_1697",
      "annotations": {
        "id": [
          "1781_100325_scf_1003_c1_597_1697"
        ],
        "product": [
          "phosphoribosylformylglycinamidine synthase"
        ],
        "cath_funfam": [
          "3.30.1330.10",
          "3.90.650.10"
        ],
        "cog": [
          "COG0046"
        ],
        "ko": [
          "KO:K01952"
        ],
        "ec_number": [
          "EC:6.3.5.3"
        ],
        "pfam": [
          "AIR",
          "AIRS_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1004_c1": {
    "1781_100325_scf_1004_c1_1_255": {
      "seqid": "NMDC:1781_100325_scf_1004_c1",
      "start": 0,
      "end": 255,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1004_c1_1_255",
      "annotations": {
        "id": [
          "1781_100325_scf_1004_c1_1_255"
        ],
        "product": [
          "predicted RNA-binding protein with TRAM domain"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG3269"
        ],
        "pfam": [
          "TRA"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1004_c1_313_1146": {
      "seqid": "NMDC:1781_100325_scf_1004_c1",
      "start": 312,
      "end": 1146,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1004_c1_313_1146",
      "annotations": {
        "id": [
          "1781_100325_scf_1004_c1_313_1146"
        ],
        "product": [
          "aspartate dehydrogenase"
        ],
        "cath_funfam": [
          "3.30.360.10",
          "3.40.50.720"
        ],
        "cog": [
          "COG1712"
        ],
        "ko": [
          "KO:K06989"
        ],
        "ec_number": [
          "EC:1.4.1.21"
        ],
        "pfam": [
          "DUF10",
          "DapB_",
          "NAD_binding_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1004_c1_1251_1433": {
      "seqid": "NMDC:1781_100325_scf_1004_c1",
      "start": 1250,
      "end": 1433,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1004_c1_1251_1433",
      "annotations": {
        "id": [
          "1781_100325_scf_1004_c1_1251_1433"
        ],
        "product": [
          "small subunit ribosomal protein S30e"
        ],
        "cog": [
          "COG4919"
        ],
        "ko": [
          "KO:K02983"
        ],
        "pfam": [
          "Ribosomal_S3"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1005_c1": {
    "1781_100325_scf_1005_c1_2_829": {
      "seqid": "NMDC:1781_100325_scf_1005_c1",
      "start": 1,
      "end": 829,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1005_c1_2_829",
      "annotations": {
        "id": [
          "1781_100325_scf_1005_c1_2_829"
        ],
        "product": [
          "DNA polymerase-4"
        ],
        "cath_funfam": [
          "1.10.150.20",
          "3.30.70.270"
        ],
        "cog": [
          "COG0389"
        ],
        "ko": [
          "KO:K02346"
        ],
        "ec_number": [
          "EC:2.7.7.7"
        ],
        "pfam": [
          "IM"
        ],
        "superfamily": [
          "SM00278"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1005_c1_877_1473": {
      "seqid": "NMDC:1781_100325_scf_1005_c1",
      "start": 876,
      "end": 1473,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1005_c1_877_1473",
      "annotations": {
        "id": [
          "1781_100325_scf_1005_c1_877_1473"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.20.5.100"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1006_c1": {
    "1781_100325_scf_1006_c1_2_730": {
      "seqid": "NMDC:1781_100325_scf_1006_c1",
      "start": 1,
      "end": 730,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1006_c1_2_730",
      "annotations": {
        "id": [
          "1781_100325_scf_1006_c1_2_730"
        ],
        "product": [
          "cysteinyl-tRNA synthetase"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "cog": [
          "COG0215"
        ],
        "ko": [
          "KO:K01883"
        ],
        "ec_number": [
          "EC:6.1.1.16"
        ],
        "pfam": [
          "tRNA-synt_1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1006_c1_761_1696": {
      "seqid": "NMDC:1781_100325_scf_1006_c1",
      "start": 760,
      "end": 1696,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1006_c1_761_1696",
      "annotations": {
        "id": [
          "1781_100325_scf_1006_c1_761_1696"
        ],
        "product": [
          "ATP-dependent Zn protease"
        ],
        "cath_funfam": [
          "1.10.8.60"
        ],
        "cog": [
          "COG0465"
        ],
        "pfam": [
          "Peptidase_M4"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1007_c1": {
    "1781_100325_scf_1007_c1_264_1550": {
      "seqid": "NMDC:1781_100325_scf_1007_c1",
      "start": 263,
      "end": 1550,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1007_c1_264_1550",
      "annotations": {
        "id": [
          "1781_100325_scf_1007_c1_264_1550"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DDE_Tnp_1_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1008_c1": {
    "1781_100325_scf_1008_c1_9_113": {
      "seqid": "NMDC:1781_100325_scf_1008_c1",
      "start": 8,
      "end": 113,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1008_c1_9_113",
      "annotations": {
        "id": [
          "1781_100325_scf_1008_c1_9_113"
        ],
        "product": [
          "elongation factor P"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "ko": [
          "KO:K02356"
        ],
        "pfam": [
          "Elong-fact-P_"
        ],
        "superfamily": [
          "SM00841"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1008_c1_118_546": {
      "seqid": "NMDC:1781_100325_scf_1008_c1",
      "start": 117,
      "end": 546,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1008_c1_118_546",
      "annotations": {
        "id": [
          "1781_100325_scf_1008_c1_118_546"
        ],
        "product": [
          "N utilization substance protein B"
        ],
        "cath_funfam": [
          "1.10.940.10"
        ],
        "cog": [
          "COG0781"
        ],
        "ko": [
          "KO:K03625"
        ],
        "pfam": [
          "Nus"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1008_c1_554_760": {
      "seqid": "NMDC:1781_100325_scf_1008_c1",
      "start": 553,
      "end": 760,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1008_c1_554_760",
      "annotations": {
        "id": [
          "1781_100325_scf_1008_c1_554_760"
        ],
        "product": [
          "sec-independent protein translocase protein TatA"
        ],
        "cog": [
          "COG1826"
        ],
        "ko": [
          "KO:K03116"
        ],
        "pfam": [
          "MttA_Hcf10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1008_c1_996_1562": {
      "seqid": "NMDC:1781_100325_scf_1008_c1",
      "start": 995,
      "end": 1562,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1008_c1_996_1562",
      "annotations": {
        "id": [
          "1781_100325_scf_1008_c1_996_1562"
        ],
        "product": [
          "pyrimidine operon attenuation protein/uracil phosphoribosyltransferase"
        ],
        "cath_funfam": [
          "3.40.50.2020"
        ],
        "cog": [
          "COG2065"
        ],
        "ko": [
          "KO:K02825"
        ],
        "ec_number": [
          "EC:2.4.2.9"
        ],
        "pfam": [
          "Pribosyltra"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1008_c1_1559_1696": {
      "seqid": "NMDC:1781_100325_scf_1008_c1",
      "start": 1558,
      "end": 1696,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1008_c1_1559_1696",
      "annotations": {
        "id": [
          "1781_100325_scf_1008_c1_1559_1696"
        ],
        "product": [
          "aspartate carbamoyltransferase catalytic subunit"
        ],
        "cath_funfam": [
          "3.40.50.1370"
        ],
        "cog": [
          "COG0540"
        ],
        "ko": [
          "KO:K00609"
        ],
        "ec_number": [
          "EC:2.1.3.2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1009_c1": {
    "1781_100325_scf_1009_c1_97_582": {
      "seqid": "NMDC:1781_100325_scf_1009_c1",
      "start": 96,
      "end": 582,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1009_c1_97_582",
      "annotations": {
        "id": [
          "1781_100325_scf_1009_c1_97_582"
        ],
        "product": [
          "HEAT repeat protein"
        ],
        "cath_funfam": [
          "1.25.10.20"
        ],
        "cog": [
          "COG1413"
        ],
        "pfam": [
          "HEAT_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1009_c1_579_749": {
      "seqid": "NMDC:1781_100325_scf_1009_c1",
      "start": 578,
      "end": 749,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1009_c1_579_749",
      "annotations": {
        "id": [
          "1781_100325_scf_1009_c1_579_749"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1009_c1_746_1693": {
      "seqid": "NMDC:1781_100325_scf_1009_c1",
      "start": 745,
      "end": 1693,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1009_c1_746_1693",
      "annotations": {
        "id": [
          "1781_100325_scf_1009_c1_746_1693"
        ],
        "product": [
          "integrase/recombinase XerD"
        ],
        "cath_funfam": [
          "1.10.150.130",
          "1.10.443.10"
        ],
        "cog": [
          "COG4974"
        ],
        "ko": [
          "KO:K04763"
        ],
        "pfam": [
          "Phage_int_SAM_",
          "Phage_integras"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_100_c1": {
    "1781_100325_scf_100_c1_2_397": {
      "seqid": "NMDC:1781_100325_scf_100_c1",
      "start": 1,
      "end": 397,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_100_c1_2_397",
      "annotations": {
        "id": [
          "1781_100325_scf_100_c1_2_397"
        ],
        "product": [
          "two-component system nitrogen regulation response regulator GlnG"
        ],
        "cath_funfam": [
          "3.40.50.2300"
        ],
        "cog": [
          "COG3437"
        ],
        "ko": [
          "KO:K07712"
        ],
        "pfam": [
          "Response_re"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_100_c1_670_2514": {
      "seqid": "NMDC:1781_100325_scf_100_c1",
      "start": 669,
      "end": 2514,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_100_c1_670_2514",
      "annotations": {
        "id": [
          "1781_100325_scf_100_c1_670_2514"
        ],
        "product": [
          "signal transduction histidine kinase"
        ],
        "cath_funfam": [
          "1.10.287.130",
          "2.60.15.10",
          "3.30.565.10"
        ],
        "cog": [
          "COG0642"
        ],
        "pfam": [
          "HATPase_",
          "HisK",
          "dCache_"
        ],
        "superfamily": [
          "SM00387",
          "SM00388"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_100_c1_2522_3418": {
      "seqid": "NMDC:1781_100325_scf_100_c1",
      "start": 2521,
      "end": 3418,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_100_c1_2522_3418",
      "annotations": {
        "id": [
          "1781_100325_scf_100_c1_2522_3418"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_100_c1_3598_3972": {
      "seqid": "NMDC:1781_100325_scf_100_c1",
      "start": 3597,
      "end": 3972,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_100_c1_3598_3972",
      "annotations": {
        "id": [
          "1781_100325_scf_100_c1_3598_3972"
        ],
        "product": [
          "DNA-binding beta-propeller fold protein YncE"
        ],
        "cath_funfam": [
          "2.120.10.30"
        ],
        "cog": [
          "COG3391"
        ],
        "pfam": [
          "DUF512",
          "NH"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1010_c1": {
    "1781_100325_scf_1010_c1_3_815": {
      "seqid": "NMDC:1781_100325_scf_1010_c1",
      "start": 2,
      "end": 815,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1010_c1_3_815",
      "annotations": {
        "id": [
          "1781_100325_scf_1010_c1_3_815"
        ],
        "product": [
          "spermidine/putrescine transport system permease protein"
        ],
        "cath_funfam": [
          "1.10.3720.10"
        ],
        "cog": [
          "COG1177"
        ],
        "ko": [
          "KO:K11070"
        ],
        "pfam": [
          "BPD_transp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1010_c1_812_1696": {
      "seqid": "NMDC:1781_100325_scf_1010_c1",
      "start": 811,
      "end": 1696,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1010_c1_812_1696",
      "annotations": {
        "id": [
          "1781_100325_scf_1010_c1_812_1696"
        ],
        "product": [
          "spermidine/putrescine transport system permease protein"
        ],
        "cath_funfam": [
          "1.10.3720.10"
        ],
        "cog": [
          "COG1176"
        ],
        "ko": [
          "KO:K11071"
        ],
        "pfam": [
          "BPD_transp_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1011_c1": {
    "1781_100325_scf_1011_c1_102_395": {
      "seqid": "NMDC:1781_100325_scf_1011_c1",
      "start": 101,
      "end": 395,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1011_c1_102_395",
      "annotations": {
        "id": [
          "1781_100325_scf_1011_c1_102_395"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1011_c1_716_985": {
      "seqid": "NMDC:1781_100325_scf_1011_c1",
      "start": 715,
      "end": 985,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1011_c1_716_985",
      "annotations": {
        "id": [
          "1781_100325_scf_1011_c1_716_985"
        ],
        "product": [
          "phage tail tube protein FII"
        ],
        "cath_funfam": [
          "1.20.120.490"
        ],
        "cog": [
          "COG3498"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1011_c1_1475_1663": {
      "seqid": "NMDC:1781_100325_scf_1011_c1",
      "start": 1474,
      "end": 1663,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1011_c1_1475_1663",
      "annotations": {
        "id": [
          "1781_100325_scf_1011_c1_1475_1663"
        ],
        "product": [
          "hypothetical protein"
        ],
        "superfamily": [
          "SM01019"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1012_c1": {
    "1781_100325_scf_1012_c1_6_116": {
      "seqid": "NMDC:1781_100325_scf_1012_c1",
      "start": 5,
      "end": 116,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1012_c1_6_116",
      "annotations": {
        "id": [
          "1781_100325_scf_1012_c1_6_116"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.720"
        ],
        "superfamily": [
          "SM00729"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1012_c1_129_311": {
      "seqid": "NMDC:1781_100325_scf_1012_c1",
      "start": 128,
      "end": 311,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1012_c1_129_311",
      "annotations": {
        "id": [
          "1781_100325_scf_1012_c1_129_311"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1012_c1_351_764": {
      "seqid": "NMDC:1781_100325_scf_1012_c1",
      "start": 350,
      "end": 764,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1012_c1_351_764",
      "annotations": {
        "id": [
          "1781_100325_scf_1012_c1_351_764"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DUF305"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1012_c1_716_1174": {
      "seqid": "NMDC:1781_100325_scf_1012_c1",
      "start": 715,
      "end": 1174,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1012_c1_716_1174",
      "annotations": {
        "id": [
          "1781_100325_scf_1012_c1_716_1174"
        ],
        "product": [
          "uncharacterized protein YecE (DUF72 family)"
        ],
        "cath_funfam": [
          "3.20.20.410"
        ],
        "cog": [
          "COG1801"
        ],
        "pfam": [
          "DUF7"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1012_c1_1390_1641": {
      "seqid": "NMDC:1781_100325_scf_1012_c1",
      "start": 1389,
      "end": 1641,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1012_c1_1390_1641",
      "annotations": {
        "id": [
          "1781_100325_scf_1012_c1_1390_1641"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.25.10.10"
        ],
        "pfam": [
          "DUF424"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1013_c1": {
    "1781_100325_scf_1013_c1_52_1173": {
      "seqid": "NMDC:1781_100325_scf_1013_c1",
      "start": 51,
      "end": 1173,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1013_c1_52_1173",
      "annotations": {
        "id": [
          "1781_100325_scf_1013_c1_52_1173"
        ],
        "product": [
          "glucose/arabinose dehydrogenase"
        ],
        "cath_funfam": [
          "2.120.10.30"
        ],
        "cog": [
          "COG2133"
        ],
        "pfam": [
          "GSD"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1013_c1_1555_1692": {
      "seqid": "NMDC:1781_100325_scf_1013_c1",
      "start": 1554,
      "end": 1692,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1013_c1_1555_1692",
      "annotations": {
        "id": [
          "1781_100325_scf_1013_c1_1555_1692"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1014_c1": {
    "1781_100325_scf_1014_c1_12_1004": {
      "seqid": "NMDC:1781_100325_scf_1014_c1",
      "start": 11,
      "end": 1004,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1014_c1_12_1004",
      "annotations": {
        "id": [
          "1781_100325_scf_1014_c1_12_1004"
        ],
        "product": [
          "UbiD family decarboxylase"
        ],
        "cath_funfam": [
          "3.40.1670.10"
        ],
        "cog": [
          "COG0043"
        ],
        "pfam": [
          "Ubi"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1014_c1_1126_1446": {
      "seqid": "NMDC:1781_100325_scf_1014_c1",
      "start": 1125,
      "end": 1446,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1014_c1_1126_1446",
      "annotations": {
        "id": [
          "1781_100325_scf_1014_c1_1126_1446"
        ],
        "product": [
          "murein L",
          "D-transpeptidase YcbB/YkuD"
        ],
        "cath_funfam": [
          "1.10.1140.10"
        ],
        "cog": [
          "COG2989"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1014_c1_1484_1693": {
      "seqid": "NMDC:1781_100325_scf_1014_c1",
      "start": 1483,
      "end": 1693,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1014_c1_1484_1693",
      "annotations": {
        "id": [
          "1781_100325_scf_1014_c1_1484_1693"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1015_c1": {
    "1781_100325_scf_1015_c1_310_1434": {
      "seqid": "NMDC:1781_100325_scf_1015_c1",
      "start": 309,
      "end": 1434,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1015_c1_310_1434",
      "annotations": {
        "id": [
          "1781_100325_scf_1015_c1_310_1434"
        ],
        "product": [
          "DNA ligase-1"
        ],
        "cath_funfam": [
          "2.40.50.140",
          "3.30.470.30"
        ],
        "cog": [
          "COG1793"
        ],
        "ko": [
          "KO:K10747"
        ],
        "ec_number": [
          "EC:6.5.1.1",
          "EC:6.5.1.6",
          "EC:6.5.1.7"
        ],
        "pfam": [
          "DNA_ligase_A_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1016_c1": {
    "1781_100325_scf_1016_c1_3_401": {
      "seqid": "NMDC:1781_100325_scf_1016_c1",
      "start": 2,
      "end": 401,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1016_c1_3_401",
      "annotations": {
        "id": [
          "1781_100325_scf_1016_c1_3_401"
        ],
        "product": [
          "predicted Zn-dependent protease"
        ],
        "cath_funfam": [
          "3.30.2290.10"
        ],
        "cog": [
          "COG0312"
        ],
        "pfam": [
          "PmbA_Tld"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1016_c1_401_1684": {
      "seqid": "NMDC:1781_100325_scf_1016_c1",
      "start": 400,
      "end": 1684,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1016_c1_401_1684",
      "annotations": {
        "id": [
          "1781_100325_scf_1016_c1_401_1684"
        ],
        "product": [
          "TldD protein"
        ],
        "cog": [
          "COG0312"
        ],
        "ko": [
          "KO:K03568"
        ],
        "pfam": [
          "PmbA_Tld"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1017_c1": {
    "1781_100325_scf_1017_c1_57_404": {
      "seqid": "NMDC:1781_100325_scf_1017_c1",
      "start": 56,
      "end": 404,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1017_c1_57_404",
      "annotations": {
        "id": [
          "1781_100325_scf_1017_c1_57_404"
        ],
        "product": [
          "pyruvate dehydrogenase (quinone)/pyruvate oxidase"
        ],
        "cath_funfam": [
          "3.40.50.970"
        ],
        "ko": [
          "KO:K00156",
          "KO:K00158"
        ],
        "ec_number": [
          "EC:1.2.3.3",
          "EC:1.2.5.1"
        ],
        "pfam": [
          "TPP_enzyme_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1017_c1_618_1682": {
      "seqid": "NMDC:1781_100325_scf_1017_c1",
      "start": 617,
      "end": 1682,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1017_c1_618_1682",
      "annotations": {
        "id": [
          "1781_100325_scf_1017_c1_618_1682"
        ],
        "product": [
          "succinate dehydrogenase/fumarate reductase flavoprotein subunit"
        ],
        "cath_funfam": [
          "1.20.58.100",
          "3.90.700.10"
        ],
        "cog": [
          "COG1053"
        ],
        "pfam": [
          "FAD_binding_",
          "Succ_DH_flav_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1018_c1": {
    "1781_100325_scf_1018_c1_2_838": {
      "seqid": "NMDC:1781_100325_scf_1018_c1",
      "start": 1,
      "end": 838,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1018_c1_2_838",
      "annotations": {
        "id": [
          "1781_100325_scf_1018_c1_2_838"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1018_c1_913_1509": {
      "seqid": "NMDC:1781_100325_scf_1018_c1",
      "start": 912,
      "end": 1509,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1018_c1_913_1509",
      "annotations": {
        "id": [
          "1781_100325_scf_1018_c1_913_1509"
        ],
        "product": [
          "proteasome beta subunit"
        ],
        "cath_funfam": [
          "3.60.20.10"
        ],
        "cog": [
          "COG0638"
        ],
        "ko": [
          "KO:K03433"
        ],
        "ec_number": [
          "EC:3.4.25.1"
        ],
        "pfam": [
          "Proteasom"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1018_c1_1557_1691": {
      "seqid": "NMDC:1781_100325_scf_1018_c1",
      "start": 1556,
      "end": 1691,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1018_c1_1557_1691",
      "annotations": {
        "id": [
          "1781_100325_scf_1018_c1_1557_1691"
        ],
        "product": [
          "predicted ribosome-associated RNA-binding protein Tma20"
        ],
        "cog": [
          "COG2016"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1019_c1": {
    "1781_100325_scf_1019_c1_787_1245": {
      "seqid": "NMDC:1781_100325_scf_1019_c1",
      "start": 786,
      "end": 1245,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1019_c1_787_1245",
      "annotations": {
        "id": [
          "1781_100325_scf_1019_c1_787_1245"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1019_c1_1380_1655": {
      "seqid": "NMDC:1781_100325_scf_1019_c1",
      "start": 1379,
      "end": 1655,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1019_c1_1380_1655",
      "annotations": {
        "id": [
          "1781_100325_scf_1019_c1_1380_1655"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.300.30"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_101_c1": {
    "1781_100325_scf_101_c1_41_778": {
      "seqid": "NMDC:1781_100325_scf_101_c1",
      "start": 40,
      "end": 778,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_101_c1_41_778",
      "annotations": {
        "id": [
          "1781_100325_scf_101_c1_41_778"
        ],
        "product": [
          "polyhydroxyalkanoate synthase"
        ],
        "cath_funfam": [
          "3.40.50.1820"
        ],
        "cog": [
          "COG3243"
        ],
        "ko": [
          "KO:K03821"
        ],
        "ec_number": [
          "EC:2.3.1.-"
        ],
        "pfam": [
          "Abhydrolase_",
          "Hydrolase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_101_c1_839_1147": {
      "seqid": "NMDC:1781_100325_scf_101_c1",
      "start": 838,
      "end": 1147,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_101_c1_839_1147",
      "annotations": {
        "id": [
          "1781_100325_scf_101_c1_839_1147"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.10.260.10"
        ],
        "superfamily": [
          "SM00441",
          "SM00966"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_101_c1_1169_1894": {
      "seqid": "NMDC:1781_100325_scf_101_c1",
      "start": 1168,
      "end": 1894,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_101_c1_1169_1894",
      "annotations": {
        "id": [
          "1781_100325_scf_101_c1_1169_1894"
        ],
        "product": [
          "pimeloyl-ACP methyl ester carboxylesterase"
        ],
        "cath_funfam": [
          "3.40.50.1820"
        ],
        "cog": [
          "COG0596"
        ],
        "pfam": [
          "Abhydrolase_",
          "Hydrolase_",
          "Nd"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_101_c1_2162_2731": {
      "seqid": "NMDC:1781_100325_scf_101_c1",
      "start": 2161,
      "end": 2731,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_101_c1_2162_2731",
      "annotations": {
        "id": [
          "1781_100325_scf_101_c1_2162_2731"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG0730"
        ],
        "ko": [
          "KO:K07090"
        ],
        "pfam": [
          "Tau"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_101_c1_2742_2966": {
      "seqid": "NMDC:1781_100325_scf_101_c1",
      "start": 2741,
      "end": 2966,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_101_c1_2742_2966",
      "annotations": {
        "id": [
          "1781_100325_scf_101_c1_2742_2966"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_101_c1_3090_3266": {
      "seqid": "NMDC:1781_100325_scf_101_c1",
      "start": 3089,
      "end": 3266,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_101_c1_3090_3266",
      "annotations": {
        "id": [
          "1781_100325_scf_101_c1_3090_3266"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.40.10"
        ],
        "superfamily": [
          "SM00355"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_101_c1_3533_3937": {
      "seqid": "NMDC:1781_100325_scf_101_c1",
      "start": 3532,
      "end": 3937,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_101_c1_3533_3937",
      "annotations": {
        "id": [
          "1781_100325_scf_101_c1_3533_3937"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "Peptidase_M5"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1020_c1": {
    "1781_100325_scf_1020_c1_3_278": {
      "seqid": "NMDC:1781_100325_scf_1020_c1",
      "start": 2,
      "end": 278,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1020_c1_3_278",
      "annotations": {
        "id": [
          "1781_100325_scf_1020_c1_3_278"
        ],
        "product": [
          "UDP-N-acetylmuramate--alanine ligase"
        ],
        "cath_funfam": [
          "3.90.190.20"
        ],
        "cog": [
          "COG0773"
        ],
        "ko": [
          "KO:K01924"
        ],
        "ec_number": [
          "EC:6.3.2.8"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1020_c1_293_1216": {
      "seqid": "NMDC:1781_100325_scf_1020_c1",
      "start": 292,
      "end": 1216,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1020_c1_293_1216",
      "annotations": {
        "id": [
          "1781_100325_scf_1020_c1_293_1216"
        ],
        "product": [
          "UDP-N-acetylmuramate dehydrogenase"
        ],
        "cath_funfam": [
          "3.30.43.10",
          "3.30.465.10",
          "3.90.78.10"
        ],
        "cog": [
          "COG0812"
        ],
        "ko": [
          "KO:K00075"
        ],
        "ec_number": [
          "EC:1.3.1.98"
        ],
        "pfam": [
          "FAD_binding_",
          "MurB_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1020_c1_1263_1688": {
      "seqid": "NMDC:1781_100325_scf_1020_c1",
      "start": 1262,
      "end": 1688,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1020_c1_1263_1688",
      "annotations": {
        "id": [
          "1781_100325_scf_1020_c1_1263_1688"
        ],
        "product": [
          "cell division protein FtsQ"
        ],
        "cog": [
          "COG1589"
        ],
        "ko": [
          "KO:K03589"
        ],
        "pfam": [
          "POTRA_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1021_c1": {
    "1781_100325_scf_1021_c1_1_339": {
      "seqid": "NMDC:1781_100325_scf_1021_c1",
      "start": 0,
      "end": 339,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1021_c1_1_339",
      "annotations": {
        "id": [
          "1781_100325_scf_1021_c1_1_339"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1021_c1_440_1690": {
      "seqid": "NMDC:1781_100325_scf_1021_c1",
      "start": 439,
      "end": 1690,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1021_c1_440_1690",
      "annotations": {
        "id": [
          "1781_100325_scf_1021_c1_440_1690"
        ],
        "product": [
          "xylulose-5-phosphate/fructose-6-phosphate phosphoketolase"
        ],
        "cath_funfam": [
          "3.40.50.970"
        ],
        "cog": [
          "COG3957"
        ],
        "ko": [
          "KO:K01621"
        ],
        "ec_number": [
          "EC:4.1.2.22",
          "EC:4.1.2.9"
        ],
        "pfam": [
          "XFP_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1022_c1": {
    "1781_100325_scf_1022_c1_130_1557": {
      "seqid": "NMDC:1781_100325_scf_1022_c1",
      "start": 129,
      "end": 1557,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1022_c1_130_1557",
      "annotations": {
        "id": [
          "1781_100325_scf_1022_c1_130_1557"
        ],
        "product": [
          "dihydropyrimidinase"
        ],
        "cath_funfam": [
          "2.30.40.10",
          "3.20.20.140"
        ],
        "cog": [
          "COG0044"
        ],
        "ko": [
          "KO:K01464"
        ],
        "ec_number": [
          "EC:3.5.2.2"
        ],
        "pfam": [
          "Amidohydro_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1022_c1_1565_1687": {
      "seqid": "NMDC:1781_100325_scf_1022_c1",
      "start": 1564,
      "end": 1687,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1022_c1_1565_1687",
      "annotations": {
        "id": [
          "1781_100325_scf_1022_c1_1565_1687"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1023_c1": {
    "1781_100325_scf_1023_c1_1206_1688": {
      "seqid": "NMDC:1781_100325_scf_1023_c1",
      "start": 1205,
      "end": 1688,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1023_c1_1206_1688",
      "annotations": {
        "id": [
          "1781_100325_scf_1023_c1_1206_1688"
        ],
        "product": [
          "NADH-ubiquinone oxidoreductase chain 4"
        ],
        "cog": [
          "COG1008"
        ],
        "ko": [
          "KO:K03881"
        ],
        "ec_number": [
          "EC:1.6.5.3"
        ],
        "pfam": [
          "Proton_antipo_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1024_c1": {
    "1781_100325_scf_1024_c1_22_810": {
      "seqid": "NMDC:1781_100325_scf_1024_c1",
      "start": 21,
      "end": 810,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1024_c1_22_810",
      "annotations": {
        "id": [
          "1781_100325_scf_1024_c1_22_810"
        ],
        "product": [
          "GTP cyclohydrolase IIa"
        ],
        "cath_funfam": [
          "3.30.70.270"
        ],
        "cog": [
          "COG2429"
        ],
        "ko": [
          "KO:K08096"
        ],
        "ec_number": [
          "EC:3.5.4.29"
        ],
        "pfam": [
          "GCH_II"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1024_c1_827_1198": {
      "seqid": "NMDC:1781_100325_scf_1024_c1",
      "start": 826,
      "end": 1198,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1024_c1_827_1198",
      "annotations": {
        "id": [
          "1781_100325_scf_1024_c1_827_1198"
        ],
        "product": [
          "6",
          "7-dimethyl-8-ribityllumazine synthase"
        ],
        "cath_funfam": [
          "3.40.50.960"
        ],
        "cog": [
          "COG0054"
        ],
        "ko": [
          "KO:K00794"
        ],
        "ec_number": [
          "EC:2.5.1.78"
        ],
        "pfam": [
          "DMRL_synthas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1024_c1_1266_1685": {
      "seqid": "NMDC:1781_100325_scf_1024_c1",
      "start": 1265,
      "end": 1685,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1024_c1_1266_1685",
      "annotations": {
        "id": [
          "1781_100325_scf_1024_c1_1266_1685"
        ],
        "product": [
          "3",
          "4-dihydroxy 2-butanone 4-phosphate synthase"
        ],
        "cath_funfam": [
          "3.90.870.10"
        ],
        "cog": [
          "COG0108"
        ],
        "ko": [
          "KO:K02858"
        ],
        "ec_number": [
          "EC:4.1.99.12"
        ],
        "pfam": [
          "DHBP_synthas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1025_c1": {
    "1781_100325_scf_1025_c1_1_84": {
      "seqid": "NMDC:1781_100325_scf_1025_c1",
      "start": 0,
      "end": 84,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1025_c1_1_84",
      "annotations": {
        "id": [
          "1781_100325_scf_1025_c1_1_84"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1025_c1_114_545": {
      "seqid": "NMDC:1781_100325_scf_1025_c1",
      "start": 113,
      "end": 545,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1025_c1_114_545",
      "annotations": {
        "id": [
          "1781_100325_scf_1025_c1_114_545"
        ],
        "product": [
          "F-type H+-transporting ATPase subunit epsilon"
        ],
        "cath_funfam": [
          "2.60.15.10"
        ],
        "cog": [
          "COG0355"
        ],
        "ko": [
          "KO:K02114"
        ],
        "pfam": [
          "ATP-synt_DE_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1025_c1_557_1687": {
      "seqid": "NMDC:1781_100325_scf_1025_c1",
      "start": 556,
      "end": 1687,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1025_c1_557_1687",
      "annotations": {
        "id": [
          "1781_100325_scf_1025_c1_557_1687"
        ],
        "product": [
          "F-type H+-transporting ATPase subunit beta"
        ],
        "cath_funfam": [
          "1.10.1140.10",
          "3.40.50.300"
        ],
        "cog": [
          "COG0055"
        ],
        "ko": [
          "KO:K02112"
        ],
        "ec_number": [
          "EC:3.6.3.14"
        ],
        "pfam": [
          "ATP-synt_a"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1026_c1": {
    "1781_100325_scf_1026_c1_2_1576": {
      "seqid": "NMDC:1781_100325_scf_1026_c1",
      "start": 1,
      "end": 1576,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1026_c1_2_1576",
      "annotations": {
        "id": [
          "1781_100325_scf_1026_c1_2_1576"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "RVT_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1027_c1": {
    "1781_100325_scf_1027_c1_2_349": {
      "seqid": "NMDC:1781_100325_scf_1027_c1",
      "start": 1,
      "end": 349,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1027_c1_2_349",
      "annotations": {
        "id": [
          "1781_100325_scf_1027_c1_2_349"
        ],
        "product": [
          "D-xylose transport system permease protein"
        ],
        "cath_funfam": [
          "1.20.1250.20"
        ],
        "cog": [
          "COG4214"
        ],
        "ko": [
          "KO:K10544"
        ],
        "pfam": [
          "BPD_transp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1027_c1_346_1128": {
      "seqid": "NMDC:1781_100325_scf_1027_c1",
      "start": 345,
      "end": 1128,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1027_c1_346_1128",
      "annotations": {
        "id": [
          "1781_100325_scf_1027_c1_346_1128"
        ],
        "product": [
          "D-xylose transport system ATP-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1129"
        ],
        "ko": [
          "KO:K10545"
        ],
        "ec_number": [
          "EC:3.6.3.17"
        ],
        "pfam": [
          "ABC_tra"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1027_c1_1135_1635": {
      "seqid": "NMDC:1781_100325_scf_1027_c1",
      "start": 1134,
      "end": 1635,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1027_c1_1135_1635",
      "annotations": {
        "id": [
          "1781_100325_scf_1027_c1_1135_1635"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1028_c1": {
    "1781_100325_scf_1028_c1_2_808": {
      "seqid": "NMDC:1781_100325_scf_1028_c1",
      "start": 1,
      "end": 808,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1028_c1_2_808",
      "annotations": {
        "id": [
          "1781_100325_scf_1028_c1_2_808"
        ],
        "product": [
          "histidinol-phosphate aminotransferase"
        ],
        "cath_funfam": [
          "3.40.640.10"
        ],
        "cog": [
          "COG0079"
        ],
        "ko": [
          "KO:K00817"
        ],
        "ec_number": [
          "EC:2.6.1.9"
        ],
        "pfam": [
          "Aminotran_1_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1028_c1_805_1686": {
      "seqid": "NMDC:1781_100325_scf_1028_c1",
      "start": 804,
      "end": 1686,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1028_c1_805_1686",
      "annotations": {
        "id": [
          "1781_100325_scf_1028_c1_805_1686"
        ],
        "product": [
          "acetolactate synthase-1/2/3 large subunit"
        ],
        "cath_funfam": [
          "3.40.50.970"
        ],
        "cog": [
          "COG0028"
        ],
        "ko": [
          "KO:K01652"
        ],
        "ec_number": [
          "EC:2.2.1.6"
        ],
        "pfam": [
          "TPP_enzyme_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1029_c1": {
    "1781_100325_scf_1029_c1_1_177": {
      "seqid": "NMDC:1781_100325_scf_1029_c1",
      "start": 0,
      "end": 177,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1029_c1_1_177",
      "annotations": {
        "id": [
          "1781_100325_scf_1029_c1_1_177"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1029_c1_260_1120": {
      "seqid": "NMDC:1781_100325_scf_1029_c1",
      "start": 259,
      "end": 1120,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1029_c1_260_1120",
      "annotations": {
        "id": [
          "1781_100325_scf_1029_c1_260_1120"
        ],
        "product": [
          "predicted TIM-barrel fold metal-dependent hydrolase"
        ],
        "cog": [
          "COG2159"
        ],
        "pfam": [
          "Amidohydro_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1029_c1_1125_1685": {
      "seqid": "NMDC:1781_100325_scf_1029_c1",
      "start": 1124,
      "end": 1685,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1029_c1_1125_1685",
      "annotations": {
        "id": [
          "1781_100325_scf_1029_c1_1125_1685"
        ],
        "product": [
          "radical SAM protein (TIGR04043 family)"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_102_c1": {
    "1781_100325_scf_102_c1_640_1260": {
      "seqid": "NMDC:1781_100325_scf_102_c1",
      "start": 639,
      "end": 1260,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_102_c1_640_1260",
      "annotations": {
        "id": [
          "1781_100325_scf_102_c1_640_1260"
        ],
        "product": [
          "SAM-dependent methyltransferase"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "cog": [
          "COG0500"
        ],
        "pfam": [
          "Methyltransf_1",
          "Methyltransf_2",
          "Methyltransf_3",
          "TPM",
          "Teh"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_102_c1_1391_2788": {
      "seqid": "NMDC:1781_100325_scf_102_c1",
      "start": 1390,
      "end": 2788,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_102_c1_1391_2788",
      "annotations": {
        "id": [
          "1781_100325_scf_102_c1_1391_2788"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_102_c1_2868_3683": {
      "seqid": "NMDC:1781_100325_scf_102_c1",
      "start": 2867,
      "end": 3683,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_102_c1_2868_3683",
      "annotations": {
        "id": [
          "1781_100325_scf_102_c1_2868_3683"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.60.120.600"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1030_c1": {
    "1781_100325_scf_1030_c1_8_652": {
      "seqid": "NMDC:1781_100325_scf_1030_c1",
      "start": 7,
      "end": 652,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1030_c1_8_652",
      "annotations": {
        "id": [
          "1781_100325_scf_1030_c1_8_652"
        ],
        "product": [
          "class 3 adenylate cyclase"
        ],
        "cath_funfam": [
          "3.30.70.1230"
        ],
        "cog": [
          "COG2114"
        ],
        "pfam": [
          "Guanylate_cy"
        ],
        "superfamily": [
          "SM00044"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1030_c1_694_1599": {
      "seqid": "NMDC:1781_100325_scf_1030_c1",
      "start": 693,
      "end": 1599,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1030_c1_694_1599",
      "annotations": {
        "id": [
          "1781_100325_scf_1030_c1_694_1599"
        ],
        "product": [
          "osmoprotectant transport system substrate-binding protein"
        ],
        "cog": [
          "COG1732"
        ],
        "ko": [
          "KO:K05845"
        ],
        "pfam": [
          "OpuA"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1031_c1": {
    "1781_100325_scf_1031_c1_1_234": {
      "seqid": "NMDC:1781_100325_scf_1031_c1",
      "start": 0,
      "end": 234,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1031_c1_1_234",
      "annotations": {
        "id": [
          "1781_100325_scf_1031_c1_1_234"
        ],
        "product": [
          "uncharacterized membrane protein"
        ],
        "cog": [
          "COG4655"
        ],
        "pfam": [
          "Ta"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1031_c1_225_644": {
      "seqid": "NMDC:1781_100325_scf_1031_c1",
      "start": 224,
      "end": 644,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1031_c1_225_644",
      "annotations": {
        "id": [
          "1781_100325_scf_1031_c1_225_644"
        ],
        "product": [
          "Flp pilus assembly protein TadG"
        ],
        "cog": [
          "COG4961"
        ],
        "pfam": [
          "Tad"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1031_c1_714_863": {
      "seqid": "NMDC:1781_100325_scf_1031_c1",
      "start": 713,
      "end": 863,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1031_c1_714_863",
      "annotations": {
        "id": [
          "1781_100325_scf_1031_c1_714_863"
        ],
        "product": [
          "Flp pilus assembly pilin Flp"
        ],
        "cog": [
          "COG3847"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1031_c1_999_1163": {
      "seqid": "NMDC:1781_100325_scf_1031_c1",
      "start": 998,
      "end": 1163,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1031_c1_999_1163",
      "annotations": {
        "id": [
          "1781_100325_scf_1031_c1_999_1163"
        ],
        "product": [
          "pilus assembly protein Flp/PilA"
        ],
        "cog": [
          "COG3847"
        ],
        "ko": [
          "KO:K02651"
        ],
        "pfam": [
          "Flp_Fa"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1031_c1_1456_1662": {
      "seqid": "NMDC:1781_100325_scf_1031_c1",
      "start": 1455,
      "end": 1662,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1031_c1_1456_1662",
      "annotations": {
        "id": [
          "1781_100325_scf_1031_c1_1456_1662"
        ],
        "product": [
          "leader peptidase (prepilin peptidase)/N-methyltransferase"
        ],
        "cog": [
          "COG1989"
        ],
        "ko": [
          "KO:K02654"
        ],
        "ec_number": [
          "EC:2.1.1.-",
          "EC:3.4.23.43"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1032_c1": {
    "1781_100325_scf_1032_c1_1_1359": {
      "seqid": "NMDC:1781_100325_scf_1032_c1",
      "start": 0,
      "end": 1359,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1032_c1_1_1359",
      "annotations": {
        "id": [
          "1781_100325_scf_1032_c1_1_1359"
        ],
        "product": [
          "trehalose 6-phosphate synthase"
        ],
        "cath_funfam": [
          "3.40.50.2000"
        ],
        "cog": [
          "COG0380"
        ],
        "ko": [
          "KO:K00697"
        ],
        "ec_number": [
          "EC:2.4.1.15"
        ],
        "pfam": [
          "Glyco_transf_2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1032_c1_1356_1682": {
      "seqid": "NMDC:1781_100325_scf_1032_c1",
      "start": 1355,
      "end": 1682,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1032_c1_1356_1682",
      "annotations": {
        "id": [
          "1781_100325_scf_1032_c1_1356_1682"
        ],
        "product": [
          "trehalose synthase"
        ],
        "cath_funfam": [
          "3.40.50.2000"
        ],
        "cog": [
          "COG0438"
        ],
        "ko": [
          "KO:K13057"
        ],
        "ec_number": [
          "EC:2.4.1.245"
        ],
        "pfam": [
          "Glyco_trans_1_",
          "Glycos_transf_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1033_c1": {
    "1781_100325_scf_1033_c1_1_726": {
      "seqid": "NMDC:1781_100325_scf_1033_c1",
      "start": 0,
      "end": 726,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1033_c1_1_726",
      "annotations": {
        "id": [
          "1781_100325_scf_1033_c1_1_726"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1033_c1_742_942": {
      "seqid": "NMDC:1781_100325_scf_1033_c1",
      "start": 741,
      "end": 942,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1033_c1_742_942",
      "annotations": {
        "id": [
          "1781_100325_scf_1033_c1_742_942"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.10.25.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1033_c1_935_1681": {
      "seqid": "NMDC:1781_100325_scf_1033_c1",
      "start": 934,
      "end": 1681,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1033_c1_935_1681",
      "annotations": {
        "id": [
          "1781_100325_scf_1033_c1_935_1681"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.70.1450"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1034_c1": {
    "1781_100325_scf_1034_c1_2_796": {
      "seqid": "NMDC:1781_100325_scf_1034_c1",
      "start": 1,
      "end": 796,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1034_c1_2_796",
      "annotations": {
        "id": [
          "1781_100325_scf_1034_c1_2_796"
        ],
        "product": [
          "LL-diaminopimelate aminotransferase"
        ],
        "cath_funfam": [
          "3.90.1150.10"
        ],
        "cog": [
          "COG0436"
        ],
        "ko": [
          "KO:K10206"
        ],
        "ec_number": [
          "EC:2.6.1.83"
        ],
        "pfam": [
          "Aminotran_1_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1034_c1_804_1682": {
      "seqid": "NMDC:1781_100325_scf_1034_c1",
      "start": 803,
      "end": 1682,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1034_c1_804_1682",
      "annotations": {
        "id": [
          "1781_100325_scf_1034_c1_804_1682"
        ],
        "product": [
          "GTP-binding protein HflX"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG2262"
        ],
        "ko": [
          "KO:K03665"
        ],
        "pfam": [
          "FeoB_",
          "GTP-bdg_",
          "MMR_HSR"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1035_c1": {
    "1781_100325_scf_1035_c1_2_508": {
      "seqid": "NMDC:1781_100325_scf_1035_c1",
      "start": 1,
      "end": 508,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1035_c1_2_508",
      "annotations": {
        "id": [
          "1781_100325_scf_1035_c1_2_508"
        ],
        "product": [
          "SRSO17 transposase"
        ],
        "cog": [
          "COG5659"
        ],
        "pfam": [
          "DDE_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1035_c1_832_1173": {
      "seqid": "NMDC:1781_100325_scf_1035_c1",
      "start": 831,
      "end": 1173,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1035_c1_832_1173",
      "annotations": {
        "id": [
          "1781_100325_scf_1035_c1_832_1173"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "RHH_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1035_c1_1306_1680": {
      "seqid": "NMDC:1781_100325_scf_1035_c1",
      "start": 1305,
      "end": 1680,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1035_c1_1306_1680",
      "annotations": {
        "id": [
          "1781_100325_scf_1035_c1_1306_1680"
        ],
        "product": [
          "site-specific DNA recombinase"
        ],
        "cath_funfam": [
          "3.40.50.1390"
        ],
        "cog": [
          "COG1961"
        ],
        "ko": [
          "KO:K06400"
        ],
        "pfam": [
          "Resolvas"
        ],
        "superfamily": [
          "SM00857"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1036_c1": {
    "1781_100325_scf_1036_c1_1_384": {
      "seqid": "NMDC:1781_100325_scf_1036_c1",
      "start": 0,
      "end": 384,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1036_c1_1_384",
      "annotations": {
        "id": [
          "1781_100325_scf_1036_c1_1_384"
        ],
        "product": [
          "DNA-binding NarL/FixJ family response regulator"
        ],
        "cath_funfam": [
          "3.40.50.2300"
        ],
        "cog": [
          "COG2197"
        ],
        "pfam": [
          "Response_re"
        ],
        "superfamily": [
          "SM00448"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1036_c1_449_1681": {
      "seqid": "NMDC:1781_100325_scf_1036_c1",
      "start": 448,
      "end": 1681,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1036_c1_449_1681",
      "annotations": {
        "id": [
          "1781_100325_scf_1036_c1_449_1681"
        ],
        "product": [
          "K+-sensing histidine kinase KdpD"
        ],
        "cath_funfam": [
          "1.10.287.130",
          "3.30.565.10"
        ],
        "cog": [
          "COG2205"
        ],
        "pfam": [
          "HATPase_"
        ],
        "superfamily": [
          "SM00387"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1037_c1": {
    "1781_100325_scf_1037_c1_2_1279": {
      "seqid": "NMDC:1781_100325_scf_1037_c1",
      "start": 1,
      "end": 1279,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1037_c1_2_1279",
      "annotations": {
        "id": [
          "1781_100325_scf_1037_c1_2_1279"
        ],
        "product": [
          "aconitate hydratase"
        ],
        "cath_funfam": [
          "3.20.19.10",
          "3.30.499.10"
        ],
        "cog": [
          "COG1048"
        ],
        "ko": [
          "KO:K01681"
        ],
        "ec_number": [
          "EC:4.2.1.3"
        ],
        "pfam": [
          "Aconitas",
          "Aconitase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1037_c1_1551_1679": {
      "seqid": "NMDC:1781_100325_scf_1037_c1",
      "start": 1550,
      "end": 1679,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1037_c1_1551_1679",
      "annotations": {
        "id": [
          "1781_100325_scf_1037_c1_1551_1679"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1038_c1": {
    "1781_100325_scf_1038_c1_1_873": {
      "seqid": "NMDC:1781_100325_scf_1038_c1",
      "start": 0,
      "end": 873,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1038_c1_1_873",
      "annotations": {
        "id": [
          "1781_100325_scf_1038_c1_1_873"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG2129"
        ],
        "ko": [
          "KO:K07096"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1038_c1_905_1651": {
      "seqid": "NMDC:1781_100325_scf_1038_c1",
      "start": 904,
      "end": 1651,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1038_c1_905_1651",
      "annotations": {
        "id": [
          "1781_100325_scf_1038_c1_905_1651"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1039_c1": {
    "1781_100325_scf_1039_c1_59_1075": {
      "seqid": "NMDC:1781_100325_scf_1039_c1",
      "start": 58,
      "end": 1075,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1039_c1_59_1075",
      "annotations": {
        "id": [
          "1781_100325_scf_1039_c1_59_1075"
        ],
        "product": [
          "peptide/nickel transport system ATP-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0444"
        ],
        "ko": [
          "KO:K02031"
        ],
        "pfam": [
          "AAA_2",
          "ABC_tra",
          "oligo_HP"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1039_c1_1072_1680": {
      "seqid": "NMDC:1781_100325_scf_1039_c1",
      "start": 1071,
      "end": 1680,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1039_c1_1072_1680",
      "annotations": {
        "id": [
          "1781_100325_scf_1039_c1_1072_1680"
        ],
        "product": [
          "ABC-type oligopeptide transport system ATPase subunit"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG4608"
        ],
        "pfam": [
          "ABC_tra"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_103_c1": {
    "1781_100325_scf_103_c1_491_1321": {
      "seqid": "NMDC:1781_100325_scf_103_c1",
      "start": 490,
      "end": 1321,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_103_c1_491_1321",
      "annotations": {
        "id": [
          "1781_100325_scf_103_c1_491_1321"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "MUL"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_103_c1_1318_1911": {
      "seqid": "NMDC:1781_100325_scf_103_c1",
      "start": 1317,
      "end": 1911,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_103_c1_1318_1911",
      "annotations": {
        "id": [
          "1781_100325_scf_103_c1_1318_1911"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_103_c1_1991_3733": {
      "seqid": "NMDC:1781_100325_scf_103_c1",
      "start": 1990,
      "end": 3733,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_103_c1_1991_3733",
      "annotations": {
        "id": [
          "1781_100325_scf_103_c1_1991_3733"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1040_c1": {
    "1781_100325_scf_1040_c1_63_686": {
      "seqid": "NMDC:1781_100325_scf_1040_c1",
      "start": 62,
      "end": 686,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1040_c1_63_686",
      "annotations": {
        "id": [
          "1781_100325_scf_1040_c1_63_686"
        ],
        "product": [
          "LPXTG-motif cell wall-anchored protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1040_c1_1112_1426": {
      "seqid": "NMDC:1781_100325_scf_1040_c1",
      "start": 1111,
      "end": 1426,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1040_c1_1112_1426",
      "annotations": {
        "id": [
          "1781_100325_scf_1040_c1_1112_1426"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1040_c1_1510_1677": {
      "seqid": "NMDC:1781_100325_scf_1040_c1",
      "start": 1509,
      "end": 1677,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1040_c1_1510_1677",
      "annotations": {
        "id": [
          "1781_100325_scf_1040_c1_1510_1677"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1041_c1": {
    "1781_100325_scf_1041_c1_1_1677": {
      "seqid": "NMDC:1781_100325_scf_1041_c1",
      "start": 0,
      "end": 1677,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1041_c1_1_1677",
      "annotations": {
        "id": [
          "1781_100325_scf_1041_c1_1_1677"
        ],
        "product": [
          "DNA-directed RNA polymerase subunit B"
        ],
        "cath_funfam": [
          "2.40.270.10",
          "3.40.50.300"
        ],
        "cog": [
          "COG0085"
        ],
        "ko": [
          "KO:K13798"
        ],
        "ec_number": [
          "EC:2.7.7.6"
        ],
        "pfam": [
          "RNA_pol_Rpb2_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1042_c1": {
    "1781_100325_scf_1042_c1_1_168": {
      "seqid": "NMDC:1781_100325_scf_1042_c1",
      "start": 0,
      "end": 168,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1042_c1_1_168",
      "annotations": {
        "id": [
          "1781_100325_scf_1042_c1_1_168"
        ],
        "product": [
          "tRNA wybutosine-synthesizing protein 1"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "ko": [
          "KO:K15449"
        ],
        "ec_number": [
          "EC:4.1.3.44"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1042_c1_273_1322": {
      "seqid": "NMDC:1781_100325_scf_1042_c1",
      "start": 272,
      "end": 1322,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1042_c1_273_1322",
      "annotations": {
        "id": [
          "1781_100325_scf_1042_c1_273_1322"
        ],
        "product": [
          "magnesium transporter"
        ],
        "cath_funfam": [
          "1.20.58.340"
        ],
        "cog": [
          "COG0598"
        ],
        "ko": [
          "KO:K03284"
        ],
        "pfam": [
          "Cor"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1043_c1": {
    "1781_100325_scf_1043_c1_357_596": {
      "seqid": "NMDC:1781_100325_scf_1043_c1",
      "start": 356,
      "end": 596,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1043_c1_357_596",
      "annotations": {
        "id": [
          "1781_100325_scf_1043_c1_357_596"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1043_c1_895_1107": {
      "seqid": "NMDC:1781_100325_scf_1043_c1",
      "start": 894,
      "end": 1107,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1043_c1_895_1107",
      "annotations": {
        "id": [
          "1781_100325_scf_1043_c1_895_1107"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1043_c1_1214_1639": {
      "seqid": "NMDC:1781_100325_scf_1043_c1",
      "start": 1213,
      "end": 1639,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1043_c1_1214_1639",
      "annotations": {
        "id": [
          "1781_100325_scf_1043_c1_1214_1639"
        ],
        "product": [
          "peptide-methionine (R)-S-oxide reductase"
        ],
        "cath_funfam": [
          "2.170.150.20"
        ],
        "cog": [
          "COG0229"
        ],
        "ko": [
          "KO:K07305"
        ],
        "ec_number": [
          "EC:1.8.4.12"
        ],
        "pfam": [
          "Sel"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1044_c1": {
    "1781_100325_scf_1044_c1_1_174": {
      "seqid": "NMDC:1781_100325_scf_1044_c1",
      "start": 0,
      "end": 174,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1044_c1_1_174",
      "annotations": {
        "id": [
          "1781_100325_scf_1044_c1_1_174"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1044_c1_193_489": {
      "seqid": "NMDC:1781_100325_scf_1044_c1",
      "start": 192,
      "end": 489,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1044_c1_193_489",
      "annotations": {
        "id": [
          "1781_100325_scf_1044_c1_193_489"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.70.1120"
        ],
        "cog": [
          "COG1550"
        ],
        "ko": [
          "KO:K09764"
        ],
        "pfam": [
          "DUF50"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1044_c1_592_933": {
      "seqid": "NMDC:1781_100325_scf_1044_c1",
      "start": 591,
      "end": 933,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1044_c1_592_933",
      "annotations": {
        "id": [
          "1781_100325_scf_1044_c1_592_933"
        ],
        "product": [
          "ribosome-binding factor A"
        ],
        "cath_funfam": [
          "3.30.300.20"
        ],
        "cog": [
          "COG0858"
        ],
        "ko": [
          "KO:K02834"
        ],
        "pfam": [
          "RBF"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1044_c1_899_1675": {
      "seqid": "NMDC:1781_100325_scf_1044_c1",
      "start": 898,
      "end": 1675,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1044_c1_899_1675",
      "annotations": {
        "id": [
          "1781_100325_scf_1044_c1_899_1675"
        ],
        "product": [
          "phosphoesterase RecJ-like protein"
        ],
        "cath_funfam": [
          "3.90.1640.10"
        ],
        "cog": [
          "COG0618"
        ],
        "ko": [
          "KO:K06881"
        ],
        "ec_number": [
          "EC:3.1.13.3",
          "EC:3.1.3.7"
        ],
        "pfam": [
          "DH"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1045_c1": {
    "1781_100325_scf_1045_c1_38_205": {
      "seqid": "NMDC:1781_100325_scf_1045_c1",
      "start": 37,
      "end": 205,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1045_c1_38_205",
      "annotations": {
        "id": [
          "1781_100325_scf_1045_c1_38_205"
        ],
        "product": [
          "uncharacterized membrane protein (DUF106 family)"
        ],
        "cog": [
          "COG1422"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1045_c1_223_810": {
      "seqid": "NMDC:1781_100325_scf_1045_c1",
      "start": 222,
      "end": 810,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1045_c1_223_810",
      "annotations": {
        "id": [
          "1781_100325_scf_1045_c1_223_810"
        ],
        "product": [
          "predicted transcriptional regulator"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG3398"
        ],
        "pfam": [
          "HTH_2"
        ],
        "superfamily": [
          "SM00347"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1045_c1_950_1252": {
      "seqid": "NMDC:1781_100325_scf_1045_c1",
      "start": 949,
      "end": 1252,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1045_c1_950_1252",
      "annotations": {
        "id": [
          "1781_100325_scf_1045_c1_950_1252"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1046_c1": {
    "1781_100325_scf_1046_c1_34_498": {
      "seqid": "NMDC:1781_100325_scf_1046_c1",
      "start": 33,
      "end": 498,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1046_c1_34_498",
      "annotations": {
        "id": [
          "1781_100325_scf_1046_c1_34_498"
        ],
        "product": [
          "ligand-binding SRPBCC domain-containing protein"
        ],
        "cog": [
          "COG4276"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1046_c1_580_1002": {
      "seqid": "NMDC:1781_100325_scf_1046_c1",
      "start": 579,
      "end": 1002,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1046_c1_580_1002",
      "annotations": {
        "id": [
          "1781_100325_scf_1046_c1_580_1002"
        ],
        "product": [
          "ribosome-associated toxin RatA of RatAB toxin-antitoxin module"
        ],
        "cath_funfam": [
          "3.30.530.20"
        ],
        "cog": [
          "COG2867"
        ],
        "pfam": [
          "Polyketide_cyc"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1046_c1_1293_1676": {
      "seqid": "NMDC:1781_100325_scf_1046_c1",
      "start": 1292,
      "end": 1676,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1046_c1_1293_1676",
      "annotations": {
        "id": [
          "1781_100325_scf_1046_c1_1293_1676"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1047_c1": {
    "1781_100325_scf_1047_c1_2_1009": {
      "seqid": "NMDC:1781_100325_scf_1047_c1",
      "start": 1,
      "end": 1009,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1047_c1_2_1009",
      "annotations": {
        "id": [
          "1781_100325_scf_1047_c1_2_1009"
        ],
        "product": [
          "O-antigen/teichoic acid export membrane protein"
        ],
        "cog": [
          "COG2244"
        ],
        "pfam": [
          "Polysacc_syn",
          "Polysacc_synt_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1047_c1_1083_1424": {
      "seqid": "NMDC:1781_100325_scf_1047_c1",
      "start": 1082,
      "end": 1424,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1047_c1_1083_1424",
      "annotations": {
        "id": [
          "1781_100325_scf_1047_c1_1083_1424"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1048_c1": {
    "1781_100325_scf_1048_c1_2_538": {
      "seqid": "NMDC:1781_100325_scf_1048_c1",
      "start": 1,
      "end": 538,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1048_c1_2_538",
      "annotations": {
        "id": [
          "1781_100325_scf_1048_c1_2_538"
        ],
        "product": [
          "cell division transport system permease protein"
        ],
        "cog": [
          "COG2177"
        ],
        "ko": [
          "KO:K09811"
        ],
        "pfam": [
          "Fts"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1048_c1_547_1023": {
      "seqid": "NMDC:1781_100325_scf_1048_c1",
      "start": 546,
      "end": 1023,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1048_c1_547_1023",
      "annotations": {
        "id": [
          "1781_100325_scf_1048_c1_547_1023"
        ],
        "product": [
          "SsrA-binding protein"
        ],
        "cath_funfam": [
          "2.40.280.10"
        ],
        "cog": [
          "COG0691"
        ],
        "ko": [
          "KO:K03664"
        ],
        "pfam": [
          "Smp"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1048_c1_1067_1420": {
      "seqid": "NMDC:1781_100325_scf_1048_c1",
      "start": 1066,
      "end": 1420,
      "strand": "+",
      "type": "SO:0000584",
      "encodes": "NMDC:1781_100325_scf_1048_c1_1067_1420",
      "annotations": {
        "id": [
          "1781_100325_scf_1048_c1_1067_1420"
        ],
        "product": [
          "transfer-messenger RNA"
        ]
      }
    }
  },
  "1781_100325_scf_1049_c1": {
    "1781_100325_scf_1049_c1_1_834": {
      "seqid": "NMDC:1781_100325_scf_1049_c1",
      "start": 0,
      "end": 834,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1049_c1_1_834",
      "annotations": {
        "id": [
          "1781_100325_scf_1049_c1_1_834"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1049_c1_1252_1434": {
      "seqid": "NMDC:1781_100325_scf_1049_c1",
      "start": 1251,
      "end": 1434,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1049_c1_1252_1434",
      "annotations": {
        "id": [
          "1781_100325_scf_1049_c1_1252_1434"
        ],
        "product": [
          "Flp pilus assembly pilin Flp"
        ],
        "cog": [
          "COG3847"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1049_c1_1449_1673": {
      "seqid": "NMDC:1781_100325_scf_1049_c1",
      "start": 1448,
      "end": 1673,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1049_c1_1449_1673",
      "annotations": {
        "id": [
          "1781_100325_scf_1049_c1_1449_1673"
        ],
        "product": [
          "Flp pilus assembly protein TadG"
        ],
        "cog": [
          "COG4961"
        ],
        "pfam": [
          "Tad"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_104_c1": {
    "1781_100325_scf_104_c1_1_192": {
      "seqid": "NMDC:1781_100325_scf_104_c1",
      "start": 0,
      "end": 192,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_104_c1_1_192",
      "annotations": {
        "id": [
          "1781_100325_scf_104_c1_1_192"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_104_c1_311_1579": {
      "seqid": "NMDC:1781_100325_scf_104_c1",
      "start": 310,
      "end": 1579,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_104_c1_311_1579",
      "annotations": {
        "id": [
          "1781_100325_scf_104_c1_311_1579"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3415"
        ],
        "pfam": [
          "DDE_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_104_c1_1996_3879": {
      "seqid": "NMDC:1781_100325_scf_104_c1",
      "start": 1995,
      "end": 3879,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_104_c1_1996_3879",
      "annotations": {
        "id": [
          "1781_100325_scf_104_c1_1996_3879"
        ],
        "product": [
          "RNA-directed DNA polymerase"
        ],
        "cath_funfam": [
          "3.10.450.160"
        ],
        "cog": [
          "COG3344"
        ],
        "ko": [
          "KO:K00986"
        ],
        "ec_number": [
          "EC:2.7.7.49"
        ],
        "pfam": [
          "Intron_maturas",
          "RVT_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1050_c1": {
    "1781_100325_scf_1050_c1_26_649": {
      "seqid": "NMDC:1781_100325_scf_1050_c1",
      "start": 25,
      "end": 649,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1050_c1_26_649",
      "annotations": {
        "id": [
          "1781_100325_scf_1050_c1_26_649"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1050_c1_660_1103": {
      "seqid": "NMDC:1781_100325_scf_1050_c1",
      "start": 659,
      "end": 1103,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1050_c1_660_1103",
      "annotations": {
        "id": [
          "1781_100325_scf_1050_c1_660_1103"
        ],
        "product": [
          "catechol-2",
          "3-dioxygenase"
        ],
        "cath_funfam": [
          "3.10.180.10"
        ],
        "cog": [
          "COG2514"
        ],
        "pfam": [
          "Glyoxalas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1050_c1_1157_1672": {
      "seqid": "NMDC:1781_100325_scf_1050_c1",
      "start": 1156,
      "end": 1672,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1050_c1_1157_1672",
      "annotations": {
        "id": [
          "1781_100325_scf_1050_c1_1157_1672"
        ],
        "product": [
          "dienelactone hydrolase"
        ],
        "cath_funfam": [
          "3.40.50.1820"
        ],
        "cog": [
          "COG0412"
        ],
        "pfam": [
          "AXE"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1051_c1": {
    "1781_100325_scf_1051_c1_2_637": {
      "seqid": "NMDC:1781_100325_scf_1051_c1",
      "start": 1,
      "end": 637,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1051_c1_2_637",
      "annotations": {
        "id": [
          "1781_100325_scf_1051_c1_2_637"
        ],
        "product": [
          "peptide/nickel transport system substrate-binding protein"
        ],
        "cog": [
          "COG3889"
        ],
        "ko": [
          "KO:K02035"
        ],
        "pfam": [
          "SBP_bac_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1051_c1_742_1371": {
      "seqid": "NMDC:1781_100325_scf_1051_c1",
      "start": 741,
      "end": 1371,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1051_c1_742_1371",
      "annotations": {
        "id": [
          "1781_100325_scf_1051_c1_742_1371"
        ],
        "product": [
          "Holliday junction resolvase-like predicted endonuclease"
        ],
        "cog": [
          "COG0792"
        ],
        "pfam": [
          "Mrr_ca"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1051_c1_1358_1621": {
      "seqid": "NMDC:1781_100325_scf_1051_c1",
      "start": 1357,
      "end": 1621,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1051_c1_1358_1621",
      "annotations": {
        "id": [
          "1781_100325_scf_1051_c1_1358_1621"
        ],
        "product": [
          "putative membrane protein"
        ],
        "cog": [
          "COG3356"
        ],
        "ko": [
          "KO:K08979"
        ],
        "pfam": [
          "DUF207"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1052_c1": {
    "1781_100325_scf_1052_c1_2_865": {
      "seqid": "NMDC:1781_100325_scf_1052_c1",
      "start": 1,
      "end": 865,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1052_c1_2_865",
      "annotations": {
        "id": [
          "1781_100325_scf_1052_c1_2_865"
        ],
        "product": [
          "uncharacterized protein YqhQ"
        ],
        "cog": [
          "COG3872"
        ],
        "pfam": [
          "DUF138"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1052_c1_873_1097": {
      "seqid": "NMDC:1781_100325_scf_1052_c1",
      "start": 872,
      "end": 1097,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1052_c1_873_1097",
      "annotations": {
        "id": [
          "1781_100325_scf_1052_c1_873_1097"
        ],
        "product": [
          "large subunit ribosomal protein L31"
        ],
        "cog": [
          "COG0254"
        ],
        "ko": [
          "KO:K02909"
        ],
        "pfam": [
          "Ribosomal_L3"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1052_c1_1094_1672": {
      "seqid": "NMDC:1781_100325_scf_1052_c1",
      "start": 1093,
      "end": 1672,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1052_c1_1094_1672",
      "annotations": {
        "id": [
          "1781_100325_scf_1052_c1_1094_1672"
        ],
        "product": [
          "threonine dehydratase"
        ],
        "cath_funfam": [
          "3.40.50.1100"
        ],
        "cog": [
          "COG1171"
        ],
        "ko": [
          "KO:K01754"
        ],
        "ec_number": [
          "EC:4.3.1.19"
        ],
        "pfam": [
          "PAL"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1053_c1": {
    "1781_100325_scf_1053_c1_1_1209": {
      "seqid": "NMDC:1781_100325_scf_1053_c1",
      "start": 0,
      "end": 1209,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1053_c1_1_1209",
      "annotations": {
        "id": [
          "1781_100325_scf_1053_c1_1_1209"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_ISAZ01"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1053_c1_1293_1670": {
      "seqid": "NMDC:1781_100325_scf_1053_c1",
      "start": 1292,
      "end": 1670,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1053_c1_1293_1670",
      "annotations": {
        "id": [
          "1781_100325_scf_1053_c1_1293_1670"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG5276"
        ],
        "pfam": [
          "LVIV"
        ],
        "superfamily": [
          "SM00564"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1054_c1": {
    "1781_100325_scf_1054_c1_3_860": {
      "seqid": "NMDC:1781_100325_scf_1054_c1",
      "start": 2,
      "end": 860,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1054_c1_3_860",
      "annotations": {
        "id": [
          "1781_100325_scf_1054_c1_3_860"
        ],
        "product": [
          "signal recognition particle subunit SRP54"
        ],
        "cath_funfam": [
          "1.20.120.140",
          "3.40.50.300"
        ],
        "cog": [
          "COG0541"
        ],
        "ko": [
          "KO:K03106"
        ],
        "pfam": [
          "SRP5",
          "SRP54_",
          "Zeta_toxi"
        ],
        "superfamily": [
          "SM00962",
          "SM00963"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1054_c1_872_1267": {
      "seqid": "NMDC:1781_100325_scf_1054_c1",
      "start": 871,
      "end": 1267,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1054_c1_872_1267",
      "annotations": {
        "id": [
          "1781_100325_scf_1054_c1_872_1267"
        ],
        "product": [
          "DNA-binding response OmpR family regulator"
        ],
        "cath_funfam": [
          "3.40.50.2300"
        ],
        "cog": [
          "COG0745"
        ],
        "pfam": [
          "Response_re"
        ],
        "superfamily": [
          "SM00448"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1054_c1_1270_1668": {
      "seqid": "NMDC:1781_100325_scf_1054_c1",
      "start": 1269,
      "end": 1668,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1054_c1_1270_1668",
      "annotations": {
        "id": [
          "1781_100325_scf_1054_c1_1270_1668"
        ],
        "product": [
          "fused signal recognition particle receptor"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0552"
        ],
        "ko": [
          "KO:K03110"
        ],
        "pfam": [
          "SRP5"
        ],
        "superfamily": [
          "SM00962"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1055_c1": {
    "1781_100325_scf_1055_c1_2_181": {
      "seqid": "NMDC:1781_100325_scf_1055_c1",
      "start": 1,
      "end": 181,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1055_c1_2_181",
      "annotations": {
        "id": [
          "1781_100325_scf_1055_c1_2_181"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.20.120.580"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1055_c1_187_834": {
      "seqid": "NMDC:1781_100325_scf_1055_c1",
      "start": 186,
      "end": 834,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1055_c1_187_834",
      "annotations": {
        "id": [
          "1781_100325_scf_1055_c1_187_834"
        ],
        "product": [
          "translin"
        ],
        "cath_funfam": [
          "1.20.58.190",
          "1.20.58.200"
        ],
        "cog": [
          "COG2178"
        ],
        "ko": [
          "KO:K07477"
        ],
        "pfam": [
          "Transli"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1055_c1_1101_1616": {
      "seqid": "NMDC:1781_100325_scf_1055_c1",
      "start": 1100,
      "end": 1616,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1055_c1_1101_1616",
      "annotations": {
        "id": [
          "1781_100325_scf_1055_c1_1101_1616"
        ],
        "product": [
          "Holliday junction resolvase"
        ],
        "cog": [
          "COG1591"
        ],
        "ko": [
          "KO:K03552"
        ],
        "pfam": [
          "Hj"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1056_c1": {
    "1781_100325_scf_1056_c1_5_409": {
      "seqid": "NMDC:1781_100325_scf_1056_c1",
      "start": 4,
      "end": 409,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1056_c1_5_409",
      "annotations": {
        "id": [
          "1781_100325_scf_1056_c1_5_409"
        ],
        "product": [
          "nickel superoxide dismutase"
        ],
        "cath_funfam": [
          "1.20.120.400"
        ],
        "ko": [
          "KO:K00518"
        ],
        "ec_number": [
          "EC:1.15.1.1"
        ],
        "pfam": [
          "Sod_N"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1056_c1_440_1417": {
      "seqid": "NMDC:1781_100325_scf_1056_c1",
      "start": 439,
      "end": 1417,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1056_c1_440_1417",
      "annotations": {
        "id": [
          "1781_100325_scf_1056_c1_440_1417"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.150.300",
          "3.10.20.30"
        ],
        "cog": [
          "COG0012"
        ],
        "ko": [
          "KO:K06942"
        ],
        "pfam": [
          "MMR_HSR",
          "YchF-GTPase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1056_c1_1506_1667": {
      "seqid": "NMDC:1781_100325_scf_1056_c1",
      "start": 1505,
      "end": 1667,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1056_c1_1506_1667",
      "annotations": {
        "id": [
          "1781_100325_scf_1056_c1_1506_1667"
        ],
        "product": [
          "excisionase family DNA binding protein"
        ],
        "cath_funfam": [
          "1.10.1660.10"
        ],
        "cog": [
          "COG0789"
        ],
        "pfam": [
          "HTH_1",
          "Mer",
          "MerR_"
        ],
        "superfamily": [
          "SM00422"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1057_c1": {
    "1781_100325_scf_1057_c1_2_877": {
      "seqid": "NMDC:1781_100325_scf_1057_c1",
      "start": 1,
      "end": 877,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1057_c1_2_877",
      "annotations": {
        "id": [
          "1781_100325_scf_1057_c1_2_877"
        ],
        "product": [
          "small subunit ribosomal protein S3"
        ],
        "cath_funfam": [
          "3.30.1140.32",
          "3.30.300.20"
        ],
        "cog": [
          "COG0092"
        ],
        "ko": [
          "KO:K02982"
        ],
        "pfam": [
          "KH_",
          "Ribosomal_S3_"
        ],
        "superfamily": [
          "SM00322"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1057_c1_877_1302": {
      "seqid": "NMDC:1781_100325_scf_1057_c1",
      "start": 876,
      "end": 1302,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1057_c1_877_1302",
      "annotations": {
        "id": [
          "1781_100325_scf_1057_c1_877_1302"
        ],
        "product": [
          "large subunit ribosomal protein L16"
        ],
        "cath_funfam": [
          "3.90.1170.10"
        ],
        "cog": [
          "COG0197"
        ],
        "ko": [
          "KO:K02878"
        ],
        "pfam": [
          "Ribosomal_L1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1057_c1_1302_1535": {
      "seqid": "NMDC:1781_100325_scf_1057_c1",
      "start": 1301,
      "end": 1535,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1057_c1_1302_1535",
      "annotations": {
        "id": [
          "1781_100325_scf_1057_c1_1302_1535"
        ],
        "product": [
          "large subunit ribosomal protein L29"
        ],
        "cath_funfam": [
          "1.10.287.310"
        ],
        "cog": [
          "COG0255"
        ],
        "ko": [
          "KO:K02904"
        ],
        "pfam": [
          "Ribosomal_L2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1057_c1_1532_1666": {
      "seqid": "NMDC:1781_100325_scf_1057_c1",
      "start": 1531,
      "end": 1666,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1057_c1_1532_1666",
      "annotations": {
        "id": [
          "1781_100325_scf_1057_c1_1532_1666"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1058_c1": {
    "1781_100325_scf_1058_c1_1_1647": {
      "seqid": "NMDC:1781_100325_scf_1058_c1",
      "start": 0,
      "end": 1647,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1058_c1_1_1647",
      "annotations": {
        "id": [
          "1781_100325_scf_1058_c1_1_1647"
        ],
        "product": [
          "diguanylate cyclase (GGDEF)-like protein/PAS domain S-box-containing protein"
        ],
        "cath_funfam": [
          "3.30.450.20",
          "3.30.70.270"
        ],
        "cog": [
          "COG2199",
          "COG2202"
        ],
        "pfam": [
          "EA",
          "GGDE",
          "PA",
          "PAS_"
        ],
        "superfamily": [
          "SM00091",
          "SM00267"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1059_c1": {
    "1781_100325_scf_1059_c1_1_738": {
      "seqid": "NMDC:1781_100325_scf_1059_c1",
      "start": 0,
      "end": 738,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1059_c1_1_738",
      "annotations": {
        "id": [
          "1781_100325_scf_1059_c1_1_738"
        ],
        "product": [
          "tryptophan 2",
          "3-dioxygenase"
        ],
        "cog": [
          "COG3483"
        ],
        "ko": [
          "KO:K00453"
        ],
        "ec_number": [
          "EC:1.13.11.11"
        ],
        "pfam": [
          "Trp_dioxygenas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1059_c1_735_1667": {
      "seqid": "NMDC:1781_100325_scf_1059_c1",
      "start": 734,
      "end": 1667,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1059_c1_735_1667",
      "annotations": {
        "id": [
          "1781_100325_scf_1059_c1_735_1667"
        ],
        "product": [
          "kynureninase"
        ],
        "cath_funfam": [
          "3.40.640.10"
        ],
        "cog": [
          "COG0520"
        ],
        "ko": [
          "KO:K01556"
        ],
        "ec_number": [
          "EC:3.7.1.3"
        ],
        "pfam": [
          "Aminotran_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_105_c1": {
    "1781_100325_scf_105_c1_2_676": {
      "seqid": "NMDC:1781_100325_scf_105_c1",
      "start": 1,
      "end": 676,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_105_c1_2_676",
      "annotations": {
        "id": [
          "1781_100325_scf_105_c1_2_676"
        ],
        "product": [
          "5",
          "10-methylenetetrahydrofolate reductase"
        ],
        "cog": [
          "COG0685"
        ],
        "pfam": [
          "MTHF"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_105_c1_816_1400": {
      "seqid": "NMDC:1781_100325_scf_105_c1",
      "start": 815,
      "end": 1400,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_105_c1_816_1400",
      "annotations": {
        "id": [
          "1781_100325_scf_105_c1_816_1400"
        ],
        "product": [
          "8-oxo-dGTP pyrophosphatase MutT (NUDIX family)"
        ],
        "cath_funfam": [
          "3.90.79.10"
        ],
        "cog": [
          "COG0494"
        ],
        "pfam": [
          "NUDI"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_105_c1_1818_3269": {
      "seqid": "NMDC:1781_100325_scf_105_c1",
      "start": 1817,
      "end": 3269,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_105_c1_1818_3269",
      "annotations": {
        "id": [
          "1781_100325_scf_105_c1_1818_3269"
        ],
        "product": [
          "4-hydroxy-3-polyprenylbenzoate decarboxylase"
        ],
        "cath_funfam": [
          "3.40.1670.10"
        ],
        "cog": [
          "COG0043"
        ],
        "ko": [
          "KO:K03182"
        ],
        "ec_number": [
          "EC:4.1.1.98"
        ],
        "pfam": [
          "Ubi"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_105_c1_3313_3873": {
      "seqid": "NMDC:1781_100325_scf_105_c1",
      "start": 3312,
      "end": 3873,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_105_c1_3313_3873",
      "annotations": {
        "id": [
          "1781_100325_scf_105_c1_3313_3873"
        ],
        "product": [
          "phosphoribosylaminoimidazole-succinocarboxamide synthase"
        ],
        "cath_funfam": [
          "3.30.200.20",
          "3.30.470.20"
        ],
        "cog": [
          "COG0152"
        ],
        "ko": [
          "KO:K01923"
        ],
        "ec_number": [
          "EC:6.3.2.6"
        ],
        "pfam": [
          "SAICAR_syn"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1060_c1": {
    "1781_100325_scf_1060_c1_88_1386": {
      "seqid": "NMDC:1781_100325_scf_1060_c1",
      "start": 87,
      "end": 1386,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1060_c1_88_1386",
      "annotations": {
        "id": [
          "1781_100325_scf_1060_c1_88_1386"
        ],
        "product": [
          "MFS family permease"
        ],
        "cath_funfam": [
          "1.20.1250.20"
        ],
        "cog": [
          "COG0477"
        ],
        "pfam": [
          "MFS_",
          "Sugar_t"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1061_c1": {
    "1781_100325_scf_1061_c1_21_713": {
      "seqid": "NMDC:1781_100325_scf_1061_c1",
      "start": 20,
      "end": 713,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1061_c1_21_713",
      "annotations": {
        "id": [
          "1781_100325_scf_1061_c1_21_713"
        ],
        "product": [
          "NDP-sugar pyrophosphorylase family protein"
        ],
        "cath_funfam": [
          "3.90.550.10"
        ],
        "cog": [
          "COG1208"
        ],
        "pfam": [
          "Isp",
          "NTP_transf_",
          "NTP_transferas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1061_c1_710_1666": {
      "seqid": "NMDC:1781_100325_scf_1061_c1",
      "start": 709,
      "end": 1666,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1061_c1_710_1666",
      "annotations": {
        "id": [
          "1781_100325_scf_1061_c1_710_1666"
        ],
        "product": [
          "alkanesulfonate monooxygenase SsuD/methylene tetrahydromethanopterin reductase-like flavin-dependent oxidoreductase (luciferase family)"
        ],
        "cath_funfam": [
          "3.20.20.30"
        ],
        "cog": [
          "COG2141"
        ],
        "pfam": [
          "Bac_luciferas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1062_c1": {
    "1781_100325_scf_1062_c1_5_283": {
      "seqid": "NMDC:1781_100325_scf_1062_c1",
      "start": 4,
      "end": 283,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1062_c1_5_283",
      "annotations": {
        "id": [
          "1781_100325_scf_1062_c1_5_283"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.720.10"
        ],
        "pfam": [
          "Rho_"
        ],
        "superfamily": [
          "SM00959"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1062_c1_335_562": {
      "seqid": "NMDC:1781_100325_scf_1062_c1",
      "start": 334,
      "end": 562,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1062_c1_335_562",
      "annotations": {
        "id": [
          "1781_100325_scf_1062_c1_335_562"
        ],
        "product": [
          "DNA-binding Lrp family transcriptional regulator"
        ],
        "cath_funfam": [
          "3.30.70.920"
        ],
        "cog": [
          "COG1522"
        ],
        "pfam": [
          "AsnC_trans_re"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1062_c1_671_1651": {
      "seqid": "NMDC:1781_100325_scf_1062_c1",
      "start": 670,
      "end": 1651,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1062_c1_671_1651",
      "annotations": {
        "id": [
          "1781_100325_scf_1062_c1_671_1651"
        ],
        "product": [
          "propanol-preferring alcohol dehydrogenase"
        ],
        "cath_funfam": [
          "3.90.180.10"
        ],
        "cog": [
          "COG1064"
        ],
        "ko": [
          "KO:K13953"
        ],
        "ec_number": [
          "EC:1.1.1.1"
        ],
        "pfam": [
          "ADH_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1063_c1": {
    "1781_100325_scf_1063_c1_54_1505": {
      "seqid": "NMDC:1781_100325_scf_1063_c1",
      "start": 53,
      "end": 1505,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1063_c1_54_1505",
      "annotations": {
        "id": [
          "1781_100325_scf_1063_c1_54_1505"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1064_c1": {
    "1781_100325_scf_1064_c1_3_611": {
      "seqid": "NMDC:1781_100325_scf_1064_c1",
      "start": 2,
      "end": 611,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1064_c1_3_611",
      "annotations": {
        "id": [
          "1781_100325_scf_1064_c1_3_611"
        ],
        "product": [
          "carbamoyl-phosphate synthase large subunit"
        ],
        "cath_funfam": [
          "3.30.1490.20"
        ],
        "cog": [
          "COG0458"
        ],
        "ko": [
          "KO:K01955"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "pfam": [
          "ATP-grasp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1064_c1_720_1343": {
      "seqid": "NMDC:1781_100325_scf_1064_c1",
      "start": 719,
      "end": 1343,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1064_c1_720_1343",
      "annotations": {
        "id": [
          "1781_100325_scf_1064_c1_720_1343"
        ],
        "product": [
          "histidinol phosphatase-like PHP family hydrolase"
        ],
        "cath_funfam": [
          "3.20.20.140"
        ],
        "cog": [
          "COG1387"
        ],
        "pfam": [
          "PH"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1065_c1": {
    "1781_100325_scf_1065_c1_1_246": {
      "seqid": "NMDC:1781_100325_scf_1065_c1",
      "start": 0,
      "end": 246,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1065_c1_1_246",
      "annotations": {
        "id": [
          "1781_100325_scf_1065_c1_1_246"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1065_c1_431_1618": {
      "seqid": "NMDC:1781_100325_scf_1065_c1",
      "start": 430,
      "end": 1618,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1065_c1_431_1618",
      "annotations": {
        "id": [
          "1781_100325_scf_1065_c1_431_1618"
        ],
        "product": [
          "4-amino-4-deoxy-L-arabinose transferase-like glycosyltransferase"
        ],
        "cog": [
          "COG1807"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1066_c1": {
    "1781_100325_scf_1066_c1_1_711": {
      "seqid": "NMDC:1781_100325_scf_1066_c1",
      "start": 0,
      "end": 711,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1066_c1_1_711",
      "annotations": {
        "id": [
          "1781_100325_scf_1066_c1_1_711"
        ],
        "product": [
          "DNA repair protein RadA"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0468"
        ],
        "ko": [
          "KO:K04483"
        ],
        "pfam": [
          "ATPas",
          "Rad5",
          "Rec"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1066_c1_836_1117": {
      "seqid": "NMDC:1781_100325_scf_1066_c1",
      "start": 835,
      "end": 1117,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1066_c1_836_1117",
      "annotations": {
        "id": [
          "1781_100325_scf_1066_c1_836_1117"
        ],
        "product": [
          "large subunit ribosomal protein L21e"
        ],
        "cath_funfam": [
          "2.30.30.70"
        ],
        "cog": [
          "COG2139"
        ],
        "ko": [
          "KO:K02889"
        ],
        "pfam": [
          "Ribosomal_L21"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1066_c1_1155_1463": {
      "seqid": "NMDC:1781_100325_scf_1066_c1",
      "start": 1154,
      "end": 1463,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1066_c1_1155_1463",
      "annotations": {
        "id": [
          "1781_100325_scf_1066_c1_1155_1463"
        ],
        "product": [
          "DNA-directed RNA polymerase subunit F"
        ],
        "cath_funfam": [
          "1.10.287.420"
        ],
        "cog": [
          "COG1460"
        ],
        "ko": [
          "KO:K03051"
        ],
        "ec_number": [
          "EC:2.7.7.6"
        ],
        "pfam": [
          "RNA_pol_Rpb"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1067_c1": {
    "1781_100325_scf_1067_c1_28_966": {
      "seqid": "NMDC:1781_100325_scf_1067_c1",
      "start": 27,
      "end": 966,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1067_c1_28_966",
      "annotations": {
        "id": [
          "1781_100325_scf_1067_c1_28_966"
        ],
        "product": [
          "transposase"
        ],
        "cath_funfam": [
          "1.10.10.350"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "DEDD_Tnp_IS11",
          "Transposase_2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1067_c1_1197_1661": {
      "seqid": "NMDC:1781_100325_scf_1067_c1",
      "start": 1196,
      "end": 1661,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1067_c1_1197_1661",
      "annotations": {
        "id": [
          "1781_100325_scf_1067_c1_1197_1661"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "DEDD_Tnp_IS11"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1068_c1": {
    "1781_100325_scf_1068_c1_2_634": {
      "seqid": "NMDC:1781_100325_scf_1068_c1",
      "start": 1,
      "end": 634,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1068_c1_2_634",
      "annotations": {
        "id": [
          "1781_100325_scf_1068_c1_2_634"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.40.128.20"
        ],
        "pfam": [
          "PHINT_rp"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1068_c1_697_1197": {
      "seqid": "NMDC:1781_100325_scf_1068_c1",
      "start": 696,
      "end": 1197,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1068_c1_697_1197",
      "annotations": {
        "id": [
          "1781_100325_scf_1068_c1_697_1197"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1068_c1_1388_1519": {
      "seqid": "NMDC:1781_100325_scf_1068_c1",
      "start": 1387,
      "end": 1519,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1068_c1_1388_1519",
      "annotations": {
        "id": [
          "1781_100325_scf_1068_c1_1388_1519"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1069_c1": {
    "1781_100325_scf_1069_c1_3_416": {
      "seqid": "NMDC:1781_100325_scf_1069_c1",
      "start": 2,
      "end": 416,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1069_c1_3_416",
      "annotations": {
        "id": [
          "1781_100325_scf_1069_c1_3_416"
        ],
        "product": [
          "PPOX class probable F420-dependent enzyme"
        ],
        "cath_funfam": [
          "2.30.110.10"
        ],
        "cog": [
          "COG3467"
        ],
        "pfam": [
          "Pyridox_oxidas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1069_c1_541_1659": {
      "seqid": "NMDC:1781_100325_scf_1069_c1",
      "start": 540,
      "end": 1659,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1069_c1_541_1659",
      "annotations": {
        "id": [
          "1781_100325_scf_1069_c1_541_1659"
        ],
        "product": [
          "glycyl-tRNA synthetase"
        ],
        "cath_funfam": [
          "3.30.930.10"
        ],
        "cog": [
          "COG0423"
        ],
        "ko": [
          "KO:K01880"
        ],
        "ec_number": [
          "EC:6.1.1.14"
        ],
        "pfam": [
          "tRNA-synt_2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_106_c1": {
    "1781_100325_scf_106_c1_2_1687": {
      "seqid": "NMDC:1781_100325_scf_106_c1",
      "start": 1,
      "end": 1687,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_106_c1_2_1687",
      "annotations": {
        "id": [
          "1781_100325_scf_106_c1_2_1687"
        ],
        "product": [
          "thermosome"
        ],
        "cath_funfam": [
          "1.10.560.10"
        ],
        "cog": [
          "COG0459"
        ],
        "pfam": [
          "Cpn60_TCP"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_106_c1_2160_2885": {
      "seqid": "NMDC:1781_100325_scf_106_c1",
      "start": 2159,
      "end": 2885,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_106_c1_2160_2885",
      "annotations": {
        "id": [
          "1781_100325_scf_106_c1_2160_2885"
        ],
        "product": [
          "protoheme IX farnesyltransferase"
        ],
        "cog": [
          "COG0109"
        ],
        "ko": [
          "KO:K02301"
        ],
        "ec_number": [
          "EC:2.5.1.-"
        ],
        "pfam": [
          "Ubi"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_106_c1_2882_3565": {
      "seqid": "NMDC:1781_100325_scf_106_c1",
      "start": 2881,
      "end": 3565,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_106_c1_2882_3565",
      "annotations": {
        "id": [
          "1781_100325_scf_106_c1_2882_3565"
        ],
        "product": [
          "rRNA small subunit pseudouridine methyltransferase Nep1"
        ],
        "cath_funfam": [
          "3.40.1280.10"
        ],
        "cog": [
          "COG1756"
        ],
        "ko": [
          "KO:K14568"
        ],
        "ec_number": [
          "EC:2.1.1.260"
        ],
        "pfam": [
          "EMG"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_106_c1_3680_3856": {
      "seqid": "NMDC:1781_100325_scf_106_c1",
      "start": 3679,
      "end": 3856,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_106_c1_3680_3856",
      "annotations": {
        "id": [
          "1781_100325_scf_106_c1_3680_3856"
        ],
        "product": [
          "ribonuclease P protein subunit RPR2"
        ],
        "cog": [
          "COG2023"
        ],
        "ko": [
          "KO:K03540"
        ],
        "ec_number": [
          "EC:3.1.26.5"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1070_c1": {
    "1781_100325_scf_1070_c1_20_379": {
      "seqid": "NMDC:1781_100325_scf_1070_c1",
      "start": 19,
      "end": 379,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1070_c1_20_379",
      "annotations": {
        "id": [
          "1781_100325_scf_1070_c1_20_379"
        ],
        "product": [
          "thiamine-monophosphate kinase"
        ],
        "cath_funfam": [
          "3.90.650.10"
        ],
        "cog": [
          "COG0611"
        ],
        "ko": [
          "KO:K00946"
        ],
        "ec_number": [
          "EC:2.7.4.16"
        ],
        "pfam": [
          "AIRS_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1070_c1_423_1205": {
      "seqid": "NMDC:1781_100325_scf_1070_c1",
      "start": 422,
      "end": 1205,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1070_c1_423_1205",
      "annotations": {
        "id": [
          "1781_100325_scf_1070_c1_423_1205"
        ],
        "product": [
          "hydroxymethylpyrimidine/phosphomethylpyrimidine kinase"
        ],
        "cath_funfam": [
          "3.40.1190.20"
        ],
        "cog": [
          "COG0351"
        ],
        "ko": [
          "KO:K00941"
        ],
        "ec_number": [
          "EC:2.7.1.49",
          "EC:2.7.4.7"
        ],
        "pfam": [
          "H",
          "Pfk",
          "Phos_pyr_ki"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1070_c1_1262_1453": {
      "seqid": "NMDC:1781_100325_scf_1070_c1",
      "start": 1261,
      "end": 1453,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1070_c1_1262_1453",
      "annotations": {
        "id": [
          "1781_100325_scf_1070_c1_1262_1453"
        ],
        "product": [
          "large subunit ribosomal protein L28"
        ],
        "cath_funfam": [
          "2.30.170.40"
        ],
        "cog": [
          "COG0227"
        ],
        "ko": [
          "KO:K02902"
        ],
        "pfam": [
          "Ribosomal_L2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1071_c1": {
    "1781_100325_scf_1071_c1_167_637": {
      "seqid": "NMDC:1781_100325_scf_1071_c1",
      "start": 166,
      "end": 637,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1071_c1_167_637",
      "annotations": {
        "id": [
          "1781_100325_scf_1071_c1_167_637"
        ],
        "product": [
          "lipoprotein-anchoring transpeptidase ErfK/SrfK"
        ],
        "cath_funfam": [
          "2.40.440.10"
        ],
        "cog": [
          "COG1376"
        ],
        "pfam": [
          "Yku"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1071_c1_830_1387": {
      "seqid": "NMDC:1781_100325_scf_1071_c1",
      "start": 829,
      "end": 1387,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1071_c1_830_1387",
      "annotations": {
        "id": [
          "1781_100325_scf_1071_c1_830_1387"
        ],
        "product": [
          "cytochrome c biogenesis protein CcmG/thiol:disulfide interchange protein DsbE"
        ],
        "cath_funfam": [
          "3.40.30.10"
        ],
        "cog": [
          "COG1225"
        ],
        "ko": [
          "KO:K02199"
        ],
        "pfam": [
          "AhpC-TS",
          "Redoxi",
          "Thioredoxi",
          "Thioredoxin_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1071_c1_1387_1659": {
      "seqid": "NMDC:1781_100325_scf_1071_c1",
      "start": 1386,
      "end": 1659,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1071_c1_1387_1659",
      "annotations": {
        "id": [
          "1781_100325_scf_1071_c1_1387_1659"
        ],
        "product": [
          "cytochrome c-type biogenesis protein CcmH"
        ],
        "cog": [
          "COG3088"
        ],
        "ko": [
          "KO:K02200"
        ],
        "pfam": [
          "Ccm"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1072_c1": {
    "1781_100325_scf_1072_c1_3_251": {
      "seqid": "NMDC:1781_100325_scf_1072_c1",
      "start": 2,
      "end": 251,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1072_c1_3_251",
      "annotations": {
        "id": [
          "1781_100325_scf_1072_c1_3_251"
        ],
        "product": [
          "dihydroorotase"
        ],
        "cath_funfam": [
          "2.30.40.10"
        ],
        "cog": [
          "COG0044"
        ],
        "ko": [
          "KO:K01465"
        ],
        "ec_number": [
          "EC:3.5.2.3"
        ],
        "pfam": [
          "Amidohydro_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1072_c1_248_1390": {
      "seqid": "NMDC:1781_100325_scf_1072_c1",
      "start": 247,
      "end": 1390,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1072_c1_248_1390",
      "annotations": {
        "id": [
          "1781_100325_scf_1072_c1_248_1390"
        ],
        "product": [
          "carbamoyl-phosphate synthase small subunit"
        ],
        "cath_funfam": [
          "3.40.50.880",
          "3.50.30.20"
        ],
        "cog": [
          "COG0505"
        ],
        "ko": [
          "KO:K01956"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "pfam": [
          "CPSase_sm_chai",
          "GATas",
          "Peptidase_C2"
        ],
        "superfamily": [
          "SM01097"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1072_c1_1390_1656": {
      "seqid": "NMDC:1781_100325_scf_1072_c1",
      "start": 1389,
      "end": 1656,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1072_c1_1390_1656",
      "annotations": {
        "id": [
          "1781_100325_scf_1072_c1_1390_1656"
        ],
        "product": [
          "carbamoyl-phosphate synthase large subunit"
        ],
        "cath_funfam": [
          "3.40.50.20"
        ],
        "cog": [
          "COG0458"
        ],
        "ko": [
          "KO:K01955"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1073_c1": {
    "1781_100325_scf_1073_c1_292_1479": {
      "seqid": "NMDC:1781_100325_scf_1073_c1",
      "start": 291,
      "end": 1479,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1073_c1_292_1479",
      "annotations": {
        "id": [
          "1781_100325_scf_1073_c1_292_1479"
        ],
        "product": [
          "SRSO17 transposase"
        ],
        "cog": [
          "COG5659"
        ],
        "pfam": [
          "DDE_",
          "DDE_Tnp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1073_c1_1552_1656": {
      "seqid": "NMDC:1781_100325_scf_1073_c1",
      "start": 1551,
      "end": 1656,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1073_c1_1552_1656",
      "annotations": {
        "id": [
          "1781_100325_scf_1073_c1_1552_1656"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.238.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1074_c1": {
    "1781_100325_scf_1074_c1_230_1261": {
      "seqid": "NMDC:1781_100325_scf_1074_c1",
      "start": 229,
      "end": 1261,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1074_c1_230_1261",
      "annotations": {
        "id": [
          "1781_100325_scf_1074_c1_230_1261"
        ],
        "product": [
          "transposase"
        ],
        "cath_funfam": [
          "1.10.150.20"
        ],
        "cog": [
          "COG3547"
        ],
        "ko": [
          "KO:K07486"
        ],
        "pfam": [
          "DEDD_Tnp_IS11",
          "Transposase_2"
        ],
        "superfamily": [
          "SM00278"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1074_c1_1314_1655": {
      "seqid": "NMDC:1781_100325_scf_1074_c1",
      "start": 1313,
      "end": 1655,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1074_c1_1314_1655",
      "annotations": {
        "id": [
          "1781_100325_scf_1074_c1_1314_1655"
        ],
        "product": [
          "uncharacterized protein YjbI with pentapeptide repeats"
        ],
        "cath_funfam": [
          "1.10.490.10"
        ],
        "cog": [
          "COG1357"
        ],
        "pfam": [
          "Pentapeptid",
          "Pentapeptide_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1075_c1": {
    "1781_100325_scf_1075_c1_419_1153": {
      "seqid": "NMDC:1781_100325_scf_1075_c1",
      "start": 418,
      "end": 1153,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1075_c1_419_1153",
      "annotations": {
        "id": [
          "1781_100325_scf_1075_c1_419_1153"
        ],
        "product": [
          "predicted dithiol-disulfide oxidoreductase (DUF899 family)"
        ],
        "cog": [
          "COG4312"
        ],
        "pfam": [
          "AhpC-TS",
          "DUF89"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1075_c1_1214_1654": {
      "seqid": "NMDC:1781_100325_scf_1075_c1",
      "start": 1213,
      "end": 1654,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1075_c1_1214_1654",
      "annotations": {
        "id": [
          "1781_100325_scf_1075_c1_1214_1654"
        ],
        "product": [
          "predicted dithiol-disulfide oxidoreductase (DUF899 family)"
        ],
        "cog": [
          "COG4312"
        ],
        "pfam": [
          "DUF89"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1076_c1": {
    "1781_100325_scf_1076_c1_1_288": {
      "seqid": "NMDC:1781_100325_scf_1076_c1",
      "start": 0,
      "end": 288,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1076_c1_1_288",
      "annotations": {
        "id": [
          "1781_100325_scf_1076_c1_1_288"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.70.330"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1076_c1_597_830": {
      "seqid": "NMDC:1781_100325_scf_1076_c1",
      "start": 596,
      "end": 830,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1076_c1_597_830",
      "annotations": {
        "id": [
          "1781_100325_scf_1076_c1_597_830"
        ],
        "product": [
          "DNA-binding protein"
        ],
        "cath_funfam": [
          "3.30.110.20"
        ],
        "cog": [
          "COG1581"
        ],
        "ko": [
          "KO:K03622"
        ],
        "pfam": [
          "Alb"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1076_c1_885_1607": {
      "seqid": "NMDC:1781_100325_scf_1076_c1",
      "start": 884,
      "end": 1607,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1076_c1_885_1607",
      "annotations": {
        "id": [
          "1781_100325_scf_1076_c1_885_1607"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1077_c1": {
    "1781_100325_scf_1077_c1_191_1609": {
      "seqid": "NMDC:1781_100325_scf_1077_c1",
      "start": 190,
      "end": 1609,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1077_c1_191_1609",
      "annotations": {
        "id": [
          "1781_100325_scf_1077_c1_191_1609"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DDE_Tnp_1_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1078_c1": {
    "1781_100325_scf_1078_c1_2_736": {
      "seqid": "NMDC:1781_100325_scf_1078_c1",
      "start": 1,
      "end": 736,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1078_c1_2_736",
      "annotations": {
        "id": [
          "1781_100325_scf_1078_c1_2_736"
        ],
        "product": [
          "phosphate transport system substrate-binding protein"
        ],
        "cog": [
          "COG0226"
        ],
        "ko": [
          "KO:K02040"
        ],
        "pfam": [
          "PBP_like_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1078_c1_820_1653": {
      "seqid": "NMDC:1781_100325_scf_1078_c1",
      "start": 819,
      "end": 1653,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1078_c1_820_1653",
      "annotations": {
        "id": [
          "1781_100325_scf_1078_c1_820_1653"
        ],
        "product": [
          "phosphate transport system permease protein"
        ],
        "cath_funfam": [
          "1.10.3720.10"
        ],
        "cog": [
          "COG0573"
        ],
        "ko": [
          "KO:K02037"
        ],
        "pfam": [
          "BPD_transp_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1079_c1": {
    "1781_100325_scf_1079_c1_1_1401": {
      "seqid": "NMDC:1781_100325_scf_1079_c1",
      "start": 0,
      "end": 1401,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1079_c1_1_1401",
      "annotations": {
        "id": [
          "1781_100325_scf_1079_c1_1_1401"
        ],
        "product": [
          "endonuclease/exonuclease/phosphatase (EEP) superfamily protein YafD"
        ],
        "cath_funfam": [
          "3.30.910.10",
          "3.60.10.10"
        ],
        "cog": [
          "COG3021"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1079_c1_1426_1620": {
      "seqid": "NMDC:1781_100325_scf_1079_c1",
      "start": 1425,
      "end": 1620,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1079_c1_1426_1620",
      "annotations": {
        "id": [
          "1781_100325_scf_1079_c1_1426_1620"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_107_c1": {
    "1781_100325_scf_107_c1_1_1014": {
      "seqid": "NMDC:1781_100325_scf_107_c1",
      "start": 0,
      "end": 1014,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_107_c1_1_1014",
      "annotations": {
        "id": [
          "1781_100325_scf_107_c1_1_1014"
        ],
        "product": [
          "chromosome segregation protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1196"
        ],
        "ko": [
          "KO:K03529"
        ],
        "pfam": [
          "AAA_1",
          "AAA_2",
          "SMC_"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_107_c1_1139_2284": {
      "seqid": "NMDC:1781_100325_scf_107_c1",
      "start": 1138,
      "end": 2284,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_107_c1_1139_2284",
      "annotations": {
        "id": [
          "1781_100325_scf_107_c1_1139_2284"
        ],
        "product": [
          "myo-inositol-1-phosphate synthase"
        ],
        "cath_funfam": [
          "3.40.50.720"
        ],
        "cog": [
          "COG1260"
        ],
        "ko": [
          "KO:K01858"
        ],
        "ec_number": [
          "EC:5.5.1.4"
        ],
        "pfam": [
          "Inos-1-P_synt"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_107_c1_2389_3846": {
      "seqid": "NMDC:1781_100325_scf_107_c1",
      "start": 2388,
      "end": 3846,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_107_c1_2389_3846",
      "annotations": {
        "id": [
          "1781_100325_scf_107_c1_2389_3846"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "superfamily": [
          "SM00471"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1080_c1": {
    "1781_100325_scf_1080_c1_50_961": {
      "seqid": "NMDC:1781_100325_scf_1080_c1",
      "start": 49,
      "end": 961,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1080_c1_50_961",
      "annotations": {
        "id": [
          "1781_100325_scf_1080_c1_50_961"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.30.40.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1080_c1_1094_1636": {
      "seqid": "NMDC:1781_100325_scf_1080_c1",
      "start": 1093,
      "end": 1636,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1080_c1_1094_1636",
      "annotations": {
        "id": [
          "1781_100325_scf_1080_c1_1094_1636"
        ],
        "product": [
          "NAD(P)H-hydrate epimerase"
        ],
        "cath_funfam": [
          "3.40.1190.20"
        ],
        "cog": [
          "COG0063"
        ],
        "ko": [
          "KO:K17759"
        ],
        "ec_number": [
          "EC:5.1.99.6"
        ],
        "pfam": [
          "Carb_kinas",
          "H",
          "Phos_pyr_ki"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1081_c1": {
    "1781_100325_scf_1081_c1_55_510": {
      "seqid": "NMDC:1781_100325_scf_1081_c1",
      "start": 54,
      "end": 510,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1081_c1_55_510",
      "annotations": {
        "id": [
          "1781_100325_scf_1081_c1_55_510"
        ],
        "product": [
          "agmatinase"
        ],
        "cath_funfam": [
          "3.40.800.10"
        ],
        "cog": [
          "COG0010"
        ],
        "ko": [
          "KO:K01480"
        ],
        "ec_number": [
          "EC:3.5.3.11"
        ],
        "pfam": [
          "Arginas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1081_c1_507_896": {
      "seqid": "NMDC:1781_100325_scf_1081_c1",
      "start": 506,
      "end": 896,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1081_c1_507_896",
      "annotations": {
        "id": [
          "1781_100325_scf_1081_c1_507_896"
        ],
        "product": [
          "urease subunit gamma"
        ],
        "cath_funfam": [
          "3.30.280.10"
        ],
        "cog": [
          "COG0831"
        ],
        "ko": [
          "KO:K01430"
        ],
        "ec_number": [
          "EC:3.5.1.5"
        ],
        "pfam": [
          "Urease_gamm"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1081_c1_913_1650": {
      "seqid": "NMDC:1781_100325_scf_1081_c1",
      "start": 912,
      "end": 1650,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1081_c1_913_1650",
      "annotations": {
        "id": [
          "1781_100325_scf_1081_c1_913_1650"
        ],
        "product": [
          "ABC-type nickel/cobalt efflux system permease component RcnA"
        ],
        "cog": [
          "COG2215"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1082_c1": {
    "1781_100325_scf_1082_c1_3_479": {
      "seqid": "NMDC:1781_100325_scf_1082_c1",
      "start": 2,
      "end": 479,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1082_c1_3_479",
      "annotations": {
        "id": [
          "1781_100325_scf_1082_c1_3_479"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG1331"
        ],
        "ko": [
          "KO:K06888"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1082_c1_492_1598": {
      "seqid": "NMDC:1781_100325_scf_1082_c1",
      "start": 491,
      "end": 1598,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1082_c1_492_1598",
      "annotations": {
        "id": [
          "1781_100325_scf_1082_c1_492_1598"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1083_c1": {
    "1781_100325_scf_1083_c1_1_477": {
      "seqid": "NMDC:1781_100325_scf_1083_c1",
      "start": 0,
      "end": 477,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1083_c1_1_477",
      "annotations": {
        "id": [
          "1781_100325_scf_1083_c1_1_477"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1083_c1_785_1642": {
      "seqid": "NMDC:1781_100325_scf_1083_c1",
      "start": 784,
      "end": 1642,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1083_c1_785_1642",
      "annotations": {
        "id": [
          "1781_100325_scf_1083_c1_785_1642"
        ],
        "product": [
          "5-methyltetrahydrofolate--homocysteine methyltransferase"
        ],
        "cath_funfam": [
          "3.10.196.10"
        ],
        "cog": [
          "COG1410"
        ],
        "ko": [
          "KO:K00548"
        ],
        "ec_number": [
          "EC:2.1.1.13"
        ],
        "pfam": [
          "Met_synt_B1"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1084_c1": {
    "1781_100325_scf_1084_c1_218_415": {
      "seqid": "NMDC:1781_100325_scf_1084_c1",
      "start": 217,
      "end": 415,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1084_c1_218_415",
      "annotations": {
        "id": [
          "1781_100325_scf_1084_c1_218_415"
        ],
        "product": [
          "antitoxin component of MazEF toxin-antitoxin module"
        ],
        "cog": [
          "COG2336"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1084_c1_412_588": {
      "seqid": "NMDC:1781_100325_scf_1084_c1",
      "start": 411,
      "end": 588,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1084_c1_412_588",
      "annotations": {
        "id": [
          "1781_100325_scf_1084_c1_412_588"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1084_c1_607_1608": {
      "seqid": "NMDC:1781_100325_scf_1084_c1",
      "start": 606,
      "end": 1608,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1084_c1_607_1608",
      "annotations": {
        "id": [
          "1781_100325_scf_1084_c1_607_1608"
        ],
        "product": [
          "acetoin utilization protein AcuC"
        ],
        "cath_funfam": [
          "3.40.800.20"
        ],
        "cog": [
          "COG0123"
        ],
        "ko": [
          "KO:K04768"
        ],
        "pfam": [
          "Hist_deacety"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1085_c1": {
    "1781_100325_scf_1085_c1_1_312": {
      "seqid": "NMDC:1781_100325_scf_1085_c1",
      "start": 0,
      "end": 312,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1085_c1_1_312",
      "annotations": {
        "id": [
          "1781_100325_scf_1085_c1_1_312"
        ],
        "product": [
          "signal-transduction protein with cAMP-binding",
          " CBS",
          " and nucleotidyltransferase domain"
        ],
        "cath_funfam": [
          "3.10.580.10"
        ],
        "cog": [
          "COG2905"
        ],
        "pfam": [
          "CB"
        ],
        "superfamily": [
          "SM00116"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1085_c1_496_930": {
      "seqid": "NMDC:1781_100325_scf_1085_c1",
      "start": 495,
      "end": 930,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1085_c1_496_930",
      "annotations": {
        "id": [
          "1781_100325_scf_1085_c1_496_930"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.200.20"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1085_c1_1377_1505": {
      "seqid": "NMDC:1781_100325_scf_1085_c1",
      "start": 1376,
      "end": 1505,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1085_c1_1377_1505",
      "annotations": {
        "id": [
          "1781_100325_scf_1085_c1_1377_1505"
        ],
        "product": [
          "ferredoxin-thioredoxin reductase catalytic subunit"
        ],
        "cog": [
          "COG4802"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1086_c1": {
    "1781_100325_scf_1086_c1_1_621": {
      "seqid": "NMDC:1781_100325_scf_1086_c1",
      "start": 0,
      "end": 621,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1086_c1_1_621",
      "annotations": {
        "id": [
          "1781_100325_scf_1086_c1_1_621"
        ],
        "product": [
          "Cu/Ag efflux pump CusA"
        ],
        "cath_funfam": [
          "3.30.70.1430"
        ],
        "cog": [
          "COG3696"
        ],
        "pfam": [
          "ACR_tra"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1086_c1_644_1093": {
      "seqid": "NMDC:1781_100325_scf_1086_c1",
      "start": 643,
      "end": 1093,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1086_c1_644_1093",
      "annotations": {
        "id": [
          "1781_100325_scf_1086_c1_644_1093"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1086_c1_1080_1646": {
      "seqid": "NMDC:1781_100325_scf_1086_c1",
      "start": 1079,
      "end": 1646,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1086_c1_1080_1646",
      "annotations": {
        "id": [
          "1781_100325_scf_1086_c1_1080_1646"
        ],
        "product": [
          "Cu/Ag efflux pump CusA"
        ],
        "cath_funfam": [
          "1.20.1640.10"
        ],
        "cog": [
          "COG3696"
        ],
        "pfam": [
          "ACR_tra",
          "SecD_Sec"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1087_c1": {
    "1781_100325_scf_1087_c1_42_1337": {
      "seqid": "NMDC:1781_100325_scf_1087_c1",
      "start": 41,
      "end": 1337,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1087_c1_42_1337",
      "annotations": {
        "id": [
          "1781_100325_scf_1087_c1_42_1337"
        ],
        "product": [
          "dihydrofolate synthase/folylpolyglutamate synthase"
        ],
        "cath_funfam": [
          "3.40.1190.10",
          "3.90.190.20"
        ],
        "cog": [
          "COG0285"
        ],
        "ko": [
          "KO:K11754"
        ],
        "ec_number": [
          "EC:6.3.2.12",
          "EC:6.3.2.17"
        ],
        "pfam": [
          "Mur_ligase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1087_c1_1392_1646": {
      "seqid": "NMDC:1781_100325_scf_1087_c1",
      "start": 1391,
      "end": 1646,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1087_c1_1392_1646",
      "annotations": {
        "id": [
          "1781_100325_scf_1087_c1_1392_1646"
        ],
        "product": [
          "nucleoside-diphosphate kinase"
        ],
        "cath_funfam": [
          "3.30.70.141"
        ],
        "cog": [
          "COG0105"
        ],
        "ko": [
          "KO:K00940"
        ],
        "ec_number": [
          "EC:2.7.4.6"
        ],
        "pfam": [
          "ND"
        ],
        "superfamily": [
          "SM00562"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1088_c1": {
    "1781_100325_scf_1088_c1_1_420": {
      "seqid": "NMDC:1781_100325_scf_1088_c1",
      "start": 0,
      "end": 420,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1088_c1_1_420",
      "annotations": {
        "id": [
          "1781_100325_scf_1088_c1_1_420"
        ],
        "product": [
          "DNA replication protein DnaC"
        ],
        "cog": [
          "COG1484"
        ],
        "pfam": [
          "IstB_IS2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1088_c1_420_1646": {
      "seqid": "NMDC:1781_100325_scf_1088_c1",
      "start": 419,
      "end": 1646,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1088_c1_420_1646",
      "annotations": {
        "id": [
          "1781_100325_scf_1088_c1_420_1646"
        ],
        "product": [
          "transposase"
        ],
        "cath_funfam": [
          "3.30.420.10"
        ],
        "cog": [
          "COG4584"
        ],
        "pfam": [
          "rv"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1089_c1": {
    "1781_100325_scf_1089_c1_1_1224": {
      "seqid": "NMDC:1781_100325_scf_1089_c1",
      "start": 0,
      "end": 1224,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1089_c1_1_1224",
      "annotations": {
        "id": [
          "1781_100325_scf_1089_c1_1_1224"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DDE_Tnp_1_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1089_c1_1437_1643": {
      "seqid": "NMDC:1781_100325_scf_1089_c1",
      "start": 1436,
      "end": 1643,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1089_c1_1437_1643",
      "annotations": {
        "id": [
          "1781_100325_scf_1089_c1_1437_1643"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_108_c1": {
    "1781_100325_scf_108_c1_28_960": {
      "seqid": "NMDC:1781_100325_scf_108_c1",
      "start": 27,
      "end": 960,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_108_c1_28_960",
      "annotations": {
        "id": [
          "1781_100325_scf_108_c1_28_960"
        ],
        "product": [
          "hypothetical protein"
        ],
        "superfamily": [
          "SM00710"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_108_c1_971_1459": {
      "seqid": "NMDC:1781_100325_scf_108_c1",
      "start": 970,
      "end": 1459,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_108_c1_971_1459",
      "annotations": {
        "id": [
          "1781_100325_scf_108_c1_971_1459"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_108_c1_2197_2553": {
      "seqid": "NMDC:1781_100325_scf_108_c1",
      "start": 2196,
      "end": 2553,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_108_c1_2197_2553",
      "annotations": {
        "id": [
          "1781_100325_scf_108_c1_2197_2553"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_108_c1_2751_2939": {
      "seqid": "NMDC:1781_100325_scf_108_c1",
      "start": 2750,
      "end": 2939,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_108_c1_2751_2939",
      "annotations": {
        "id": [
          "1781_100325_scf_108_c1_2751_2939"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_108_c1_2974_3351": {
      "seqid": "NMDC:1781_100325_scf_108_c1",
      "start": 2973,
      "end": 3351,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_108_c1_2974_3351",
      "annotations": {
        "id": [
          "1781_100325_scf_108_c1_2974_3351"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG5015"
        ],
        "ko": [
          "KO:K07006"
        ],
        "pfam": [
          "Pyridox_oxidas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_108_c1_3528_3836": {
      "seqid": "NMDC:1781_100325_scf_108_c1",
      "start": 3527,
      "end": 3836,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_108_c1_3528_3836",
      "annotations": {
        "id": [
          "1781_100325_scf_108_c1_3528_3836"
        ],
        "product": [
          "DNA-binding HxlR family transcriptional regulator"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG1733"
        ],
        "pfam": [
          "Hxl"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1090_c1": {
    "1781_100325_scf_1090_c1_1_234": {
      "seqid": "NMDC:1781_100325_scf_1090_c1",
      "start": 0,
      "end": 234,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1090_c1_1_234",
      "annotations": {
        "id": [
          "1781_100325_scf_1090_c1_1_234"
        ],
        "product": [
          "uncharacterized protein with predicted RNA binding PUA domain"
        ],
        "cath_funfam": [
          "3.10.450.90"
        ],
        "cog": [
          "COG1370"
        ],
        "ko": [
          "KO:K07398"
        ],
        "pfam": [
          "TGT_C"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1090_c1_488_862": {
      "seqid": "NMDC:1781_100325_scf_1090_c1",
      "start": 487,
      "end": 862,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1090_c1_488_862",
      "annotations": {
        "id": [
          "1781_100325_scf_1090_c1_488_862"
        ],
        "product": [
          "putative transcription factor"
        ],
        "cath_funfam": [
          "1.10.260.40"
        ],
        "cog": [
          "COG1813"
        ],
        "ko": [
          "KO:K03627"
        ],
        "superfamily": [
          "SM00530"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1090_c1_855_1643": {
      "seqid": "NMDC:1781_100325_scf_1090_c1",
      "start": 854,
      "end": 1643,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1090_c1_855_1643",
      "annotations": {
        "id": [
          "1781_100325_scf_1090_c1_855_1643"
        ],
        "product": [
          "GTP-binding protein HflX"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG2262"
        ],
        "ko": [
          "KO:K03665"
        ],
        "pfam": [
          "FeoB_",
          "GTP-bdg_",
          "MMR_HSR"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1091_c1": {
    "1781_100325_scf_1091_c1_152_880": {
      "seqid": "NMDC:1781_100325_scf_1091_c1",
      "start": 151,
      "end": 880,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1091_c1_152_880",
      "annotations": {
        "id": [
          "1781_100325_scf_1091_c1_152_880"
        ],
        "product": [
          "chlorite dismutase"
        ],
        "cath_funfam": [
          "3.30.70.1100"
        ],
        "cog": [
          "COG3253"
        ],
        "ko": [
          "KO:K09162"
        ],
        "ec_number": [
          "EC:1.13.11.49"
        ],
        "pfam": [
          "Chlor_dismutas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1091_c1_883_1482": {
      "seqid": "NMDC:1781_100325_scf_1091_c1",
      "start": 882,
      "end": 1482,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1091_c1_883_1482",
      "annotations": {
        "id": [
          "1781_100325_scf_1091_c1_883_1482"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG4293"
        ],
        "pfam": [
          "DUF180"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1091_c1_1473_1643": {
      "seqid": "NMDC:1781_100325_scf_1091_c1",
      "start": 1472,
      "end": 1643,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1091_c1_1473_1643",
      "annotations": {
        "id": [
          "1781_100325_scf_1091_c1_1473_1643"
        ],
        "product": [
          "aryl-alcohol dehydrogenase-like predicted oxidoreductase"
        ],
        "cath_funfam": [
          "3.20.20.100"
        ],
        "cog": [
          "COG0667"
        ],
        "pfam": [
          "Aldo_ket_re"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1092_c1": {
    "1781_100325_scf_1092_c1_1_1509": {
      "seqid": "NMDC:1781_100325_scf_1092_c1",
      "start": 0,
      "end": 1509,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1092_c1_1_1509",
      "annotations": {
        "id": [
          "1781_100325_scf_1092_c1_1_1509"
        ],
        "product": [
          "glucose-6-phosphate 1-dehydrogenase"
        ],
        "cath_funfam": [
          "3.30.360.10"
        ],
        "cog": [
          "COG0364"
        ],
        "ko": [
          "KO:K00036"
        ],
        "ec_number": [
          "EC:1.1.1.363",
          "EC:1.1.1.49"
        ],
        "pfam": [
          "G6PD_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1092_c1_1506_1643": {
      "seqid": "NMDC:1781_100325_scf_1092_c1",
      "start": 1505,
      "end": 1643,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1092_c1_1506_1643",
      "annotations": {
        "id": [
          "1781_100325_scf_1092_c1_1506_1643"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1093_c1": {
    "1781_100325_scf_1093_c1_3_539": {
      "seqid": "NMDC:1781_100325_scf_1093_c1",
      "start": 2,
      "end": 539,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1093_c1_3_539",
      "annotations": {
        "id": [
          "1781_100325_scf_1093_c1_3_539"
        ],
        "product": [
          "S-adenosylmethionine synthetase"
        ],
        "cath_funfam": [
          "3.30.300.10"
        ],
        "cog": [
          "COG0192"
        ],
        "ko": [
          "KO:K00789"
        ],
        "ec_number": [
          "EC:2.5.1.6"
        ],
        "pfam": [
          "S-AdoMet_synt_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1093_c1_576_1442": {
      "seqid": "NMDC:1781_100325_scf_1093_c1",
      "start": 575,
      "end": 1442,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1093_c1_576_1442",
      "annotations": {
        "id": [
          "1781_100325_scf_1093_c1_576_1442"
        ],
        "product": [
          "RIO kinase 2"
        ],
        "cath_funfam": [
          "1.10.10.10",
          "1.10.510.10",
          "3.30.200.20"
        ],
        "cog": [
          "COG0478"
        ],
        "ko": [
          "KO:K07179"
        ],
        "ec_number": [
          "EC:2.7.11.1"
        ],
        "pfam": [
          "RIO",
          "Rio2_"
        ],
        "superfamily": [
          "SM00090"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1093_c1_1504_1644": {
      "seqid": "NMDC:1781_100325_scf_1093_c1",
      "start": 1503,
      "end": 1644,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1093_c1_1504_1644",
      "annotations": {
        "id": [
          "1781_100325_scf_1093_c1_1504_1644"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1094_c1": {
    "1781_100325_scf_1094_c1_1_1386": {
      "seqid": "NMDC:1781_100325_scf_1094_c1",
      "start": 0,
      "end": 1386,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1094_c1_1_1386",
      "annotations": {
        "id": [
          "1781_100325_scf_1094_c1_1_1386"
        ],
        "product": [
          "DNA topoisomerase-1"
        ],
        "cath_funfam": [
          "1.10.10.10",
          "1.10.460.10",
          "3.30.65.10"
        ],
        "cog": [
          "COG0550"
        ],
        "ko": [
          "KO:K03168"
        ],
        "ec_number": [
          "EC:5.99.1.2"
        ],
        "pfam": [
          "Topoisom_ba"
        ],
        "superfamily": [
          "SM00437"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1094_c1_1353_1637": {
      "seqid": "NMDC:1781_100325_scf_1094_c1",
      "start": 1352,
      "end": 1637,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1094_c1_1353_1637",
      "annotations": {
        "id": [
          "1781_100325_scf_1094_c1_1353_1637"
        ],
        "product": [
          "predicted amidohydrolase"
        ],
        "cath_funfam": [
          "3.60.110.10"
        ],
        "cog": [
          "COG0388"
        ],
        "pfam": [
          "CN_hydrolas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1095_c1": {
    "1781_100325_scf_1095_c1_110_493": {
      "seqid": "NMDC:1781_100325_scf_1095_c1",
      "start": 109,
      "end": 493,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1095_c1_110_493",
      "annotations": {
        "id": [
          "1781_100325_scf_1095_c1_110_493"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.40.50.40"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1095_c1_828_1112": {
      "seqid": "NMDC:1781_100325_scf_1095_c1",
      "start": 827,
      "end": 1112,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1095_c1_828_1112",
      "annotations": {
        "id": [
          "1781_100325_scf_1095_c1_828_1112"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.25.40.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1095_c1_1272_1457": {
      "seqid": "NMDC:1781_100325_scf_1095_c1",
      "start": 1271,
      "end": 1457,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1095_c1_1272_1457",
      "annotations": {
        "id": [
          "1781_100325_scf_1095_c1_1272_1457"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.40.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1096_c1": {
    "1781_100325_scf_1096_c1_547_873": {
      "seqid": "NMDC:1781_100325_scf_1096_c1",
      "start": 546,
      "end": 873,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1096_c1_547_873",
      "annotations": {
        "id": [
          "1781_100325_scf_1096_c1_547_873"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.60.110.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1096_c1_870_1631": {
      "seqid": "NMDC:1781_100325_scf_1096_c1",
      "start": 869,
      "end": 1631,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1096_c1_870_1631",
      "annotations": {
        "id": [
          "1781_100325_scf_1096_c1_870_1631"
        ],
        "product": [
          "amidophosphoribosyltransferase"
        ],
        "cath_funfam": [
          "3.40.50.2020"
        ],
        "cog": [
          "COG0034"
        ],
        "ko": [
          "KO:K00764"
        ],
        "ec_number": [
          "EC:2.4.2.14"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1097_c1": {
    "1781_100325_scf_1097_c1_3_245": {
      "seqid": "NMDC:1781_100325_scf_1097_c1",
      "start": 2,
      "end": 245,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1097_c1_3_245",
      "annotations": {
        "id": [
          "1781_100325_scf_1097_c1_3_245"
        ],
        "product": [
          "carbamoyl-phosphate synthase small subunit"
        ],
        "cath_funfam": [
          "3.50.30.20"
        ],
        "cog": [
          "COG0505"
        ],
        "ko": [
          "KO:K01956"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "pfam": [
          "CPSase_sm_chai"
        ],
        "superfamily": [
          "SM01097"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1097_c1_390_1577": {
      "seqid": "NMDC:1781_100325_scf_1097_c1",
      "start": 389,
      "end": 1577,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1097_c1_390_1577",
      "annotations": {
        "id": [
          "1781_100325_scf_1097_c1_390_1577"
        ],
        "product": [
          "SpoVK/Ycf46/Vps4 family AAA+-type ATPase"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0464"
        ],
        "pfam": [
          "AA",
          "AAA_",
          "Vps4_"
        ],
        "superfamily": [
          "SM00382",
          "SM00745"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1098_c1": {
    "1781_100325_scf_1098_c1_51_467": {
      "seqid": "NMDC:1781_100325_scf_1098_c1",
      "start": 50,
      "end": 467,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1098_c1_51_467",
      "annotations": {
        "id": [
          "1781_100325_scf_1098_c1_51_467"
        ],
        "product": [
          "deazaflavin-dependent oxidoreductase (nitroreductase family)"
        ],
        "pfam": [
          "DUF38"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1098_c1_526_1116": {
      "seqid": "NMDC:1781_100325_scf_1098_c1",
      "start": 525,
      "end": 1116,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1098_c1_526_1116",
      "annotations": {
        "id": [
          "1781_100325_scf_1098_c1_526_1116"
        ],
        "product": [
          "response regulator NasT"
        ],
        "cath_funfam": [
          "1.10.10.10",
          "3.40.50.2300"
        ],
        "cog": [
          "COG3707"
        ],
        "ko": [
          "KO:K07183"
        ],
        "pfam": [
          "ANTA"
        ],
        "superfamily": [
          "SM01012"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1098_c1_1346_1636": {
      "seqid": "NMDC:1781_100325_scf_1098_c1",
      "start": 1345,
      "end": 1636,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1098_c1_1346_1636",
      "annotations": {
        "id": [
          "1781_100325_scf_1098_c1_1346_1636"
        ],
        "product": [
          "anti-anti-sigma factor"
        ],
        "cath_funfam": [
          "3.30.750.24"
        ],
        "cog": [
          "COG1366"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1099_c1": {
    "1781_100325_scf_1099_c1_26_751": {
      "seqid": "NMDC:1781_100325_scf_1099_c1",
      "start": 25,
      "end": 751,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1099_c1_26_751",
      "annotations": {
        "id": [
          "1781_100325_scf_1099_c1_26_751"
        ],
        "product": [
          "[lysine-biosynthesis-protein LysW]--L-2-aminoadipate ligase"
        ],
        "cath_funfam": [
          "3.30.1490.20"
        ],
        "cog": [
          "COG0189"
        ],
        "ko": [
          "KO:K05827"
        ],
        "ec_number": [
          "EC:6.3.2.43"
        ],
        "pfam": [
          "ATP-grasp_",
          "CPSase_L_D",
          "GSH-S_AT",
          "Rim"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1099_c1_755_1642": {
      "seqid": "NMDC:1781_100325_scf_1099_c1",
      "start": 754,
      "end": 1642,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1099_c1_755_1642",
      "annotations": {
        "id": [
          "1781_100325_scf_1099_c1_755_1642"
        ],
        "product": [
          "LysW-gamma-L-lysine carboxypeptidase"
        ],
        "cath_funfam": [
          "3.40.630.10"
        ],
        "cog": [
          "COG0624"
        ],
        "ko": [
          "KO:K05831"
        ],
        "pfam": [
          "M20_dime",
          "Peptidase_M2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_109_c1": {
    "1781_100325_scf_109_c1_233_1810": {
      "seqid": "NMDC:1781_100325_scf_109_c1",
      "start": 232,
      "end": 1810,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_109_c1_233_1810",
      "annotations": {
        "id": [
          "1781_100325_scf_109_c1_233_1810"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DDE_Tnp_1_",
          "DUF77"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_109_c1_2020_3648": {
      "seqid": "NMDC:1781_100325_scf_109_c1",
      "start": 2019,
      "end": 3648,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_109_c1_2020_3648",
      "annotations": {
        "id": [
          "1781_100325_scf_109_c1_2020_3648"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_109_c1_3708_3803": {
      "seqid": "NMDC:1781_100325_scf_109_c1",
      "start": 3707,
      "end": 3803,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_109_c1_3708_3803",
      "annotations": {
        "id": [
          "1781_100325_scf_109_c1_3708_3803"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_10_c1": {
    "1781_100325_scf_10_c1_1_366": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 0,
      "end": 366,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_1_366",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_1_366"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_319_1026": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 318,
      "end": 1026,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_319_1026",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_319_1026"
        ],
        "product": [
          "Holliday junction DNA helicase RuvB"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0714"
        ],
        "ko": [
          "KO:K03551"
        ],
        "ec_number": [
          "EC:3.6.4.12"
        ],
        "pfam": [
          "AA",
          "MC",
          "RuvB_"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_1049_1381": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 1048,
      "end": 1381,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_1049_1381",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_1049_1381"
        ],
        "product": [
          "uncharacterized membrane protein (Fun14 family)"
        ],
        "cog": [
          "COG2383"
        ],
        "pfam": [
          "FUN1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_1528_1668": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 1527,
      "end": 1668,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_1528_1668",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_1528_1668"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_1910_2161": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 1909,
      "end": 2161,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_1910_2161",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_1910_2161"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_2270_2791": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 2269,
      "end": 2791,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_2270_2791",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_2270_2791"
        ],
        "product": [
          "nucleoside-triphosphatase"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1618"
        ],
        "ko": [
          "KO:K06928"
        ],
        "ec_number": [
          "EC:3.6.1.15"
        ],
        "pfam": [
          "DUF247",
          "NTPase_"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_2877_3134": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 2876,
      "end": 3134,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_2877_3134",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_2877_3134"
        ],
        "product": [
          "uncharacterized protein YecE (DUF72 family)"
        ],
        "cog": [
          "COG1801"
        ],
        "pfam": [
          "DUF7"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_3141_5390": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 3140,
      "end": 5390,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_3141_5390",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_3141_5390"
        ],
        "product": [
          "DNA polymerase-2"
        ],
        "cath_funfam": [
          "3.30.420.10",
          "3.50.50.60",
          "3.90.1600.10"
        ],
        "cog": [
          "COG0417"
        ],
        "ko": [
          "KO:K02336"
        ],
        "ec_number": [
          "EC:2.7.7.7"
        ],
        "pfam": [
          "DNA_pol_",
          "DNA_pol_B_exo"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_5416_5673": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 5415,
      "end": 5673,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_5416_5673",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_5416_5673"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_5690_5923": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 5689,
      "end": 5923,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_5690_5923",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_5690_5923"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.238.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_5964_6761": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 5963,
      "end": 6761,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_5964_6761",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_5964_6761"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "pfam": [
          "Rad5"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_10_c1_6861_7706": {
      "seqid": "NMDC:1781_100325_scf_10_c1",
      "start": 6860,
      "end": 7706,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_10_c1_6861_7706",
      "annotations": {
        "id": [
          "1781_100325_scf_10_c1_6861_7706"
        ],
        "product": [
          "uncharacterized protein YecE (DUF72 family)"
        ],
        "cath_funfam": [
          "3.20.20.410"
        ],
        "cog": [
          "COG1801"
        ],
        "pfam": [
          "DUF7"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1100_c1": {
    "1781_100325_scf_1100_c1_253_555": {
      "seqid": "NMDC:1781_100325_scf_1100_c1",
      "start": 252,
      "end": 555,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1100_c1_253_555",
      "annotations": {
        "id": [
          "1781_100325_scf_1100_c1_253_555"
        ],
        "product": [
          "DNA-binding FrmR family transcriptional regulator"
        ],
        "cog": [
          "COG1937"
        ],
        "pfam": [
          "Trns_repr_meta"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1100_c1_559_1641": {
      "seqid": "NMDC:1781_100325_scf_1100_c1",
      "start": 558,
      "end": 1641,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1100_c1_559_1641",
      "annotations": {
        "id": [
          "1781_100325_scf_1100_c1_559_1641"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG0701"
        ],
        "ko": [
          "KO:K07089"
        ],
        "pfam": [
          "ArsP_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1101_c1": {
    "1781_100325_scf_1101_c1_1_300": {
      "seqid": "NMDC:1781_100325_scf_1101_c1",
      "start": 0,
      "end": 300,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1101_c1_1_300",
      "annotations": {
        "id": [
          "1781_100325_scf_1101_c1_1_300"
        ],
        "product": [
          "carbamoyl-phosphate synthase large subunit"
        ],
        "cath_funfam": [
          "3.40.50.20"
        ],
        "cog": [
          "COG0458"
        ],
        "ko": [
          "KO:K01955"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1101_c1_293_1468": {
      "seqid": "NMDC:1781_100325_scf_1101_c1",
      "start": 292,
      "end": 1468,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1101_c1_293_1468",
      "annotations": {
        "id": [
          "1781_100325_scf_1101_c1_293_1468"
        ],
        "product": [
          "carbamoyl-phosphate synthase small subunit"
        ],
        "cath_funfam": [
          "3.40.50.880",
          "3.50.30.20"
        ],
        "cog": [
          "COG0505"
        ],
        "ko": [
          "KO:K01956"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "pfam": [
          "CPSase_sm_chai",
          "GATas",
          "Peptidase_C2"
        ],
        "superfamily": [
          "SM01097"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1101_c1_1491_1640": {
      "seqid": "NMDC:1781_100325_scf_1101_c1",
      "start": 1490,
      "end": 1640,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1101_c1_1491_1640",
      "annotations": {
        "id": [
          "1781_100325_scf_1101_c1_1491_1640"
        ],
        "product": [
          "dihydroorotase-like cyclic amidohydrolase"
        ],
        "cath_funfam": [
          "2.30.40.10"
        ],
        "cog": [
          "COG0044"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1102_c1": {
    "1781_100325_scf_1102_c1_3_593": {
      "seqid": "NMDC:1781_100325_scf_1102_c1",
      "start": 2,
      "end": 593,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1102_c1_3_593",
      "annotations": {
        "id": [
          "1781_100325_scf_1102_c1_3_593"
        ],
        "product": [
          "integrase/recombinase XerD"
        ],
        "cath_funfam": [
          "1.10.443.10"
        ],
        "cog": [
          "COG4974"
        ],
        "ko": [
          "KO:K04763"
        ],
        "pfam": [
          "Phage_integras"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1102_c1_590_946": {
      "seqid": "NMDC:1781_100325_scf_1102_c1",
      "start": 589,
      "end": 946,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1102_c1_590_946",
      "annotations": {
        "id": [
          "1781_100325_scf_1102_c1_590_946"
        ],
        "product": [
          "DnaK suppressor protein"
        ],
        "cog": [
          "COG1734"
        ],
        "ko": [
          "KO:K06204"
        ],
        "pfam": [
          "zf-dskA_tra"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1102_c1_999_1640": {
      "seqid": "NMDC:1781_100325_scf_1102_c1",
      "start": 998,
      "end": 1640,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1102_c1_999_1640",
      "annotations": {
        "id": [
          "1781_100325_scf_1102_c1_999_1640"
        ],
        "product": [
          "phosphopentomutase"
        ],
        "cath_funfam": [
          "3.30.70.1250"
        ],
        "cog": [
          "COG1015"
        ],
        "ko": [
          "KO:K01839"
        ],
        "ec_number": [
          "EC:5.4.2.7"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1103_c1": {
    "1781_100325_scf_1103_c1_95_1624": {
      "seqid": "NMDC:1781_100325_scf_1103_c1",
      "start": 94,
      "end": 1624,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1103_c1_95_1624",
      "annotations": {
        "id": [
          "1781_100325_scf_1103_c1_95_1624"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DUF199"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1104_c1": {
    "1781_100325_scf_1104_c1_1_1251": {
      "seqid": "NMDC:1781_100325_scf_1104_c1",
      "start": 0,
      "end": 1251,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1104_c1_1_1251",
      "annotations": {
        "id": [
          "1781_100325_scf_1104_c1_1_1251"
        ],
        "product": [
          "tryptophan synthase beta chain"
        ],
        "cath_funfam": [
          "3.40.50.1100"
        ],
        "cog": [
          "COG1350"
        ],
        "ko": [
          "KO:K06001"
        ],
        "ec_number": [
          "EC:4.2.1.20"
        ],
        "pfam": [
          "PAL"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1104_c1_1307_1639": {
      "seqid": "NMDC:1781_100325_scf_1104_c1",
      "start": 1306,
      "end": 1639,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1104_c1_1307_1639",
      "annotations": {
        "id": [
          "1781_100325_scf_1104_c1_1307_1639"
        ],
        "product": [
          "kynureninase"
        ],
        "cath_funfam": [
          "3.90.1150.10"
        ],
        "cog": [
          "COG3844"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1105_c1": {
    "1781_100325_scf_1105_c1_2_628": {
      "seqid": "NMDC:1781_100325_scf_1105_c1",
      "start": 1,
      "end": 628,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1105_c1_2_628",
      "annotations": {
        "id": [
          "1781_100325_scf_1105_c1_2_628"
        ],
        "product": [
          "isopenicillin-N N-acyltransferase-like protein"
        ],
        "ko": [
          "KO:K19200"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1105_c1_625_1635": {
      "seqid": "NMDC:1781_100325_scf_1105_c1",
      "start": 624,
      "end": 1635,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1105_c1_625_1635",
      "annotations": {
        "id": [
          "1781_100325_scf_1105_c1_625_1635"
        ],
        "product": [
          "acetylornithine deacetylase/succinyl-diaminopimelate desuccinylase-like protein"
        ],
        "cath_funfam": [
          "3.30.70.360"
        ],
        "cog": [
          "COG0624"
        ],
        "pfam": [
          "M20_dime",
          "Peptidase_M2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1106_c1": {
    "1781_100325_scf_1106_c1_2_181": {
      "seqid": "NMDC:1781_100325_scf_1106_c1",
      "start": 1,
      "end": 181,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1106_c1_2_181",
      "annotations": {
        "id": [
          "1781_100325_scf_1106_c1_2_181"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1106_c1_165_704": {
      "seqid": "NMDC:1781_100325_scf_1106_c1",
      "start": 164,
      "end": 704,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1106_c1_165_704",
      "annotations": {
        "id": [
          "1781_100325_scf_1106_c1_165_704"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1106_c1_789_1634": {
      "seqid": "NMDC:1781_100325_scf_1106_c1",
      "start": 788,
      "end": 1634,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1106_c1_789_1634",
      "annotations": {
        "id": [
          "1781_100325_scf_1106_c1_789_1634"
        ],
        "product": [
          "predicted PurR-regulated permease PerM"
        ],
        "cog": [
          "COG0628"
        ],
        "pfam": [
          "AI-2E_transpor"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1107_c1": {
    "1781_100325_scf_1107_c1_3_248": {
      "seqid": "NMDC:1781_100325_scf_1107_c1",
      "start": 2,
      "end": 248,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1107_c1_3_248",
      "annotations": {
        "id": [
          "1781_100325_scf_1107_c1_3_248"
        ],
        "product": [
          "DNA-binding transcriptional MerR regulator"
        ],
        "cath_funfam": [
          "1.10.1660.10"
        ],
        "cog": [
          "COG0789"
        ],
        "pfam": [
          "MerR_"
        ],
        "superfamily": [
          "SM00422"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1107_c1_395_907": {
      "seqid": "NMDC:1781_100325_scf_1107_c1",
      "start": 394,
      "end": 907,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1107_c1_395_907",
      "annotations": {
        "id": [
          "1781_100325_scf_1107_c1_395_907"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG1259"
        ],
        "ko": [
          "KO:K08999"
        ],
        "pfam": [
          "DNase-RNas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1107_c1_983_1546": {
      "seqid": "NMDC:1781_100325_scf_1107_c1",
      "start": 982,
      "end": 1546,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1107_c1_983_1546",
      "annotations": {
        "id": [
          "1781_100325_scf_1107_c1_983_1546"
        ],
        "product": [
          "hypoxanthine phosphoribosyltransferase"
        ],
        "cath_funfam": [
          "3.40.50.2020"
        ],
        "cog": [
          "COG0634"
        ],
        "ko": [
          "KO:K00760"
        ],
        "ec_number": [
          "EC:2.4.2.8"
        ],
        "pfam": [
          "Pribosyltra"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1108_c1": {
    "1781_100325_scf_1108_c1_229_1632": {
      "seqid": "NMDC:1781_100325_scf_1108_c1",
      "start": 228,
      "end": 1632,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1108_c1_229_1632",
      "annotations": {
        "id": [
          "1781_100325_scf_1108_c1_229_1632"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.10.60",
          "3.30.420.10"
        ],
        "pfam": [
          "HTH_2",
          "LZ_Tnp_IS48",
          "Terminase_",
          "rv"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1109_c1": {
    "1781_100325_scf_1109_c1_3_140": {
      "seqid": "NMDC:1781_100325_scf_1109_c1",
      "start": 2,
      "end": 140,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1109_c1_3_140",
      "annotations": {
        "id": [
          "1781_100325_scf_1109_c1_3_140"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.110.10.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1109_c1_447_1634": {
      "seqid": "NMDC:1781_100325_scf_1109_c1",
      "start": 446,
      "end": 1634,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1109_c1_447_1634",
      "annotations": {
        "id": [
          "1781_100325_scf_1109_c1_447_1634"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "DEDD_Tnp_IS11",
          "Transposase_2"
        ],
        "superfamily": [
          "SM00278"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_110_c1": {
    "1781_100325_scf_110_c1_2_358": {
      "seqid": "NMDC:1781_100325_scf_110_c1",
      "start": 1,
      "end": 358,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_110_c1_2_358",
      "annotations": {
        "id": [
          "1781_100325_scf_110_c1_2_358"
        ],
        "product": [
          "transcription initiation factor TFIIB"
        ],
        "cath_funfam": [
          "1.10.472.10"
        ],
        "cog": [
          "COG1405"
        ],
        "ko": [
          "KO:K03124"
        ],
        "pfam": [
          "TFII"
        ],
        "superfamily": [
          "SM00385"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_110_c1_457_954": {
      "seqid": "NMDC:1781_100325_scf_110_c1",
      "start": 456,
      "end": 954,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_110_c1_457_954",
      "annotations": {
        "id": [
          "1781_100325_scf_110_c1_457_954"
        ],
        "product": [
          "methane/ammonia monooxygenase subunit B"
        ],
        "ko": [
          "KO:K10945"
        ],
        "pfam": [
          "Monooxygenase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_110_c1_1266_1550": {
      "seqid": "NMDC:1781_100325_scf_110_c1",
      "start": 1265,
      "end": 1550,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_110_c1_1266_1550",
      "annotations": {
        "id": [
          "1781_100325_scf_110_c1_1266_1550"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_110_c1_1762_2412": {
      "seqid": "NMDC:1781_100325_scf_110_c1",
      "start": 1761,
      "end": 2412,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_110_c1_1762_2412",
      "annotations": {
        "id": [
          "1781_100325_scf_110_c1_1762_2412"
        ],
        "product": [
          "methane/ammonia monooxygenase subunit A"
        ],
        "ko": [
          "KO:K10944"
        ],
        "ec_number": [
          "EC:1.14.18.3",
          "EC:1.14.99.39"
        ],
        "pfam": [
          "Archaeal_Amo"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_110_c1_2809_3801": {
      "seqid": "NMDC:1781_100325_scf_110_c1",
      "start": 2808,
      "end": 3801,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_110_c1_2809_3801",
      "annotations": {
        "id": [
          "1781_100325_scf_110_c1_2809_3801"
        ],
        "product": [
          "2-oxoglutarate ferredoxin oxidoreductase subunit alpha"
        ],
        "cath_funfam": [
          "3.40.920.10"
        ],
        "cog": [
          "COG1014"
        ],
        "ko": [
          "KO:K00174"
        ],
        "ec_number": [
          "EC:1.2.7.11",
          "EC:1.2.7.3"
        ],
        "pfam": [
          "PO",
          "POR_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1110_c1": {
    "1781_100325_scf_1110_c1_53_1168": {
      "seqid": "NMDC:1781_100325_scf_1110_c1",
      "start": 52,
      "end": 1168,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1110_c1_53_1168",
      "annotations": {
        "id": [
          "1781_100325_scf_1110_c1_53_1168"
        ],
        "product": [
          "ATP-binding cassette subfamily E protein 1"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1245"
        ],
        "ko": [
          "KO:K06174"
        ],
        "pfam": [
          "ABC_tra"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1110_c1_1184_1633": {
      "seqid": "NMDC:1781_100325_scf_1110_c1",
      "start": 1183,
      "end": 1633,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1110_c1_1184_1633",
      "annotations": {
        "id": [
          "1781_100325_scf_1110_c1_1184_1633"
        ],
        "product": [
          "tRNA (guanine37-N1)-methyltransferase"
        ],
        "cath_funfam": [
          "3.30.300.110"
        ],
        "cog": [
          "COG2520"
        ],
        "ko": [
          "KO:K15429"
        ],
        "ec_number": [
          "EC:2.1.1.228"
        ],
        "pfam": [
          "Met_1"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1111_c1": {
    "1781_100325_scf_1111_c1_3_176": {
      "seqid": "NMDC:1781_100325_scf_1111_c1",
      "start": 2,
      "end": 176,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1111_c1_3_176",
      "annotations": {
        "id": [
          "1781_100325_scf_1111_c1_3_176"
        ],
        "product": [
          "hypothetical protein"
        ],
        "superfamily": [
          "SM00862"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1111_c1_325_1062": {
      "seqid": "NMDC:1781_100325_scf_1111_c1",
      "start": 324,
      "end": 1062,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1111_c1_325_1062",
      "annotations": {
        "id": [
          "1781_100325_scf_1111_c1_325_1062"
        ],
        "product": [
          "protein MpaA"
        ],
        "cog": [
          "COG3608"
        ],
        "ko": [
          "KO:K14054"
        ],
        "pfam": [
          "AstE_Asp",
          "Peptidase_M1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1111_c1_1044_1253": {
      "seqid": "NMDC:1781_100325_scf_1111_c1",
      "start": 1043,
      "end": 1253,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1111_c1_1044_1253",
      "annotations": {
        "id": [
          "1781_100325_scf_1111_c1_1044_1253"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1111_c1_1341_1604": {
      "seqid": "NMDC:1781_100325_scf_1111_c1",
      "start": 1340,
      "end": 1604,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1111_c1_1341_1604",
      "annotations": {
        "id": [
          "1781_100325_scf_1111_c1_1341_1604"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1112_c1": {
    "1781_100325_scf_1112_c1_3_545": {
      "seqid": "NMDC:1781_100325_scf_1112_c1",
      "start": 2,
      "end": 545,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1112_c1_3_545",
      "annotations": {
        "id": [
          "1781_100325_scf_1112_c1_3_545"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3415"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1112_c1_917_990": {
      "seqid": "NMDC:1781_100325_scf_1112_c1",
      "start": 916,
      "end": 990,
      "strand": "-",
      "type": "SO:0000655",
      "encodes": "NMDC:1781_100325_scf_1112_c1_917_990",
      "annotations": {
        "id": [
          "1781_100325_scf_1112_c1_917_990"
        ],
        "product": [
          "Group II catalytic intron"
        ]
      }
    },
    "1781_100325_scf_1112_c1_1001_1627": {
      "seqid": "NMDC:1781_100325_scf_1112_c1",
      "start": 1000,
      "end": 1627,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1112_c1_1001_1627",
      "annotations": {
        "id": [
          "1781_100325_scf_1112_c1_1001_1627"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.70.270"
        ],
        "pfam": [
          "GII",
          "RVT_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1113_c1": {
    "1781_100325_scf_1113_c1_2_646": {
      "seqid": "NMDC:1781_100325_scf_1113_c1",
      "start": 1,
      "end": 646,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1113_c1_2_646",
      "annotations": {
        "id": [
          "1781_100325_scf_1113_c1_2_646"
        ],
        "product": [
          "nucleotide-binding universal stress UspA family protein"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "cog": [
          "COG0589"
        ],
        "pfam": [
          "Us"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1113_c1_690_824": {
      "seqid": "NMDC:1781_100325_scf_1113_c1",
      "start": 689,
      "end": 824,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1113_c1_690_824",
      "annotations": {
        "id": [
          "1781_100325_scf_1113_c1_690_824"
        ],
        "product": [
          "HSP20 family protein"
        ],
        "cath_funfam": [
          "2.60.40.790"
        ],
        "cog": [
          "COG0071"
        ],
        "ko": [
          "KO:K13993"
        ],
        "pfam": [
          "HSP2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1113_c1_1124_1630": {
      "seqid": "NMDC:1781_100325_scf_1113_c1",
      "start": 1123,
      "end": 1630,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1113_c1_1124_1630",
      "annotations": {
        "id": [
          "1781_100325_scf_1113_c1_1124_1630"
        ],
        "product": [
          "regulator of protease activity HflC (stomatin/prohibitin superfamily)"
        ],
        "cath_funfam": [
          "3.30.420.110"
        ],
        "cog": [
          "COG0330"
        ],
        "pfam": [
          "Band_"
        ],
        "superfamily": [
          "SM00244"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1114_c1": {
    "1781_100325_scf_1114_c1_2_142": {
      "seqid": "NMDC:1781_100325_scf_1114_c1",
      "start": 1,
      "end": 142,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1114_c1_2_142",
      "annotations": {
        "id": [
          "1781_100325_scf_1114_c1_2_142"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1114_c1_583_1290": {
      "seqid": "NMDC:1781_100325_scf_1114_c1",
      "start": 582,
      "end": 1290,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1114_c1_583_1290",
      "annotations": {
        "id": [
          "1781_100325_scf_1114_c1_583_1290"
        ],
        "product": [
          "Holliday junction DNA helicase RuvB"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0714"
        ],
        "ko": [
          "KO:K03551"
        ],
        "ec_number": [
          "EC:3.6.4.12"
        ],
        "pfam": [
          "AA",
          "AAA_",
          "MC",
          "RuvB_"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1114_c1_1309_1629": {
      "seqid": "NMDC:1781_100325_scf_1114_c1",
      "start": 1308,
      "end": 1629,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1114_c1_1309_1629",
      "annotations": {
        "id": [
          "1781_100325_scf_1114_c1_1309_1629"
        ],
        "product": [
          "uncharacterized membrane protein (Fun14 family)"
        ],
        "cog": [
          "COG2383"
        ],
        "pfam": [
          "FUN1"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1115_c1": {
    "1781_100325_scf_1115_c1_160_432": {
      "seqid": "NMDC:1781_100325_scf_1115_c1",
      "start": 159,
      "end": 432,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1115_c1_160_432",
      "annotations": {
        "id": [
          "1781_100325_scf_1115_c1_160_432"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1115_c1_580_1485": {
      "seqid": "NMDC:1781_100325_scf_1115_c1",
      "start": 579,
      "end": 1485,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1115_c1_580_1485",
      "annotations": {
        "id": [
          "1781_100325_scf_1115_c1_580_1485"
        ],
        "product": [
          "signal transduction histidine kinase"
        ],
        "cath_funfam": [
          "1.10.287.130",
          "3.30.565.10"
        ],
        "cog": [
          "COG0642"
        ],
        "pfam": [
          "HATPase_",
          "HisK"
        ],
        "superfamily": [
          "SM00387",
          "SM00388"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1116_c1": {
    "1781_100325_scf_1116_c1_2_316": {
      "seqid": "NMDC:1781_100325_scf_1116_c1",
      "start": 1,
      "end": 316,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1116_c1_2_316",
      "annotations": {
        "id": [
          "1781_100325_scf_1116_c1_2_316"
        ],
        "product": [
          "Holliday junction DNA helicase RuvA"
        ],
        "cath_funfam": [
          "1.10.150.20",
          "1.10.8.10"
        ],
        "cog": [
          "COG0632"
        ],
        "ko": [
          "KO:K03550"
        ],
        "ec_number": [
          "EC:3.6.4.12"
        ],
        "pfam": [
          "HHH_",
          "RuvA_"
        ],
        "superfamily": [
          "SM00278"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1116_c1_313_1329": {
      "seqid": "NMDC:1781_100325_scf_1116_c1",
      "start": 312,
      "end": 1329,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1116_c1_313_1329",
      "annotations": {
        "id": [
          "1781_100325_scf_1116_c1_313_1329"
        ],
        "product": [
          "Holliday junction DNA helicase RuvB"
        ],
        "cath_funfam": [
          "1.10.10.10",
          "1.10.8.60",
          "3.40.50.300"
        ],
        "cog": [
          "COG2255"
        ],
        "ko": [
          "KO:K03551"
        ],
        "ec_number": [
          "EC:3.6.4.12"
        ],
        "pfam": [
          "AA",
          "AAA_",
          "RuvB_"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1116_c1_1337_1627": {
      "seqid": "NMDC:1781_100325_scf_1116_c1",
      "start": 1336,
      "end": 1627,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1116_c1_1337_1627",
      "annotations": {
        "id": [
          "1781_100325_scf_1116_c1_1337_1627"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1117_c1": {
    "1781_100325_scf_1117_c1_76_1002": {
      "seqid": "NMDC:1781_100325_scf_1117_c1",
      "start": 75,
      "end": 1002,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1117_c1_76_1002",
      "annotations": {
        "id": [
          "1781_100325_scf_1117_c1_76_1002"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1117_c1_1201_1629": {
      "seqid": "NMDC:1781_100325_scf_1117_c1",
      "start": 1200,
      "end": 1629,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1117_c1_1201_1629",
      "annotations": {
        "id": [
          "1781_100325_scf_1117_c1_1201_1629"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1118_c1": {
    "1781_100325_scf_1118_c1_175_693": {
      "seqid": "NMDC:1781_100325_scf_1118_c1",
      "start": 174,
      "end": 693,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1118_c1_175_693",
      "annotations": {
        "id": [
          "1781_100325_scf_1118_c1_175_693"
        ],
        "product": [
          "RNA polymerase sigma-70 factor (ECF subfamily)"
        ],
        "cath_funfam": [
          "1.10.1740.10"
        ],
        "cog": [
          "COG1595"
        ],
        "ko": [
          "KO:K03088"
        ],
        "pfam": [
          "Sigma70_r",
          "Sigma70_r4_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1118_c1_690_1628": {
      "seqid": "NMDC:1781_100325_scf_1118_c1",
      "start": 689,
      "end": 1628,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1118_c1_690_1628",
      "annotations": {
        "id": [
          "1781_100325_scf_1118_c1_690_1628"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "zf-HC"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1119_c1": {
    "1781_100325_scf_1119_c1_2_184": {
      "seqid": "NMDC:1781_100325_scf_1119_c1",
      "start": 1,
      "end": 184,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1119_c1_2_184",
      "annotations": {
        "id": [
          "1781_100325_scf_1119_c1_2_184"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1119_c1_351_1295": {
      "seqid": "NMDC:1781_100325_scf_1119_c1",
      "start": 350,
      "end": 1295,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1119_c1_351_1295",
      "annotations": {
        "id": [
          "1781_100325_scf_1119_c1_351_1295"
        ],
        "product": [
          "16S rRNA G966 N2-methylase RsmD"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "cog": [
          "COG0742"
        ],
        "pfam": [
          "N6_N4_Mtas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1119_c1_1316_1627": {
      "seqid": "NMDC:1781_100325_scf_1119_c1",
      "start": 1315,
      "end": 1627,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1119_c1_1316_1627",
      "annotations": {
        "id": [
          "1781_100325_scf_1119_c1_1316_1627"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_111_c1": {
    "1781_100325_scf_111_c1_1_537": {
      "seqid": "NMDC:1781_100325_scf_111_c1",
      "start": 0,
      "end": 537,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_111_c1_1_537",
      "annotations": {
        "id": [
          "1781_100325_scf_111_c1_1_537"
        ],
        "product": [
          "Holliday junction DNA helicase RuvB"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0714"
        ],
        "ko": [
          "KO:K03551"
        ],
        "ec_number": [
          "EC:3.6.4.12"
        ],
        "pfam": [
          "AA",
          "MC"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_111_c1_706_1029": {
      "seqid": "NMDC:1781_100325_scf_111_c1",
      "start": 705,
      "end": 1029,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_111_c1_706_1029",
      "annotations": {
        "id": [
          "1781_100325_scf_111_c1_706_1029"
        ],
        "product": [
          "uncharacterized membrane protein (Fun14 family)"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "cog": [
          "COG2383"
        ],
        "pfam": [
          "FUN1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_111_c1_1123_1269": {
      "seqid": "NMDC:1781_100325_scf_111_c1",
      "start": 1122,
      "end": 1269,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_111_c1_1123_1269",
      "annotations": {
        "id": [
          "1781_100325_scf_111_c1_1123_1269"
        ],
        "product": [
          "antitoxin component of MazEF toxin-antitoxin module"
        ],
        "cog": [
          "COG2336"
        ],
        "pfam": [
          "MazE_antitoxi"
        ],
        "superfamily": [
          "SM00966"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_111_c1_1293_1466": {
      "seqid": "NMDC:1781_100325_scf_111_c1",
      "start": 1292,
      "end": 1466,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_111_c1_1293_1466",
      "annotations": {
        "id": [
          "1781_100325_scf_111_c1_1293_1466"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_111_c1_1789_2448": {
      "seqid": "NMDC:1781_100325_scf_111_c1",
      "start": 1788,
      "end": 2448,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_111_c1_1789_2448",
      "annotations": {
        "id": [
          "1781_100325_scf_111_c1_1789_2448"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_111_c1_2784_3017": {
      "seqid": "NMDC:1781_100325_scf_111_c1",
      "start": 2783,
      "end": 3017,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_111_c1_2784_3017",
      "annotations": {
        "id": [
          "1781_100325_scf_111_c1_2784_3017"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_111_c1_2993_3754": {
      "seqid": "NMDC:1781_100325_scf_111_c1",
      "start": 2992,
      "end": 3754,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_111_c1_2993_3754",
      "annotations": {
        "id": [
          "1781_100325_scf_111_c1_2993_3754"
        ],
        "product": [
          "Ca2+-binding RTX toxin-like protein"
        ],
        "cath_funfam": [
          "2.150.10.10"
        ],
        "cog": [
          "COG2931"
        ],
        "pfam": [
          "HemolysinCabin"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1120_c1": {
    "1781_100325_scf_1120_c1_63_389": {
      "seqid": "NMDC:1781_100325_scf_1120_c1",
      "start": 62,
      "end": 389,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1120_c1_63_389",
      "annotations": {
        "id": [
          "1781_100325_scf_1120_c1_63_389"
        ],
        "product": [
          "metal-sulfur cluster biosynthetic enzyme"
        ],
        "cath_funfam": [
          "3.30.300.130"
        ],
        "cog": [
          "COG2151"
        ],
        "pfam": [
          "DUF5"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1120_c1_456_1628": {
      "seqid": "NMDC:1781_100325_scf_1120_c1",
      "start": 455,
      "end": 1628,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1120_c1_456_1628",
      "annotations": {
        "id": [
          "1781_100325_scf_1120_c1_456_1628"
        ],
        "product": [
          "argininosuccinate lyase"
        ],
        "cath_funfam": [
          "1.10.275.10",
          "1.20.200.10"
        ],
        "cog": [
          "COG0165"
        ],
        "ko": [
          "KO:K01755"
        ],
        "ec_number": [
          "EC:4.3.2.1"
        ],
        "pfam": [
          "ASL_C",
          "Lyase_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1121_c1": {
    "1781_100325_scf_1121_c1_56_820": {
      "seqid": "NMDC:1781_100325_scf_1121_c1",
      "start": 55,
      "end": 820,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1121_c1_56_820",
      "annotations": {
        "id": [
          "1781_100325_scf_1121_c1_56_820"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.40.10.10"
        ],
        "pfam": [
          "Trypsi"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1121_c1_845_1141": {
      "seqid": "NMDC:1781_100325_scf_1121_c1",
      "start": 844,
      "end": 1141,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1121_c1_845_1141",
      "annotations": {
        "id": [
          "1781_100325_scf_1121_c1_845_1141"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1121_c1_1227_1625": {
      "seqid": "NMDC:1781_100325_scf_1121_c1",
      "start": 1226,
      "end": 1625,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1121_c1_1227_1625",
      "annotations": {
        "id": [
          "1781_100325_scf_1121_c1_1227_1625"
        ],
        "product": [
          "two-component system cell cycle response regulator"
        ],
        "cath_funfam": [
          "3.30.70.270"
        ],
        "cog": [
          "COG3706"
        ],
        "ko": [
          "KO:K02488"
        ],
        "ec_number": [
          "EC:2.7.7.65"
        ],
        "pfam": [
          "GGDE"
        ],
        "superfamily": [
          "SM00267"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1122_c1": {
    "1781_100325_scf_1122_c1_2_505": {
      "seqid": "NMDC:1781_100325_scf_1122_c1",
      "start": 1,
      "end": 505,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1122_c1_2_505",
      "annotations": {
        "id": [
          "1781_100325_scf_1122_c1_2_505"
        ],
        "product": [
          "septal ring factor EnvC (AmiA/AmiB activator)"
        ],
        "cath_funfam": [
          "1.10.3890.10"
        ],
        "cog": [
          "COG4942"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1122_c1_625_735": {
      "seqid": "NMDC:1781_100325_scf_1122_c1",
      "start": 624,
      "end": 735,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1122_c1_625_735",
      "annotations": {
        "id": [
          "1781_100325_scf_1122_c1_625_735"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1122_c1_757_1413": {
      "seqid": "NMDC:1781_100325_scf_1122_c1",
      "start": 756,
      "end": 1413,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1122_c1_757_1413",
      "annotations": {
        "id": [
          "1781_100325_scf_1122_c1_757_1413"
        ],
        "product": [
          "CRISPR-associated exonuclease Cas4"
        ],
        "cog": [
          "COG1468"
        ],
        "ko": [
          "KO:K07464"
        ],
        "ec_number": [
          "EC:3.1.12.1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1122_c1_1451_1600": {
      "seqid": "NMDC:1781_100325_scf_1122_c1",
      "start": 1450,
      "end": 1600,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1122_c1_1451_1600",
      "annotations": {
        "id": [
          "1781_100325_scf_1122_c1_1451_1600"
        ],
        "product": [
          "phosphate/sulfate permease"
        ],
        "cog": [
          "COG0306"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1123_c1": {
    "1781_100325_scf_1123_c1_22_549": {
      "seqid": "NMDC:1781_100325_scf_1123_c1",
      "start": 21,
      "end": 549,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1123_c1_22_549",
      "annotations": {
        "id": [
          "1781_100325_scf_1123_c1_22_549"
        ],
        "product": [
          "phosphoenolpyruvate carboxykinase (ATP)"
        ],
        "cath_funfam": [
          "3.90.228.20"
        ],
        "cog": [
          "COG1866"
        ],
        "ko": [
          "KO:K01610"
        ],
        "ec_number": [
          "EC:4.1.1.49"
        ],
        "pfam": [
          "PEPCK_AT"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1123_c1_743_1315": {
      "seqid": "NMDC:1781_100325_scf_1123_c1",
      "start": 742,
      "end": 1315,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1123_c1_743_1315",
      "annotations": {
        "id": [
          "1781_100325_scf_1123_c1_743_1315"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.20.1050.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1123_c1_1428_1625": {
      "seqid": "NMDC:1781_100325_scf_1123_c1",
      "start": 1427,
      "end": 1625,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1123_c1_1428_1625",
      "annotations": {
        "id": [
          "1781_100325_scf_1123_c1_1428_1625"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1124_c1": {
    "1781_100325_scf_1124_c1_2_301": {
      "seqid": "NMDC:1781_100325_scf_1124_c1",
      "start": 1,
      "end": 301,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1124_c1_2_301",
      "annotations": {
        "id": [
          "1781_100325_scf_1124_c1_2_301"
        ],
        "product": [
          "methylisocitrate lyase"
        ],
        "cath_funfam": [
          "3.20.20.60"
        ],
        "cog": [
          "COG2513"
        ],
        "ko": [
          "KO:K03417"
        ],
        "ec_number": [
          "EC:4.1.3.30"
        ],
        "pfam": [
          "PEP_mutas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1124_c1_335_844": {
      "seqid": "NMDC:1781_100325_scf_1124_c1",
      "start": 334,
      "end": 844,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1124_c1_335_844",
      "annotations": {
        "id": [
          "1781_100325_scf_1124_c1_335_844"
        ],
        "product": [
          "DNA-binding PadR family transcriptional regulator"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG1695"
        ],
        "pfam": [
          "Pad"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1124_c1_953_1624": {
      "seqid": "NMDC:1781_100325_scf_1124_c1",
      "start": 952,
      "end": 1624,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1124_c1_953_1624",
      "annotations": {
        "id": [
          "1781_100325_scf_1124_c1_953_1624"
        ],
        "product": [
          "succinate dehydrogenase / fumarate reductase flavoprotein subunit"
        ],
        "cath_funfam": [
          "3.50.50.60"
        ],
        "cog": [
          "COG1053"
        ],
        "ko": [
          "KO:K00239"
        ],
        "ec_number": [
          "EC:1.3.5.1",
          "EC:1.3.5.4"
        ],
        "pfam": [
          "FAD_binding_",
          "GID",
          "Pyr_redox_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1125_c1": {
    "1781_100325_scf_1125_c1_43_360": {
      "seqid": "NMDC:1781_100325_scf_1125_c1",
      "start": 42,
      "end": 360,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1125_c1_43_360",
      "annotations": {
        "id": [
          "1781_100325_scf_1125_c1_43_360"
        ],
        "product": [
          "translation initiation factor 2 subunit 2"
        ],
        "cath_funfam": [
          "2.20.28.10"
        ],
        "cog": [
          "COG1601"
        ],
        "ko": [
          "KO:K03238"
        ],
        "pfam": [
          "eIF-5_eIF-2"
        ],
        "superfamily": [
          "SM00653"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1125_c1_360_659": {
      "seqid": "NMDC:1781_100325_scf_1125_c1",
      "start": 359,
      "end": 659,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1125_c1_360_659",
      "annotations": {
        "id": [
          "1781_100325_scf_1125_c1_360_659"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.1860.10"
        ],
        "cog": [
          "COG2412"
        ],
        "ko": [
          "KO:K09148"
        ],
        "pfam": [
          "DUF42"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1125_c1_705_1016": {
      "seqid": "NMDC:1781_100325_scf_1125_c1",
      "start": 704,
      "end": 1016,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1125_c1_705_1016",
      "annotations": {
        "id": [
          "1781_100325_scf_1125_c1_705_1016"
        ],
        "product": [
          "translation initiation factor 1A"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG0361"
        ],
        "ko": [
          "KO:K03236"
        ],
        "pfam": [
          "eIF-1"
        ],
        "superfamily": [
          "SM00652"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1125_c1_1059_1622": {
      "seqid": "NMDC:1781_100325_scf_1125_c1",
      "start": 1058,
      "end": 1622,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1125_c1_1059_1622",
      "annotations": {
        "id": [
          "1781_100325_scf_1125_c1_1059_1622"
        ],
        "product": [
          "RIO kinase 1"
        ],
        "cath_funfam": [
          "3.30.200.20"
        ],
        "cog": [
          "COG1718"
        ],
        "ko": [
          "KO:K07178"
        ],
        "ec_number": [
          "EC:2.7.11.1"
        ],
        "pfam": [
          "RIO"
        ],
        "superfamily": [
          "SM00090"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1126_c1": {
    "1781_100325_scf_1126_c1_1_1623": {
      "seqid": "NMDC:1781_100325_scf_1126_c1",
      "start": 0,
      "end": 1623,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1126_c1_1_1623",
      "annotations": {
        "id": [
          "1781_100325_scf_1126_c1_1_1623"
        ],
        "product": [
          "uncharacterized protein YodC (DUF2158 family)"
        ],
        "cath_funfam": [
          "2.60.40.10"
        ],
        "cog": [
          "COG5475"
        ],
        "superfamily": [
          "SM00089"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1127_c1": {
    "1781_100325_scf_1127_c1_3_401": {
      "seqid": "NMDC:1781_100325_scf_1127_c1",
      "start": 2,
      "end": 401,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1127_c1_3_401",
      "annotations": {
        "id": [
          "1781_100325_scf_1127_c1_3_401"
        ],
        "product": [
          "zinc transporter ZupT"
        ],
        "cog": [
          "COG0428"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1127_c1_433_921": {
      "seqid": "NMDC:1781_100325_scf_1127_c1",
      "start": 432,
      "end": 921,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1127_c1_433_921",
      "annotations": {
        "id": [
          "1781_100325_scf_1127_c1_433_921"
        ],
        "product": [
          "Mn-dependent DtxR family transcriptional regulator"
        ],
        "cath_funfam": [
          "1.10.10.10",
          "1.10.60.10"
        ],
        "cog": [
          "COG1321"
        ],
        "pfam": [
          "Fe_dep_repr_",
          "Fe_dep_repres"
        ],
        "superfamily": [
          "SM00529"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1127_c1_1114_1623": {
      "seqid": "NMDC:1781_100325_scf_1127_c1",
      "start": 1113,
      "end": 1623,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1127_c1_1114_1623",
      "annotations": {
        "id": [
          "1781_100325_scf_1127_c1_1114_1623"
        ],
        "product": [
          "protein-disulfide isomerase"
        ],
        "cath_funfam": [
          "3.40.30.10"
        ],
        "cog": [
          "COG1651"
        ],
        "pfam": [
          "DSB",
          "Thioredoxin_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1128_c1": {
    "1781_100325_scf_1128_c1_2_1621": {
      "seqid": "NMDC:1781_100325_scf_1128_c1",
      "start": 1,
      "end": 1621,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1128_c1_2_1621",
      "annotations": {
        "id": [
          "1781_100325_scf_1128_c1_2_1621"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.60.40.740"
        ],
        "pfam": [
          "DUF1"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1129_c1": {
    "1781_100325_scf_1129_c1_2_178": {
      "seqid": "NMDC:1781_100325_scf_1129_c1",
      "start": 1,
      "end": 178,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1129_c1_2_178",
      "annotations": {
        "id": [
          "1781_100325_scf_1129_c1_2_178"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1129_c1_232_1620": {
      "seqid": "NMDC:1781_100325_scf_1129_c1",
      "start": 231,
      "end": 1620,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1129_c1_232_1620",
      "annotations": {
        "id": [
          "1781_100325_scf_1129_c1_232_1620"
        ],
        "product": [
          "phosphoenolpyruvate carboxykinase (ATP)"
        ],
        "cath_funfam": [
          "3.40.449.10",
          "3.90.228.20"
        ],
        "cog": [
          "COG1866"
        ],
        "ko": [
          "KO:K01610"
        ],
        "ec_number": [
          "EC:4.1.1.49"
        ],
        "pfam": [
          "PEPCK_AT"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_112_c1": {
    "1781_100325_scf_112_c1_3_113": {
      "seqid": "NMDC:1781_100325_scf_112_c1",
      "start": 2,
      "end": 113,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_112_c1_3_113",
      "annotations": {
        "id": [
          "1781_100325_scf_112_c1_3_113"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_112_c1_126_830": {
      "seqid": "NMDC:1781_100325_scf_112_c1",
      "start": 125,
      "end": 830,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_112_c1_126_830",
      "annotations": {
        "id": [
          "1781_100325_scf_112_c1_126_830"
        ],
        "product": [
          "NAD(P)-dependent dehydrogenase (short-subunit alcohol dehydrogenase family)"
        ],
        "cath_funfam": [
          "3.40.50.720"
        ],
        "cog": [
          "COG1028"
        ],
        "pfam": [
          "K",
          "adh_shor",
          "adh_short_C"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_112_c1_949_1470": {
      "seqid": "NMDC:1781_100325_scf_112_c1",
      "start": 948,
      "end": 1470,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_112_c1_949_1470",
      "annotations": {
        "id": [
          "1781_100325_scf_112_c1_949_1470"
        ],
        "product": [
          "nitroreductase"
        ],
        "cath_funfam": [
          "3.40.109.10"
        ],
        "cog": [
          "COG0778"
        ],
        "pfam": [
          "Nitroreductas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_112_c1_1593_2522": {
      "seqid": "NMDC:1781_100325_scf_112_c1",
      "start": 1592,
      "end": 2522,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_112_c1_1593_2522",
      "annotations": {
        "id": [
          "1781_100325_scf_112_c1_1593_2522"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.470.20"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_112_c1_2638_3771": {
      "seqid": "NMDC:1781_100325_scf_112_c1",
      "start": 2637,
      "end": 3771,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_112_c1_2638_3771",
      "annotations": {
        "id": [
          "1781_100325_scf_112_c1_2638_3771"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1130_c1": {
    "1781_100325_scf_1130_c1_3_1616": {
      "seqid": "NMDC:1781_100325_scf_1130_c1",
      "start": 2,
      "end": 1616,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1130_c1_3_1616",
      "annotations": {
        "id": [
          "1781_100325_scf_1130_c1_3_1616"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.50.10.10"
        ],
        "cog": [
          "COG1331"
        ],
        "ko": [
          "KO:K06888"
        ],
        "pfam": [
          "GlcNAc_2-epi",
          "Thioredox_Dsb"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1131_c1": {
    "1781_100325_scf_1131_c1_2_1228": {
      "seqid": "NMDC:1781_100325_scf_1131_c1",
      "start": 1,
      "end": 1228,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1131_c1_2_1228",
      "annotations": {
        "id": [
          "1781_100325_scf_1131_c1_2_1228"
        ],
        "product": [
          "transposase"
        ],
        "cath_funfam": [
          "4.10.860.10"
        ],
        "cog": [
          "COG3436"
        ],
        "pfam": [
          "DDE_Tnp_IS6"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1132_c1": {
    "1781_100325_scf_1132_c1_3_410": {
      "seqid": "NMDC:1781_100325_scf_1132_c1",
      "start": 2,
      "end": 410,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1132_c1_3_410",
      "annotations": {
        "id": [
          "1781_100325_scf_1132_c1_3_410"
        ],
        "product": [
          "carboxylate-amine ligase"
        ],
        "cog": [
          "COG2170"
        ],
        "ko": [
          "KO:K06048"
        ],
        "ec_number": [
          "EC:6.3.-"
        ],
        "pfam": [
          "GCS"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1132_c1_533_1030": {
      "seqid": "NMDC:1781_100325_scf_1132_c1",
      "start": 532,
      "end": 1030,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1132_c1_533_1030",
      "annotations": {
        "id": [
          "1781_100325_scf_1132_c1_533_1030"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1132_c1_1074_1514": {
      "seqid": "NMDC:1781_100325_scf_1132_c1",
      "start": 1073,
      "end": 1514,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1132_c1_1074_1514",
      "annotations": {
        "id": [
          "1781_100325_scf_1132_c1_1074_1514"
        ],
        "product": [
          "enamine deaminase RidA (YjgF/YER057c/UK114 family)"
        ],
        "cath_funfam": [
          "3.30.1330.40"
        ],
        "cog": [
          "COG0251"
        ],
        "pfam": [
          "Ribonuc_L-PS"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1133_c1": {
    "1781_100325_scf_1133_c1_3_992": {
      "seqid": "NMDC:1781_100325_scf_1133_c1",
      "start": 2,
      "end": 992,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1133_c1_3_992",
      "annotations": {
        "id": [
          "1781_100325_scf_1133_c1_3_992"
        ],
        "product": [
          "signal recognition particle subunit SRP54"
        ],
        "cath_funfam": [
          "1.20.120.140",
          "3.40.50.300"
        ],
        "cog": [
          "COG0541"
        ],
        "ko": [
          "KO:K03106"
        ],
        "pfam": [
          "Cbi",
          "SRP5",
          "SRP54_",
          "Zeta_toxi"
        ],
        "superfamily": [
          "SM00962",
          "SM00963"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1133_c1_1043_1249": {
      "seqid": "NMDC:1781_100325_scf_1133_c1",
      "start": 1042,
      "end": 1249,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1133_c1_1043_1249",
      "annotations": {
        "id": [
          "1781_100325_scf_1133_c1_1043_1249"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG3360"
        ],
        "ko": [
          "KO:K09165"
        ],
        "pfam": [
          "Dodeci"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1133_c1_1260_1571": {
      "seqid": "NMDC:1781_100325_scf_1133_c1",
      "start": 1259,
      "end": 1571,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1133_c1_1260_1571",
      "annotations": {
        "id": [
          "1781_100325_scf_1133_c1_1260_1571"
        ],
        "product": [
          "heme-degrading monooxygenase HmoA"
        ],
        "cog": [
          "COG2329"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1134_c1": {
    "1781_100325_scf_1134_c1_3_695": {
      "seqid": "NMDC:1781_100325_scf_1134_c1",
      "start": 2,
      "end": 695,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1134_c1_3_695",
      "annotations": {
        "id": [
          "1781_100325_scf_1134_c1_3_695"
        ],
        "product": [
          "glutamate-ammonia-ligase adenylyltransferase"
        ],
        "cath_funfam": [
          "1.10.4050.10"
        ],
        "cog": [
          "COG1391"
        ],
        "ko": [
          "KO:K00982"
        ],
        "ec_number": [
          "EC:2.7.7.42"
        ],
        "pfam": [
          "Gln"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1134_c1_702_1616": {
      "seqid": "NMDC:1781_100325_scf_1134_c1",
      "start": 701,
      "end": 1616,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1134_c1_702_1616",
      "annotations": {
        "id": [
          "1781_100325_scf_1134_c1_702_1616"
        ],
        "product": [
          "glutamine synthetase"
        ],
        "cath_funfam": [
          "3.30.590.10"
        ],
        "cog": [
          "COG0174"
        ],
        "ko": [
          "KO:K01915"
        ],
        "ec_number": [
          "EC:6.3.1.2"
        ],
        "pfam": [
          "Gln-synt_"
        ],
        "superfamily": [
          "SM01230"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1135_c1": {
    "1781_100325_scf_1135_c1_3_1556": {
      "seqid": "NMDC:1781_100325_scf_1135_c1",
      "start": 2,
      "end": 1556,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1135_c1_3_1556",
      "annotations": {
        "id": [
          "1781_100325_scf_1135_c1_3_1556"
        ],
        "product": [
          "cell division protein FtsI (penicillin-binding protein 3)"
        ],
        "cath_funfam": [
          "3.40.710.10"
        ],
        "cog": [
          "COG0768"
        ],
        "ko": [
          "KO:K03587"
        ],
        "pfam": [
          "Beta-lactamase",
          "PBP_dime",
          "Transpeptidas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1136_c1": {
    "1781_100325_scf_1136_c1_9_239": {
      "seqid": "NMDC:1781_100325_scf_1136_c1",
      "start": 8,
      "end": 239,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1136_c1_9_239",
      "annotations": {
        "id": [
          "1781_100325_scf_1136_c1_9_239"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1136_c1_256_1041": {
      "seqid": "NMDC:1781_100325_scf_1136_c1",
      "start": 255,
      "end": 1041,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1136_c1_256_1041",
      "annotations": {
        "id": [
          "1781_100325_scf_1136_c1_256_1041"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1136_c1_1151_1615": {
      "seqid": "NMDC:1781_100325_scf_1136_c1",
      "start": 1150,
      "end": 1615,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1136_c1_1151_1615",
      "annotations": {
        "id": [
          "1781_100325_scf_1136_c1_1151_1615"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1137_c1": {
    "1781_100325_scf_1137_c1_2_151": {
      "seqid": "NMDC:1781_100325_scf_1137_c1",
      "start": 1,
      "end": 151,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1137_c1_2_151",
      "annotations": {
        "id": [
          "1781_100325_scf_1137_c1_2_151"
        ],
        "product": [
          "foldase protein PrsA"
        ],
        "cath_funfam": [
          "3.10.50.40"
        ],
        "cog": [
          "COG0760"
        ],
        "ko": [
          "KO:K07533"
        ],
        "ec_number": [
          "EC:5.2.1.8"
        ],
        "pfam": [
          "Rotamase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1137_c1_340_1584": {
      "seqid": "NMDC:1781_100325_scf_1137_c1",
      "start": 339,
      "end": 1584,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1137_c1_340_1584",
      "annotations": {
        "id": [
          "1781_100325_scf_1137_c1_340_1584"
        ],
        "product": [
          "exonuclease SbcC"
        ],
        "cath_funfam": [
          "1.20.1050.10",
          "3.40.50.300"
        ],
        "cog": [
          "COG0419"
        ],
        "ko": [
          "KO:K03546"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1138_c1": {
    "1781_100325_scf_1138_c1_29_184": {
      "seqid": "NMDC:1781_100325_scf_1138_c1",
      "start": 28,
      "end": 184,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1138_c1_29_184",
      "annotations": {
        "id": [
          "1781_100325_scf_1138_c1_29_184"
        ],
        "product": [
          "hypothetical protein"
        ],
        "superfamily": [
          "SM00729"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1138_c1_302_1450": {
      "seqid": "NMDC:1781_100325_scf_1138_c1",
      "start": 301,
      "end": 1450,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1138_c1_302_1450",
      "annotations": {
        "id": [
          "1781_100325_scf_1138_c1_302_1450"
        ],
        "product": [
          "CPA2 family monovalent cation:H+ antiporter-2"
        ],
        "cog": [
          "COG0475"
        ],
        "ko": [
          "KO:K03455"
        ],
        "pfam": [
          "Na_H_Exchange"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1139_c1": {
    "1781_100325_scf_1139_c1_19_669": {
      "seqid": "NMDC:1781_100325_scf_1139_c1",
      "start": 18,
      "end": 669,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1139_c1_19_669",
      "annotations": {
        "id": [
          "1781_100325_scf_1139_c1_19_669"
        ],
        "product": [
          "diguanylate cyclase (GGDEF)-like protein"
        ],
        "cath_funfam": [
          "3.30.70.270"
        ],
        "cog": [
          "COG2199"
        ],
        "pfam": [
          "GGDE"
        ],
        "superfamily": [
          "SM00267"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1139_c1_675_1604": {
      "seqid": "NMDC:1781_100325_scf_1139_c1",
      "start": 674,
      "end": 1604,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1139_c1_675_1604",
      "annotations": {
        "id": [
          "1781_100325_scf_1139_c1_675_1604"
        ],
        "product": [
          "DNA-binding transcriptional LysR family regulator"
        ],
        "cath_funfam": [
          "1.10.10.10",
          "3.40.190.10"
        ],
        "cog": [
          "COG0583"
        ],
        "pfam": [
          "HTH_",
          "LysR_substrat"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_113_c1": {
    "1781_100325_scf_113_c1_322_852": {
      "seqid": "NMDC:1781_100325_scf_113_c1",
      "start": 321,
      "end": 852,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_113_c1_322_852",
      "annotations": {
        "id": [
          "1781_100325_scf_113_c1_322_852"
        ],
        "product": [
          "HSP20 family protein"
        ],
        "cath_funfam": [
          "2.60.40.790"
        ],
        "cog": [
          "COG0071"
        ],
        "ko": [
          "KO:K13993"
        ],
        "pfam": [
          "HSP2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_113_c1_916_1242": {
      "seqid": "NMDC:1781_100325_scf_113_c1",
      "start": 915,
      "end": 1242,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_113_c1_916_1242",
      "annotations": {
        "id": [
          "1781_100325_scf_113_c1_916_1242"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_113_c1_1269_1664": {
      "seqid": "NMDC:1781_100325_scf_113_c1",
      "start": 1268,
      "end": 1664,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_113_c1_1269_1664",
      "annotations": {
        "id": [
          "1781_100325_scf_113_c1_1269_1664"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG2164"
        ],
        "ko": [
          "KO:K09143"
        ],
        "pfam": [
          "Cyclophil_lik"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_113_c1_1738_2709": {
      "seqid": "NMDC:1781_100325_scf_113_c1",
      "start": 1737,
      "end": 2709,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_113_c1_1738_2709",
      "annotations": {
        "id": [
          "1781_100325_scf_113_c1_1738_2709"
        ],
        "product": [
          "DNA-binding beta-propeller fold protein YncE"
        ],
        "cath_funfam": [
          "2.120.10.30"
        ],
        "cog": [
          "COG3391"
        ],
        "pfam": [
          "DUF512",
          "NH",
          "SBB"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_113_c1_2841_3059": {
      "seqid": "NMDC:1781_100325_scf_113_c1",
      "start": 2840,
      "end": 3059,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_113_c1_2841_3059",
      "annotations": {
        "id": [
          "1781_100325_scf_113_c1_2841_3059"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.20.28.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_113_c1_3367_3747": {
      "seqid": "NMDC:1781_100325_scf_113_c1",
      "start": 3366,
      "end": 3747,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_113_c1_3367_3747",
      "annotations": {
        "id": [
          "1781_100325_scf_113_c1_3367_3747"
        ],
        "product": [
          "transcription initiation factor TFIIB"
        ],
        "cath_funfam": [
          "2.20.25.10"
        ],
        "cog": [
          "COG1405"
        ],
        "ko": [
          "KO:K03124"
        ],
        "pfam": [
          "TF_Zn_Ribbo"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1140_c1": {
    "1781_100325_scf_1140_c1_3_119": {
      "seqid": "NMDC:1781_100325_scf_1140_c1",
      "start": 2,
      "end": 119,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1140_c1_3_119",
      "annotations": {
        "id": [
          "1781_100325_scf_1140_c1_3_119"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1140_c1_465_1361": {
      "seqid": "NMDC:1781_100325_scf_1140_c1",
      "start": 464,
      "end": 1361,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1140_c1_465_1361",
      "annotations": {
        "id": [
          "1781_100325_scf_1140_c1_465_1361"
        ],
        "product": [
          "methionyl aminopeptidase"
        ],
        "cath_funfam": [
          "3.90.230.10"
        ],
        "cog": [
          "COG0024"
        ],
        "ko": [
          "KO:K01265"
        ],
        "ec_number": [
          "EC:3.4.11.18"
        ],
        "pfam": [
          "Peptidase_M2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1140_c1_1513_1614": {
      "seqid": "NMDC:1781_100325_scf_1140_c1",
      "start": 1512,
      "end": 1614,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1140_c1_1513_1614",
      "annotations": {
        "id": [
          "1781_100325_scf_1140_c1_1513_1614"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1141_c1": {
    "1781_100325_scf_1141_c1_15_1061": {
      "seqid": "NMDC:1781_100325_scf_1141_c1",
      "start": 14,
      "end": 1061,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1141_c1_15_1061",
      "annotations": {
        "id": [
          "1781_100325_scf_1141_c1_15_1061"
        ],
        "product": [
          "pyruvate dehydrogenase E1 component alpha subunit"
        ],
        "cath_funfam": [
          "3.40.50.970"
        ],
        "cog": [
          "COG1071"
        ],
        "ko": [
          "KO:K00161"
        ],
        "ec_number": [
          "EC:1.2.4.1"
        ],
        "pfam": [
          "E1_d"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1141_c1_1072_1614": {
      "seqid": "NMDC:1781_100325_scf_1141_c1",
      "start": 1071,
      "end": 1614,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1141_c1_1072_1614",
      "annotations": {
        "id": [
          "1781_100325_scf_1141_c1_1072_1614"
        ],
        "product": [
          "2-oxoisovalerate dehydrogenase E1 component beta subunit"
        ],
        "cath_funfam": [
          "3.40.50.970"
        ],
        "cog": [
          "COG0022"
        ],
        "ko": [
          "KO:K00167"
        ],
        "ec_number": [
          "EC:1.2.4.4"
        ],
        "pfam": [
          "Transket_py"
        ],
        "superfamily": [
          "SM00861"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1142_c1": {
    "1781_100325_scf_1142_c1_120_1343": {
      "seqid": "NMDC:1781_100325_scf_1142_c1",
      "start": 119,
      "end": 1343,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1142_c1_120_1343",
      "annotations": {
        "id": [
          "1781_100325_scf_1142_c1_120_1343"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG1615"
        ],
        "ko": [
          "KO:K09118"
        ],
        "pfam": [
          "UPF018"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1142_c1_1485_1607": {
      "seqid": "NMDC:1781_100325_scf_1142_c1",
      "start": 1484,
      "end": 1607,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1142_c1_1485_1607",
      "annotations": {
        "id": [
          "1781_100325_scf_1142_c1_1485_1607"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1143_c1": {
    "1781_100325_scf_1143_c1_68_1345": {
      "seqid": "NMDC:1781_100325_scf_1143_c1",
      "start": 67,
      "end": 1345,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1143_c1_68_1345",
      "annotations": {
        "id": [
          "1781_100325_scf_1143_c1_68_1345"
        ],
        "product": [
          "arylsulfatase A-like enzyme"
        ],
        "cath_funfam": [
          "3.40.720.10"
        ],
        "cog": [
          "COG3119"
        ],
        "pfam": [
          "Phosphodies",
          "Sulfatas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1143_c1_1375_1614": {
      "seqid": "NMDC:1781_100325_scf_1143_c1",
      "start": 1374,
      "end": 1614,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1143_c1_1375_1614",
      "annotations": {
        "id": [
          "1781_100325_scf_1143_c1_1375_1614"
        ],
        "product": [
          "arylsulfatase A-like enzyme"
        ],
        "cog": [
          "COG3119"
        ],
        "pfam": [
          "Sulfatas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1144_c1": {
    "1781_100325_scf_1144_c1_23_1576": {
      "seqid": "NMDC:1781_100325_scf_1144_c1",
      "start": 22,
      "end": 1576,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1144_c1_23_1576",
      "annotations": {
        "id": [
          "1781_100325_scf_1144_c1_23_1576"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.40.270.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1145_c1": {
    "1781_100325_scf_1145_c1_1_756": {
      "seqid": "NMDC:1781_100325_scf_1145_c1",
      "start": 0,
      "end": 756,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1145_c1_1_756",
      "annotations": {
        "id": [
          "1781_100325_scf_1145_c1_1_756"
        ],
        "product": [
          "S-adenosylmethionine synthetase"
        ],
        "cath_funfam": [
          "3.30.300.10"
        ],
        "cog": [
          "COG0192"
        ],
        "ko": [
          "KO:K00789"
        ],
        "ec_number": [
          "EC:2.5.1.6"
        ],
        "pfam": [
          "S-AdoMet_synt_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1145_c1_793_1041": {
      "seqid": "NMDC:1781_100325_scf_1145_c1",
      "start": 792,
      "end": 1041,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1145_c1_793_1041",
      "annotations": {
        "id": [
          "1781_100325_scf_1145_c1_793_1041"
        ],
        "product": [
          "small nuclear ribonucleoprotein"
        ],
        "cath_funfam": [
          "2.30.30.100"
        ],
        "cog": [
          "COG1958"
        ],
        "ko": [
          "KO:K04796"
        ],
        "pfam": [
          "LS"
        ],
        "superfamily": [
          "SM00651"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1145_c1_1142_1612": {
      "seqid": "NMDC:1781_100325_scf_1145_c1",
      "start": 1141,
      "end": 1612,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1145_c1_1142_1612",
      "annotations": {
        "id": [
          "1781_100325_scf_1145_c1_1142_1612"
        ],
        "product": [
          "RecA/RadA recombinase"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0468"
        ],
        "pfam": [
          "Rad5"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1146_c1": {
    "1781_100325_scf_1146_c1_2_310": {
      "seqid": "NMDC:1781_100325_scf_1146_c1",
      "start": 1,
      "end": 310,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1146_c1_2_310",
      "annotations": {
        "id": [
          "1781_100325_scf_1146_c1_2_310"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.20.70.10"
        ],
        "cog": [
          "COG3791"
        ],
        "pfam": [
          "GF"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1146_c1_559_1572": {
      "seqid": "NMDC:1781_100325_scf_1146_c1",
      "start": 558,
      "end": 1572,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1146_c1_559_1572",
      "annotations": {
        "id": [
          "1781_100325_scf_1146_c1_559_1572"
        ],
        "product": [
          "transposase"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "DEDD_Tnp_IS11",
          "Transposase_2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1147_c1": {
    "1781_100325_scf_1147_c1_2_934": {
      "seqid": "NMDC:1781_100325_scf_1147_c1",
      "start": 1,
      "end": 934,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1147_c1_2_934",
      "annotations": {
        "id": [
          "1781_100325_scf_1147_c1_2_934"
        ],
        "product": [
          "replication factor A1"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "ko": [
          "KO:K07466"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1147_c1_931_1608": {
      "seqid": "NMDC:1781_100325_scf_1147_c1",
      "start": 930,
      "end": 1608,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1147_c1_931_1608",
      "annotations": {
        "id": [
          "1781_100325_scf_1147_c1_931_1608"
        ],
        "product": [
          "ATP-dependent Lhr-like helicase"
        ],
        "cog": [
          "COG2835"
        ],
        "ko": [
          "KO:K03724"
        ],
        "ec_number": [
          "EC:3.6.4.-"
        ],
        "pfam": [
          "DEAD_asso"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1148_c1": {
    "1781_100325_scf_1148_c1_2_154": {
      "seqid": "NMDC:1781_100325_scf_1148_c1",
      "start": 1,
      "end": 154,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1148_c1_2_154",
      "annotations": {
        "id": [
          "1781_100325_scf_1148_c1_2_154"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1148_c1_503_1423": {
      "seqid": "NMDC:1781_100325_scf_1148_c1",
      "start": 502,
      "end": 1423,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1148_c1_503_1423",
      "annotations": {
        "id": [
          "1781_100325_scf_1148_c1_503_1423"
        ],
        "product": [
          "4-hydroxy-3-methylbut-2-enyl diphosphate reductase"
        ],
        "cog": [
          "COG0761"
        ],
        "ko": [
          "KO:K03527"
        ],
        "ec_number": [
          "EC:1.17.1.2"
        ],
        "pfam": [
          "LYT"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1148_c1_1462_1608": {
      "seqid": "NMDC:1781_100325_scf_1148_c1",
      "start": 1461,
      "end": 1608,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1148_c1_1462_1608",
      "annotations": {
        "id": [
          "1781_100325_scf_1148_c1_1462_1608"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1149_c1": {
    "1781_100325_scf_1149_c1_3_1085": {
      "seqid": "NMDC:1781_100325_scf_1149_c1",
      "start": 2,
      "end": 1085,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1149_c1_3_1085",
      "annotations": {
        "id": [
          "1781_100325_scf_1149_c1_3_1085"
        ],
        "product": [
          "acyl-CoA synthetase (NDP forming)"
        ],
        "cath_funfam": [
          "3.30.470.20",
          "3.40.50.261"
        ],
        "cog": [
          "COG1042"
        ],
        "pfam": [
          "ATP-grasp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1149_c1_1075_1608": {
      "seqid": "NMDC:1781_100325_scf_1149_c1",
      "start": 1074,
      "end": 1608,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1149_c1_1075_1608",
      "annotations": {
        "id": [
          "1781_100325_scf_1149_c1_1075_1608"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.720"
        ],
        "cog": [
          "COG1028"
        ],
        "ko": [
          "KO:K00100"
        ],
        "pfam": [
          "K",
          "adh_shor",
          "adh_short_C"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_114_c1": {
    "1781_100325_scf_114_c1_1_774": {
      "seqid": "NMDC:1781_100325_scf_114_c1",
      "start": 0,
      "end": 774,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_114_c1_1_774",
      "annotations": {
        "id": [
          "1781_100325_scf_114_c1_1_774"
        ],
        "product": [
          "glyoxylase-like metal-dependent hydrolase (beta-lactamase superfamily II)"
        ],
        "cog": [
          "COG0491"
        ],
        "pfam": [
          "Lactamase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_114_c1_762_1355": {
      "seqid": "NMDC:1781_100325_scf_114_c1",
      "start": 761,
      "end": 1355,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_114_c1_762_1355",
      "annotations": {
        "id": [
          "1781_100325_scf_114_c1_762_1355"
        ],
        "product": [
          "tetratricopeptide (TPR) repeat protein"
        ],
        "cath_funfam": [
          "1.25.40.10"
        ],
        "cog": [
          "COG0457"
        ],
        "pfam": [
          "TPR_",
          "TPR_1"
        ],
        "superfamily": [
          "SM00028"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_114_c1_1529_1645": {
      "seqid": "NMDC:1781_100325_scf_114_c1",
      "start": 1528,
      "end": 1645,
      "strand": "-",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_114_c1_1529_1645",
      "annotations": {
        "id": [
          "1781_100325_scf_114_c1_1529_1645"
        ],
        "product": [
          "5S ribosomal RNA"
        ]
      }
    },
    "1781_100325_scf_114_c1_1734_3740": {
      "seqid": "NMDC:1781_100325_scf_114_c1",
      "start": 1733,
      "end": 3740,
      "strand": "-",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_114_c1_1734_3740",
      "annotations": {
        "id": [
          "1781_100325_scf_114_c1_1734_3740"
        ],
        "product": [
          "23S ribosomal RNA"
        ]
      }
    }
  },
  "1781_100325_scf_1150_c1": {
    "1781_100325_scf_1150_c1_61_1122": {
      "seqid": "NMDC:1781_100325_scf_1150_c1",
      "start": 60,
      "end": 1122,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1150_c1_61_1122",
      "annotations": {
        "id": [
          "1781_100325_scf_1150_c1_61_1122"
        ],
        "product": [
          "Na+/proline symporter"
        ],
        "cog": [
          "COG0591"
        ],
        "pfam": [
          "SS"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1150_c1_1240_1608": {
      "seqid": "NMDC:1781_100325_scf_1150_c1",
      "start": 1239,
      "end": 1608,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1150_c1_1240_1608",
      "annotations": {
        "id": [
          "1781_100325_scf_1150_c1_1240_1608"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1151_c1": {
    "1781_100325_scf_1151_c1_1_1605": {
      "seqid": "NMDC:1781_100325_scf_1151_c1",
      "start": 0,
      "end": 1605,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1151_c1_1_1605",
      "annotations": {
        "id": [
          "1781_100325_scf_1151_c1_1_1605"
        ],
        "product": [
          "single-stranded-DNA-specific exonuclease"
        ],
        "cog": [
          "COG0608"
        ],
        "ko": [
          "KO:K07462"
        ],
        "ec_number": [
          "EC:3.1.-"
        ],
        "pfam": [
          "DH",
          "DHHA"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1152_c1": {
    "1781_100325_scf_1152_c1_3_383": {
      "seqid": "NMDC:1781_100325_scf_1152_c1",
      "start": 2,
      "end": 383,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1152_c1_3_383",
      "annotations": {
        "id": [
          "1781_100325_scf_1152_c1_3_383"
        ],
        "product": [
          "ferredoxin-NADP reductase"
        ],
        "cath_funfam": [
          "2.40.30.10"
        ],
        "cog": [
          "COG1018"
        ],
        "pfam": [
          "FAD_binding_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1152_c1_975_1607": {
      "seqid": "NMDC:1781_100325_scf_1152_c1",
      "start": 974,
      "end": 1607,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1152_c1_975_1607",
      "annotations": {
        "id": [
          "1781_100325_scf_1152_c1_975_1607"
        ],
        "product": [
          "DMSO/TMAO reductase YedYZ molybdopterin-dependent catalytic subunit"
        ],
        "cath_funfam": [
          "3.90.420.10"
        ],
        "cog": [
          "COG2041"
        ],
        "pfam": [
          "Oxidored_moly"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1153_c1": {
    "1781_100325_scf_1153_c1_3_119": {
      "seqid": "NMDC:1781_100325_scf_1153_c1",
      "start": 2,
      "end": 119,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1153_c1_3_119",
      "annotations": {
        "id": [
          "1781_100325_scf_1153_c1_3_119"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1153_c1_151_1080": {
      "seqid": "NMDC:1781_100325_scf_1153_c1",
      "start": 150,
      "end": 1080,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1153_c1_151_1080",
      "annotations": {
        "id": [
          "1781_100325_scf_1153_c1_151_1080"
        ],
        "product": [
          "riboflavin kinase/FMN adenylyltransferase"
        ],
        "cath_funfam": [
          "2.40.30.30",
          "3.40.50.620"
        ],
        "cog": [
          "COG0196"
        ],
        "ko": [
          "KO:K11753"
        ],
        "ec_number": [
          "EC:2.7.1.26",
          "EC:2.7.7.2"
        ],
        "pfam": [
          "FAD_sy",
          "Flavokinas"
        ],
        "superfamily": [
          "SM00904"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1153_c1_1200_1469": {
      "seqid": "NMDC:1781_100325_scf_1153_c1",
      "start": 1199,
      "end": 1469,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1153_c1_1200_1469",
      "annotations": {
        "id": [
          "1781_100325_scf_1153_c1_1200_1469"
        ],
        "product": [
          "small subunit ribosomal protein S15"
        ],
        "cath_funfam": [
          "1.10.287.10"
        ],
        "cog": [
          "COG0184"
        ],
        "ko": [
          "KO:K02956"
        ],
        "pfam": [
          "Ribosomal_S1"
        ],
        "superfamily": [
          "SM01387"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1154_c1": {
    "1781_100325_scf_1154_c1_1_1602": {
      "seqid": "NMDC:1781_100325_scf_1154_c1",
      "start": 0,
      "end": 1602,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1154_c1_1_1602",
      "annotations": {
        "id": [
          "1781_100325_scf_1154_c1_1_1602"
        ],
        "product": [
          "small subunit ribosomal protein S1"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG0539"
        ],
        "ko": [
          "KO:K02945"
        ],
        "pfam": [
          "S"
        ],
        "superfamily": [
          "SM00316"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1155_c1": {
    "1781_100325_scf_1155_c1_46_498": {
      "seqid": "NMDC:1781_100325_scf_1155_c1",
      "start": 45,
      "end": 498,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1155_c1_46_498",
      "annotations": {
        "id": [
          "1781_100325_scf_1155_c1_46_498"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1155_c1_896_1459": {
      "seqid": "NMDC:1781_100325_scf_1155_c1",
      "start": 895,
      "end": 1459,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1155_c1_896_1459",
      "annotations": {
        "id": [
          "1781_100325_scf_1155_c1_896_1459"
        ],
        "product": [
          "Zn-dependent protease"
        ],
        "cog": [
          "COG1994"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1155_c1_1436_1573": {
      "seqid": "NMDC:1781_100325_scf_1155_c1",
      "start": 1435,
      "end": 1573,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1155_c1_1436_1573",
      "annotations": {
        "id": [
          "1781_100325_scf_1155_c1_1436_1573"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1155_c1_1485_1607": {
      "seqid": "NMDC:1781_100325_scf_1155_c1",
      "start": 1484,
      "end": 1607,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1155_c1_1485_1607",
      "annotations": {
        "id": [
          "1781_100325_scf_1155_c1_1485_1607"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1156_c1": {
    "1781_100325_scf_1156_c1_3_749": {
      "seqid": "NMDC:1781_100325_scf_1156_c1",
      "start": 2,
      "end": 749,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1156_c1_3_749",
      "annotations": {
        "id": [
          "1781_100325_scf_1156_c1_3_749"
        ],
        "product": [
          "acetyl-CoA C-acetyltransferase"
        ],
        "cath_funfam": [
          "3.40.47.10"
        ],
        "cog": [
          "COG0183"
        ],
        "ko": [
          "KO:K00626"
        ],
        "ec_number": [
          "EC:2.3.1.9"
        ],
        "pfam": [
          "Thiolase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1156_c1_765_1160": {
      "seqid": "NMDC:1781_100325_scf_1156_c1",
      "start": 764,
      "end": 1160,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1156_c1_765_1160",
      "annotations": {
        "id": [
          "1781_100325_scf_1156_c1_765_1160"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.20.20.30"
        ],
        "cog": [
          "COG1545"
        ],
        "ko": [
          "KO:K07068"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1156_c1_1347_1607": {
      "seqid": "NMDC:1781_100325_scf_1156_c1",
      "start": 1346,
      "end": 1607,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1156_c1_1347_1607",
      "annotations": {
        "id": [
          "1781_100325_scf_1156_c1_1347_1607"
        ],
        "product": [
          "division protein CdvB (Snf7/Vps24/ESCRT-III family)"
        ],
        "cath_funfam": [
          "1.20.1170.10"
        ],
        "cog": [
          "COG5491"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1157_c1": {
    "1781_100325_scf_1157_c1_31_1353": {
      "seqid": "NMDC:1781_100325_scf_1157_c1",
      "start": 30,
      "end": 1353,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1157_c1_31_1353",
      "annotations": {
        "id": [
          "1781_100325_scf_1157_c1_31_1353"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1157_c1_1410_1553": {
      "seqid": "NMDC:1781_100325_scf_1157_c1",
      "start": 1409,
      "end": 1553,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1157_c1_1410_1553",
      "annotations": {
        "id": [
          "1781_100325_scf_1157_c1_1410_1553"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1158_c1": {
    "1781_100325_scf_1158_c1_3_113": {
      "seqid": "NMDC:1781_100325_scf_1158_c1",
      "start": 2,
      "end": 113,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1158_c1_3_113",
      "annotations": {
        "id": [
          "1781_100325_scf_1158_c1_3_113"
        ],
        "product": [
          "cyclic pyranopterin phosphate synthase"
        ],
        "ko": [
          "KO:K03639"
        ],
        "ec_number": [
          "EC:4.1.99.18"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1158_c1_119_754": {
      "seqid": "NMDC:1781_100325_scf_1158_c1",
      "start": 118,
      "end": 754,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1158_c1_119_754",
      "annotations": {
        "id": [
          "1781_100325_scf_1158_c1_119_754"
        ],
        "product": [
          "CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase"
        ],
        "cog": [
          "COG0558"
        ],
        "ko": [
          "KO:K00995"
        ],
        "ec_number": [
          "EC:2.7.8.5"
        ],
        "pfam": [
          "CDP-OH_P_trans"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1158_c1_781_1605": {
      "seqid": "NMDC:1781_100325_scf_1158_c1",
      "start": 780,
      "end": 1605,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1158_c1_781_1605",
      "annotations": {
        "id": [
          "1781_100325_scf_1158_c1_781_1605"
        ],
        "product": [
          "predicted transcriptional regulator"
        ],
        "cog": [
          "COG3905"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1159_c1": {
    "1781_100325_scf_1159_c1_1_522": {
      "seqid": "NMDC:1781_100325_scf_1159_c1",
      "start": 0,
      "end": 522,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1159_c1_1_522",
      "annotations": {
        "id": [
          "1781_100325_scf_1159_c1_1_522"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1159_c1_545_1462": {
      "seqid": "NMDC:1781_100325_scf_1159_c1",
      "start": 544,
      "end": 1462,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1159_c1_545_1462",
      "annotations": {
        "id": [
          "1781_100325_scf_1159_c1_545_1462"
        ],
        "product": [
          "transposase InsO family protein"
        ],
        "cath_funfam": [
          "3.30.420.10"
        ],
        "cog": [
          "COG2801"
        ],
        "pfam": [
          "HTH_2",
          "LZ_Tnp_IS48",
          "rv",
          "rve_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1159_c1_1459_1605": {
      "seqid": "NMDC:1781_100325_scf_1159_c1",
      "start": 1458,
      "end": 1605,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1159_c1_1459_1605",
      "annotations": {
        "id": [
          "1781_100325_scf_1159_c1_1459_1605"
        ],
        "product": [
          "LysM repeat protein"
        ],
        "cath_funfam": [
          "3.10.350.10"
        ],
        "cog": [
          "COG1388"
        ],
        "pfam": [
          "Lys"
        ],
        "superfamily": [
          "SM00257"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_115_c1": {
    "1781_100325_scf_115_c1_3_290": {
      "seqid": "NMDC:1781_100325_scf_115_c1",
      "start": 2,
      "end": 290,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_115_c1_3_290",
      "annotations": {
        "id": [
          "1781_100325_scf_115_c1_3_290"
        ],
        "product": [
          "ABC-type transporter Mla subunit MlaD"
        ],
        "cog": [
          "COG1463"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_115_c2": {
    "1781_100325_scf_115_c2_209_442": {
      "seqid": "NMDC:1781_100325_scf_115_c2",
      "start": 208,
      "end": 442,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_115_c2_209_442",
      "annotations": {
        "id": [
          "1781_100325_scf_115_c2_209_442"
        ],
        "product": [
          "DNA-binding Lrp family transcriptional regulator"
        ],
        "cath_funfam": [
          "3.30.70.920"
        ],
        "cog": [
          "COG1522"
        ],
        "pfam": [
          "AsnC_trans_re"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_115_c2_855_1034": {
      "seqid": "NMDC:1781_100325_scf_115_c2",
      "start": 854,
      "end": 1034,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_115_c2_855_1034",
      "annotations": {
        "id": [
          "1781_100325_scf_115_c2_855_1034"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_115_c2_1362_2147": {
      "seqid": "NMDC:1781_100325_scf_115_c2",
      "start": 1361,
      "end": 2147,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_115_c2_1362_2147",
      "annotations": {
        "id": [
          "1781_100325_scf_115_c2_1362_2147"
        ],
        "product": [
          "creatinine amidohydrolase"
        ],
        "cath_funfam": [
          "3.40.50.10310"
        ],
        "cog": [
          "COG1402"
        ],
        "ko": [
          "KO:K01470"
        ],
        "ec_number": [
          "EC:3.5.2.10"
        ],
        "pfam": [
          "Creatininas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_115_c2_2252_2464": {
      "seqid": "NMDC:1781_100325_scf_115_c2",
      "start": 2251,
      "end": 2464,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_115_c2_2252_2464",
      "annotations": {
        "id": [
          "1781_100325_scf_115_c2_2252_2464"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.20.25.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_115_c2_2683_2916": {
      "seqid": "NMDC:1781_100325_scf_115_c2",
      "start": 2682,
      "end": 2916,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_115_c2_2683_2916",
      "annotations": {
        "id": [
          "1781_100325_scf_115_c2_2683_2916"
        ],
        "product": [
          "malate dehydrogenase (oxaloacetate-decarboxylating)"
        ],
        "cath_funfam": [
          "3.40.50.10380"
        ],
        "cog": [
          "COG0281"
        ],
        "ko": [
          "KO:K00027"
        ],
        "ec_number": [
          "EC:1.1.1.38"
        ],
        "pfam": [
          "mali"
        ],
        "superfamily": [
          "SM01274"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1160_c1": {
    "1781_100325_scf_1160_c1_2_202": {
      "seqid": "NMDC:1781_100325_scf_1160_c1",
      "start": 1,
      "end": 202,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1160_c1_2_202",
      "annotations": {
        "id": [
          "1781_100325_scf_1160_c1_2_202"
        ],
        "product": [
          "geranylgeranyl diphosphate synthase type I"
        ],
        "cath_funfam": [
          "1.10.600.10"
        ],
        "cog": [
          "COG0142"
        ],
        "ko": [
          "KO:K13787"
        ],
        "ec_number": [
          "EC:2.5.1.1",
          "EC:2.5.1.10",
          "EC:2.5.1.29"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1160_c1_184_834": {
      "seqid": "NMDC:1781_100325_scf_1160_c1",
      "start": 183,
      "end": 834,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1160_c1_184_834",
      "annotations": {
        "id": [
          "1781_100325_scf_1160_c1_184_834"
        ],
        "product": [
          "isopentenyl-diphosphate delta-isomerase"
        ],
        "cath_funfam": [
          "3.90.79.10"
        ],
        "cog": [
          "COG1443"
        ],
        "ko": [
          "KO:K01823"
        ],
        "ec_number": [
          "EC:5.3.3.2"
        ],
        "pfam": [
          "NUDI"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1160_c1_834_1571": {
      "seqid": "NMDC:1781_100325_scf_1160_c1",
      "start": 833,
      "end": 1571,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1160_c1_834_1571",
      "annotations": {
        "id": [
          "1781_100325_scf_1160_c1_834_1571"
        ],
        "product": [
          "isopentenyl phosphate kinase"
        ],
        "cath_funfam": [
          "3.40.1160.10"
        ],
        "cog": [
          "COG1608"
        ],
        "ko": [
          "KO:K06981"
        ],
        "ec_number": [
          "EC:2.7.4.26"
        ],
        "pfam": [
          "AA_kinas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1161_c1": {
    "1781_100325_scf_1161_c1_675_1316": {
      "seqid": "NMDC:1781_100325_scf_1161_c1",
      "start": 674,
      "end": 1316,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1161_c1_675_1316",
      "annotations": {
        "id": [
          "1781_100325_scf_1161_c1_675_1316"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.8.10",
          "3.30.160.60"
        ],
        "superfamily": [
          "SM00355"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1161_c1_1461_1601": {
      "seqid": "NMDC:1781_100325_scf_1161_c1",
      "start": 1460,
      "end": 1601,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1161_c1_1461_1601",
      "annotations": {
        "id": [
          "1781_100325_scf_1161_c1_1461_1601"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1162_c1": {
    "1781_100325_scf_1162_c1_274_987": {
      "seqid": "NMDC:1781_100325_scf_1162_c1",
      "start": 273,
      "end": 987,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1162_c1_274_987",
      "annotations": {
        "id": [
          "1781_100325_scf_1162_c1_274_987"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1162_c1_951_1184": {
      "seqid": "NMDC:1781_100325_scf_1162_c1",
      "start": 950,
      "end": 1184,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1162_c1_951_1184",
      "annotations": {
        "id": [
          "1781_100325_scf_1162_c1_951_1184"
        ],
        "product": [
          "predicted transcriptional regulator"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG3355"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1162_c1_1286_1603": {
      "seqid": "NMDC:1781_100325_scf_1162_c1",
      "start": 1285,
      "end": 1603,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1162_c1_1286_1603",
      "annotations": {
        "id": [
          "1781_100325_scf_1162_c1_1286_1603"
        ],
        "product": [
          "argininosuccinate synthase"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "cog": [
          "COG0137"
        ],
        "ko": [
          "KO:K01940"
        ],
        "ec_number": [
          "EC:6.3.4.5"
        ],
        "pfam": [
          "Arginosuc_synt",
          "Que"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1163_c1": {
    "1781_100325_scf_1163_c1_52_1602": {
      "seqid": "NMDC:1781_100325_scf_1163_c1",
      "start": 51,
      "end": 1602,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1163_c1_52_1602",
      "annotations": {
        "id": [
          "1781_100325_scf_1163_c1_52_1602"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_IS6"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1164_c1": {
    "1781_100325_scf_1164_c1_3_131": {
      "seqid": "NMDC:1781_100325_scf_1164_c1",
      "start": 2,
      "end": 131,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1164_c1_3_131",
      "annotations": {
        "id": [
          "1781_100325_scf_1164_c1_3_131"
        ],
        "product": [
          "DNA-binding beta-propeller fold protein YncE"
        ],
        "cath_funfam": [
          "2.120.10.30"
        ],
        "cog": [
          "COG3391"
        ],
        "pfam": [
          "NH"
        ],
        "superfamily": [
          "SM00135"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1164_c1_228_1601": {
      "seqid": "NMDC:1781_100325_scf_1164_c1",
      "start": 227,
      "end": 1601,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1164_c1_228_1601",
      "annotations": {
        "id": [
          "1781_100325_scf_1164_c1_228_1601"
        ],
        "product": [
          "phenylalanyl-tRNA synthetase beta chain"
        ],
        "cath_funfam": [
          "3.30.56.10",
          "3.30.930.10",
          "3.50.40.10"
        ],
        "cog": [
          "COG0072"
        ],
        "ko": [
          "KO:K01890"
        ],
        "ec_number": [
          "EC:6.1.1.20"
        ],
        "pfam": [
          "B",
          "B3_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1165_c1": {
    "1781_100325_scf_1165_c1_73_948": {
      "seqid": "NMDC:1781_100325_scf_1165_c1",
      "start": 72,
      "end": 948,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1165_c1_73_948",
      "annotations": {
        "id": [
          "1781_100325_scf_1165_c1_73_948"
        ],
        "product": [
          "glycosyltransferase involved in cell wall biosynthesis"
        ],
        "cath_funfam": [
          "3.40.50.2000"
        ],
        "cog": [
          "COG0438"
        ],
        "pfam": [
          "Glyco_trans_1_",
          "Glycos_transf_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1165_c1_945_1601": {
      "seqid": "NMDC:1781_100325_scf_1165_c1",
      "start": 944,
      "end": 1601,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1165_c1_945_1601",
      "annotations": {
        "id": [
          "1781_100325_scf_1165_c1_945_1601"
        ],
        "product": [
          "UDP-perosamine 4-acetyltransferase"
        ],
        "cath_funfam": [
          "2.160.10.10"
        ],
        "cog": [
          "COG0110"
        ],
        "ko": [
          "KO:K13006"
        ],
        "ec_number": [
          "EC:2.3.1.-"
        ],
        "pfam": [
          "Hexape",
          "Hexapep_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1166_c1": {
    "1781_100325_scf_1166_c1_2_664": {
      "seqid": "NMDC:1781_100325_scf_1166_c1",
      "start": 1,
      "end": 664,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1166_c1_2_664",
      "annotations": {
        "id": [
          "1781_100325_scf_1166_c1_2_664"
        ],
        "product": [
          "ribose-phosphate pyrophosphokinase"
        ],
        "cath_funfam": [
          "3.40.50.2020"
        ],
        "cog": [
          "COG0462"
        ],
        "ko": [
          "KO:K00948"
        ],
        "ec_number": [
          "EC:2.7.6.1"
        ],
        "pfam": [
          "Pribosyl_synt",
          "Pribosyltra"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1166_c1_681_1598": {
      "seqid": "NMDC:1781_100325_scf_1166_c1",
      "start": 680,
      "end": 1598,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1166_c1_681_1598",
      "annotations": {
        "id": [
          "1781_100325_scf_1166_c1_681_1598"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1167_c1": {
    "1781_100325_scf_1167_c1_1_1041": {
      "seqid": "NMDC:1781_100325_scf_1167_c1",
      "start": 0,
      "end": 1041,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1167_c1_1_1041",
      "annotations": {
        "id": [
          "1781_100325_scf_1167_c1_1_1041"
        ],
        "product": [
          "elongation factor 2"
        ],
        "cath_funfam": [
          "2.40.30.10",
          "3.40.50.300"
        ],
        "cog": [
          "COG0480"
        ],
        "ko": [
          "KO:K03234"
        ],
        "pfam": [
          "GTP_EFT"
        ],
        "superfamily": [
          "SM00739"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1167_c1_1182_1601": {
      "seqid": "NMDC:1781_100325_scf_1167_c1",
      "start": 1181,
      "end": 1601,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1167_c1_1182_1601",
      "annotations": {
        "id": [
          "1781_100325_scf_1167_c1_1182_1601"
        ],
        "product": [
          "1",
          "4-dihydroxy-6-naphthoate synthase"
        ],
        "cog": [
          "COG2107"
        ],
        "ko": [
          "KO:K11785"
        ],
        "ec_number": [
          "EC:1.14.-"
        ],
        "pfam": [
          "VitK2_biosynt"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1168_c1": {
    "1781_100325_scf_1168_c1_1_255": {
      "seqid": "NMDC:1781_100325_scf_1168_c1",
      "start": 0,
      "end": 255,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1168_c1_1_255",
      "annotations": {
        "id": [
          "1781_100325_scf_1168_c1_1_255"
        ],
        "product": [
          "plastocyanin"
        ],
        "cath_funfam": [
          "2.60.40.420"
        ],
        "cog": [
          "COG3794"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1168_c1_400_1302": {
      "seqid": "NMDC:1781_100325_scf_1168_c1",
      "start": 399,
      "end": 1302,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1168_c1_400_1302",
      "annotations": {
        "id": [
          "1781_100325_scf_1168_c1_400_1302"
        ],
        "product": [
          "transposase InsO family protein"
        ],
        "cath_funfam": [
          "1.10.10.60",
          "3.30.420.10"
        ],
        "cog": [
          "COG2801"
        ],
        "pfam": [
          "HTH_2",
          "LZ_Tnp_IS48",
          "rv",
          "rve_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1169_c1": {
    "1781_100325_scf_1169_c1_1_1143": {
      "seqid": "NMDC:1781_100325_scf_1169_c1",
      "start": 0,
      "end": 1143,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1169_c1_1_1143",
      "annotations": {
        "id": [
          "1781_100325_scf_1169_c1_1_1143"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_116_c1": {
    "1781_100325_scf_116_c1_3_221": {
      "seqid": "NMDC:1781_100325_scf_116_c1",
      "start": 2,
      "end": 221,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_116_c1_3_221",
      "annotations": {
        "id": [
          "1781_100325_scf_116_c1_3_221"
        ],
        "product": [
          "putative N-acetylmannosamine-6-phosphate epimerase"
        ],
        "cog": [
          "COG3010"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_116_c1_224_928": {
      "seqid": "NMDC:1781_100325_scf_116_c1",
      "start": 223,
      "end": 928,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_116_c1_224_928",
      "annotations": {
        "id": [
          "1781_100325_scf_116_c1_224_928"
        ],
        "product": [
          "deoxyribose-phosphate aldolase"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "cog": [
          "COG0274"
        ],
        "ko": [
          "KO:K01619"
        ],
        "ec_number": [
          "EC:4.1.2.4"
        ],
        "pfam": [
          "Deo"
        ],
        "superfamily": [
          "SM01133"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_116_c1_1028_1819": {
      "seqid": "NMDC:1781_100325_scf_116_c1",
      "start": 1027,
      "end": 1819,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_116_c1_1028_1819",
      "annotations": {
        "id": [
          "1781_100325_scf_116_c1_1028_1819"
        ],
        "product": [
          "acyl-CoA reductase-like NAD-dependent aldehyde dehydrogenase"
        ],
        "cath_funfam": [
          "3.40.605.10"
        ],
        "cog": [
          "COG1012"
        ],
        "pfam": [
          "Alded"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_116_c1_1914_3392": {
      "seqid": "NMDC:1781_100325_scf_116_c1",
      "start": 1913,
      "end": 3392,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_116_c1_1914_3392",
      "annotations": {
        "id": [
          "1781_100325_scf_116_c1_1914_3392"
        ],
        "product": [
          "aldehyde dehydrogenase (NAD+)"
        ],
        "cath_funfam": [
          "3.40.309.10",
          "3.40.605.10"
        ],
        "cog": [
          "COG1012"
        ],
        "ko": [
          "KO:K00128"
        ],
        "ec_number": [
          "EC:1.2.1.3"
        ],
        "pfam": [
          "Alded"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_116_c1_3442_3693": {
      "seqid": "NMDC:1781_100325_scf_116_c1",
      "start": 3441,
      "end": 3693,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_116_c1_3442_3693",
      "annotations": {
        "id": [
          "1781_100325_scf_116_c1_3442_3693"
        ],
        "product": [
          "deoxyribose-phosphate aldolase"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "cog": [
          "COG0274"
        ],
        "ko": [
          "KO:K01619"
        ],
        "ec_number": [
          "EC:4.1.2.4"
        ],
        "superfamily": [
          "SM01133"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1170_c1": {
    "1781_100325_scf_1170_c1_2_835": {
      "seqid": "NMDC:1781_100325_scf_1170_c1",
      "start": 1,
      "end": 835,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1170_c1_2_835",
      "annotations": {
        "id": [
          "1781_100325_scf_1170_c1_2_835"
        ],
        "product": [
          "N-acetyl-gamma-glutamyl-phosphate/LysW-gamma-L-alpha-aminoadipyl-6-phosphate reductase"
        ],
        "cath_funfam": [
          "3.30.360.10",
          "3.40.50.720"
        ],
        "cog": [
          "COG0002"
        ],
        "ko": [
          "KO:K05829"
        ],
        "ec_number": [
          "EC:1.2.1.-"
        ],
        "pfam": [
          "Semialdhyde_d",
          "Semialdhyde_dh"
        ],
        "superfamily": [
          "SM00859"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1170_c1_866_1597": {
      "seqid": "NMDC:1781_100325_scf_1170_c1",
      "start": 865,
      "end": 1597,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1170_c1_866_1597",
      "annotations": {
        "id": [
          "1781_100325_scf_1170_c1_866_1597"
        ],
        "product": [
          "[lysine-biosynthesis-protein LysW]--L-2-aminoadipate ligase"
        ],
        "cath_funfam": [
          "3.30.1490.20"
        ],
        "cog": [
          "COG0189"
        ],
        "ko": [
          "KO:K05827"
        ],
        "ec_number": [
          "EC:6.3.2.43"
        ],
        "pfam": [
          "ATP-gras",
          "ATP-grasp_",
          "CPSase_L_D",
          "GSH-S_AT",
          "Rim"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1171_c1": {
    "1781_100325_scf_1171_c1_43_1596": {
      "seqid": "NMDC:1781_100325_scf_1171_c1",
      "start": 42,
      "end": 1596,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1171_c1_43_1596",
      "annotations": {
        "id": [
          "1781_100325_scf_1171_c1_43_1596"
        ],
        "product": [
          "cytochrome c oxidase subunit 1"
        ],
        "cath_funfam": [
          "1.20.210.10"
        ],
        "cog": [
          "COG0843"
        ],
        "ko": [
          "KO:K02274"
        ],
        "ec_number": [
          "EC:1.9.3.1"
        ],
        "pfam": [
          "COX"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1172_c1": {
    "1781_100325_scf_1172_c1_47_574": {
      "seqid": "NMDC:1781_100325_scf_1172_c1",
      "start": 46,
      "end": 574,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1172_c1_47_574",
      "annotations": {
        "id": [
          "1781_100325_scf_1172_c1_47_574"
        ],
        "product": [
          "aconitate hydratase"
        ],
        "cath_funfam": [
          "3.20.19.10"
        ],
        "cog": [
          "COG1048"
        ],
        "ko": [
          "KO:K01681"
        ],
        "ec_number": [
          "EC:4.2.1.3"
        ],
        "pfam": [
          "Aconitase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1172_c1_586_1233": {
      "seqid": "NMDC:1781_100325_scf_1172_c1",
      "start": 585,
      "end": 1233,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1172_c1_586_1233",
      "annotations": {
        "id": [
          "1781_100325_scf_1172_c1_586_1233"
        ],
        "product": [
          "5'-phosphate synthase pdxT subunit"
        ],
        "cath_funfam": [
          "3.40.50.880"
        ],
        "cog": [
          "COG0311"
        ],
        "ko": [
          "KO:K08681"
        ],
        "ec_number": [
          "EC:4.3.3.6"
        ],
        "pfam": [
          "GATas",
          "GATase_",
          "Peptidase_S5",
          "SN"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1172_c1_1230_1595": {
      "seqid": "NMDC:1781_100325_scf_1172_c1",
      "start": 1229,
      "end": 1595,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1172_c1_1230_1595",
      "annotations": {
        "id": [
          "1781_100325_scf_1172_c1_1230_1595"
        ],
        "product": [
          "pyridoxal 5'-phosphate synthase pdxS subunit"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "cog": [
          "COG0214"
        ],
        "ko": [
          "KO:K06215"
        ],
        "ec_number": [
          "EC:4.3.3.6"
        ],
        "pfam": [
          "SOR_SN",
          "Thi"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1173_c1": {
    "1781_100325_scf_1173_c1_3_1133": {
      "seqid": "NMDC:1781_100325_scf_1173_c1",
      "start": 2,
      "end": 1133,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1173_c1_3_1133",
      "annotations": {
        "id": [
          "1781_100325_scf_1173_c1_3_1133"
        ],
        "product": [
          "DNA polymerase I"
        ],
        "cath_funfam": [
          "3.90.1600.10"
        ],
        "cog": [
          "COG0417"
        ],
        "ko": [
          "KO:K02319"
        ],
        "ec_number": [
          "EC:2.7.7.7"
        ],
        "pfam": [
          "DNA_pol_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1173_c1_1198_1596": {
      "seqid": "NMDC:1781_100325_scf_1173_c1",
      "start": 1197,
      "end": 1596,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1173_c1_1198_1596",
      "annotations": {
        "id": [
          "1781_100325_scf_1173_c1_1198_1596"
        ],
        "product": [
          "arginase family enzyme"
        ],
        "cath_funfam": [
          "3.40.800.10"
        ],
        "cog": [
          "COG0010"
        ],
        "pfam": [
          "Arginas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1174_c1": {
    "1781_100325_scf_1174_c1_217_1134": {
      "seqid": "NMDC:1781_100325_scf_1174_c1",
      "start": 216,
      "end": 1134,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1174_c1_217_1134",
      "annotations": {
        "id": [
          "1781_100325_scf_1174_c1_217_1134"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "TIR-lik"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1175_c1": {
    "1781_100325_scf_1175_c1_2_1567": {
      "seqid": "NMDC:1781_100325_scf_1175_c1",
      "start": 1,
      "end": 1567,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1175_c1_2_1567",
      "annotations": {
        "id": [
          "1781_100325_scf_1175_c1_2_1567"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "LVIV"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1176_c1": {
    "1781_100325_scf_1176_c1_1_282": {
      "seqid": "NMDC:1781_100325_scf_1176_c1",
      "start": 0,
      "end": 282,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1176_c1_1_282",
      "annotations": {
        "id": [
          "1781_100325_scf_1176_c1_1_282"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1176_c1_974_1594": {
      "seqid": "NMDC:1781_100325_scf_1176_c1",
      "start": 973,
      "end": 1594,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1176_c1_974_1594",
      "annotations": {
        "id": [
          "1781_100325_scf_1176_c1_974_1594"
        ],
        "product": [
          "Ca2+-binding RTX toxin-like protein"
        ],
        "cath_funfam": [
          "2.150.10.10"
        ],
        "cog": [
          "COG2931"
        ],
        "pfam": [
          "HemolysinCabin"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1177_c1": {
    "1781_100325_scf_1177_c1_3_161": {
      "seqid": "NMDC:1781_100325_scf_1177_c1",
      "start": 2,
      "end": 161,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1177_c1_3_161",
      "annotations": {
        "id": [
          "1781_100325_scf_1177_c1_3_161"
        ],
        "product": [
          "glutathione S-transferase"
        ],
        "cath_funfam": [
          "3.40.30.10"
        ],
        "cog": [
          "COG0625"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1177_c1_334_1416": {
      "seqid": "NMDC:1781_100325_scf_1177_c1",
      "start": 333,
      "end": 1416,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1177_c1_334_1416",
      "annotations": {
        "id": [
          "1781_100325_scf_1177_c1_334_1416"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3666"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DDE_Tnp_1_",
          "DUF77"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1178_c1": {
    "1781_100325_scf_1178_c1_2_88": {
      "seqid": "NMDC:1781_100325_scf_1178_c1",
      "start": 1,
      "end": 88,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1178_c1_2_88",
      "annotations": {
        "id": [
          "1781_100325_scf_1178_c1_2_88"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1178_c1_129_818": {
      "seqid": "NMDC:1781_100325_scf_1178_c1",
      "start": 128,
      "end": 818,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1178_c1_129_818",
      "annotations": {
        "id": [
          "1781_100325_scf_1178_c1_129_818"
        ],
        "product": [
          "GMP synthase (glutamine-hydrolysing)"
        ],
        "cath_funfam": [
          "3.40.50.880"
        ],
        "cog": [
          "COG0518"
        ],
        "ko": [
          "KO:K01951"
        ],
        "ec_number": [
          "EC:6.3.5.2"
        ],
        "pfam": [
          "GATas",
          "Peptidase_C2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1178_c1_815_1594": {
      "seqid": "NMDC:1781_100325_scf_1178_c1",
      "start": 814,
      "end": 1594,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1178_c1_815_1594",
      "annotations": {
        "id": [
          "1781_100325_scf_1178_c1_815_1594"
        ],
        "product": [
          "NAD-dependent deacetylase"
        ],
        "cath_funfam": [
          "3.40.50.1220"
        ],
        "cog": [
          "COG0846"
        ],
        "ko": [
          "KO:K12410"
        ],
        "ec_number": [
          "EC:3.5.1.-"
        ],
        "pfam": [
          "SIR"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1179_c1": {
    "1781_100325_scf_1179_c1_3_353": {
      "seqid": "NMDC:1781_100325_scf_1179_c1",
      "start": 2,
      "end": 353,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1179_c1_3_353",
      "annotations": {
        "id": [
          "1781_100325_scf_1179_c1_3_353"
        ],
        "product": [
          "signal transduction histidine kinase"
        ],
        "cath_funfam": [
          "1.20.5.170"
        ],
        "cog": [
          "COG4585"
        ],
        "pfam": [
          "HisKA_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1179_c1_562_1593": {
      "seqid": "NMDC:1781_100325_scf_1179_c1",
      "start": 561,
      "end": 1593,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1179_c1_562_1593",
      "annotations": {
        "id": [
          "1781_100325_scf_1179_c1_562_1593"
        ],
        "product": [
          "Fe-S oxidoreductase"
        ],
        "cog": [
          "COG0247"
        ],
        "pfam": [
          "CC"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_117_c1": {
    "1781_100325_scf_117_c1_3_77": {
      "seqid": "NMDC:1781_100325_scf_117_c1",
      "start": 2,
      "end": 77,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_117_c1_3_77",
      "annotations": {
        "id": [
          "1781_100325_scf_117_c1_3_77"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_117_c1_118_471": {
      "seqid": "NMDC:1781_100325_scf_117_c1",
      "start": 117,
      "end": 471,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_117_c1_118_471",
      "annotations": {
        "id": [
          "1781_100325_scf_117_c1_118_471"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_117_c1_1042_1320": {
      "seqid": "NMDC:1781_100325_scf_117_c1",
      "start": 1041,
      "end": 1320,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_117_c1_1042_1320",
      "annotations": {
        "id": [
          "1781_100325_scf_117_c1_1042_1320"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.150.20"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_117_c1_1650_2174": {
      "seqid": "NMDC:1781_100325_scf_117_c1",
      "start": 1649,
      "end": 2174,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_117_c1_1650_2174",
      "annotations": {
        "id": [
          "1781_100325_scf_117_c1_1650_2174"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.443.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_117_c1_2343_3491": {
      "seqid": "NMDC:1781_100325_scf_117_c1",
      "start": 2342,
      "end": 3491,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_117_c1_2343_3491",
      "annotations": {
        "id": [
          "1781_100325_scf_117_c1_2343_3491"
        ],
        "product": [
          "glycosyltransferase involved in cell wall biosynthesis"
        ],
        "cath_funfam": [
          "3.40.50.2000"
        ],
        "cog": [
          "COG0438"
        ],
        "pfam": [
          "Glyco_trans_1_",
          "Glyco_transf_",
          "Glycos_transf_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1180_c1": {
    "1781_100325_scf_1180_c1_1_669": {
      "seqid": "NMDC:1781_100325_scf_1180_c1",
      "start": 0,
      "end": 669,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1180_c1_1_669",
      "annotations": {
        "id": [
          "1781_100325_scf_1180_c1_1_669"
        ],
        "product": [
          "zinc transport system ATP-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1121"
        ],
        "ko": [
          "KO:K09817"
        ],
        "ec_number": [
          "EC:3.6.3.-"
        ],
        "pfam": [
          "AAA_2",
          "ABC_tra"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1180_c1_657_1571": {
      "seqid": "NMDC:1781_100325_scf_1180_c1",
      "start": 656,
      "end": 1571,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1180_c1_657_1571",
      "annotations": {
        "id": [
          "1781_100325_scf_1180_c1_657_1571"
        ],
        "product": [
          "zinc transport system substrate-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.1980"
        ],
        "cog": [
          "COG0803"
        ],
        "ko": [
          "KO:K09815"
        ],
        "pfam": [
          "Znu"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1181_c1": {
    "1781_100325_scf_1181_c1_1_114": {
      "seqid": "NMDC:1781_100325_scf_1181_c1",
      "start": 0,
      "end": 114,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1181_c1_1_114",
      "annotations": {
        "id": [
          "1781_100325_scf_1181_c1_1_114"
        ],
        "product": [
          "5-methyltetrahydrofolate--homocysteine methyltransferase"
        ],
        "cath_funfam": [
          "3.20.20.330"
        ],
        "cog": [
          "COG0646"
        ],
        "ko": [
          "KO:K00548"
        ],
        "ec_number": [
          "EC:2.1.1.13"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1181_c1_583_1065": {
      "seqid": "NMDC:1781_100325_scf_1181_c1",
      "start": 582,
      "end": 1065,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1181_c1_583_1065",
      "annotations": {
        "id": [
          "1781_100325_scf_1181_c1_583_1065"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1181_c1_1224_1592": {
      "seqid": "NMDC:1781_100325_scf_1181_c1",
      "start": 1223,
      "end": 1592,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1181_c1_1224_1592",
      "annotations": {
        "id": [
          "1781_100325_scf_1181_c1_1224_1592"
        ],
        "product": [
          "hypothetical protein"
        ],
        "superfamily": [
          "SM00184"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1182_c1": {
    "1781_100325_scf_1182_c1_32_331": {
      "seqid": "NMDC:1781_100325_scf_1182_c1",
      "start": 31,
      "end": 331,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1182_c1_32_331",
      "annotations": {
        "id": [
          "1781_100325_scf_1182_c1_32_331"
        ],
        "product": [
          "anti-anti-sigma regulatory factor"
        ],
        "cath_funfam": [
          "3.30.750.24"
        ],
        "cog": [
          "COG1366"
        ],
        "pfam": [
          "STAS_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1182_c1_372_1379": {
      "seqid": "NMDC:1781_100325_scf_1182_c1",
      "start": 371,
      "end": 1379,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1182_c1_372_1379",
      "annotations": {
        "id": [
          "1781_100325_scf_1182_c1_372_1379"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.60.120.10"
        ],
        "cog": [
          "COG1741"
        ],
        "ko": [
          "KO:K06911"
        ],
        "pfam": [
          "Piri",
          "Pirin_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1183_c1": {
    "1781_100325_scf_1183_c1_1_468": {
      "seqid": "NMDC:1781_100325_scf_1183_c1",
      "start": 0,
      "end": 468,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1183_c1_1_468",
      "annotations": {
        "id": [
          "1781_100325_scf_1183_c1_1_468"
        ],
        "product": [
          "ABC-type glycerol-3-phosphate transport system substrate-binding protein"
        ],
        "cog": [
          "COG1653"
        ],
        "pfam": [
          "SBP_bac_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1183_c1_478_1590": {
      "seqid": "NMDC:1781_100325_scf_1183_c1",
      "start": 477,
      "end": 1590,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1183_c1_478_1590",
      "annotations": {
        "id": [
          "1781_100325_scf_1183_c1_478_1590"
        ],
        "product": [
          "alpha-glucoside transport system permease protein"
        ],
        "cath_funfam": [
          "1.10.3720.10"
        ],
        "cog": [
          "COG1175"
        ],
        "ko": [
          "KO:K10233"
        ],
        "pfam": [
          "BPD_transp_",
          "CarboxypepD_re",
          "SdrD_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1184_c1": {
    "1781_100325_scf_1184_c1_2_100": {
      "seqid": "NMDC:1781_100325_scf_1184_c1",
      "start": 1,
      "end": 100,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1184_c1_2_100",
      "annotations": {
        "id": [
          "1781_100325_scf_1184_c1_2_100"
        ],
        "product": [
          "ribosomal protein L23"
        ],
        "cath_funfam": [
          "3.30.70.330"
        ],
        "cog": [
          "COG0089"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1184_c1_100_912": {
      "seqid": "NMDC:1781_100325_scf_1184_c1",
      "start": 99,
      "end": 912,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1184_c1_100_912",
      "annotations": {
        "id": [
          "1781_100325_scf_1184_c1_100_912"
        ],
        "product": [
          "large subunit ribosomal protein L4e"
        ],
        "cath_funfam": [
          "3.40.1370.10"
        ],
        "cog": [
          "COG0088"
        ],
        "ko": [
          "KO:K02930"
        ],
        "pfam": [
          "Ribosomal_L"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1184_c1_909_1592": {
      "seqid": "NMDC:1781_100325_scf_1184_c1",
      "start": 908,
      "end": 1592,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1184_c1_909_1592",
      "annotations": {
        "id": [
          "1781_100325_scf_1184_c1_909_1592"
        ],
        "product": [
          "large subunit ribosomal protein L3"
        ],
        "cath_funfam": [
          "2.40.30.10"
        ],
        "cog": [
          "COG0087"
        ],
        "ko": [
          "KO:K02906"
        ],
        "pfam": [
          "Ribosomal_L"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1185_c1": {
    "1781_100325_scf_1185_c1_289_1215": {
      "seqid": "NMDC:1781_100325_scf_1185_c1",
      "start": 288,
      "end": 1215,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1185_c1_289_1215",
      "annotations": {
        "id": [
          "1781_100325_scf_1185_c1_289_1215"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG0613"
        ],
        "ko": [
          "KO:K07053"
        ],
        "pfam": [
          "PHP_"
        ],
        "superfamily": [
          "SM00481"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1185_c1_1279_1458": {
      "seqid": "NMDC:1781_100325_scf_1185_c1",
      "start": 1278,
      "end": 1458,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1185_c1_1279_1458",
      "annotations": {
        "id": [
          "1781_100325_scf_1185_c1_1279_1458"
        ],
        "product": [
          "CDGSH-type Zn-finger protein"
        ],
        "cog": [
          "COG3369"
        ],
        "pfam": [
          "zf-CDGS"
        ],
        "superfamily": [
          "SM00704"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1185_c1_1474_1590": {
      "seqid": "NMDC:1781_100325_scf_1185_c1",
      "start": 1473,
      "end": 1590,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1185_c1_1474_1590",
      "annotations": {
        "id": [
          "1781_100325_scf_1185_c1_1474_1590"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1186_c1": {
    "1781_100325_scf_1186_c1_11_457": {
      "seqid": "NMDC:1781_100325_scf_1186_c1",
      "start": 10,
      "end": 457,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1186_c1_11_457",
      "annotations": {
        "id": [
          "1781_100325_scf_1186_c1_11_457"
        ],
        "product": [
          "transposase-like protein"
        ],
        "cog": [
          "COG3328"
        ],
        "pfam": [
          "Transposase_mu"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1186_c1_417_1370": {
      "seqid": "NMDC:1781_100325_scf_1186_c1",
      "start": 416,
      "end": 1370,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1186_c1_417_1370",
      "annotations": {
        "id": [
          "1781_100325_scf_1186_c1_417_1370"
        ],
        "product": [
          "aminoglycoside phosphotransferase (APT) family kinase protein"
        ],
        "cog": [
          "COG3173"
        ],
        "pfam": [
          "AP"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1186_c1_1475_1588": {
      "seqid": "NMDC:1781_100325_scf_1186_c1",
      "start": 1474,
      "end": 1588,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1186_c1_1475_1588",
      "annotations": {
        "id": [
          "1781_100325_scf_1186_c1_1475_1588"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1187_c1": {
    "1781_100325_scf_1187_c1_87_485": {
      "seqid": "NMDC:1781_100325_scf_1187_c1",
      "start": 86,
      "end": 485,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1187_c1_87_485",
      "annotations": {
        "id": [
          "1781_100325_scf_1187_c1_87_485"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1187_c1_595_1206": {
      "seqid": "NMDC:1781_100325_scf_1187_c1",
      "start": 594,
      "end": 1206,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1187_c1_595_1206",
      "annotations": {
        "id": [
          "1781_100325_scf_1187_c1_595_1206"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1187_c1_1206_1589": {
      "seqid": "NMDC:1781_100325_scf_1187_c1",
      "start": 1205,
      "end": 1589,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1187_c1_1206_1589",
      "annotations": {
        "id": [
          "1781_100325_scf_1187_c1_1206_1589"
        ],
        "product": [
          "outer membrane biosynthesis protein TonB"
        ],
        "cog": [
          "COG0810"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1187_c1_1510_1590": {
      "seqid": "NMDC:1781_100325_scf_1187_c1",
      "start": 1509,
      "end": 1590,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1187_c1_1510_1590",
      "annotations": {
        "id": [
          "1781_100325_scf_1187_c1_1510_1590"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1188_c1": {
    "1781_100325_scf_1188_c1_125_718": {
      "seqid": "NMDC:1781_100325_scf_1188_c1",
      "start": 124,
      "end": 718,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1188_c1_125_718",
      "annotations": {
        "id": [
          "1781_100325_scf_1188_c1_125_718"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1188_c1_779_1588": {
      "seqid": "NMDC:1781_100325_scf_1188_c1",
      "start": 778,
      "end": 1588,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1188_c1_779_1588",
      "annotations": {
        "id": [
          "1781_100325_scf_1188_c1_779_1588"
        ],
        "product": [
          "Fanconi anemia group M protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0513"
        ],
        "ko": [
          "KO:K10896"
        ],
        "pfam": [
          "Helicase_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1189_c1": {
    "1781_100325_scf_1189_c1_140_676": {
      "seqid": "NMDC:1781_100325_scf_1189_c1",
      "start": 139,
      "end": 676,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1189_c1_140_676",
      "annotations": {
        "id": [
          "1781_100325_scf_1189_c1_140_676"
        ],
        "product": [
          "site-specific recombinase XerD"
        ],
        "cath_funfam": [
          "1.10.443.10"
        ],
        "cog": [
          "COG4974"
        ],
        "pfam": [
          "Phage_integras"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1189_c1_673_1587": {
      "seqid": "NMDC:1781_100325_scf_1189_c1",
      "start": 672,
      "end": 1587,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1189_c1_673_1587",
      "annotations": {
        "id": [
          "1781_100325_scf_1189_c1_673_1587"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_118_c1": {
    "1781_100325_scf_118_c1_2_178": {
      "seqid": "NMDC:1781_100325_scf_118_c1",
      "start": 1,
      "end": 178,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_118_c1_2_178",
      "annotations": {
        "id": [
          "1781_100325_scf_118_c1_2_178"
        ],
        "product": [
          "glucose/arabinose dehydrogenase"
        ],
        "cog": [
          "COG2133"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_118_c1_190_1452": {
      "seqid": "NMDC:1781_100325_scf_118_c1",
      "start": 189,
      "end": 1452,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_118_c1_190_1452",
      "annotations": {
        "id": [
          "1781_100325_scf_118_c1_190_1452"
        ],
        "product": [
          "hydroxymethylglutaryl-CoA reductase"
        ],
        "cath_funfam": [
          "3.90.770.10"
        ],
        "cog": [
          "COG1257"
        ],
        "ko": [
          "KO:K00054"
        ],
        "ec_number": [
          "EC:1.1.1.88"
        ],
        "pfam": [
          "HMG-CoA_re"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_118_c1_1580_2557": {
      "seqid": "NMDC:1781_100325_scf_118_c1",
      "start": 1579,
      "end": 2557,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_118_c1_1580_2557",
      "annotations": {
        "id": [
          "1781_100325_scf_118_c1_1580_2557"
        ],
        "product": [
          "ATP phosphoribosyltransferase"
        ],
        "cath_funfam": [
          "3.30.70.120",
          "3.40.190.10"
        ],
        "cog": [
          "COG0040"
        ],
        "ko": [
          "KO:K00765"
        ],
        "ec_number": [
          "EC:2.4.2.17"
        ],
        "pfam": [
          "His",
          "HisG_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_118_c1_2554_3702": {
      "seqid": "NMDC:1781_100325_scf_118_c1",
      "start": 2553,
      "end": 3702,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_118_c1_2554_3702",
      "annotations": {
        "id": [
          "1781_100325_scf_118_c1_2554_3702"
        ],
        "product": [
          "histidinol dehydrogenase"
        ],
        "cath_funfam": [
          "3.40.50.1980"
        ],
        "cog": [
          "COG0141"
        ],
        "ko": [
          "KO:K00013"
        ],
        "ec_number": [
          "EC:1.1.1.23"
        ],
        "pfam": [
          "Histidinol_d"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1190_c1": {
    "1781_100325_scf_1190_c1_190_360": {
      "seqid": "NMDC:1781_100325_scf_1190_c1",
      "start": 189,
      "end": 360,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1190_c1_190_360",
      "annotations": {
        "id": [
          "1781_100325_scf_1190_c1_190_360"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1190_c1_457_1200": {
      "seqid": "NMDC:1781_100325_scf_1190_c1",
      "start": 456,
      "end": 1200,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1190_c1_457_1200",
      "annotations": {
        "id": [
          "1781_100325_scf_1190_c1_457_1200"
        ],
        "product": [
          "plastocyanin"
        ],
        "cath_funfam": [
          "2.60.40.420"
        ],
        "cog": [
          "COG3794"
        ],
        "pfam": [
          "Copper-bin",
          "Cupredoxin_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1190_c1_1206_1391": {
      "seqid": "NMDC:1781_100325_scf_1190_c1",
      "start": 1205,
      "end": 1391,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1190_c1_1206_1391",
      "annotations": {
        "id": [
          "1781_100325_scf_1190_c1_1206_1391"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1191_c1": {
    "1781_100325_scf_1191_c1_1_897": {
      "seqid": "NMDC:1781_100325_scf_1191_c1",
      "start": 0,
      "end": 897,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1191_c1_1_897",
      "annotations": {
        "id": [
          "1781_100325_scf_1191_c1_1_897"
        ],
        "product": [
          "S1-C subfamily serine protease"
        ],
        "cath_funfam": [
          "2.30.42.10",
          "2.40.10.10"
        ],
        "cog": [
          "COG0265"
        ],
        "pfam": [
          "PDZ_",
          "Trypsi",
          "Trypsin_"
        ],
        "superfamily": [
          "SM00228"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1191_c1_1278_1496": {
      "seqid": "NMDC:1781_100325_scf_1191_c1",
      "start": 1277,
      "end": 1496,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1191_c1_1278_1496",
      "annotations": {
        "id": [
          "1781_100325_scf_1191_c1_1278_1496"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.90.79.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1192_c1": {
    "1781_100325_scf_1192_c1_4_867": {
      "seqid": "NMDC:1781_100325_scf_1192_c1",
      "start": 3,
      "end": 867,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1192_c1_4_867",
      "annotations": {
        "id": [
          "1781_100325_scf_1192_c1_4_867"
        ],
        "product": [
          "pilus assembly protein CpaE"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG4963"
        ],
        "ko": [
          "KO:K02282"
        ],
        "pfam": [
          "Cbi",
          "Par"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1192_c1_880_1584": {
      "seqid": "NMDC:1781_100325_scf_1192_c1",
      "start": 879,
      "end": 1584,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1192_c1_880_1584",
      "annotations": {
        "id": [
          "1781_100325_scf_1192_c1_880_1584"
        ],
        "product": [
          "pilus assembly protein CpaF"
        ],
        "cog": [
          "COG4962"
        ],
        "ko": [
          "KO:K02283"
        ],
        "pfam": [
          "T2SS"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1193_c1": {
    "1781_100325_scf_1193_c1_3_1586": {
      "seqid": "NMDC:1781_100325_scf_1193_c1",
      "start": 2,
      "end": 1586,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1193_c1_3_1586",
      "annotations": {
        "id": [
          "1781_100325_scf_1193_c1_3_1586"
        ],
        "product": [
          "pyruvate",
          "orthophosphate dikinase"
        ],
        "cath_funfam": [
          "3.20.20.60",
          "3.50.30.10"
        ],
        "cog": [
          "COG0574"
        ],
        "ko": [
          "KO:K01006"
        ],
        "ec_number": [
          "EC:2.7.9.1"
        ],
        "pfam": [
          "PEP-utilizer",
          "PEP-utilizers_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1194_c1": {
    "1781_100325_scf_1194_c1_1_186": {
      "seqid": "NMDC:1781_100325_scf_1194_c1",
      "start": 0,
      "end": 186,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1194_c1_1_186",
      "annotations": {
        "id": [
          "1781_100325_scf_1194_c1_1_186"
        ],
        "product": [
          "small subunit ribosomal protein S11"
        ],
        "cath_funfam": [
          "3.30.420.80"
        ],
        "cog": [
          "COG0100"
        ],
        "ko": [
          "KO:K02948"
        ],
        "pfam": [
          "Ribosomal_S1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1194_c1_254_634": {
      "seqid": "NMDC:1781_100325_scf_1194_c1",
      "start": 253,
      "end": 634,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1194_c1_254_634",
      "annotations": {
        "id": [
          "1781_100325_scf_1194_c1_254_634"
        ],
        "product": [
          "small subunit ribosomal protein S13"
        ],
        "cath_funfam": [
          "1.10.8.50",
          "4.10.910.10"
        ],
        "cog": [
          "COG0099"
        ],
        "ko": [
          "KO:K02952"
        ],
        "pfam": [
          "Ribosomal_S1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1194_c1_647_760": {
      "seqid": "NMDC:1781_100325_scf_1194_c1",
      "start": 646,
      "end": 760,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1194_c1_647_760",
      "annotations": {
        "id": [
          "1781_100325_scf_1194_c1_647_760"
        ],
        "product": [
          "large subunit ribosomal protein L36"
        ],
        "cog": [
          "COG0257"
        ],
        "ko": [
          "KO:K02919"
        ],
        "pfam": [
          "Ribosomal_L3"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1194_c1_829_1047": {
      "seqid": "NMDC:1781_100325_scf_1194_c1",
      "start": 828,
      "end": 1047,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1194_c1_829_1047",
      "annotations": {
        "id": [
          "1781_100325_scf_1194_c1_829_1047"
        ],
        "product": [
          "translation initiation factor IF-1"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG0361"
        ],
        "ko": [
          "KO:K02518"
        ],
        "pfam": [
          "eIF-1"
        ],
        "superfamily": [
          "SM00316"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1194_c1_1193_1585": {
      "seqid": "NMDC:1781_100325_scf_1194_c1",
      "start": 1192,
      "end": 1585,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1194_c1_1193_1585",
      "annotations": {
        "id": [
          "1781_100325_scf_1194_c1_1193_1585"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1195_c1": {
    "1781_100325_scf_1195_c1_2_268": {
      "seqid": "NMDC:1781_100325_scf_1195_c1",
      "start": 1,
      "end": 268,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1195_c1_2_268",
      "annotations": {
        "id": [
          "1781_100325_scf_1195_c1_2_268"
        ],
        "product": [
          "transposase"
        ],
        "cath_funfam": [
          "3.40.50.10070"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "Transposase_2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1195_c1_358_1392": {
      "seqid": "NMDC:1781_100325_scf_1195_c1",
      "start": 357,
      "end": 1392,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1195_c1_358_1392",
      "annotations": {
        "id": [
          "1781_100325_scf_1195_c1_358_1392"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "DEDD_Tnp_IS11",
          "Transposase_2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1196_c1": {
    "1781_100325_scf_1196_c1_166_1542": {
      "seqid": "NMDC:1781_100325_scf_1196_c1",
      "start": 165,
      "end": 1542,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1196_c1_166_1542",
      "annotations": {
        "id": [
          "1781_100325_scf_1196_c1_166_1542"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.246.40",
          "1.10.740.10"
        ],
        "pfam": [
          "DDE_Tnp_",
          "Dimer_Tnp_Tn",
          "Tnp_DNA_bin"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1197_c1": {
    "1781_100325_scf_1197_c1_1_654": {
      "seqid": "NMDC:1781_100325_scf_1197_c1",
      "start": 0,
      "end": 654,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1197_c1_1_654",
      "annotations": {
        "id": [
          "1781_100325_scf_1197_c1_1_654"
        ],
        "product": [
          "V/A-type H+-transporting ATPase subunit D"
        ],
        "cog": [
          "COG1394"
        ],
        "ko": [
          "KO:K02120"
        ],
        "pfam": [
          "ATP-synt_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1197_c1_658_1584": {
      "seqid": "NMDC:1781_100325_scf_1197_c1",
      "start": 657,
      "end": 1584,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1197_c1_658_1584",
      "annotations": {
        "id": [
          "1781_100325_scf_1197_c1_658_1584"
        ],
        "product": [
          "V/A-type H+-transporting ATPase subunit B"
        ],
        "cath_funfam": [
          "1.10.220.10",
          "3.40.50.300"
        ],
        "cog": [
          "COG1156"
        ],
        "ko": [
          "KO:K02118"
        ],
        "pfam": [
          "ATP-synt_a"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1198_c1": {
    "1781_100325_scf_1198_c1_181_1413": {
      "seqid": "NMDC:1781_100325_scf_1198_c1",
      "start": 180,
      "end": 1413,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1198_c1_181_1413",
      "annotations": {
        "id": [
          "1781_100325_scf_1198_c1_181_1413"
        ],
        "product": [
          "transposase-like protein"
        ],
        "cog": [
          "COG3328"
        ],
        "pfam": [
          "Transposase_mu"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1198_c1_1457_1582": {
      "seqid": "NMDC:1781_100325_scf_1198_c1",
      "start": 1456,
      "end": 1582,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1198_c1_1457_1582",
      "annotations": {
        "id": [
          "1781_100325_scf_1198_c1_1457_1582"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1199_c1": {
    "1781_100325_scf_1199_c1_1_477": {
      "seqid": "NMDC:1781_100325_scf_1199_c1",
      "start": 0,
      "end": 477,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1199_c1_1_477",
      "annotations": {
        "id": [
          "1781_100325_scf_1199_c1_1_477"
        ],
        "product": [
          "bifunctional non-homologous end joining protein LigD"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG1793"
        ],
        "ko": [
          "KO:K01971"
        ],
        "ec_number": [
          "EC:6.5.1.1"
        ],
        "pfam": [
          "DNA_ligase_A_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1199_c1_484_999": {
      "seqid": "NMDC:1781_100325_scf_1199_c1",
      "start": 483,
      "end": 999,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1199_c1_484_999",
      "annotations": {
        "id": [
          "1781_100325_scf_1199_c1_484_999"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.20.20.30"
        ],
        "superfamily": [
          "SM00180"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1199_c1_999_1553": {
      "seqid": "NMDC:1781_100325_scf_1199_c1",
      "start": 998,
      "end": 1553,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1199_c1_999_1553",
      "annotations": {
        "id": [
          "1781_100325_scf_1199_c1_999_1553"
        ],
        "product": [
          "LmbE family N-acetylglucosaminyl deacetylase"
        ],
        "cath_funfam": [
          "3.40.50.10320"
        ],
        "cog": [
          "COG2120"
        ],
        "pfam": [
          "PIG-"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_119_c1": {
    "1781_100325_scf_119_c1_40_804": {
      "seqid": "NMDC:1781_100325_scf_119_c1",
      "start": 39,
      "end": 804,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_119_c1_40_804",
      "annotations": {
        "id": [
          "1781_100325_scf_119_c1_40_804"
        ],
        "product": [
          "site-specific DNA-methyltransferase (adenine-specific)"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "cog": [
          "COG0863"
        ],
        "ko": [
          "KO:K00571"
        ],
        "ec_number": [
          "EC:2.1.1.72"
        ],
        "pfam": [
          "N6_N4_Mtas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_119_c1_821_1159": {
      "seqid": "NMDC:1781_100325_scf_119_c1",
      "start": 820,
      "end": 1159,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_119_c1_821_1159",
      "annotations": {
        "id": [
          "1781_100325_scf_119_c1_821_1159"
        ],
        "product": [
          "thiol-disulfide isomerase/thioredoxin"
        ],
        "cath_funfam": [
          "3.40.30.10"
        ],
        "cog": [
          "COG0526"
        ],
        "pfam": [
          "Thioredoxi",
          "Thioredoxin_",
          "Tra"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_119_c1_1495_2004": {
      "seqid": "NMDC:1781_100325_scf_119_c1",
      "start": 1494,
      "end": 2004,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_119_c1_1495_2004",
      "annotations": {
        "id": [
          "1781_100325_scf_119_c1_1495_2004"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_119_c1_2347_3339": {
      "seqid": "NMDC:1781_100325_scf_119_c1",
      "start": 2346,
      "end": 3339,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_119_c1_2347_3339",
      "annotations": {
        "id": [
          "1781_100325_scf_119_c1_2347_3339"
        ],
        "product": [
          "NAD(P)H-flavin reductase"
        ],
        "cath_funfam": [
          "2.40.30.10"
        ],
        "cog": [
          "COG0543"
        ],
        "pfam": [
          "FAD_binding_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_11_c1": {
    "1781_100325_scf_11_c1_177_2002": {
      "seqid": "NMDC:1781_100325_scf_11_c1",
      "start": 176,
      "end": 2002,
      "strand": "+",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_11_c1_177_2002",
      "annotations": {
        "id": [
          "1781_100325_scf_11_c1_177_2002"
        ],
        "product": [
          "18S ribosomal RNA"
        ]
      }
    },
    "1781_100325_scf_11_c1_2024_2296": {
      "seqid": "NMDC:1781_100325_scf_11_c1",
      "start": 2023,
      "end": 2296,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_11_c1_2024_2296",
      "annotations": {
        "id": [
          "1781_100325_scf_11_c1_2024_2296"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_11_c1_2190_2456": {
      "seqid": "NMDC:1781_100325_scf_11_c1",
      "start": 2189,
      "end": 2456,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_11_c1_2190_2456",
      "annotations": {
        "id": [
          "1781_100325_scf_11_c1_2190_2456"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_11_c1_2455_2608": {
      "seqid": "NMDC:1781_100325_scf_11_c1",
      "start": 2454,
      "end": 2608,
      "strand": "+",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_11_c1_2455_2608",
      "annotations": {
        "id": [
          "1781_100325_scf_11_c1_2455_2608"
        ],
        "product": [
          "5S ribosomal RNA"
        ]
      }
    },
    "1781_100325_scf_11_c1_2649_2813": {
      "seqid": "NMDC:1781_100325_scf_11_c1",
      "start": 2648,
      "end": 2813,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_11_c1_2649_2813",
      "annotations": {
        "id": [
          "1781_100325_scf_11_c1_2649_2813"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_11_c1_2960_6742": {
      "seqid": "NMDC:1781_100325_scf_11_c1",
      "start": 2959,
      "end": 6742,
      "strand": "+",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_11_c1_2960_6742",
      "annotations": {
        "id": [
          "1781_100325_scf_11_c1_2960_6742"
        ],
        "product": [
          "28S ribosomal RNA"
        ]
      }
    },
    "1781_100325_scf_11_c1_7358_7564": {
      "seqid": "NMDC:1781_100325_scf_11_c1",
      "start": 7357,
      "end": 7564,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_11_c1_7358_7564",
      "annotations": {
        "id": [
          "1781_100325_scf_11_c1_7358_7564"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "4.10.60.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1200_c1": {
    "1781_100325_scf_1200_c1_1_546": {
      "seqid": "NMDC:1781_100325_scf_1200_c1",
      "start": 0,
      "end": 546,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1200_c1_1_546",
      "annotations": {
        "id": [
          "1781_100325_scf_1200_c1_1_546"
        ],
        "product": [
          "chaperonin GroEL"
        ],
        "cath_funfam": [
          "1.10.560.10"
        ],
        "cog": [
          "COG0459"
        ],
        "ko": [
          "KO:K04077"
        ],
        "pfam": [
          "Cpn60_TCP"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1200_c1_666_1571": {
      "seqid": "NMDC:1781_100325_scf_1200_c1",
      "start": 665,
      "end": 1571,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1200_c1_666_1571",
      "annotations": {
        "id": [
          "1781_100325_scf_1200_c1_666_1571"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1201_c1": {
    "1781_100325_scf_1201_c1_2_808": {
      "seqid": "NMDC:1781_100325_scf_1201_c1",
      "start": 1,
      "end": 808,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1201_c1_2_808",
      "annotations": {
        "id": [
          "1781_100325_scf_1201_c1_2_808"
        ],
        "product": [
          "mannosyl-3-phosphoglycerate phosphatase"
        ],
        "cath_funfam": [
          "3.40.50.1000"
        ],
        "cog": [
          "COG3769"
        ],
        "ko": [
          "KO:K07026"
        ],
        "ec_number": [
          "EC:3.1.3.70"
        ],
        "pfam": [
          "Hydrolase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1201_c1_864_1517": {
      "seqid": "NMDC:1781_100325_scf_1201_c1",
      "start": 863,
      "end": 1517,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1201_c1_864_1517",
      "annotations": {
        "id": [
          "1781_100325_scf_1201_c1_864_1517"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1202_c1": {
    "1781_100325_scf_1202_c1_94_195": {
      "seqid": "NMDC:1781_100325_scf_1202_c1",
      "start": 93,
      "end": 195,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1202_c1_94_195",
      "annotations": {
        "id": [
          "1781_100325_scf_1202_c1_94_195"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.540.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1202_c1_192_1352": {
      "seqid": "NMDC:1781_100325_scf_1202_c1",
      "start": 191,
      "end": 1352,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1202_c1_192_1352",
      "annotations": {
        "id": [
          "1781_100325_scf_1202_c1_192_1352"
        ],
        "product": [
          "acyl-CoA dehydrogenase"
        ],
        "cath_funfam": [
          "1.10.540.10",
          "1.20.140.10",
          "2.40.110.10"
        ],
        "cog": [
          "COG1960"
        ],
        "ko": [
          "KO:K00249"
        ],
        "ec_number": [
          "EC:1.3.8.7"
        ],
        "pfam": [
          "Acyl-CoA_dh_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1202_c1_1371_1580": {
      "seqid": "NMDC:1781_100325_scf_1202_c1",
      "start": 1370,
      "end": 1580,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1202_c1_1371_1580",
      "annotations": {
        "id": [
          "1781_100325_scf_1202_c1_1371_1580"
        ],
        "product": [
          "ribosomal protein S18 acetylase RimI-like enzyme"
        ],
        "cath_funfam": [
          "3.40.630.30"
        ],
        "cog": [
          "COG0456"
        ],
        "pfam": [
          "Acetyltransf_",
          "Acetyltransf_1",
          "FR4"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1203_c1": {
    "1781_100325_scf_1203_c1_1_1580": {
      "seqid": "NMDC:1781_100325_scf_1203_c1",
      "start": 0,
      "end": 1580,
      "strand": "+",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_1203_c1_1_1580",
      "annotations": {
        "id": [
          "1781_100325_scf_1203_c1_1_1580"
        ],
        "product": [
          "28S ribosomal RNA"
        ]
      }
    }
  },
  "1781_100325_scf_1204_c1": {
    "1781_100325_scf_1204_c1_83_328": {
      "seqid": "NMDC:1781_100325_scf_1204_c1",
      "start": 82,
      "end": 328,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1204_c1_83_328",
      "annotations": {
        "id": [
          "1781_100325_scf_1204_c1_83_328"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1204_c1_333_902": {
      "seqid": "NMDC:1781_100325_scf_1204_c1",
      "start": 332,
      "end": 902,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1204_c1_333_902",
      "annotations": {
        "id": [
          "1781_100325_scf_1204_c1_333_902"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.20.5.510"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1204_c1_1100_1579": {
      "seqid": "NMDC:1781_100325_scf_1204_c1",
      "start": 1099,
      "end": 1579,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1204_c1_1100_1579",
      "annotations": {
        "id": [
          "1781_100325_scf_1204_c1_1100_1579"
        ],
        "product": [
          "DNA polymerase-3 subunit alpha"
        ],
        "cath_funfam": [
          "3.20.20.140"
        ],
        "cog": [
          "COG0587"
        ],
        "ko": [
          "KO:K02337"
        ],
        "ec_number": [
          "EC:2.7.7.7"
        ],
        "pfam": [
          "PH"
        ],
        "superfamily": [
          "SM00481"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1205_c1": {
    "1781_100325_scf_1205_c1_7_174": {
      "seqid": "NMDC:1781_100325_scf_1205_c1",
      "start": 6,
      "end": 174,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1205_c1_7_174",
      "annotations": {
        "id": [
          "1781_100325_scf_1205_c1_7_174"
        ],
        "product": [
          "transcriptional/translational regulatory protein YebC/TACO1"
        ],
        "cath_funfam": [
          "3.30.70.980"
        ],
        "cog": [
          "COG0217"
        ],
        "pfam": [
          "Transcrip_re"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1205_c1_201_782": {
      "seqid": "NMDC:1781_100325_scf_1205_c1",
      "start": 200,
      "end": 782,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1205_c1_201_782",
      "annotations": {
        "id": [
          "1781_100325_scf_1205_c1_201_782"
        ],
        "product": [
          "maltose O-acetyltransferase"
        ],
        "cath_funfam": [
          "2.160.10.10"
        ],
        "cog": [
          "COG0110"
        ],
        "ko": [
          "KO:K00661"
        ],
        "ec_number": [
          "EC:2.3.1.79"
        ],
        "pfam": [
          "Hexape",
          "Hexapep_",
          "Ma"
        ],
        "superfamily": [
          "SM01266"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1205_c1_891_1304": {
      "seqid": "NMDC:1781_100325_scf_1205_c1",
      "start": 890,
      "end": 1304,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1205_c1_891_1304",
      "annotations": {
        "id": [
          "1781_100325_scf_1205_c1_891_1304"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.10.180.10"
        ],
        "cog": [
          "COG0346"
        ],
        "ko": [
          "KO:K07032"
        ],
        "pfam": [
          "Glyoxalas",
          "Glyoxalase_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1206_c1": {
    "1781_100325_scf_1206_c1_1_1095": {
      "seqid": "NMDC:1781_100325_scf_1206_c1",
      "start": 0,
      "end": 1095,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1206_c1_1_1095",
      "annotations": {
        "id": [
          "1781_100325_scf_1206_c1_1_1095"
        ],
        "product": [
          "glutamine synthetase"
        ],
        "cath_funfam": [
          "3.30.590.10"
        ],
        "cog": [
          "COG0174"
        ],
        "ko": [
          "KO:K01915"
        ],
        "ec_number": [
          "EC:6.3.1.2"
        ],
        "pfam": [
          "Gln-synt_"
        ],
        "superfamily": [
          "SM01230"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1206_c1_1194_1577": {
      "seqid": "NMDC:1781_100325_scf_1206_c1",
      "start": 1193,
      "end": 1577,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1206_c1_1194_1577",
      "annotations": {
        "id": [
          "1781_100325_scf_1206_c1_1194_1577"
        ],
        "product": [
          "RimJ/RimL family protein N-acetyltransferase"
        ],
        "cog": [
          "COG1670"
        ],
        "pfam": [
          "Acetyltransf_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1207_c1": {
    "1781_100325_scf_1207_c1_3_155": {
      "seqid": "NMDC:1781_100325_scf_1207_c1",
      "start": 2,
      "end": 155,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1207_c1_3_155",
      "annotations": {
        "id": [
          "1781_100325_scf_1207_c1_3_155"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1207_c1_161_769": {
      "seqid": "NMDC:1781_100325_scf_1207_c1",
      "start": 160,
      "end": 769,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1207_c1_161_769",
      "annotations": {
        "id": [
          "1781_100325_scf_1207_c1_161_769"
        ],
        "product": [
          "elongation factor Ts"
        ],
        "cath_funfam": [
          "1.10.8.10",
          "3.30.479.20"
        ],
        "cog": [
          "COG0264"
        ],
        "ko": [
          "KO:K02357"
        ],
        "pfam": [
          "EF_T"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1207_c1_780_1529": {
      "seqid": "NMDC:1781_100325_scf_1207_c1",
      "start": 779,
      "end": 1529,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1207_c1_780_1529",
      "annotations": {
        "id": [
          "1781_100325_scf_1207_c1_780_1529"
        ],
        "product": [
          "uridylate kinase"
        ],
        "cath_funfam": [
          "3.40.1160.10"
        ],
        "cog": [
          "COG0528"
        ],
        "ko": [
          "KO:K09903"
        ],
        "ec_number": [
          "EC:2.7.4.22"
        ],
        "pfam": [
          "AA_kinas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1208_c1": {
    "1781_100325_scf_1208_c1_3_374": {
      "seqid": "NMDC:1781_100325_scf_1208_c1",
      "start": 2,
      "end": 374,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1208_c1_3_374",
      "annotations": {
        "id": [
          "1781_100325_scf_1208_c1_3_374"
        ],
        "product": [
          "phosphomannomutase"
        ],
        "cath_funfam": [
          "3.40.120.10"
        ],
        "cog": [
          "COG1109"
        ],
        "ko": [
          "KO:K01840"
        ],
        "ec_number": [
          "EC:5.4.2.8"
        ],
        "pfam": [
          "PGM_PMM_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1208_c1_400_591": {
      "seqid": "NMDC:1781_100325_scf_1208_c1",
      "start": 399,
      "end": 591,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1208_c1_400_591",
      "annotations": {
        "id": [
          "1781_100325_scf_1208_c1_400_591"
        ],
        "product": [
          "formate dehydrogenase maturation protein FdhE"
        ],
        "cath_funfam": [
          "3.90.1670.10"
        ],
        "cog": [
          "COG3058"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1208_c1_750_959": {
      "seqid": "NMDC:1781_100325_scf_1208_c1",
      "start": 749,
      "end": 959,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1208_c1_750_959",
      "annotations": {
        "id": [
          "1781_100325_scf_1208_c1_750_959"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DUF349"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1208_c1_1207_1575": {
      "seqid": "NMDC:1781_100325_scf_1208_c1",
      "start": 1206,
      "end": 1575,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1208_c1_1207_1575",
      "annotations": {
        "id": [
          "1781_100325_scf_1208_c1_1207_1575"
        ],
        "product": [
          "L",
          "D-transpeptidase ErfK/SrfK"
        ],
        "cath_funfam": [
          "2.40.440.10"
        ],
        "cog": [
          "COG1376"
        ],
        "ko": [
          "KO:K16291"
        ],
        "pfam": [
          "Yku"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1209_c1": {
    "1781_100325_scf_1209_c1_6_647": {
      "seqid": "NMDC:1781_100325_scf_1209_c1",
      "start": 5,
      "end": 647,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1209_c1_6_647",
      "annotations": {
        "id": [
          "1781_100325_scf_1209_c1_6_647"
        ],
        "product": [
          "formyltetrahydrofolate deformylase"
        ],
        "cath_funfam": [
          "3.40.50.170"
        ],
        "cog": [
          "COG0788"
        ],
        "ko": [
          "KO:K01433"
        ],
        "ec_number": [
          "EC:3.5.1.10"
        ],
        "pfam": [
          "Formyl_trans_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1209_c1_640_1374": {
      "seqid": "NMDC:1781_100325_scf_1209_c1",
      "start": 639,
      "end": 1374,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1209_c1_640_1374",
      "annotations": {
        "id": [
          "1781_100325_scf_1209_c1_640_1374"
        ],
        "product": [
          "creatinine amidohydrolase"
        ],
        "cath_funfam": [
          "3.40.50.10310"
        ],
        "cog": [
          "COG1402"
        ],
        "ko": [
          "KO:K01470"
        ],
        "ec_number": [
          "EC:3.5.2.10"
        ],
        "pfam": [
          "Creatininas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1209_c1_1420_1575": {
      "seqid": "NMDC:1781_100325_scf_1209_c1",
      "start": 1419,
      "end": 1575,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1209_c1_1420_1575",
      "annotations": {
        "id": [
          "1781_100325_scf_1209_c1_1420_1575"
        ],
        "product": [
          "small nuclear ribonucleoprotein"
        ],
        "cath_funfam": [
          "2.30.30.100"
        ],
        "cog": [
          "COG1958"
        ],
        "ko": [
          "KO:K04796"
        ],
        "pfam": [
          "LS"
        ],
        "superfamily": [
          "SM00651"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_120_c1": {
    "1781_100325_scf_120_c1_130_612": {
      "seqid": "NMDC:1781_100325_scf_120_c1",
      "start": 129,
      "end": 612,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_120_c1_130_612",
      "annotations": {
        "id": [
          "1781_100325_scf_120_c1_130_612"
        ],
        "product": [
          "predicted extracellular nuclease"
        ],
        "cath_funfam": [
          "3.60.10.10"
        ],
        "cog": [
          "COG2374"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_120_c1_1300_2466": {
      "seqid": "NMDC:1781_100325_scf_120_c1",
      "start": 1299,
      "end": 2466,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_120_c1_1300_2466",
      "annotations": {
        "id": [
          "1781_100325_scf_120_c1_1300_2466"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_120_c1_3205_3660": {
      "seqid": "NMDC:1781_100325_scf_120_c1",
      "start": 3204,
      "end": 3660,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_120_c1_3205_3660",
      "annotations": {
        "id": [
          "1781_100325_scf_120_c1_3205_3660"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1210_c1": {
    "1781_100325_scf_1210_c1_326_1432": {
      "seqid": "NMDC:1781_100325_scf_1210_c1",
      "start": 325,
      "end": 1432,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1210_c1_326_1432",
      "annotations": {
        "id": [
          "1781_100325_scf_1210_c1_326_1432"
        ],
        "product": [
          "dTDP-4-amino-4",
          "6-dideoxygalactose transaminase"
        ],
        "cath_funfam": [
          "3.40.640.10",
          "3.90.1150.10"
        ],
        "cog": [
          "COG0399"
        ],
        "pfam": [
          "Aminotran_1_",
          "DegT_DnrJ_EryC"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1211_c1": {
    "1781_100325_scf_1211_c1_7_1461": {
      "seqid": "NMDC:1781_100325_scf_1211_c1",
      "start": 6,
      "end": 1461,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1211_c1_7_1461",
      "annotations": {
        "id": [
          "1781_100325_scf_1211_c1_7_1461"
        ],
        "product": [
          "magnesium chelatase subunit I"
        ],
        "cath_funfam": [
          "3.30.450.20",
          "3.40.50.300"
        ],
        "cog": [
          "COG1239"
        ],
        "ko": [
          "KO:K03405"
        ],
        "ec_number": [
          "EC:6.6.1.1"
        ],
        "pfam": [
          "AAA_",
          "Sigma54_activa"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1211_c1_1448_1573": {
      "seqid": "NMDC:1781_100325_scf_1211_c1",
      "start": 1447,
      "end": 1573,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1211_c1_1448_1573",
      "annotations": {
        "id": [
          "1781_100325_scf_1211_c1_1448_1573"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1212_c1": {
    "1781_100325_scf_1212_c1_2_856": {
      "seqid": "NMDC:1781_100325_scf_1212_c1",
      "start": 1,
      "end": 856,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1212_c1_2_856",
      "annotations": {
        "id": [
          "1781_100325_scf_1212_c1_2_856"
        ],
        "product": [
          "[acyl-carrier-protein] S-malonyltransferase"
        ],
        "cath_funfam": [
          "3.40.366.10"
        ],
        "cog": [
          "COG0331"
        ],
        "ko": [
          "KO:K00645"
        ],
        "ec_number": [
          "EC:2.3.1.39"
        ],
        "pfam": [
          "Acyl_transf_"
        ],
        "superfamily": [
          "SM00827"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1212_c1_974_1573": {
      "seqid": "NMDC:1781_100325_scf_1212_c1",
      "start": 973,
      "end": 1573,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1212_c1_974_1573",
      "annotations": {
        "id": [
          "1781_100325_scf_1212_c1_974_1573"
        ],
        "product": [
          "3-oxoacyl-[acyl-carrier-protein] synthase-3"
        ],
        "cath_funfam": [
          "3.40.47.10"
        ],
        "cog": [
          "COG0332"
        ],
        "ko": [
          "KO:K00648"
        ],
        "ec_number": [
          "EC:2.3.1.180"
        ],
        "pfam": [
          "ACP_syn_II",
          "SpoVA",
          "Thiolase_",
          "ketoacyl-syn"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1213_c1": {
    "1781_100325_scf_1213_c1_560_820": {
      "seqid": "NMDC:1781_100325_scf_1213_c1",
      "start": 559,
      "end": 820,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1213_c1_560_820",
      "annotations": {
        "id": [
          "1781_100325_scf_1213_c1_560_820"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1213_c1_1253_1573": {
      "seqid": "NMDC:1781_100325_scf_1213_c1",
      "start": 1252,
      "end": 1573,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1213_c1_1253_1573",
      "annotations": {
        "id": [
          "1781_100325_scf_1213_c1_1253_1573"
        ],
        "product": [
          "aryl-alcohol dehydrogenase-like predicted oxidoreductase"
        ],
        "cath_funfam": [
          "3.20.20.100"
        ],
        "cog": [
          "COG0667"
        ],
        "pfam": [
          "Aldo_ket_re"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1214_c1": {
    "1781_100325_scf_1214_c1_31_366": {
      "seqid": "NMDC:1781_100325_scf_1214_c1",
      "start": 30,
      "end": 366,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1214_c1_31_366",
      "annotations": {
        "id": [
          "1781_100325_scf_1214_c1_31_366"
        ],
        "product": [
          "3-phosphoshikimate 1-carboxyvinyltransferase"
        ],
        "cath_funfam": [
          "3.65.10.10"
        ],
        "cog": [
          "COG0128"
        ],
        "ko": [
          "KO:K00800"
        ],
        "ec_number": [
          "EC:2.5.1.19"
        ],
        "pfam": [
          "EPSP_synthas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1214_c1_472_1572": {
      "seqid": "NMDC:1781_100325_scf_1214_c1",
      "start": 471,
      "end": 1572,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1214_c1_472_1572",
      "annotations": {
        "id": [
          "1781_100325_scf_1214_c1_472_1572"
        ],
        "product": [
          "chorismate synthase"
        ],
        "cath_funfam": [
          "3.60.150.10"
        ],
        "cog": [
          "COG0082"
        ],
        "ko": [
          "KO:K01736"
        ],
        "ec_number": [
          "EC:4.2.3.5"
        ],
        "pfam": [
          "Chorismate_syn"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1215_c1": {
    "1781_100325_scf_1215_c1_597_818": {
      "seqid": "NMDC:1781_100325_scf_1215_c1",
      "start": 596,
      "end": 818,
      "strand": "+",
      "type": "SO:0000655",
      "encodes": "NMDC:1781_100325_scf_1215_c1_597_818",
      "annotations": {
        "id": [
          "1781_100325_scf_1215_c1_597_818"
        ],
        "product": [
          "Group II catalytic intron D1-D4-6"
        ]
      }
    },
    "1781_100325_scf_1215_c1_824_1186": {
      "seqid": "NMDC:1781_100325_scf_1215_c1",
      "start": 823,
      "end": 1186,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1215_c1_824_1186",
      "annotations": {
        "id": [
          "1781_100325_scf_1215_c1_824_1186"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1216_c1": {
    "1781_100325_scf_1216_c1_159_1571": {
      "seqid": "NMDC:1781_100325_scf_1216_c1",
      "start": 158,
      "end": 1571,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1216_c1_159_1571",
      "annotations": {
        "id": [
          "1781_100325_scf_1216_c1_159_1571"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1217_c1": {
    "1781_100325_scf_1217_c1_37_1359": {
      "seqid": "NMDC:1781_100325_scf_1217_c1",
      "start": 36,
      "end": 1359,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1217_c1_37_1359",
      "annotations": {
        "id": [
          "1781_100325_scf_1217_c1_37_1359"
        ],
        "product": [
          "valyl-tRNA synthetase"
        ],
        "cath_funfam": [
          "1.10.730.10",
          "3.40.50.620"
        ],
        "cog": [
          "COG0525"
        ],
        "ko": [
          "KO:K01873"
        ],
        "ec_number": [
          "EC:6.1.1.9"
        ],
        "pfam": [
          "Anticodon_",
          "tRNA-synt_",
          "tRNA-synt_1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1217_c1_1383_1571": {
      "seqid": "NMDC:1781_100325_scf_1217_c1",
      "start": 1382,
      "end": 1571,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1217_c1_1383_1571",
      "annotations": {
        "id": [
          "1781_100325_scf_1217_c1_1383_1571"
        ],
        "product": [
          "NADPH:quinone reductase-like Zn-dependent oxidoreductase"
        ],
        "cath_funfam": [
          "3.90.180.10"
        ],
        "cog": [
          "COG0604"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1218_c1": {
    "1781_100325_scf_1218_c1_1_177": {
      "seqid": "NMDC:1781_100325_scf_1218_c1",
      "start": 0,
      "end": 177,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1218_c1_1_177",
      "annotations": {
        "id": [
          "1781_100325_scf_1218_c1_1_177"
        ],
        "product": [
          "histidyl-tRNA synthetase"
        ],
        "cath_funfam": [
          "3.30.930.10"
        ],
        "cog": [
          "COG0124"
        ],
        "ko": [
          "KO:K01892"
        ],
        "ec_number": [
          "EC:6.1.1.21"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1218_c1_178_795": {
      "seqid": "NMDC:1781_100325_scf_1218_c1",
      "start": 177,
      "end": 795,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1218_c1_178_795",
      "annotations": {
        "id": [
          "1781_100325_scf_1218_c1_178_795"
        ],
        "product": [
          "glyoxylase-like metal-dependent hydrolase (beta-lactamase superfamily II)"
        ],
        "cath_funfam": [
          "3.60.15.10"
        ],
        "cog": [
          "COG0491"
        ],
        "pfam": [
          "Lactamase_"
        ],
        "superfamily": [
          "SM00849"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1218_c1_849_1109": {
      "seqid": "NMDC:1781_100325_scf_1218_c1",
      "start": 848,
      "end": 1109,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1218_c1_849_1109",
      "annotations": {
        "id": [
          "1781_100325_scf_1218_c1_849_1109"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1218_c1_1168_1554": {
      "seqid": "NMDC:1781_100325_scf_1218_c1",
      "start": 1167,
      "end": 1554,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1218_c1_1168_1554",
      "annotations": {
        "id": [
          "1781_100325_scf_1218_c1_1168_1554"
        ],
        "product": [
          "D-tyrosyl-tRNA(Tyr) deacylase"
        ],
        "cath_funfam": [
          "3.50.80.10"
        ],
        "cog": [
          "COG1490"
        ],
        "ko": [
          "KO:K07560"
        ],
        "ec_number": [
          "EC:3.1.-"
        ],
        "pfam": [
          "Tyr_Deacylas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1219_c1": {
    "1781_100325_scf_1219_c1_9_128": {
      "seqid": "NMDC:1781_100325_scf_1219_c1",
      "start": 8,
      "end": 128,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1219_c1_9_128",
      "annotations": {
        "id": [
          "1781_100325_scf_1219_c1_9_128"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1219_c1_157_1113": {
      "seqid": "NMDC:1781_100325_scf_1219_c1",
      "start": 156,
      "end": 1113,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1219_c1_157_1113",
      "annotations": {
        "id": [
          "1781_100325_scf_1219_c1_157_1113"
        ],
        "product": [
          "deoxyhypusine synthase"
        ],
        "cath_funfam": [
          "3.40.910.10"
        ],
        "cog": [
          "COG1899"
        ],
        "ko": [
          "KO:K00809"
        ],
        "ec_number": [
          "EC:2.5.1.46"
        ],
        "pfam": [
          "D"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1219_c1_1292_1570": {
      "seqid": "NMDC:1781_100325_scf_1219_c1",
      "start": 1291,
      "end": 1570,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1219_c1_1292_1570",
      "annotations": {
        "id": [
          "1781_100325_scf_1219_c1_1292_1570"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_121_c1": {
    "1781_100325_scf_121_c1_33_194": {
      "seqid": "NMDC:1781_100325_scf_121_c1",
      "start": 32,
      "end": 194,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_121_c1_33_194",
      "annotations": {
        "id": [
          "1781_100325_scf_121_c1_33_194"
        ],
        "product": [
          "sugar phosphate isomerase/epimerase"
        ],
        "cath_funfam": [
          "3.20.20.150"
        ],
        "cog": [
          "COG1082"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_121_c1_434_706": {
      "seqid": "NMDC:1781_100325_scf_121_c1",
      "start": 433,
      "end": 706,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_121_c1_434_706",
      "annotations": {
        "id": [
          "1781_100325_scf_121_c1_434_706"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_121_c1_822_1172": {
      "seqid": "NMDC:1781_100325_scf_121_c1",
      "start": 821,
      "end": 1172,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_121_c1_822_1172",
      "annotations": {
        "id": [
          "1781_100325_scf_121_c1_822_1172"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_121_c1_1218_2543": {
      "seqid": "NMDC:1781_100325_scf_121_c1",
      "start": 1217,
      "end": 2543,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_121_c1_1218_2543",
      "annotations": {
        "id": [
          "1781_100325_scf_121_c1_1218_2543"
        ],
        "product": [
          "predicted AlkP superfamily pyrophosphatase or phosphodiesterase"
        ],
        "cath_funfam": [
          "3.40.720.10"
        ],
        "cog": [
          "COG1524"
        ],
        "pfam": [
          "Phosphodies"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_121_c1_2603_3397": {
      "seqid": "NMDC:1781_100325_scf_121_c1",
      "start": 2602,
      "end": 3397,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_121_c1_2603_3397",
      "annotations": {
        "id": [
          "1781_100325_scf_121_c1_2603_3397"
        ],
        "product": [
          "sugar phosphate isomerase/epimerase"
        ],
        "cath_funfam": [
          "3.20.20.150"
        ],
        "cog": [
          "COG1082"
        ],
        "pfam": [
          "AP_endonuc_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_121_c1_3445_3645": {
      "seqid": "NMDC:1781_100325_scf_121_c1",
      "start": 3444,
      "end": 3645,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_121_c1_3445_3645",
      "annotations": {
        "id": [
          "1781_100325_scf_121_c1_3445_3645"
        ],
        "product": [
          "uncharacterized SAM-dependent methyltransferase"
        ],
        "cog": [
          "COG4301"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1220_c1": {
    "1781_100325_scf_1220_c1_2_418": {
      "seqid": "NMDC:1781_100325_scf_1220_c1",
      "start": 1,
      "end": 418,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1220_c1_2_418",
      "annotations": {
        "id": [
          "1781_100325_scf_1220_c1_2_418"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1220_c1_1218_1571": {
      "seqid": "NMDC:1781_100325_scf_1220_c1",
      "start": 1217,
      "end": 1571,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1220_c1_1218_1571",
      "annotations": {
        "id": [
          "1781_100325_scf_1220_c1_1218_1571"
        ],
        "product": [
          "quinol monooxygenase YgiN"
        ],
        "cog": [
          "COG1359"
        ],
        "pfam": [
          "AB"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1221_c1": {
    "1781_100325_scf_1221_c1_102_1166": {
      "seqid": "NMDC:1781_100325_scf_1221_c1",
      "start": 101,
      "end": 1166,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1221_c1_102_1166",
      "annotations": {
        "id": [
          "1781_100325_scf_1221_c1_102_1166"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "DEDD_Tnp_IS11",
          "Transposase_2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1222_c1": {
    "1781_100325_scf_1222_c1_1_207": {
      "seqid": "NMDC:1781_100325_scf_1222_c1",
      "start": 0,
      "end": 207,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1222_c1_1_207",
      "annotations": {
        "id": [
          "1781_100325_scf_1222_c1_1_207"
        ],
        "product": [
          "23S rRNA U2552 (ribose-2'-O)-methylase RlmE/FtsJ"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "cog": [
          "COG0293"
        ],
        "pfam": [
          "Fts"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1222_c1_592_747": {
      "seqid": "NMDC:1781_100325_scf_1222_c1",
      "start": 591,
      "end": 747,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1222_c1_592_747",
      "annotations": {
        "id": [
          "1781_100325_scf_1222_c1_592_747"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.160.60"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1222_c1_1176_1568": {
      "seqid": "NMDC:1781_100325_scf_1222_c1",
      "start": 1175,
      "end": 1568,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1222_c1_1176_1568",
      "annotations": {
        "id": [
          "1781_100325_scf_1222_c1_1176_1568"
        ],
        "product": [
          "Ca2+-binding RTX toxin-like protein"
        ],
        "cath_funfam": [
          "2.150.10.10"
        ],
        "cog": [
          "COG2931"
        ],
        "pfam": [
          "HemolysinCabin"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1223_c1": {
    "1781_100325_scf_1223_c1_3_248": {
      "seqid": "NMDC:1781_100325_scf_1223_c1",
      "start": 2,
      "end": 248,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1223_c1_3_248",
      "annotations": {
        "id": [
          "1781_100325_scf_1223_c1_3_248"
        ],
        "product": [
          "uncharacterized protein"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "cog": [
          "COG1606"
        ],
        "ko": [
          "KO:K06864"
        ],
        "pfam": [
          "ATP_bind_",
          "Asn_synthas",
          "NAD_synthas",
          "Que",
          "tRNA_Me_tran"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1223_c1_236_1468": {
      "seqid": "NMDC:1781_100325_scf_1223_c1",
      "start": 235,
      "end": 1468,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1223_c1_236_1468",
      "annotations": {
        "id": [
          "1781_100325_scf_1223_c1_236_1468"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.10.20.300",
          "3.30.70.1380"
        ],
        "cog": [
          "COG1641"
        ],
        "ko": [
          "KO:K09121"
        ],
        "pfam": [
          "DUF11"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1224_c1": {
    "1781_100325_scf_1224_c1_3_1076": {
      "seqid": "NMDC:1781_100325_scf_1224_c1",
      "start": 2,
      "end": 1076,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1224_c1_3_1076",
      "annotations": {
        "id": [
          "1781_100325_scf_1224_c1_3_1076"
        ],
        "product": [
          "tryptophan synthase beta chain"
        ],
        "cath_funfam": [
          "3.40.50.1100"
        ],
        "cog": [
          "COG0133"
        ],
        "ko": [
          "KO:K01696"
        ],
        "ec_number": [
          "EC:4.2.1.20"
        ],
        "pfam": [
          "PAL"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1224_c1_1079_1567": {
      "seqid": "NMDC:1781_100325_scf_1224_c1",
      "start": 1078,
      "end": 1567,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1224_c1_1079_1567",
      "annotations": {
        "id": [
          "1781_100325_scf_1224_c1_1079_1567"
        ],
        "product": [
          "phosphoribosylanthranilate isomerase"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "cog": [
          "COG0135"
        ],
        "ko": [
          "KO:K01817"
        ],
        "ec_number": [
          "EC:5.3.1.24"
        ],
        "pfam": [
          "PRA"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1225_c1": {
    "1781_100325_scf_1225_c1_1379_1567": {
      "seqid": "NMDC:1781_100325_scf_1225_c1",
      "start": 1378,
      "end": 1567,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1225_c1_1379_1567",
      "annotations": {
        "id": [
          "1781_100325_scf_1225_c1_1379_1567"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1226_c1": {
    "1781_100325_scf_1226_c1_2_127": {
      "seqid": "NMDC:1781_100325_scf_1226_c1",
      "start": 1,
      "end": 127,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1226_c1_2_127",
      "annotations": {
        "id": [
          "1781_100325_scf_1226_c1_2_127"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1226_c1_124_1323": {
      "seqid": "NMDC:1781_100325_scf_1226_c1",
      "start": 123,
      "end": 1323,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1226_c1_124_1323",
      "annotations": {
        "id": [
          "1781_100325_scf_1226_c1_124_1323"
        ],
        "product": [
          "simple sugar transport system permease protein"
        ],
        "cog": [
          "COG4603"
        ],
        "ko": [
          "KO:K02057"
        ],
        "pfam": [
          "BPD_transp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1226_c1_1320_1568": {
      "seqid": "NMDC:1781_100325_scf_1226_c1",
      "start": 1319,
      "end": 1568,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1226_c1_1320_1568",
      "annotations": {
        "id": [
          "1781_100325_scf_1226_c1_1320_1568"
        ],
        "product": [
          "simple sugar transport system ATP-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG3845"
        ],
        "ko": [
          "KO:K02056"
        ],
        "ec_number": [
          "EC:3.6.3.17"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1227_c1": {
    "1781_100325_scf_1227_c1_101_1366": {
      "seqid": "NMDC:1781_100325_scf_1227_c1",
      "start": 100,
      "end": 1366,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1227_c1_101_1366",
      "annotations": {
        "id": [
          "1781_100325_scf_1227_c1_101_1366"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1228_c1": {
    "1781_100325_scf_1228_c1_1_930": {
      "seqid": "NMDC:1781_100325_scf_1228_c1",
      "start": 0,
      "end": 930,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1228_c1_1_930",
      "annotations": {
        "id": [
          "1781_100325_scf_1228_c1_1_930"
        ],
        "product": [
          "isocitrate dehydrogenase"
        ],
        "cath_funfam": [
          "3.40.718.10"
        ],
        "cog": [
          "COG0473"
        ],
        "ko": [
          "KO:K00031"
        ],
        "ec_number": [
          "EC:1.1.1.42"
        ],
        "pfam": [
          "Iso_d"
        ],
        "superfamily": [
          "SM01329"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1228_c1_1049_1567": {
      "seqid": "NMDC:1781_100325_scf_1228_c1",
      "start": 1048,
      "end": 1567,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1228_c1_1049_1567",
      "annotations": {
        "id": [
          "1781_100325_scf_1228_c1_1049_1567"
        ],
        "product": [
          "phospholipase C"
        ],
        "cog": [
          "COG3511"
        ],
        "pfam": [
          "Phosphoesteras"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1229_c1": {
    "1781_100325_scf_1229_c1_3_182": {
      "seqid": "NMDC:1781_100325_scf_1229_c1",
      "start": 2,
      "end": 182,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1229_c1_3_182",
      "annotations": {
        "id": [
          "1781_100325_scf_1229_c1_3_182"
        ],
        "product": [
          "uncharacterized cofD-like protein"
        ],
        "cog": [
          "COG0391"
        ],
        "pfam": [
          "UPF005"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1229_c1_179_1078": {
      "seqid": "NMDC:1781_100325_scf_1229_c1",
      "start": 178,
      "end": 1078,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1229_c1_179_1078",
      "annotations": {
        "id": [
          "1781_100325_scf_1229_c1_179_1078"
        ],
        "product": [
          "UPF0042 nucleotide-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1660"
        ],
        "ko": [
          "KO:K06958"
        ],
        "pfam": [
          "ATP_bind_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1229_c1_1075_1566": {
      "seqid": "NMDC:1781_100325_scf_1229_c1",
      "start": 1074,
      "end": 1566,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1229_c1_1075_1566",
      "annotations": {
        "id": [
          "1781_100325_scf_1229_c1_1075_1566"
        ],
        "product": [
          "excinuclease ABC subunit C"
        ],
        "cath_funfam": [
          "1.10.150.20"
        ],
        "cog": [
          "COG0322"
        ],
        "ko": [
          "KO:K03703"
        ],
        "pfam": [
          "HHH_",
          "UvrC_HhH_"
        ],
        "superfamily": [
          "SM00278"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_122_c1": {
    "1781_100325_scf_122_c1_3_302": {
      "seqid": "NMDC:1781_100325_scf_122_c1",
      "start": 2,
      "end": 302,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_122_c1_3_302",
      "annotations": {
        "id": [
          "1781_100325_scf_122_c1_3_302"
        ],
        "product": [
          "molecular chaperone DnaK"
        ],
        "cath_funfam": [
          "1.20.1270.10"
        ],
        "ko": [
          "KO:K04043"
        ],
        "pfam": [
          "HSP7"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_122_c1_302_808": {
      "seqid": "NMDC:1781_100325_scf_122_c1",
      "start": 301,
      "end": 808,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_122_c1_302_808",
      "annotations": {
        "id": [
          "1781_100325_scf_122_c1_302_808"
        ],
        "product": [
          "molecular chaperone GrpE"
        ],
        "cath_funfam": [
          "2.30.22.10",
          "3.90.20.20"
        ],
        "cog": [
          "COG0576"
        ],
        "ko": [
          "KO:K03687"
        ],
        "pfam": [
          "Grp"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_122_c1_930_2048": {
      "seqid": "NMDC:1781_100325_scf_122_c1",
      "start": 929,
      "end": 2048,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_122_c1_930_2048",
      "annotations": {
        "id": [
          "1781_100325_scf_122_c1_930_2048"
        ],
        "product": [
          "molecular chaperone DnaJ"
        ],
        "cath_funfam": [
          "1.10.287.110",
          "2.60.260.20"
        ],
        "cog": [
          "COG0484"
        ],
        "ko": [
          "KO:K03686"
        ],
        "pfam": [
          "Dna",
          "DnaJ_",
          "DnaJ_CXXCXGX"
        ],
        "superfamily": [
          "SM00271"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_122_c1_2045_2269": {
      "seqid": "NMDC:1781_100325_scf_122_c1",
      "start": 2044,
      "end": 2269,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_122_c1_2045_2269",
      "annotations": {
        "id": [
          "1781_100325_scf_122_c1_2045_2269"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_122_c1_2269_2697": {
      "seqid": "NMDC:1781_100325_scf_122_c1",
      "start": 2268,
      "end": 2697,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_122_c1_2269_2697",
      "annotations": {
        "id": [
          "1781_100325_scf_122_c1_2269_2697"
        ],
        "product": [
          "MerR family transcriptional regulator/heat shock protein HspR"
        ],
        "cath_funfam": [
          "1.10.1660.10"
        ],
        "cog": [
          "COG0789"
        ],
        "ko": [
          "KO:K13640"
        ],
        "pfam": [
          "Mer",
          "MerR_"
        ],
        "superfamily": [
          "SM00422"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_122_c1_2708_3637": {
      "seqid": "NMDC:1781_100325_scf_122_c1",
      "start": 2707,
      "end": 3637,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_122_c1_2708_3637",
      "annotations": {
        "id": [
          "1781_100325_scf_122_c1_2708_3637"
        ],
        "product": [
          "ATP-dependent Clp protease ATP-binding subunit ClpB"
        ],
        "cath_funfam": [
          "1.10.1780.10",
          "3.40.50.300"
        ],
        "cog": [
          "COG0542"
        ],
        "ko": [
          "KO:K03695"
        ],
        "pfam": [
          "AA",
          "Clp_"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1230_c1": {
    "1781_100325_scf_1230_c1_216_587": {
      "seqid": "NMDC:1781_100325_scf_1230_c1",
      "start": 215,
      "end": 587,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1230_c1_216_587",
      "annotations": {
        "id": [
          "1781_100325_scf_1230_c1_216_587"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1230_c1_809_1438": {
      "seqid": "NMDC:1781_100325_scf_1230_c1",
      "start": 808,
      "end": 1438,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1230_c1_809_1438",
      "annotations": {
        "id": [
          "1781_100325_scf_1230_c1_809_1438"
        ],
        "product": [
          "ubiquinone/menaquinone biosynthesis C-methylase UbiE"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "cog": [
          "COG2226"
        ],
        "pfam": [
          "MT",
          "Methyltransf_1",
          "Methyltransf_2",
          "Methyltransf_3",
          "TPM",
          "Teh"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1231_c1": {
    "1781_100325_scf_1231_c1_1_513": {
      "seqid": "NMDC:1781_100325_scf_1231_c1",
      "start": 0,
      "end": 513,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1231_c1_1_513",
      "annotations": {
        "id": [
          "1781_100325_scf_1231_c1_1_513"
        ],
        "product": [
          "transposase-like protein"
        ],
        "cog": [
          "COG2963"
        ],
        "pfam": [
          "HTH_Tnp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1231_c1_510_1346": {
      "seqid": "NMDC:1781_100325_scf_1231_c1",
      "start": 509,
      "end": 1346,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1231_c1_510_1346",
      "annotations": {
        "id": [
          "1781_100325_scf_1231_c1_510_1346"
        ],
        "product": [
          "putative transposase"
        ],
        "cath_funfam": [
          "3.30.420.10"
        ],
        "cog": [
          "COG2801"
        ],
        "ko": [
          "KO:K07497"
        ],
        "pfam": [
          "DDE_Tnp_IS24",
          "HTH_2",
          "rv",
          "rve_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1232_c1": {
    "1781_100325_scf_1232_c1_2_1561": {
      "seqid": "NMDC:1781_100325_scf_1232_c1",
      "start": 1,
      "end": 1561,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1232_c1_2_1561",
      "annotations": {
        "id": [
          "1781_100325_scf_1232_c1_2_1561"
        ],
        "product": [
          "transglutaminase-like putative cysteine protease"
        ],
        "cog": [
          "COG1305"
        ],
        "pfam": [
          "Transglut_cor"
        ],
        "superfamily": [
          "SM00460"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1233_c1": {
    "1781_100325_scf_1233_c1_37_471": {
      "seqid": "NMDC:1781_100325_scf_1233_c1",
      "start": 36,
      "end": 471,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1233_c1_37_471",
      "annotations": {
        "id": [
          "1781_100325_scf_1233_c1_37_471"
        ],
        "product": [
          "peptide-methionine (S)-S-oxide reductase"
        ],
        "cath_funfam": [
          "3.30.1060.10"
        ],
        "cog": [
          "COG0225"
        ],
        "ko": [
          "KO:K07304"
        ],
        "ec_number": [
          "EC:1.8.4.11"
        ],
        "pfam": [
          "PMS"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1233_c1_1040_1435": {
      "seqid": "NMDC:1781_100325_scf_1233_c1",
      "start": 1039,
      "end": 1435,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1233_c1_1040_1435",
      "annotations": {
        "id": [
          "1781_100325_scf_1233_c1_1040_1435"
        ],
        "product": [
          "malate dehydrogenase (oxaloacetate-decarboxylating)"
        ],
        "cath_funfam": [
          "3.40.50.720"
        ],
        "cog": [
          "COG0281"
        ],
        "ko": [
          "KO:K00027"
        ],
        "ec_number": [
          "EC:1.1.1.38"
        ],
        "pfam": [
          "Malic_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1234_c1": {
    "1781_100325_scf_1234_c1_1_771": {
      "seqid": "NMDC:1781_100325_scf_1234_c1",
      "start": 0,
      "end": 771,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1234_c1_1_771",
      "annotations": {
        "id": [
          "1781_100325_scf_1234_c1_1_771"
        ],
        "product": [
          "ubiquinol-cytochrome c reductase cytochrome b subunit"
        ],
        "cath_funfam": [
          "1.20.810.10"
        ],
        "cog": [
          "COG1290"
        ],
        "ko": [
          "KO:K00412"
        ],
        "pfam": [
          "Cytochrom_B_N_",
          "Cytochrome_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1234_c1_833_1444": {
      "seqid": "NMDC:1781_100325_scf_1234_c1",
      "start": 832,
      "end": 1444,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1234_c1_833_1444",
      "annotations": {
        "id": [
          "1781_100325_scf_1234_c1_833_1444"
        ],
        "product": [
          "ubiquinol-cytochrome c reductase iron-sulfur subunit"
        ],
        "cath_funfam": [
          "1.20.5.510",
          "2.102.10.10"
        ],
        "cog": [
          "COG0723"
        ],
        "ko": [
          "KO:K00411"
        ],
        "ec_number": [
          "EC:1.10.2.2"
        ],
        "pfam": [
          "Riesk"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1235_c1": {
    "1781_100325_scf_1235_c1_2_1561": {
      "seqid": "NMDC:1781_100325_scf_1235_c1",
      "start": 1,
      "end": 1561,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1235_c1_2_1561",
      "annotations": {
        "id": [
          "1781_100325_scf_1235_c1_2_1561"
        ],
        "product": [
          "HAD superfamily hydrolase (TIGR01490 family)"
        ],
        "cog": [
          "COG0560"
        ],
        "pfam": [
          "HA",
          "NAD_binding_",
          "Steril"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1236_c1": {
    "1781_100325_scf_1236_c1_2_1537": {
      "seqid": "NMDC:1781_100325_scf_1236_c1",
      "start": 1,
      "end": 1537,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1236_c1_2_1537",
      "annotations": {
        "id": [
          "1781_100325_scf_1236_c1_2_1537"
        ],
        "product": [
          "diguanylate cyclase (GGDEF)-like protein/PAS domain S-box-containing protein"
        ],
        "cath_funfam": [
          "3.20.20.450",
          "3.30.70.270"
        ],
        "cog": [
          "COG5001"
        ],
        "pfam": [
          "EA",
          "GGDE",
          "PAS_"
        ],
        "superfamily": [
          "SM00052",
          "SM00267"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1237_c1": {
    "1781_100325_scf_1237_c1_300_725": {
      "seqid": "NMDC:1781_100325_scf_1237_c1",
      "start": 299,
      "end": 725,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1237_c1_300_725",
      "annotations": {
        "id": [
          "1781_100325_scf_1237_c1_300_725"
        ],
        "product": [
          "pyridoxamine 5'-phosphate oxidase family protein"
        ],
        "cath_funfam": [
          "2.30.110.10"
        ],
        "ko": [
          "KO:K05558"
        ],
        "pfam": [
          "Pyridox_oxidas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1237_c1_722_1105": {
      "seqid": "NMDC:1781_100325_scf_1237_c1",
      "start": 721,
      "end": 1105,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1237_c1_722_1105",
      "annotations": {
        "id": [
          "1781_100325_scf_1237_c1_722_1105"
        ],
        "product": [
          "catechol 2",
          "3-dioxygenase-like lactoylglutathione lyase family enzyme"
        ],
        "cath_funfam": [
          "3.10.180.10"
        ],
        "cog": [
          "COG0346"
        ],
        "pfam": [
          "Glyoxalas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1237_c1_1077_1559": {
      "seqid": "NMDC:1781_100325_scf_1237_c1",
      "start": 1076,
      "end": 1559,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1237_c1_1077_1559",
      "annotations": {
        "id": [
          "1781_100325_scf_1237_c1_1077_1559"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DinB_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1238_c1": {
    "1781_100325_scf_1238_c1_97_393": {
      "seqid": "NMDC:1781_100325_scf_1238_c1",
      "start": 96,
      "end": 393,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1238_c1_97_393",
      "annotations": {
        "id": [
          "1781_100325_scf_1238_c1_97_393"
        ],
        "product": [
          "1",
          "4-alpha-glucan branching enzyme"
        ],
        "cath_funfam": [
          "2.60.40.10"
        ],
        "cog": [
          "COG0296"
        ],
        "pfam": [
          "CBM_4"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1238_c1_449_1528": {
      "seqid": "NMDC:1781_100325_scf_1238_c1",
      "start": 448,
      "end": 1528,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1238_c1_449_1528",
      "annotations": {
        "id": [
          "1781_100325_scf_1238_c1_449_1528"
        ],
        "product": [
          "transposase"
        ],
        "cath_funfam": [
          "1.10.10.60",
          "3.30.420.10"
        ],
        "cog": [
          "COG3335",
          "COG3415"
        ],
        "pfam": [
          "DDE_",
          "HTH_2",
          "HTH_3",
          "rv"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1239_c1": {
    "1781_100325_scf_1239_c1_3_329": {
      "seqid": "NMDC:1781_100325_scf_1239_c1",
      "start": 2,
      "end": 329,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1239_c1_3_329",
      "annotations": {
        "id": [
          "1781_100325_scf_1239_c1_3_329"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1239_c1_744_1283": {
      "seqid": "NMDC:1781_100325_scf_1239_c1",
      "start": 743,
      "end": 1283,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1239_c1_744_1283",
      "annotations": {
        "id": [
          "1781_100325_scf_1239_c1_744_1283"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_123_c1": {
    "1781_100325_scf_123_c1_71_184": {
      "seqid": "NMDC:1781_100325_scf_123_c1",
      "start": 70,
      "end": 184,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_123_c1_71_184",
      "annotations": {
        "id": [
          "1781_100325_scf_123_c1_71_184"
        ],
        "product": [
          "heme/copper-type cytochrome/quinol oxidase subunit 2"
        ],
        "cath_funfam": [
          "1.10.287.90"
        ],
        "cog": [
          "COG1622"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_123_c1_187_993": {
      "seqid": "NMDC:1781_100325_scf_123_c1",
      "start": 186,
      "end": 993,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_123_c1_187_993",
      "annotations": {
        "id": [
          "1781_100325_scf_123_c1_187_993"
        ],
        "product": [
          "cytochrome c oxidase subunit 2"
        ],
        "cath_funfam": [
          "2.60.40.420"
        ],
        "cog": [
          "COG3794"
        ],
        "ko": [
          "KO:K02275"
        ],
        "ec_number": [
          "EC:1.9.3.1"
        ],
        "pfam": [
          "COX",
          "Copper-bin",
          "Cupredoxin_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_123_c1_1137_2633": {
      "seqid": "NMDC:1781_100325_scf_123_c1",
      "start": 1136,
      "end": 2633,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_123_c1_1137_2633",
      "annotations": {
        "id": [
          "1781_100325_scf_123_c1_1137_2633"
        ],
        "product": [
          "cytochrome c oxidase subunit 1"
        ],
        "cath_funfam": [
          "1.20.210.10"
        ],
        "cog": [
          "COG0843"
        ],
        "ko": [
          "KO:K02274"
        ],
        "ec_number": [
          "EC:1.9.3.1"
        ],
        "pfam": [
          "COX"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_123_c1_2858_2947": {
      "seqid": "NMDC:1781_100325_scf_123_c1",
      "start": 2857,
      "end": 2947,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_123_c1_2858_2947",
      "annotations": {
        "id": [
          "1781_100325_scf_123_c1_2858_2947"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_123_c1_2907_3149": {
      "seqid": "NMDC:1781_100325_scf_123_c1",
      "start": 2906,
      "end": 3149,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_123_c1_2907_3149",
      "annotations": {
        "id": [
          "1781_100325_scf_123_c1_2907_3149"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_123_c1_3251_3505": {
      "seqid": "NMDC:1781_100325_scf_123_c1",
      "start": 3250,
      "end": 3505,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_123_c1_3251_3505",
      "annotations": {
        "id": [
          "1781_100325_scf_123_c1_3251_3505"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.90.730.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_123_c1_3505_3636": {
      "seqid": "NMDC:1781_100325_scf_123_c1",
      "start": 3504,
      "end": 3636,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_123_c1_3505_3636",
      "annotations": {
        "id": [
          "1781_100325_scf_123_c1_3505_3636"
        ],
        "product": [
          "plastocyanin"
        ],
        "cath_funfam": [
          "2.60.40.420"
        ],
        "cog": [
          "COG3794"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1240_c1": {
    "1781_100325_scf_1240_c1_3_713": {
      "seqid": "NMDC:1781_100325_scf_1240_c1",
      "start": 2,
      "end": 713,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1240_c1_3_713",
      "annotations": {
        "id": [
          "1781_100325_scf_1240_c1_3_713"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.7700"
        ],
        "cog": [
          "COG1691"
        ],
        "ko": [
          "KO:K06898"
        ],
        "pfam": [
          "AIR"
        ],
        "superfamily": [
          "SM01001"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1240_c1_749_1525": {
      "seqid": "NMDC:1781_100325_scf_1240_c1",
      "start": 748,
      "end": 1525,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1240_c1_749_1525",
      "annotations": {
        "id": [
          "1781_100325_scf_1240_c1_749_1525"
        ],
        "product": [
          "malate dehydrogenase"
        ],
        "cath_funfam": [
          "3.40.50.720",
          "3.90.110.10"
        ],
        "cog": [
          "COG0039"
        ],
        "ko": [
          "KO:K00024"
        ],
        "ec_number": [
          "EC:1.1.1.37"
        ],
        "pfam": [
          "Ldh_1_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1241_c1": {
    "1781_100325_scf_1241_c1_43_909": {
      "seqid": "NMDC:1781_100325_scf_1241_c1",
      "start": 42,
      "end": 909,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1241_c1_43_909",
      "annotations": {
        "id": [
          "1781_100325_scf_1241_c1_43_909"
        ],
        "product": [
          "UDP-3-O-[3-hydroxymyristoyl] glucosamine N-acyltransferase"
        ],
        "cath_funfam": [
          "2.160.10.10"
        ],
        "cog": [
          "COG1044"
        ],
        "ko": [
          "KO:K02536"
        ],
        "ec_number": [
          "EC:2.3.1.191"
        ],
        "pfam": [
          "Hexape",
          "Hexapep_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1241_c1_893_1351": {
      "seqid": "NMDC:1781_100325_scf_1241_c1",
      "start": 892,
      "end": 1351,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1241_c1_893_1351",
      "annotations": {
        "id": [
          "1781_100325_scf_1241_c1_893_1351"
        ],
        "product": [
          "beta-hydroxyacyl-ACP dehydratase FabZ"
        ],
        "cath_funfam": [
          "3.10.129.10"
        ],
        "cog": [
          "COG0764"
        ],
        "pfam": [
          "Fab",
          "MaoC_dehydrata"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1241_c1_1380_1556": {
      "seqid": "NMDC:1781_100325_scf_1241_c1",
      "start": 1379,
      "end": 1556,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1241_c1_1380_1556",
      "annotations": {
        "id": [
          "1781_100325_scf_1241_c1_1380_1556"
        ],
        "product": [
          "UDP-N-acetylglucosamine acyltransferase"
        ],
        "cath_funfam": [
          "2.160.10.10"
        ],
        "cog": [
          "COG1043"
        ],
        "ko": [
          "KO:K00677"
        ],
        "ec_number": [
          "EC:2.3.1.129"
        ],
        "pfam": [
          "Hexape"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1242_c1": {
    "1781_100325_scf_1242_c1_2_358": {
      "seqid": "NMDC:1781_100325_scf_1242_c1",
      "start": 1,
      "end": 358,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1242_c1_2_358",
      "annotations": {
        "id": [
          "1781_100325_scf_1242_c1_2_358"
        ],
        "product": [
          "formate/nitrite transporter FocA (FNT family)"
        ],
        "cath_funfam": [
          "1.20.1080.10"
        ],
        "cog": [
          "COG2116"
        ],
        "pfam": [
          "Form_Nir_tran"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1242_c1_386_862": {
      "seqid": "NMDC:1781_100325_scf_1242_c1",
      "start": 385,
      "end": 862,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1242_c1_386_862",
      "annotations": {
        "id": [
          "1781_100325_scf_1242_c1_386_862"
        ],
        "product": [
          "CBS domain-containing protein"
        ],
        "cath_funfam": [
          "3.10.580.10"
        ],
        "cog": [
          "COG0517"
        ],
        "ko": [
          "KO:K07182"
        ],
        "pfam": [
          "CB"
        ],
        "superfamily": [
          "SM00116"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1242_c1_978_1556": {
      "seqid": "NMDC:1781_100325_scf_1242_c1",
      "start": 977,
      "end": 1556,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1242_c1_978_1556",
      "annotations": {
        "id": [
          "1781_100325_scf_1242_c1_978_1556"
        ],
        "product": [
          "GAF domain-containing protein"
        ],
        "cath_funfam": [
          "3.30.450.40"
        ],
        "cog": [
          "COG2203"
        ],
        "pfam": [
          "GA",
          "GAF_",
          "HisKA_"
        ],
        "superfamily": [
          "SM00065"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1243_c1": {
    "1781_100325_scf_1243_c1_215_1558": {
      "seqid": "NMDC:1781_100325_scf_1243_c1",
      "start": 214,
      "end": 1558,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1243_c1_215_1558",
      "annotations": {
        "id": [
          "1781_100325_scf_1243_c1_215_1558"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3666"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DUF77"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1244_c1": {
    "1781_100325_scf_1244_c1_79_1548": {
      "seqid": "NMDC:1781_100325_scf_1244_c1",
      "start": 78,
      "end": 1548,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1244_c1_79_1548",
      "annotations": {
        "id": [
          "1781_100325_scf_1244_c1_79_1548"
        ],
        "product": [
          "FAD/FMN-containing dehydrogenase"
        ],
        "cath_funfam": [
          "1.10.45.10",
          "3.30.43.10",
          "3.30.465.10"
        ],
        "cog": [
          "COG0277"
        ],
        "pfam": [
          "FAD-oxidase_",
          "FAD_binding_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1245_c1": {
    "1781_100325_scf_1245_c1_8_313": {
      "seqid": "NMDC:1781_100325_scf_1245_c1",
      "start": 7,
      "end": 313,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1245_c1_8_313",
      "annotations": {
        "id": [
          "1781_100325_scf_1245_c1_8_313"
        ],
        "product": [
          "acetyl-CoA synthetase"
        ],
        "cath_funfam": [
          "3.30.300.30"
        ],
        "cog": [
          "COG0365"
        ],
        "ko": [
          "KO:K01895"
        ],
        "ec_number": [
          "EC:6.2.1.1"
        ],
        "pfam": [
          "AMP-binding_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1245_c1_366_1211": {
      "seqid": "NMDC:1781_100325_scf_1245_c1",
      "start": 365,
      "end": 1211,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1245_c1_366_1211",
      "annotations": {
        "id": [
          "1781_100325_scf_1245_c1_366_1211"
        ],
        "product": [
          "diguanylate cyclase (GGDEF)-like protein"
        ],
        "cath_funfam": [
          "3.30.70.270",
          "3.40.50.2300"
        ],
        "cog": [
          "COG3706"
        ],
        "pfam": [
          "GGDE",
          "Response_re"
        ],
        "superfamily": [
          "SM00267"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1245_c1_1351_1557": {
      "seqid": "NMDC:1781_100325_scf_1245_c1",
      "start": 1350,
      "end": 1557,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1245_c1_1351_1557",
      "annotations": {
        "id": [
          "1781_100325_scf_1245_c1_1351_1557"
        ],
        "product": [
          "RNA polymerase sigma-70 factor (ECF subfamily)"
        ],
        "cath_funfam": [
          "1.10.1740.10"
        ],
        "cog": [
          "COG1595"
        ],
        "ko": [
          "KO:K03088"
        ],
        "pfam": [
          "Sigma70_r"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1246_c1": {
    "1781_100325_scf_1246_c1_98_433": {
      "seqid": "NMDC:1781_100325_scf_1246_c1",
      "start": 97,
      "end": 433,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1246_c1_98_433",
      "annotations": {
        "id": [
          "1781_100325_scf_1246_c1_98_433"
        ],
        "product": [
          "molybdopterin biosynthesis enzyme"
        ],
        "cath_funfam": [
          "2.40.340.10"
        ],
        "cog": [
          "COG0303"
        ],
        "pfam": [
          "MoeA_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1246_c1_441_1070": {
      "seqid": "NMDC:1781_100325_scf_1246_c1",
      "start": 440,
      "end": 1070,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1246_c1_441_1070",
      "annotations": {
        "id": [
          "1781_100325_scf_1246_c1_441_1070"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG0730"
        ],
        "ko": [
          "KO:K07090"
        ],
        "pfam": [
          "Tau"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1246_c1_1207_1557": {
      "seqid": "NMDC:1781_100325_scf_1246_c1",
      "start": 1206,
      "end": 1557,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1246_c1_1207_1557",
      "annotations": {
        "id": [
          "1781_100325_scf_1246_c1_1207_1557"
        ],
        "product": [
          "molybdenum cofactor synthesis domain-containing protein"
        ],
        "cath_funfam": [
          "3.40.980.10"
        ],
        "cog": [
          "COG0521"
        ],
        "pfam": [
          "MoCF_biosynt"
        ],
        "superfamily": [
          "SM00852"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1247_c1": {
    "1781_100325_scf_1247_c1_2_1555": {
      "seqid": "NMDC:1781_100325_scf_1247_c1",
      "start": 1,
      "end": 1555,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1247_c1_2_1555",
      "annotations": {
        "id": [
          "1781_100325_scf_1247_c1_2_1555"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.70.270"
        ],
        "pfam": [
          "RVT_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1248_c1": {
    "1781_100325_scf_1248_c1_1_1536": {
      "seqid": "NMDC:1781_100325_scf_1248_c1",
      "start": 0,
      "end": 1536,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1248_c1_1_1536",
      "annotations": {
        "id": [
          "1781_100325_scf_1248_c1_1_1536"
        ],
        "product": [
          "ATP-dependent Lhr-like helicase"
        ],
        "cog": [
          "COG1201"
        ],
        "ko": [
          "KO:K03724"
        ],
        "ec_number": [
          "EC:3.6.4.-"
        ],
        "pfam": [
          "DEAD_asso"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1249_c1": {
    "1781_100325_scf_1249_c1_3_251": {
      "seqid": "NMDC:1781_100325_scf_1249_c1",
      "start": 2,
      "end": 251,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1249_c1_3_251",
      "annotations": {
        "id": [
          "1781_100325_scf_1249_c1_3_251"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.20.1250.20"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1249_c1_332_1555": {
      "seqid": "NMDC:1781_100325_scf_1249_c1",
      "start": 331,
      "end": 1555,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1249_c1_332_1555",
      "annotations": {
        "id": [
          "1781_100325_scf_1249_c1_332_1555"
        ],
        "product": [
          "phytoene dehydrogenase-like protein"
        ],
        "cath_funfam": [
          "3.50.50.60"
        ],
        "cog": [
          "COG1233"
        ],
        "pfam": [
          "FAD_binding_",
          "FAD_oxidore",
          "NAD_binding_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_124_c1": {
    "1781_100325_scf_124_c1_467_1831": {
      "seqid": "NMDC:1781_100325_scf_124_c1",
      "start": 466,
      "end": 1831,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_124_c1_467_1831",
      "annotations": {
        "id": [
          "1781_100325_scf_124_c1_467_1831"
        ],
        "product": [
          "cytochrome P450"
        ],
        "cath_funfam": [
          "1.10.630.10"
        ],
        "cog": [
          "COG2124"
        ],
        "pfam": [
          "p45"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_124_c1_2193_2648": {
      "seqid": "NMDC:1781_100325_scf_124_c1",
      "start": 2192,
      "end": 2648,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_124_c1_2193_2648",
      "annotations": {
        "id": [
          "1781_100325_scf_124_c1_2193_2648"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_124_c1_3361_3606": {
      "seqid": "NMDC:1781_100325_scf_124_c1",
      "start": 3360,
      "end": 3606,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_124_c1_3361_3606",
      "annotations": {
        "id": [
          "1781_100325_scf_124_c1_3361_3606"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.2300"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1250_c1": {
    "1781_100325_scf_1250_c1_399_1553": {
      "seqid": "NMDC:1781_100325_scf_1250_c1",
      "start": 398,
      "end": 1553,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1250_c1_399_1553",
      "annotations": {
        "id": [
          "1781_100325_scf_1250_c1_399_1553"
        ],
        "product": [
          "cobyrinic acid a",
          "c-diamide synthase"
        ],
        "cath_funfam": [
          "3.40.50.300",
          "3.40.50.880"
        ],
        "cog": [
          "COG1797"
        ],
        "ko": [
          "KO:K02224"
        ],
        "ec_number": [
          "EC:6.3.5.11",
          "EC:6.3.5.9"
        ],
        "pfam": [
          "AAA_2",
          "Cbi",
          "GATase_"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1251_c1": {
    "1781_100325_scf_1251_c1_1_1554": {
      "seqid": "NMDC:1781_100325_scf_1251_c1",
      "start": 0,
      "end": 1554,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1251_c1_1_1554",
      "annotations": {
        "id": [
          "1781_100325_scf_1251_c1_1_1554"
        ],
        "product": [
          "carbon-monoxide dehydrogenase large subunit"
        ],
        "cath_funfam": [
          "3.30.365.10"
        ],
        "cog": [
          "COG1529"
        ],
        "ko": [
          "KO:K03520"
        ],
        "ec_number": [
          "EC:1.2.99.2"
        ],
        "pfam": [
          "Ald_Xan_dh_",
          "Ald_Xan_dh_C"
        ],
        "superfamily": [
          "SM01008"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1252_c1": {
    "1781_100325_scf_1252_c1_1_1212": {
      "seqid": "NMDC:1781_100325_scf_1252_c1",
      "start": 0,
      "end": 1212,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1252_c1_1_1212",
      "annotations": {
        "id": [
          "1781_100325_scf_1252_c1_1_1212"
        ],
        "product": [
          "DNA primase"
        ],
        "cath_funfam": [
          "3.40.1360.10"
        ],
        "cog": [
          "COG0358"
        ],
        "ko": [
          "KO:K02316"
        ],
        "ec_number": [
          "EC:2.7.7.-"
        ],
        "pfam": [
          "DnaB_bin",
          "Topri",
          "Toprim_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1252_c1_1303_1554": {
      "seqid": "NMDC:1781_100325_scf_1252_c1",
      "start": 1302,
      "end": 1554,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1252_c1_1303_1554",
      "annotations": {
        "id": [
          "1781_100325_scf_1252_c1_1303_1554"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.390.30"
        ],
        "pfam": [
          "Sigma70_r1_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1253_c1": {
    "1781_100325_scf_1253_c1_1_366": {
      "seqid": "NMDC:1781_100325_scf_1253_c1",
      "start": 0,
      "end": 366,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1253_c1_1_366",
      "annotations": {
        "id": [
          "1781_100325_scf_1253_c1_1_366"
        ],
        "product": [
          "catechol 2",
          "3-dioxygenase-like lactoylglutathione lyase family enzyme"
        ],
        "cath_funfam": [
          "3.10.180.10"
        ],
        "cog": [
          "COG0346"
        ],
        "pfam": [
          "Glyoxalas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1253_c1_499_687": {
      "seqid": "NMDC:1781_100325_scf_1253_c1",
      "start": 498,
      "end": 687,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1253_c1_499_687",
      "annotations": {
        "id": [
          "1781_100325_scf_1253_c1_499_687"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1253_c1_817_942": {
      "seqid": "NMDC:1781_100325_scf_1253_c1",
      "start": 816,
      "end": 942,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1253_c1_817_942",
      "annotations": {
        "id": [
          "1781_100325_scf_1253_c1_817_942"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1253_c1_1187_1534": {
      "seqid": "NMDC:1781_100325_scf_1253_c1",
      "start": 1186,
      "end": 1534,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1253_c1_1187_1534",
      "annotations": {
        "id": [
          "1781_100325_scf_1253_c1_1187_1534"
        ],
        "product": [
          "dihydrolipoamide dehydrogenase"
        ],
        "cath_funfam": [
          "3.30.390.30"
        ],
        "cog": [
          "COG1249"
        ],
        "ko": [
          "KO:K00382"
        ],
        "ec_number": [
          "EC:1.8.1.4"
        ],
        "pfam": [
          "Pyr_redox_di"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1254_c1": {
    "1781_100325_scf_1254_c1_2_268": {
      "seqid": "NMDC:1781_100325_scf_1254_c1",
      "start": 1,
      "end": 268,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1254_c1_2_268",
      "annotations": {
        "id": [
          "1781_100325_scf_1254_c1_2_268"
        ],
        "product": [
          "phosphopantothenoylcysteine decarboxylase/phosphopantothenate--cysteine ligase"
        ],
        "cath_funfam": [
          "3.40.50.10300"
        ],
        "cog": [
          "COG0452"
        ],
        "ko": [
          "KO:K13038"
        ],
        "ec_number": [
          "EC:4.1.1.36",
          "EC:6.3.2.5"
        ],
        "pfam": [
          "DF"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1254_c1_350_1537": {
      "seqid": "NMDC:1781_100325_scf_1254_c1",
      "start": 349,
      "end": 1537,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1254_c1_350_1537",
      "annotations": {
        "id": [
          "1781_100325_scf_1254_c1_350_1537"
        ],
        "product": [
          "S-adenosylmethionine synthetase"
        ],
        "cath_funfam": [
          "3.30.300.10"
        ],
        "cog": [
          "COG0192"
        ],
        "ko": [
          "KO:K00789"
        ],
        "ec_number": [
          "EC:2.5.1.6"
        ],
        "pfam": [
          "S-AdoMet_synt_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1255_c1": {
    "1781_100325_scf_1255_c1_1_552": {
      "seqid": "NMDC:1781_100325_scf_1255_c1",
      "start": 0,
      "end": 552,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1255_c1_1_552",
      "annotations": {
        "id": [
          "1781_100325_scf_1255_c1_1_552"
        ],
        "product": [
          "NCS1 family nucleobase:cation symporter-1"
        ],
        "cog": [
          "COG1457"
        ],
        "ko": [
          "KO:K03457"
        ],
        "pfam": [
          "Transp_cyt_pu"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1255_c1_542_648": {
      "seqid": "NMDC:1781_100325_scf_1255_c1",
      "start": 541,
      "end": 648,
      "strand": "-",
      "type": null,
      "encodes": "NMDC:1781_100325_scf_1255_c1_542_648",
      "annotations": {
        "id": [
          "1781_100325_scf_1255_c1_542_648"
        ]
      }
    },
    "1781_100325_scf_1255_c1_650_1255": {
      "seqid": "NMDC:1781_100325_scf_1255_c1",
      "start": 649,
      "end": 1255,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1255_c1_650_1255",
      "annotations": {
        "id": [
          "1781_100325_scf_1255_c1_650_1255"
        ],
        "product": [
          "probable phosphoglycerate mutase"
        ],
        "cath_funfam": [
          "3.40.50.1240"
        ],
        "cog": [
          "COG0406"
        ],
        "ko": [
          "KO:K15634"
        ],
        "ec_number": [
          "EC:5.4.2.12"
        ],
        "pfam": [
          "His_Phos_"
        ],
        "superfamily": [
          "SM00855"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1255_c1_1255_1551": {
      "seqid": "NMDC:1781_100325_scf_1255_c1",
      "start": 1254,
      "end": 1551,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1255_c1_1255_1551",
      "annotations": {
        "id": [
          "1781_100325_scf_1255_c1_1255_1551"
        ],
        "product": [
          "sarcosine oxidase subunit beta"
        ],
        "cath_funfam": [
          "3.50.50.60"
        ],
        "cog": [
          "COG0665"
        ],
        "ko": [
          "KO:K00303"
        ],
        "ec_number": [
          "EC:1.5.3.1"
        ],
        "pfam": [
          "DA"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1256_c1": {
    "1781_100325_scf_1256_c1_446_868": {
      "seqid": "NMDC:1781_100325_scf_1256_c1",
      "start": 445,
      "end": 868,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1256_c1_446_868",
      "annotations": {
        "id": [
          "1781_100325_scf_1256_c1_446_868"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1256_c1_923_1414": {
      "seqid": "NMDC:1781_100325_scf_1256_c1",
      "start": 922,
      "end": 1414,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1256_c1_923_1414",
      "annotations": {
        "id": [
          "1781_100325_scf_1256_c1_923_1414"
        ],
        "product": [
          "MoaA/NifB/PqqE/SkfB family radical SAM enzyme"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "cog": [
          "COG0535"
        ],
        "pfam": [
          "Fer4_1",
          "Radical_SA"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1256_c1_1426_1551": {
      "seqid": "NMDC:1781_100325_scf_1256_c1",
      "start": 1425,
      "end": 1551,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1256_c1_1426_1551",
      "annotations": {
        "id": [
          "1781_100325_scf_1256_c1_1426_1551"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1257_c1": {
    "1781_100325_scf_1257_c1_3_155": {
      "seqid": "NMDC:1781_100325_scf_1257_c1",
      "start": 2,
      "end": 155,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1257_c1_3_155",
      "annotations": {
        "id": [
          "1781_100325_scf_1257_c1_3_155"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1257_c1_148_582": {
      "seqid": "NMDC:1781_100325_scf_1257_c1",
      "start": 147,
      "end": 582,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1257_c1_148_582",
      "annotations": {
        "id": [
          "1781_100325_scf_1257_c1_148_582"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1257_c1_645_1520": {
      "seqid": "NMDC:1781_100325_scf_1257_c1",
      "start": 644,
      "end": 1520,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1257_c1_645_1520",
      "annotations": {
        "id": [
          "1781_100325_scf_1257_c1_645_1520"
        ],
        "product": [
          "2-oxoglutarate ferredoxin oxidoreductase subunit beta"
        ],
        "cath_funfam": [
          "3.40.50.970"
        ],
        "cog": [
          "COG1013"
        ],
        "ko": [
          "KO:K00175"
        ],
        "ec_number": [
          "EC:1.2.7.11",
          "EC:1.2.7.3"
        ],
        "pfam": [
          "PFO_beta_",
          "TPP_enzyme_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1258_c1": {
    "1781_100325_scf_1258_c1_3_1040": {
      "seqid": "NMDC:1781_100325_scf_1258_c1",
      "start": 2,
      "end": 1040,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1258_c1_3_1040",
      "annotations": {
        "id": [
          "1781_100325_scf_1258_c1_3_1040"
        ],
        "product": [
          "uncharacterized protein (DUF885 family)"
        ],
        "cog": [
          "COG4805"
        ],
        "pfam": [
          "DUF88"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1258_c1_1182_1550": {
      "seqid": "NMDC:1781_100325_scf_1258_c1",
      "start": 1181,
      "end": 1550,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1258_c1_1182_1550",
      "annotations": {
        "id": [
          "1781_100325_scf_1258_c1_1182_1550"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.130.10.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1259_c1": {
    "1781_100325_scf_1259_c1_3_794": {
      "seqid": "NMDC:1781_100325_scf_1259_c1",
      "start": 2,
      "end": 794,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1259_c1_3_794",
      "annotations": {
        "id": [
          "1781_100325_scf_1259_c1_3_794"
        ],
        "product": [
          "glyceraldehyde 3-phosphate dehydrogenase"
        ],
        "cath_funfam": [
          "3.40.50.720"
        ],
        "cog": [
          "COG0057"
        ],
        "ko": [
          "KO:K00134"
        ],
        "ec_number": [
          "EC:1.2.1.12"
        ],
        "pfam": [
          "Gp_dh_"
        ],
        "superfamily": [
          "SM00846"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1259_c1_877_1542": {
      "seqid": "NMDC:1781_100325_scf_1259_c1",
      "start": 876,
      "end": 1542,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1259_c1_877_1542",
      "annotations": {
        "id": [
          "1781_100325_scf_1259_c1_877_1542"
        ],
        "product": [
          "UPF0042 nucleotide-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1660"
        ],
        "ko": [
          "KO:K06958"
        ],
        "pfam": [
          "ATP_bind_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_125_c1": {
    "1781_100325_scf_125_c1_88_282": {
      "seqid": "NMDC:1781_100325_scf_125_c1",
      "start": 87,
      "end": 282,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_125_c1_88_282",
      "annotations": {
        "id": [
          "1781_100325_scf_125_c1_88_282"
        ],
        "product": [
          "arginyl-tRNA synthetase"
        ],
        "cath_funfam": [
          "1.10.730.10"
        ],
        "cog": [
          "COG0018"
        ],
        "ko": [
          "KO:K01887"
        ],
        "ec_number": [
          "EC:6.1.1.19"
        ],
        "pfam": [
          "DALR_"
        ],
        "superfamily": [
          "SM00836"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_125_c1_336_605": {
      "seqid": "NMDC:1781_100325_scf_125_c1",
      "start": 335,
      "end": 605,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_125_c1_336_605",
      "annotations": {
        "id": [
          "1781_100325_scf_125_c1_336_605"
        ],
        "product": [
          "phosphoribosylformylglycinamidine synthase"
        ],
        "cath_funfam": [
          "3.30.1280.10"
        ],
        "cog": [
          "COG1828"
        ],
        "ko": [
          "KO:K01952"
        ],
        "ec_number": [
          "EC:6.3.5.3"
        ],
        "pfam": [
          "Pur"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_125_c1_1024_1353": {
      "seqid": "NMDC:1781_100325_scf_125_c1",
      "start": 1023,
      "end": 1353,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_125_c1_1024_1353",
      "annotations": {
        "id": [
          "1781_100325_scf_125_c1_1024_1353"
        ],
        "product": [
          "DNA-binding transcriptional ArsR family regulator"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG0640"
        ],
        "pfam": [
          "HTH_",
          "HTH_2"
        ],
        "superfamily": [
          "SM00418"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_125_c1_1487_1747": {
      "seqid": "NMDC:1781_100325_scf_125_c1",
      "start": 1486,
      "end": 1747,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_125_c1_1487_1747",
      "annotations": {
        "id": [
          "1781_100325_scf_125_c1_1487_1747"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.287.110"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_125_c1_1855_2502": {
      "seqid": "NMDC:1781_100325_scf_125_c1",
      "start": 1854,
      "end": 2502,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_125_c1_1855_2502",
      "annotations": {
        "id": [
          "1781_100325_scf_125_c1_1855_2502"
        ],
        "product": [
          "division protein CdvB (Snf7/Vps24/ESCRT-III family)"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG5491"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_125_c1_2499_2849": {
      "seqid": "NMDC:1781_100325_scf_125_c1",
      "start": 2498,
      "end": 2849,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_125_c1_2499_2849",
      "annotations": {
        "id": [
          "1781_100325_scf_125_c1_2499_2849"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_125_c1_3164_3580": {
      "seqid": "NMDC:1781_100325_scf_125_c1",
      "start": 3163,
      "end": 3580,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_125_c1_3164_3580",
      "annotations": {
        "id": [
          "1781_100325_scf_125_c1_3164_3580"
        ],
        "product": [
          "glycine C-acetyltransferase"
        ],
        "cath_funfam": [
          "3.90.1150.10"
        ],
        "cog": [
          "COG0156"
        ],
        "ko": [
          "KO:K00639"
        ],
        "ec_number": [
          "EC:2.3.1.29"
        ],
        "pfam": [
          "Aminotran_1_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1260_c1": {
    "1781_100325_scf_1260_c1_3_1244": {
      "seqid": "NMDC:1781_100325_scf_1260_c1",
      "start": 2,
      "end": 1244,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1260_c1_3_1244",
      "annotations": {
        "id": [
          "1781_100325_scf_1260_c1_3_1244"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.40.10"
        ],
        "pfam": [
          "Y2_Tn",
          "Zn_Tnp_IS9"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1260_c1_1407_1550": {
      "seqid": "NMDC:1781_100325_scf_1260_c1",
      "start": 1406,
      "end": 1550,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1260_c1_1407_1550",
      "annotations": {
        "id": [
          "1781_100325_scf_1260_c1_1407_1550"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1261_c1": {
    "1781_100325_scf_1261_c1_11_517": {
      "seqid": "NMDC:1781_100325_scf_1261_c1",
      "start": 10,
      "end": 517,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1261_c1_11_517",
      "annotations": {
        "id": [
          "1781_100325_scf_1261_c1_11_517"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1261_c1_517_1107": {
      "seqid": "NMDC:1781_100325_scf_1261_c1",
      "start": 516,
      "end": 1107,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1261_c1_517_1107",
      "annotations": {
        "id": [
          "1781_100325_scf_1261_c1_517_1107"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1261_c1_1134_1412": {
      "seqid": "NMDC:1781_100325_scf_1261_c1",
      "start": 1133,
      "end": 1412,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1261_c1_1134_1412",
      "annotations": {
        "id": [
          "1781_100325_scf_1261_c1_1134_1412"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1261_c1_1409_1549": {
      "seqid": "NMDC:1781_100325_scf_1261_c1",
      "start": 1408,
      "end": 1549,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1261_c1_1409_1549",
      "annotations": {
        "id": [
          "1781_100325_scf_1261_c1_1409_1549"
        ],
        "product": [
          "3-oxoacyl-[acyl-carrier protein] reductase"
        ],
        "cath_funfam": [
          "3.40.50.720"
        ],
        "cog": [
          "COG1028"
        ],
        "ko": [
          "KO:K00059"
        ],
        "ec_number": [
          "EC:1.1.1.100"
        ],
        "pfam": [
          "adh_shor"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1262_c1": {
    "1781_100325_scf_1262_c1_1_1314": {
      "seqid": "NMDC:1781_100325_scf_1262_c1",
      "start": 0,
      "end": 1314,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1262_c1_1_1314",
      "annotations": {
        "id": [
          "1781_100325_scf_1262_c1_1_1314"
        ],
        "product": [
          "dihydroxy-acid dehydratase"
        ],
        "cog": [
          "COG0129"
        ],
        "ko": [
          "KO:K01687"
        ],
        "ec_number": [
          "EC:4.2.1.9"
        ],
        "pfam": [
          "ILVD_ED"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1262_c1_1461_1550": {
      "seqid": "NMDC:1781_100325_scf_1262_c1",
      "start": 1460,
      "end": 1550,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1262_c1_1461_1550",
      "annotations": {
        "id": [
          "1781_100325_scf_1262_c1_1461_1550"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1263_c1": {
    "1781_100325_scf_1263_c1_1_1548": {
      "seqid": "NMDC:1781_100325_scf_1263_c1",
      "start": 0,
      "end": 1548,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1263_c1_1_1548",
      "annotations": {
        "id": [
          "1781_100325_scf_1263_c1_1_1548"
        ],
        "product": [
          "starch synthase (maltosyl-transferring)"
        ],
        "cath_funfam": [
          "3.20.20.80"
        ],
        "cog": [
          "COG0366"
        ],
        "ko": [
          "KO:K16147"
        ],
        "ec_number": [
          "EC:2.4.99.16"
        ],
        "pfam": [
          "Alpha-amylas",
          "DUF341"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1264_c1": {
    "1781_100325_scf_1264_c1_1_723": {
      "seqid": "NMDC:1781_100325_scf_1264_c1",
      "start": 0,
      "end": 723,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1264_c1_1_723",
      "annotations": {
        "id": [
          "1781_100325_scf_1264_c1_1_723"
        ],
        "product": [
          "HD-GYP domain-containing protein (c-di-GMP phosphodiesterase class II)"
        ],
        "cath_funfam": [
          "1.10.3210.10"
        ],
        "cog": [
          "COG2206"
        ],
        "pfam": [
          "H",
          "HD_"
        ],
        "superfamily": [
          "SM00471"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1264_c1_763_1548": {
      "seqid": "NMDC:1781_100325_scf_1264_c1",
      "start": 762,
      "end": 1548,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1264_c1_763_1548",
      "annotations": {
        "id": [
          "1781_100325_scf_1264_c1_763_1548"
        ],
        "product": [
          "L-asparaginase II"
        ],
        "cog": [
          "COG4448"
        ],
        "pfam": [
          "Asparaginase_I"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1265_c1": {
    "1781_100325_scf_1265_c1_3_434": {
      "seqid": "NMDC:1781_100325_scf_1265_c1",
      "start": 2,
      "end": 434,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1265_c1_3_434",
      "annotations": {
        "id": [
          "1781_100325_scf_1265_c1_3_434"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.30.30.40"
        ],
        "pfam": [
          "ADH_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1265_c1_423_1403": {
      "seqid": "NMDC:1781_100325_scf_1265_c1",
      "start": 422,
      "end": 1403,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1265_c1_423_1403",
      "annotations": {
        "id": [
          "1781_100325_scf_1265_c1_423_1403"
        ],
        "product": [
          "NitT/TauT family transport system substrate-binding protein"
        ],
        "cath_funfam": [
          "3.40.190.10"
        ],
        "cog": [
          "COG0715"
        ],
        "ko": [
          "KO:K02051"
        ],
        "pfam": [
          "NMT",
          "NMT1_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1266_c1": {
    "1781_100325_scf_1266_c1_14_574": {
      "seqid": "NMDC:1781_100325_scf_1266_c1",
      "start": 13,
      "end": 574,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1266_c1_14_574",
      "annotations": {
        "id": [
          "1781_100325_scf_1266_c1_14_574"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "Phosphodies"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1266_c1_571_1548": {
      "seqid": "NMDC:1781_100325_scf_1266_c1",
      "start": 570,
      "end": 1548,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1266_c1_571_1548",
      "annotations": {
        "id": [
          "1781_100325_scf_1266_c1_571_1548"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "Phosphodies"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1267_c1": {
    "1781_100325_scf_1267_c1_1_369": {
      "seqid": "NMDC:1781_100325_scf_1267_c1",
      "start": 0,
      "end": 369,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1267_c1_1_369",
      "annotations": {
        "id": [
          "1781_100325_scf_1267_c1_1_369"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.410"
        ],
        "cog": [
          "COG3552"
        ],
        "ko": [
          "KO:K07161"
        ],
        "pfam": [
          "VWA_Cox"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1267_c1_393_836": {
      "seqid": "NMDC:1781_100325_scf_1267_c1",
      "start": 392,
      "end": 836,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1267_c1_393_836",
      "annotations": {
        "id": [
          "1781_100325_scf_1267_c1_393_836"
        ],
        "product": [
          "molybdopterin synthase catalytic subunit"
        ],
        "cath_funfam": [
          "3.90.1170.40"
        ],
        "cog": [
          "COG0314"
        ],
        "ko": [
          "KO:K03635"
        ],
        "ec_number": [
          "EC:2.8.1.12"
        ],
        "pfam": [
          "Moa"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1267_c1_927_1391": {
      "seqid": "NMDC:1781_100325_scf_1267_c1",
      "start": 926,
      "end": 1391,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1267_c1_927_1391",
      "annotations": {
        "id": [
          "1781_100325_scf_1267_c1_927_1391"
        ],
        "product": [
          "histidine triad (HIT) family protein"
        ],
        "cath_funfam": [
          "3.30.428.10"
        ],
        "cog": [
          "COG0537"
        ],
        "ko": [
          "KO:K02503"
        ],
        "pfam": [
          "DcpS_",
          "HI"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1267_c1_1449_1547": {
      "seqid": "NMDC:1781_100325_scf_1267_c1",
      "start": 1448,
      "end": 1547,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1267_c1_1449_1547",
      "annotations": {
        "id": [
          "1781_100325_scf_1267_c1_1449_1547"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1268_c1": {
    "1781_100325_scf_1268_c1_81_1331": {
      "seqid": "NMDC:1781_100325_scf_1268_c1",
      "start": 80,
      "end": 1331,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1268_c1_81_1331",
      "annotations": {
        "id": [
          "1781_100325_scf_1268_c1_81_1331"
        ],
        "product": [
          "crotonobetainyl-CoA:carnitine CoA-transferase CaiB-like acyl-CoA transferase"
        ],
        "cath_funfam": [
          "3.40.50.10540"
        ],
        "cog": [
          "COG1804"
        ],
        "pfam": [
          "CoA_transf_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1268_c1_1410_1547": {
      "seqid": "NMDC:1781_100325_scf_1268_c1",
      "start": 1409,
      "end": 1547,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1268_c1_1410_1547",
      "annotations": {
        "id": [
          "1781_100325_scf_1268_c1_1410_1547"
        ],
        "product": [
          "hypothetical protein"
        ],
        "superfamily": [
          "SM01184"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1269_c1": {
    "1781_100325_scf_1269_c1_1_546": {
      "seqid": "NMDC:1781_100325_scf_1269_c1",
      "start": 0,
      "end": 546,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1269_c1_1_546",
      "annotations": {
        "id": [
          "1781_100325_scf_1269_c1_1_546"
        ],
        "product": [
          "CPA2 family monovalent cation:H+ antiporter-2"
        ],
        "cath_funfam": [
          "1.20.1250.20"
        ],
        "cog": [
          "COG0475"
        ],
        "ko": [
          "KO:K03455"
        ],
        "pfam": [
          "Na_H_Exchange"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1269_c1_1093_1323": {
      "seqid": "NMDC:1781_100325_scf_1269_c1",
      "start": 1092,
      "end": 1323,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1269_c1_1093_1323",
      "annotations": {
        "id": [
          "1781_100325_scf_1269_c1_1093_1323"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG5588"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_126_c1": {
    "1781_100325_scf_126_c1_3_128": {
      "seqid": "NMDC:1781_100325_scf_126_c1",
      "start": 2,
      "end": 128,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_126_c1_3_128",
      "annotations": {
        "id": [
          "1781_100325_scf_126_c1_3_128"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.2300"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_126_c1_313_1434": {
      "seqid": "NMDC:1781_100325_scf_126_c1",
      "start": 312,
      "end": 1434,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_126_c1_313_1434",
      "annotations": {
        "id": [
          "1781_100325_scf_126_c1_313_1434"
        ],
        "product": [
          "ferredoxin-NADP reductase/nitrite reductase/ring-hydroxylating ferredoxin subunit"
        ],
        "cath_funfam": [
          "2.102.10.10",
          "2.40.30.10",
          "3.40.50.80"
        ],
        "cog": [
          "COG1018",
          "COG2146"
        ],
        "pfam": [
          "FAD_binding_",
          "NAD_binding_",
          "Riesk",
          "Rieske_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_126_c1_1501_2244": {
      "seqid": "NMDC:1781_100325_scf_126_c1",
      "start": 1500,
      "end": 2244,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_126_c1_1501_2244",
      "annotations": {
        "id": [
          "1781_100325_scf_126_c1_1501_2244"
        ],
        "product": [
          "uncharacterized protein"
        ],
        "cog": [
          "COG1938"
        ],
        "ko": [
          "KO:K06869"
        ],
        "pfam": [
          "PAC"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_126_c1_2490_2957": {
      "seqid": "NMDC:1781_100325_scf_126_c1",
      "start": 2489,
      "end": 2957,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_126_c1_2490_2957",
      "annotations": {
        "id": [
          "1781_100325_scf_126_c1_2490_2957"
        ],
        "product": [
          "nucleotide-binding universal stress UspA family protein"
        ],
        "cath_funfam": [
          "3.40.50.620"
        ],
        "cog": [
          "COG0589"
        ],
        "pfam": [
          "Us"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_126_c1_3119_3499": {
      "seqid": "NMDC:1781_100325_scf_126_c1",
      "start": 3118,
      "end": 3499,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_126_c1_3119_3499",
      "annotations": {
        "id": [
          "1781_100325_scf_126_c1_3119_3499"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.40.50.40"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1270_c1": {
    "1781_100325_scf_1270_c1_20_1249": {
      "seqid": "NMDC:1781_100325_scf_1270_c1",
      "start": 19,
      "end": 1249,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1270_c1_20_1249",
      "annotations": {
        "id": [
          "1781_100325_scf_1270_c1_20_1249"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3547"
        ],
        "pfam": [
          "DEDD_Tnp_IS11",
          "Transposase_2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1271_c1": {
    "1781_100325_scf_1271_c1_1_675": {
      "seqid": "NMDC:1781_100325_scf_1271_c1",
      "start": 0,
      "end": 675,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1271_c1_1_675",
      "annotations": {
        "id": [
          "1781_100325_scf_1271_c1_1_675"
        ],
        "product": [
          "BASS family bile acid:Na+ symporter"
        ],
        "cog": [
          "COG0385"
        ],
        "ko": [
          "KO:K03453"
        ],
        "pfam": [
          "SB"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1271_c1_886_1380": {
      "seqid": "NMDC:1781_100325_scf_1271_c1",
      "start": 885,
      "end": 1380,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1271_c1_886_1380",
      "annotations": {
        "id": [
          "1781_100325_scf_1271_c1_886_1380"
        ],
        "product": [
          "4a-hydroxytetrahydrobiopterin dehydratase"
        ],
        "cath_funfam": [
          "3.30.1360.20"
        ],
        "cog": [
          "COG2154"
        ],
        "ko": [
          "KO:K01724"
        ],
        "ec_number": [
          "EC:4.2.1.96"
        ],
        "pfam": [
          "Pterin_4"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1272_c1": {
    "1781_100325_scf_1272_c1_77_427": {
      "seqid": "NMDC:1781_100325_scf_1272_c1",
      "start": 76,
      "end": 427,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1272_c1_77_427",
      "annotations": {
        "id": [
          "1781_100325_scf_1272_c1_77_427"
        ],
        "product": [
          "anti-sigma B factor antagonist"
        ],
        "cath_funfam": [
          "3.30.750.24"
        ],
        "cog": [
          "COG1366"
        ],
        "ko": [
          "KO:K04749"
        ],
        "pfam": [
          "STA",
          "STAS_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1272_c1_610_1545": {
      "seqid": "NMDC:1781_100325_scf_1272_c1",
      "start": 609,
      "end": 1545,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1272_c1_610_1545",
      "annotations": {
        "id": [
          "1781_100325_scf_1272_c1_610_1545"
        ],
        "product": [
          "predicted PurR-regulated permease PerM"
        ],
        "cog": [
          "COG0628"
        ],
        "pfam": [
          "AI-2E_transpor"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1273_c1": {
    "1781_100325_scf_1273_c1_2_304": {
      "seqid": "NMDC:1781_100325_scf_1273_c1",
      "start": 1,
      "end": 304,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1273_c1_2_304",
      "annotations": {
        "id": [
          "1781_100325_scf_1273_c1_2_304"
        ],
        "product": [
          "glycerol-3-phosphate dehydrogenase"
        ],
        "cath_funfam": [
          "3.50.50.60"
        ],
        "cog": [
          "COG0578"
        ],
        "ko": [
          "KO:K00111"
        ],
        "ec_number": [
          "EC:1.1.5.3"
        ],
        "pfam": [
          "DA",
          "FAD_binding_",
          "NAD_binding_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1273_c1_332_601": {
      "seqid": "NMDC:1781_100325_scf_1273_c1",
      "start": 331,
      "end": 601,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1273_c1_332_601",
      "annotations": {
        "id": [
          "1781_100325_scf_1273_c1_332_601"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1273_c1_656_793": {
      "seqid": "NMDC:1781_100325_scf_1273_c1",
      "start": 655,
      "end": 793,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1273_c1_656_793",
      "annotations": {
        "id": [
          "1781_100325_scf_1273_c1_656_793"
        ],
        "product": [
          "glycerol kinase"
        ],
        "cath_funfam": [
          "3.30.420.40"
        ],
        "cog": [
          "COG0554"
        ],
        "ko": [
          "KO:K00864"
        ],
        "ec_number": [
          "EC:2.7.1.30"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1274_c1": {
    "1781_100325_scf_1274_c1_3_1433": {
      "seqid": "NMDC:1781_100325_scf_1274_c1",
      "start": 2,
      "end": 1433,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1274_c1_3_1433",
      "annotations": {
        "id": [
          "1781_100325_scf_1274_c1_3_1433"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1275_c1": {
    "1781_100325_scf_1275_c1_379_903": {
      "seqid": "NMDC:1781_100325_scf_1275_c1",
      "start": 378,
      "end": 903,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1275_c1_379_903",
      "annotations": {
        "id": [
          "1781_100325_scf_1275_c1_379_903"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1275_c1_1336_1500": {
      "seqid": "NMDC:1781_100325_scf_1275_c1",
      "start": 1335,
      "end": 1500,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1275_c1_1336_1500",
      "annotations": {
        "id": [
          "1781_100325_scf_1275_c1_1336_1500"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1276_c1": {
    "1781_100325_scf_1276_c1_770_913": {
      "seqid": "NMDC:1781_100325_scf_1276_c1",
      "start": 769,
      "end": 913,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1276_c1_770_913",
      "annotations": {
        "id": [
          "1781_100325_scf_1276_c1_770_913"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1276_c1_973_1149": {
      "seqid": "NMDC:1781_100325_scf_1276_c1",
      "start": 972,
      "end": 1149,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1276_c1_973_1149",
      "annotations": {
        "id": [
          "1781_100325_scf_1276_c1_973_1149"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1276_c1_1419_1544": {
      "seqid": "NMDC:1781_100325_scf_1276_c1",
      "start": 1418,
      "end": 1544,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1276_c1_1419_1544",
      "annotations": {
        "id": [
          "1781_100325_scf_1276_c1_1419_1544"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1277_c1": {
    "1781_100325_scf_1277_c1_2_148": {
      "seqid": "NMDC:1781_100325_scf_1277_c1",
      "start": 1,
      "end": 148,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1277_c1_2_148",
      "annotations": {
        "id": [
          "1781_100325_scf_1277_c1_2_148"
        ],
        "product": [
          "RNA-directed DNA polymerase"
        ],
        "ko": [
          "KO:K00986"
        ],
        "ec_number": [
          "EC:2.7.7.49"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1277_c1_264_539": {
      "seqid": "NMDC:1781_100325_scf_1277_c1",
      "start": 263,
      "end": 539,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1277_c1_264_539",
      "annotations": {
        "id": [
          "1781_100325_scf_1277_c1_264_539"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1277_c1_1466_1543": {
      "seqid": "NMDC:1781_100325_scf_1277_c1",
      "start": 1465,
      "end": 1543,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1277_c1_1466_1543",
      "annotations": {
        "id": [
          "1781_100325_scf_1277_c1_1466_1543"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1278_c1": {
    "1781_100325_scf_1278_c1_1_726": {
      "seqid": "NMDC:1781_100325_scf_1278_c1",
      "start": 0,
      "end": 726,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1278_c1_1_726",
      "annotations": {
        "id": [
          "1781_100325_scf_1278_c1_1_726"
        ],
        "product": [
          "phosphate starvation-inducible PhoH-like protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1702"
        ],
        "ko": [
          "KO:K06217"
        ],
        "pfam": [
          "AAA_3",
          "Pho"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1278_c1_719_1159": {
      "seqid": "NMDC:1781_100325_scf_1278_c1",
      "start": 718,
      "end": 1159,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1278_c1_719_1159",
      "annotations": {
        "id": [
          "1781_100325_scf_1278_c1_719_1159"
        ],
        "product": [
          "probable rRNA maturation factor"
        ],
        "cath_funfam": [
          "3.40.390.30"
        ],
        "cog": [
          "COG0319"
        ],
        "ko": [
          "KO:K07042"
        ],
        "pfam": [
          "UPF005"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1278_c1_1156_1545": {
      "seqid": "NMDC:1781_100325_scf_1278_c1",
      "start": 1155,
      "end": 1545,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1278_c1_1156_1545",
      "annotations": {
        "id": [
          "1781_100325_scf_1278_c1_1156_1545"
        ],
        "product": [
          "Mg2+/Co2+ transporter CorB"
        ],
        "cath_funfam": [
          "1.10.287.70"
        ],
        "cog": [
          "COG4536"
        ],
        "pfam": [
          "DUF2"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1279_c1": {
    "1781_100325_scf_1279_c1_56_646": {
      "seqid": "NMDC:1781_100325_scf_1279_c1",
      "start": 55,
      "end": 646,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1279_c1_56_646",
      "annotations": {
        "id": [
          "1781_100325_scf_1279_c1_56_646"
        ],
        "product": [
          "arginine decarboxylase"
        ],
        "cath_funfam": [
          "3.50.20.10"
        ],
        "cog": [
          "COG1945"
        ],
        "ko": [
          "KO:K02626"
        ],
        "ec_number": [
          "EC:4.1.1.19"
        ],
        "pfam": [
          "PvlArgD"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1279_c1_747_1166": {
      "seqid": "NMDC:1781_100325_scf_1279_c1",
      "start": 746,
      "end": 1166,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1279_c1_747_1166",
      "annotations": {
        "id": [
          "1781_100325_scf_1279_c1_747_1166"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.40.30.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_127_c1": {
    "1781_100325_scf_127_c1_15_938": {
      "seqid": "NMDC:1781_100325_scf_127_c1",
      "start": 14,
      "end": 938,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_127_c1_15_938",
      "annotations": {
        "id": [
          "1781_100325_scf_127_c1_15_938"
        ],
        "product": [
          "3-isopropylmalate/(R)-2-methylmalate dehydratase large subunit"
        ],
        "cath_funfam": [
          "3.30.499.10",
          "3.40.1060.10"
        ],
        "cog": [
          "COG0065"
        ],
        "ko": [
          "KO:K01703"
        ],
        "ec_number": [
          "EC:4.2.1.33",
          "EC:4.2.1.35"
        ],
        "pfam": [
          "Aconitas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_127_c1_935_1423": {
      "seqid": "NMDC:1781_100325_scf_127_c1",
      "start": 934,
      "end": 1423,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_127_c1_935_1423",
      "annotations": {
        "id": [
          "1781_100325_scf_127_c1_935_1423"
        ],
        "product": [
          "3-isopropylmalate/(R)-2-methylmalate dehydratase small subunit"
        ],
        "cath_funfam": [
          "3.20.19.10"
        ],
        "cog": [
          "COG0066"
        ],
        "ko": [
          "KO:K01704"
        ],
        "ec_number": [
          "EC:4.2.1.33",
          "EC:4.2.1.35"
        ],
        "pfam": [
          "Aconitase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_127_c1_1420_1647": {
      "seqid": "NMDC:1781_100325_scf_127_c1",
      "start": 1419,
      "end": 1647,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_127_c1_1420_1647",
      "annotations": {
        "id": [
          "1781_100325_scf_127_c1_1420_1647"
        ],
        "product": [
          "uncharacterized protein (UPF0248 family)"
        ],
        "cog": [
          "COG1531"
        ],
        "pfam": [
          "DUF50"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_127_c1_1681_2271": {
      "seqid": "NMDC:1781_100325_scf_127_c1",
      "start": 1680,
      "end": 2271,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_127_c1_1681_2271",
      "annotations": {
        "id": [
          "1781_100325_scf_127_c1_1681_2271"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG0727"
        ],
        "ko": [
          "KO:K06940"
        ],
        "pfam": [
          "CxxCxxC"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_127_c1_2264_2779": {
      "seqid": "NMDC:1781_100325_scf_127_c1",
      "start": 2263,
      "end": 2779,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_127_c1_2264_2779",
      "annotations": {
        "id": [
          "1781_100325_scf_127_c1_2264_2779"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_127_c1_2962_3138": {
      "seqid": "NMDC:1781_100325_scf_127_c1",
      "start": 2961,
      "end": 3138,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_127_c1_2962_3138",
      "annotations": {
        "id": [
          "1781_100325_scf_127_c1_2962_3138"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_127_c1_3265_3561": {
      "seqid": "NMDC:1781_100325_scf_127_c1",
      "start": 3264,
      "end": 3561,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_127_c1_3265_3561",
      "annotations": {
        "id": [
          "1781_100325_scf_127_c1_3265_3561"
        ],
        "product": [
          "L-asparagine transporter-like permease"
        ],
        "cog": [
          "COG1113"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1280_c1": {
    "1781_100325_scf_1280_c1_8_652": {
      "seqid": "NMDC:1781_100325_scf_1280_c1",
      "start": 7,
      "end": 652,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1280_c1_8_652",
      "annotations": {
        "id": [
          "1781_100325_scf_1280_c1_8_652"
        ],
        "product": [
          "RNA polymerase primary sigma factor"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG0568"
        ],
        "ko": [
          "KO:K03086"
        ],
        "pfam": [
          "Sigma70_r"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1280_c1_1252_1542": {
      "seqid": "NMDC:1781_100325_scf_1280_c1",
      "start": 1251,
      "end": 1542,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1280_c1_1252_1542",
      "annotations": {
        "id": [
          "1781_100325_scf_1280_c1_1252_1542"
        ],
        "product": [
          "Ala-tRNA(Pro) deacylase"
        ],
        "cath_funfam": [
          "3.90.960.10"
        ],
        "cog": [
          "COG3760"
        ],
        "ko": [
          "KO:K19055"
        ],
        "ec_number": [
          "EC:3.1.1.-"
        ],
        "pfam": [
          "tRNA_edi"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1281_c1": {
    "1781_100325_scf_1281_c1_1_204": {
      "seqid": "NMDC:1781_100325_scf_1281_c1",
      "start": 0,
      "end": 204,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1281_c1_1_204",
      "annotations": {
        "id": [
          "1781_100325_scf_1281_c1_1_204"
        ],
        "product": [
          "small subunit ribosomal protein S19"
        ],
        "cath_funfam": [
          "3.30.860.10"
        ],
        "cog": [
          "COG0185"
        ],
        "ko": [
          "KO:K02965"
        ],
        "pfam": [
          "Ribosomal_S1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1281_c1_204_1034": {
      "seqid": "NMDC:1781_100325_scf_1281_c1",
      "start": 203,
      "end": 1034,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1281_c1_204_1034",
      "annotations": {
        "id": [
          "1781_100325_scf_1281_c1_204_1034"
        ],
        "product": [
          "large subunit ribosomal protein L2"
        ],
        "cath_funfam": [
          "2.30.30.30",
          "2.40.50.140",
          "4.10.950.10"
        ],
        "cog": [
          "COG0090"
        ],
        "ko": [
          "KO:K02886"
        ],
        "pfam": [
          "Ribosomal_L",
          "Ribosomal_L2_"
        ],
        "superfamily": [
          "SM01382",
          "SM01383"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1281_c1_1038_1328": {
      "seqid": "NMDC:1781_100325_scf_1281_c1",
      "start": 1037,
      "end": 1328,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1281_c1_1038_1328",
      "annotations": {
        "id": [
          "1781_100325_scf_1281_c1_1038_1328"
        ],
        "product": [
          "large subunit ribosomal protein L23"
        ],
        "cath_funfam": [
          "3.30.70.330"
        ],
        "cog": [
          "COG0089"
        ],
        "ko": [
          "KO:K02892"
        ],
        "pfam": [
          "Ribosomal_L2"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1281_c1_1325_1543": {
      "seqid": "NMDC:1781_100325_scf_1281_c1",
      "start": 1324,
      "end": 1543,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1281_c1_1325_1543",
      "annotations": {
        "id": [
          "1781_100325_scf_1281_c1_1325_1543"
        ],
        "product": [
          "ribosomal protein L4"
        ],
        "cath_funfam": [
          "3.40.1370.10"
        ],
        "cog": [
          "COG0088"
        ],
        "pfam": [
          "Ribosomal_L"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1282_c1": {
    "1781_100325_scf_1282_c1_2_196": {
      "seqid": "NMDC:1781_100325_scf_1282_c1",
      "start": 1,
      "end": 196,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1282_c1_2_196",
      "annotations": {
        "id": [
          "1781_100325_scf_1282_c1_2_196"
        ],
        "product": [
          "peroxiredoxin"
        ],
        "cath_funfam": [
          "3.40.30.10"
        ],
        "cog": [
          "COG2077"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1282_c1_215_550": {
      "seqid": "NMDC:1781_100325_scf_1282_c1",
      "start": 214,
      "end": 550,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1282_c1_215_550",
      "annotations": {
        "id": [
          "1781_100325_scf_1282_c1_215_550"
        ],
        "product": [
          "peroxiredoxin"
        ],
        "cath_funfam": [
          "3.40.30.10"
        ],
        "cog": [
          "COG1225"
        ],
        "pfam": [
          "AhpC-TS"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1282_c1_832_1275": {
      "seqid": "NMDC:1781_100325_scf_1282_c1",
      "start": 831,
      "end": 1275,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1282_c1_832_1275",
      "annotations": {
        "id": [
          "1781_100325_scf_1282_c1_832_1275"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1282_c1_1441_1542": {
      "seqid": "NMDC:1781_100325_scf_1282_c1",
      "start": 1440,
      "end": 1542,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1282_c1_1441_1542",
      "annotations": {
        "id": [
          "1781_100325_scf_1282_c1_1441_1542"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1283_c1": {
    "1781_100325_scf_1283_c1_58_1131": {
      "seqid": "NMDC:1781_100325_scf_1283_c1",
      "start": 57,
      "end": 1131,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1283_c1_58_1131",
      "annotations": {
        "id": [
          "1781_100325_scf_1283_c1_58_1131"
        ],
        "product": [
          "N-acetyl-gamma-glutamyl-phosphate/LysW-gamma-L-alpha-aminoadipyl-6-phosphate reductase"
        ],
        "cath_funfam": [
          "3.30.360.10",
          "3.40.50.720"
        ],
        "cog": [
          "COG0002"
        ],
        "ko": [
          "KO:K05829"
        ],
        "ec_number": [
          "EC:1.2.1.-"
        ],
        "pfam": [
          "Semialdhyde_d",
          "Semialdhyde_dh"
        ],
        "superfamily": [
          "SM00859"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1283_c1_1128_1544": {
      "seqid": "NMDC:1781_100325_scf_1283_c1",
      "start": 1127,
      "end": 1544,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1283_c1_1128_1544",
      "annotations": {
        "id": [
          "1781_100325_scf_1283_c1_1128_1544"
        ],
        "product": [
          "acetylglutamate/LysW-gamma-L-alpha-aminoadipate kinase"
        ],
        "cath_funfam": [
          "3.40.1160.10"
        ],
        "cog": [
          "COG0548"
        ],
        "ko": [
          "KO:K05828"
        ],
        "ec_number": [
          "EC:2.7.2.-"
        ],
        "pfam": [
          "AA_kinas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1284_c1": {
    "1781_100325_scf_1284_c1_30_443": {
      "seqid": "NMDC:1781_100325_scf_1284_c1",
      "start": 29,
      "end": 443,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1284_c1_30_443",
      "annotations": {
        "id": [
          "1781_100325_scf_1284_c1_30_443"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG1931"
        ],
        "ko": [
          "KO:K09736"
        ],
        "pfam": [
          "RNA_bindin"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1284_c1_461_1045": {
      "seqid": "NMDC:1781_100325_scf_1284_c1",
      "start": 460,
      "end": 1045,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1284_c1_461_1045",
      "annotations": {
        "id": [
          "1781_100325_scf_1284_c1_461_1045"
        ],
        "product": [
          "dephospho-CoA kinase"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG0237"
        ],
        "pfam": [
          "AA",
          "AAA_1"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1284_c1_1080_1310": {
      "seqid": "NMDC:1781_100325_scf_1284_c1",
      "start": 1079,
      "end": 1310,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1284_c1_1080_1310",
      "annotations": {
        "id": [
          "1781_100325_scf_1284_c1_1080_1310"
        ],
        "product": [
          "histone H3/H4"
        ],
        "cath_funfam": [
          "1.10.20.10"
        ],
        "cog": [
          "COG2036"
        ],
        "pfam": [
          "CBFD_NFYB_HM",
          "Histon"
        ],
        "superfamily": [
          "SM00417"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1285_c1": {
    "1781_100325_scf_1285_c1_3_359": {
      "seqid": "NMDC:1781_100325_scf_1285_c1",
      "start": 2,
      "end": 359,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1285_c1_3_359",
      "annotations": {
        "id": [
          "1781_100325_scf_1285_c1_3_359"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.20.20.30"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1285_c1_389_751": {
      "seqid": "NMDC:1781_100325_scf_1285_c1",
      "start": 388,
      "end": 751,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1285_c1_389_751",
      "annotations": {
        "id": [
          "1781_100325_scf_1285_c1_389_751"
        ],
        "product": [
          "rubrerythrin"
        ],
        "cath_funfam": [
          "2.20.20.30"
        ],
        "cog": [
          "COG1592"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1285_c1_880_1446": {
      "seqid": "NMDC:1781_100325_scf_1285_c1",
      "start": 879,
      "end": 1446,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1285_c1_880_1446",
      "annotations": {
        "id": [
          "1781_100325_scf_1285_c1_880_1446"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.20.1250.20"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1285_c1_1375_1509": {
      "seqid": "NMDC:1781_100325_scf_1285_c1",
      "start": 1374,
      "end": 1509,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1285_c1_1375_1509",
      "annotations": {
        "id": [
          "1781_100325_scf_1285_c1_1375_1509"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1286_c1": {
    "1781_100325_scf_1286_c1_1_1542": {
      "seqid": "NMDC:1781_100325_scf_1286_c1",
      "start": 0,
      "end": 1542,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1286_c1_1_1542",
      "annotations": {
        "id": [
          "1781_100325_scf_1286_c1_1_1542"
        ],
        "product": [
          "ATP-dependent exoDNAse (exonuclease V) beta subunit"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1074"
        ],
        "pfam": [
          "AAA_1",
          "UvrD-helicas",
          "UvrD_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1287_c1": {
    "1781_100325_scf_1287_c1_1_177": {
      "seqid": "NMDC:1781_100325_scf_1287_c1",
      "start": 0,
      "end": 177,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1287_c1_1_177",
      "annotations": {
        "id": [
          "1781_100325_scf_1287_c1_1_177"
        ],
        "product": [
          "translation initiation factor 2 subunit 1"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG1093"
        ],
        "ko": [
          "KO:K03237"
        ],
        "pfam": [
          "S"
        ],
        "superfamily": [
          "SM00316"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1287_c1_216_749": {
      "seqid": "NMDC:1781_100325_scf_1287_c1",
      "start": 215,
      "end": 749,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1287_c1_216_749",
      "annotations": {
        "id": [
          "1781_100325_scf_1287_c1_216_749"
        ],
        "product": [
          "cob(I)alamin adenosyltransferase"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG2109"
        ],
        "ko": [
          "KO:K19221"
        ],
        "ec_number": [
          "EC:2.5.1.17"
        ],
        "pfam": [
          "CobA_CobO_Btu"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1287_c1_840_1541": {
      "seqid": "NMDC:1781_100325_scf_1287_c1",
      "start": 839,
      "end": 1541,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1287_c1_840_1541",
      "annotations": {
        "id": [
          "1781_100325_scf_1287_c1_840_1541"
        ],
        "product": [
          "cobyrinic acid a",
          "c-diamide synthase"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1797"
        ],
        "ko": [
          "KO:K02224"
        ],
        "ec_number": [
          "EC:6.3.5.11",
          "EC:6.3.5.9"
        ],
        "pfam": [
          "AAA_2",
          "Cbi"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1288_c1": {
    "1781_100325_scf_1288_c1_2_1222": {
      "seqid": "NMDC:1781_100325_scf_1288_c1",
      "start": 1,
      "end": 1222,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1288_c1_2_1222",
      "annotations": {
        "id": [
          "1781_100325_scf_1288_c1_2_1222"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "Cellulas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1288_c1_1363_1542": {
      "seqid": "NMDC:1781_100325_scf_1288_c1",
      "start": 1362,
      "end": 1542,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1288_c1_1363_1542",
      "annotations": {
        "id": [
          "1781_100325_scf_1288_c1_1363_1542"
        ],
        "product": [
          "predicted acylesterase/phospholipase RssA"
        ],
        "cath_funfam": [
          "3.40.1090.10"
        ],
        "cog": [
          "COG1752"
        ],
        "pfam": [
          "Patati"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1289_c1": {
    "1781_100325_scf_1289_c1_14_562": {
      "seqid": "NMDC:1781_100325_scf_1289_c1",
      "start": 13,
      "end": 562,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1289_c1_14_562",
      "annotations": {
        "id": [
          "1781_100325_scf_1289_c1_14_562"
        ],
        "product": [
          "cell division protein FtsZ"
        ],
        "cath_funfam": [
          "3.30.1330.20"
        ],
        "cog": [
          "COG0206"
        ],
        "ko": [
          "KO:K03531"
        ],
        "pfam": [
          "FtsZ_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1289_c1_752_1471": {
      "seqid": "NMDC:1781_100325_scf_1289_c1",
      "start": 751,
      "end": 1471,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1289_c1_752_1471",
      "annotations": {
        "id": [
          "1781_100325_scf_1289_c1_752_1471"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.20.20.10"
        ],
        "cog": [
          "COG0325"
        ],
        "ko": [
          "KO:K06997"
        ],
        "pfam": [
          "Ala_racemase_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_128_c1": {
    "1781_100325_scf_128_c1_2_364": {
      "seqid": "NMDC:1781_100325_scf_128_c1",
      "start": 1,
      "end": 364,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_128_c1_2_364",
      "annotations": {
        "id": [
          "1781_100325_scf_128_c1_2_364"
        ],
        "product": [
          "ribosome maturation protein SDO1"
        ],
        "cath_funfam": [
          "3.30.1250.10"
        ],
        "cog": [
          "COG1500"
        ],
        "ko": [
          "KO:K14574"
        ],
        "pfam": [
          "SBD"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_128_c1_474_1958": {
      "seqid": "NMDC:1781_100325_scf_128_c1",
      "start": 473,
      "end": 1958,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_128_c1_474_1958",
      "annotations": {
        "id": [
          "1781_100325_scf_128_c1_474_1958"
        ],
        "product": [
          "Amt family ammonium transporter"
        ],
        "cath_funfam": [
          "1.10.3430.10"
        ],
        "cog": [
          "COG0004"
        ],
        "ko": [
          "KO:K03320"
        ],
        "pfam": [
          "Ammonium_trans"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_128_c1_2445_2669": {
      "seqid": "NMDC:1781_100325_scf_128_c1",
      "start": 2444,
      "end": 2669,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_128_c1_2445_2669",
      "annotations": {
        "id": [
          "1781_100325_scf_128_c1_2445_2669"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_128_c1_2884_3561": {
      "seqid": "NMDC:1781_100325_scf_128_c1",
      "start": 2883,
      "end": 3561,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_128_c1_2884_3561",
      "annotations": {
        "id": [
          "1781_100325_scf_128_c1_2884_3561"
        ],
        "product": [
          "tetratricopeptide (TPR) repeat protein"
        ],
        "cath_funfam": [
          "1.25.40.10"
        ],
        "cog": [
          "COG0457"
        ],
        "pfam": [
          "TPR_",
          "TPR_1"
        ],
        "superfamily": [
          "SM00028"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1290_c1": {
    "1781_100325_scf_1290_c1_1_1470": {
      "seqid": "NMDC:1781_100325_scf_1290_c1",
      "start": 0,
      "end": 1470,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1290_c1_1_1470",
      "annotations": {
        "id": [
          "1781_100325_scf_1290_c1_1_1470"
        ],
        "product": [
          "tight adherence protein B"
        ],
        "cath_funfam": [
          "3.40.50.410"
        ],
        "cog": [
          "COG4965"
        ],
        "ko": [
          "KO:K12510"
        ],
        "pfam": [
          "T2SS",
          "VW",
          "VWA_"
        ],
        "superfamily": [
          "SM00327"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1291_c1": {
    "1781_100325_scf_1291_c1_3_641": {
      "seqid": "NMDC:1781_100325_scf_1291_c1",
      "start": 2,
      "end": 641,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1291_c1_3_641",
      "annotations": {
        "id": [
          "1781_100325_scf_1291_c1_3_641"
        ],
        "product": [
          "aspartyl-tRNA synthetase"
        ],
        "cath_funfam": [
          "3.30.930.10"
        ],
        "cog": [
          "COG0017"
        ],
        "ko": [
          "KO:K01876"
        ],
        "ec_number": [
          "EC:6.1.1.12"
        ],
        "pfam": [
          "tRNA-synt_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1291_c1_675_947": {
      "seqid": "NMDC:1781_100325_scf_1291_c1",
      "start": 674,
      "end": 947,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1291_c1_675_947",
      "annotations": {
        "id": [
          "1781_100325_scf_1291_c1_675_947"
        ],
        "product": [
          "aspartyl/glutamyl-tRNA(Asn/Gln) amidotransferase C subunit"
        ],
        "cog": [
          "COG0721"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1291_c1_949_1539": {
      "seqid": "NMDC:1781_100325_scf_1291_c1",
      "start": 948,
      "end": 1539,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1291_c1_949_1539",
      "annotations": {
        "id": [
          "1781_100325_scf_1291_c1_949_1539"
        ],
        "product": [
          "aspartyl-tRNA(Asn)/glutamyl-tRNA(Gln) amidotransferase subunit A"
        ],
        "cath_funfam": [
          "3.90.1300.10"
        ],
        "cog": [
          "COG0154"
        ],
        "ko": [
          "KO:K02433"
        ],
        "ec_number": [
          "EC:6.3.5.6",
          "EC:6.3.5.7"
        ],
        "pfam": [
          "Amidas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1292_c1": {
    "1781_100325_scf_1292_c1_2_334": {
      "seqid": "NMDC:1781_100325_scf_1292_c1",
      "start": 1,
      "end": 334,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1292_c1_2_334",
      "annotations": {
        "id": [
          "1781_100325_scf_1292_c1_2_334"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1292_c1_312_1250": {
      "seqid": "NMDC:1781_100325_scf_1292_c1",
      "start": 311,
      "end": 1250,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1292_c1_312_1250",
      "annotations": {
        "id": [
          "1781_100325_scf_1292_c1_312_1250"
        ],
        "product": [
          "glycosyltransferase involved in cell wall biosynthesis"
        ],
        "cath_funfam": [
          "3.90.550.10"
        ],
        "cog": [
          "COG0463"
        ],
        "pfam": [
          "Glyco_tranf_2_",
          "Glycos_transf_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1293_c1": {
    "1781_100325_scf_1293_c1_99_737": {
      "seqid": "NMDC:1781_100325_scf_1293_c1",
      "start": 98,
      "end": 737,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1293_c1_99_737",
      "annotations": {
        "id": [
          "1781_100325_scf_1293_c1_99_737"
        ],
        "product": [
          "aspartyl-tRNA(Asn)/glutamyl-tRNA(Gln) amidotransferase subunit A"
        ],
        "cath_funfam": [
          "3.90.1300.10"
        ],
        "cog": [
          "COG0154"
        ],
        "ko": [
          "KO:K02433"
        ],
        "ec_number": [
          "EC:6.3.5.6",
          "EC:6.3.5.7"
        ],
        "pfam": [
          "Amidas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1293_c1_715_1233": {
      "seqid": "NMDC:1781_100325_scf_1293_c1",
      "start": 714,
      "end": 1233,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1293_c1_715_1233",
      "annotations": {
        "id": [
          "1781_100325_scf_1293_c1_715_1233"
        ],
        "product": [
          "6-phosphogluconolactonase"
        ],
        "cath_funfam": [
          "3.40.50.1360"
        ],
        "cog": [
          "COG0363"
        ],
        "ko": [
          "KO:K01057"
        ],
        "ec_number": [
          "EC:3.1.1.31"
        ],
        "pfam": [
          "Glucosamine_is"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1293_c1_1314_1538": {
      "seqid": "NMDC:1781_100325_scf_1293_c1",
      "start": 1313,
      "end": 1538,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1293_c1_1314_1538",
      "annotations": {
        "id": [
          "1781_100325_scf_1293_c1_1314_1538"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.280.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1294_c1": {
    "1781_100325_scf_1294_c1_380_1147": {
      "seqid": "NMDC:1781_100325_scf_1294_c1",
      "start": 379,
      "end": 1147,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1294_c1_380_1147",
      "annotations": {
        "id": [
          "1781_100325_scf_1294_c1_380_1147"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.1940.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1294_c1_1313_1525": {
      "seqid": "NMDC:1781_100325_scf_1294_c1",
      "start": 1312,
      "end": 1525,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1294_c1_1313_1525",
      "annotations": {
        "id": [
          "1781_100325_scf_1294_c1_1313_1525"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1295_c1": {
    "1781_100325_scf_1295_c1_32_1117": {
      "seqid": "NMDC:1781_100325_scf_1295_c1",
      "start": 31,
      "end": 1117,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1295_c1_32_1117",
      "annotations": {
        "id": [
          "1781_100325_scf_1295_c1_32_1117"
        ],
        "product": [
          "carbamoyl-phosphate synthase small subunit"
        ],
        "cath_funfam": [
          "3.40.50.880",
          "3.50.30.20"
        ],
        "cog": [
          "COG0505"
        ],
        "ko": [
          "KO:K01956"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "pfam": [
          "CPSase_sm_chai",
          "GATas",
          "Peptidase_C2"
        ],
        "superfamily": [
          "SM01097"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1295_c1_1226_1540": {
      "seqid": "NMDC:1781_100325_scf_1295_c1",
      "start": 1225,
      "end": 1540,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1295_c1_1226_1540",
      "annotations": {
        "id": [
          "1781_100325_scf_1295_c1_1226_1540"
        ],
        "product": [
          "carbamoyl-phosphate synthase large subunit"
        ],
        "cath_funfam": [
          "3.40.50.20"
        ],
        "cog": [
          "COG0458"
        ],
        "ko": [
          "KO:K01955"
        ],
        "ec_number": [
          "EC:6.3.5.5"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1296_c1": {
    "1781_100325_scf_1296_c1_238_1530": {
      "seqid": "NMDC:1781_100325_scf_1296_c1",
      "start": 237,
      "end": 1530,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1296_c1_238_1530",
      "annotations": {
        "id": [
          "1781_100325_scf_1296_c1_238_1530"
        ],
        "product": [
          "imidazolonepropionase-like amidohydrolase"
        ],
        "cath_funfam": [
          "1.10.287.440",
          "2.30.40.10",
          "3.20.20.140"
        ],
        "cog": [
          "COG1228"
        ],
        "pfam": [
          "Amidohydro_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1297_c1": {
    "1781_100325_scf_1297_c1_1_888": {
      "seqid": "NMDC:1781_100325_scf_1297_c1",
      "start": 0,
      "end": 888,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1297_c1_1_888",
      "annotations": {
        "id": [
          "1781_100325_scf_1297_c1_1_888"
        ],
        "product": [
          "Tfp pilus assembly protein PilX"
        ],
        "cog": [
          "COG4726"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1297_c1_898_1527": {
      "seqid": "NMDC:1781_100325_scf_1297_c1",
      "start": 897,
      "end": 1527,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1297_c1_898_1527",
      "annotations": {
        "id": [
          "1781_100325_scf_1297_c1_898_1527"
        ],
        "product": [
          "type II secretory pathway pseudopilin PulG"
        ],
        "cog": [
          "COG2165"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1298_c1": {
    "1781_100325_scf_1298_c1_113_1183": {
      "seqid": "NMDC:1781_100325_scf_1298_c1",
      "start": 112,
      "end": 1183,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1298_c1_113_1183",
      "annotations": {
        "id": [
          "1781_100325_scf_1298_c1_113_1183"
        ],
        "product": [
          "glycine betaine/proline transport system ATP-binding protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG4175"
        ],
        "ko": [
          "KO:K02000"
        ],
        "ec_number": [
          "EC:3.6.3.32"
        ],
        "pfam": [
          "ABC_tra"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1298_c1_1186_1536": {
      "seqid": "NMDC:1781_100325_scf_1298_c1",
      "start": 1185,
      "end": 1536,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1298_c1_1186_1536",
      "annotations": {
        "id": [
          "1781_100325_scf_1298_c1_1186_1536"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1299_c1": {
    "1781_100325_scf_1299_c1_334_1074": {
      "seqid": "NMDC:1781_100325_scf_1299_c1",
      "start": 333,
      "end": 1074,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1299_c1_334_1074",
      "annotations": {
        "id": [
          "1781_100325_scf_1299_c1_334_1074"
        ],
        "product": [
          "ureidoacrylate peracid hydrolase"
        ],
        "cath_funfam": [
          "3.40.50.850"
        ],
        "cog": [
          "COG1335"
        ],
        "ko": [
          "KO:K09020"
        ],
        "ec_number": [
          "EC:3.5.1.110"
        ],
        "pfam": [
          "Isochorismatas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1299_c1_1345_1536": {
      "seqid": "NMDC:1781_100325_scf_1299_c1",
      "start": 1344,
      "end": 1536,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1299_c1_1345_1536",
      "annotations": {
        "id": [
          "1781_100325_scf_1299_c1_1345_1536"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_129_c1": {
    "1781_100325_scf_129_c1_4_804": {
      "seqid": "NMDC:1781_100325_scf_129_c1",
      "start": 3,
      "end": 804,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_129_c1_4_804",
      "annotations": {
        "id": [
          "1781_100325_scf_129_c1_4_804"
        ],
        "product": [
          "thiosulfate/3-mercaptopyruvate sulfurtransferase"
        ],
        "cath_funfam": [
          "3.40.250.10"
        ],
        "cog": [
          "COG2897"
        ],
        "ko": [
          "KO:K01011"
        ],
        "ec_number": [
          "EC:2.8.1.1",
          "EC:2.8.1.2"
        ],
        "pfam": [
          "Rhodanes"
        ],
        "superfamily": [
          "SM00450"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_129_c1_899_1522": {
      "seqid": "NMDC:1781_100325_scf_129_c1",
      "start": 898,
      "end": 1522,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_129_c1_899_1522",
      "annotations": {
        "id": [
          "1781_100325_scf_129_c1_899_1522"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_129_c1_2276_2440": {
      "seqid": "NMDC:1781_100325_scf_129_c1",
      "start": 2275,
      "end": 2440,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_129_c1_2276_2440",
      "annotations": {
        "id": [
          "1781_100325_scf_129_c1_2276_2440"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_129_c1_2911_3543": {
      "seqid": "NMDC:1781_100325_scf_129_c1",
      "start": 2910,
      "end": 3543,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_129_c1_2911_3543",
      "annotations": {
        "id": [
          "1781_100325_scf_129_c1_2911_3543"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_12_c1": {
    "1781_100325_scf_12_c1_1_381": {
      "seqid": "NMDC:1781_100325_scf_12_c1",
      "start": 0,
      "end": 381,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_12_c1_1_381",
      "annotations": {
        "id": [
          "1781_100325_scf_12_c1_1_381"
        ],
        "product": [
          "predicted dithiol-disulfide oxidoreductase (DUF899 family)"
        ],
        "cog": [
          "COG4312"
        ],
        "pfam": [
          "DUF89"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_12_c1_1278_2333": {
      "seqid": "NMDC:1781_100325_scf_12_c1",
      "start": 1277,
      "end": 2333,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_12_c1_1278_2333",
      "annotations": {
        "id": [
          "1781_100325_scf_12_c1_1278_2333"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_12_c1_2673_2972": {
      "seqid": "NMDC:1781_100325_scf_12_c1",
      "start": 2672,
      "end": 2972,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_12_c1_2673_2972",
      "annotations": {
        "id": [
          "1781_100325_scf_12_c1_2673_2972"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_12_c1_3173_3322": {
      "seqid": "NMDC:1781_100325_scf_12_c1",
      "start": 3172,
      "end": 3322,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_12_c1_3173_3322",
      "annotations": {
        "id": [
          "1781_100325_scf_12_c1_3173_3322"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_12_c1_3771_4556": {
      "seqid": "NMDC:1781_100325_scf_12_c1",
      "start": 3770,
      "end": 4556,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_12_c1_3771_4556",
      "annotations": {
        "id": [
          "1781_100325_scf_12_c1_3771_4556"
        ],
        "product": [
          "N-formylglutamate amidohydrolase"
        ],
        "cog": [
          "COG3741"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_12_c1_4907_5962": {
      "seqid": "NMDC:1781_100325_scf_12_c1",
      "start": 4906,
      "end": 5962,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_12_c1_4907_5962",
      "annotations": {
        "id": [
          "1781_100325_scf_12_c1_4907_5962"
        ],
        "product": [
          "N-acetylneuraminic acid mutarotase"
        ],
        "cath_funfam": [
          "2.120.10.80"
        ],
        "cog": [
          "COG3055"
        ],
        "pfam": [
          "Kelch_"
        ],
        "superfamily": [
          "SM00612"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_12_c1_6748_7125": {
      "seqid": "NMDC:1781_100325_scf_12_c1",
      "start": 6747,
      "end": 7125,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_12_c1_6748_7125",
      "annotations": {
        "id": [
          "1781_100325_scf_12_c1_6748_7125"
        ],
        "product": [
          "uncharacterized protein (TIGR02246 family)"
        ],
        "cath_funfam": [
          "3.10.450.50"
        ],
        "cog": [
          "COG4319"
        ],
        "pfam": [
          "DUF444",
          "SnoaL_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1300_c1": {
    "1781_100325_scf_1300_c1_1_1191": {
      "seqid": "NMDC:1781_100325_scf_1300_c1",
      "start": 0,
      "end": 1191,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1300_c1_1_1191",
      "annotations": {
        "id": [
          "1781_100325_scf_1300_c1_1_1191"
        ],
        "product": [
          "4-amino-4-deoxy-L-arabinose transferase-like glycosyltransferase"
        ],
        "cog": [
          "COG1807"
        ],
        "pfam": [
          "PMT_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1301_c1": {
    "1781_100325_scf_1301_c1_3_1535": {
      "seqid": "NMDC:1781_100325_scf_1301_c1",
      "start": 2,
      "end": 1535,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1301_c1_3_1535",
      "annotations": {
        "id": [
          "1781_100325_scf_1301_c1_3_1535"
        ],
        "product": [
          "ribonucleoside-diphosphate reductase alpha chain"
        ],
        "cath_funfam": [
          "3.20.70.20"
        ],
        "cog": [
          "COG0209"
        ],
        "ko": [
          "KO:K00525"
        ],
        "ec_number": [
          "EC:1.17.4.1"
        ],
        "pfam": [
          "Ribonuc_red_2_",
          "Ribonuc_red_lg"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1302_c1": {
    "1781_100325_scf_1302_c1_1_726": {
      "seqid": "NMDC:1781_100325_scf_1302_c1",
      "start": 0,
      "end": 726,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1302_c1_1_726",
      "annotations": {
        "id": [
          "1781_100325_scf_1302_c1_1_726"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1302_c1_749_1147": {
      "seqid": "NMDC:1781_100325_scf_1302_c1",
      "start": 748,
      "end": 1147,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1302_c1_749_1147",
      "annotations": {
        "id": [
          "1781_100325_scf_1302_c1_749_1147"
        ],
        "product": [
          "secondary thiamine-phosphate synthase enzyme"
        ],
        "cath_funfam": [
          "2.60.120.460"
        ],
        "cog": [
          "COG0432"
        ],
        "pfam": [
          "UPF004"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1302_c1_1152_1535": {
      "seqid": "NMDC:1781_100325_scf_1302_c1",
      "start": 1151,
      "end": 1535,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1302_c1_1152_1535",
      "annotations": {
        "id": [
          "1781_100325_scf_1302_c1_1152_1535"
        ],
        "product": [
          "23S rRNA (uracil1939-C5)-methyltransferase"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG2265"
        ],
        "ko": [
          "KO:K03215"
        ],
        "ec_number": [
          "EC:2.1.1.190"
        ],
        "pfam": [
          "TRA"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1303_c1": {
    "1781_100325_scf_1303_c1_1_1527": {
      "seqid": "NMDC:1781_100325_scf_1303_c1",
      "start": 0,
      "end": 1527,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1303_c1_1_1527",
      "annotations": {
        "id": [
          "1781_100325_scf_1303_c1_1_1527"
        ],
        "product": [
          "DNA-directed RNA polymerase subunit beta'"
        ],
        "cath_funfam": [
          "2.40.40.20"
        ],
        "cog": [
          "COG0086"
        ],
        "ko": [
          "KO:K03046"
        ],
        "ec_number": [
          "EC:2.7.7.6"
        ],
        "pfam": [
          "RNA_pol_Rpb1_"
        ],
        "superfamily": [
          "SM00663"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1304_c1": {
    "1781_100325_scf_1304_c1_280_432": {
      "seqid": "NMDC:1781_100325_scf_1304_c1",
      "start": 279,
      "end": 432,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1304_c1_280_432",
      "annotations": {
        "id": [
          "1781_100325_scf_1304_c1_280_432"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.160.60"
        ],
        "superfamily": [
          "SM00355"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1304_c1_659_805": {
      "seqid": "NMDC:1781_100325_scf_1304_c1",
      "start": 658,
      "end": 805,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1304_c1_659_805",
      "annotations": {
        "id": [
          "1781_100325_scf_1304_c1_659_805"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.60.20"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1304_c1_963_1535": {
      "seqid": "NMDC:1781_100325_scf_1304_c1",
      "start": 962,
      "end": 1535,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1304_c1_963_1535",
      "annotations": {
        "id": [
          "1781_100325_scf_1304_c1_963_1535"
        ],
        "product": [
          "23S rRNA (uridine2552-2'-O)-methyltransferase"
        ],
        "cath_funfam": [
          "3.40.50.150"
        ],
        "cog": [
          "COG0293"
        ],
        "ko": [
          "KO:K02427"
        ],
        "ec_number": [
          "EC:2.1.1.166"
        ],
        "pfam": [
          "Fts"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1305_c1": {
    "1781_100325_scf_1305_c1_2_133": {
      "seqid": "NMDC:1781_100325_scf_1305_c1",
      "start": 1,
      "end": 133,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1305_c1_2_133",
      "annotations": {
        "id": [
          "1781_100325_scf_1305_c1_2_133"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1305_c1_251_568": {
      "seqid": "NMDC:1781_100325_scf_1305_c1",
      "start": 250,
      "end": 568,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1305_c1_251_568",
      "annotations": {
        "id": [
          "1781_100325_scf_1305_c1_251_568"
        ],
        "product": [
          "AbrB family looped-hinge helix DNA binding protein"
        ],
        "cog": [
          "COG2002"
        ],
        "pfam": [
          "MazE_antitoxi"
        ],
        "superfamily": [
          "SM00966"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1305_c1_543_950": {
      "seqid": "NMDC:1781_100325_scf_1305_c1",
      "start": 542,
      "end": 950,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1305_c1_543_950",
      "annotations": {
        "id": [
          "1781_100325_scf_1305_c1_543_950"
        ],
        "product": [
          "ribonuclease VapC"
        ],
        "cath_funfam": [
          "3.40.50.1010"
        ],
        "cog": [
          "COG1848"
        ],
        "ko": [
          "KO:K19686"
        ],
        "ec_number": [
          "EC:3.1.-"
        ],
        "pfam": [
          "PI"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1305_c1_1061_1180": {
      "seqid": "NMDC:1781_100325_scf_1305_c1",
      "start": 1060,
      "end": 1180,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1305_c1_1061_1180",
      "annotations": {
        "id": [
          "1781_100325_scf_1305_c1_1061_1180"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1305_c1_1285_1527": {
      "seqid": "NMDC:1781_100325_scf_1305_c1",
      "start": 1284,
      "end": 1527,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1305_c1_1285_1527",
      "annotations": {
        "id": [
          "1781_100325_scf_1305_c1_1285_1527"
        ],
        "product": [
          "putative PIN family toxin of toxin-antitoxin system"
        ],
        "cog": [
          "COG1569"
        ],
        "pfam": [
          "PIN_"
        ],
        "superfamily": [
          "SM00670"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1306_c1": {
    "1781_100325_scf_1306_c1_26_418": {
      "seqid": "NMDC:1781_100325_scf_1306_c1",
      "start": 25,
      "end": 418,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1306_c1_26_418",
      "annotations": {
        "id": [
          "1781_100325_scf_1306_c1_26_418"
        ],
        "product": [
          "peptide chain release factor 1"
        ],
        "cath_funfam": [
          "3.30.160.20"
        ],
        "cog": [
          "COG0216"
        ],
        "ko": [
          "KO:K02835"
        ],
        "pfam": [
          "RF-"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1306_c1_421_1251": {
      "seqid": "NMDC:1781_100325_scf_1306_c1",
      "start": 420,
      "end": 1251,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1306_c1_421_1251",
      "annotations": {
        "id": [
          "1781_100325_scf_1306_c1_421_1251"
        ],
        "product": [
          "release factor glutamine methyltransferase"
        ],
        "cath_funfam": [
          "1.10.8.10",
          "3.40.50.150"
        ],
        "cog": [
          "COG2890"
        ],
        "ko": [
          "KO:K02493"
        ],
        "ec_number": [
          "EC:2.1.1.297"
        ],
        "pfam": [
          "MT",
          "Methyltransf_1",
          "Methyltransf_2",
          "Methyltransf_3",
          "Prm",
          "UPF002"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1306_c1_1248_1532": {
      "seqid": "NMDC:1781_100325_scf_1306_c1",
      "start": 1247,
      "end": 1532,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1306_c1_1248_1532",
      "annotations": {
        "id": [
          "1781_100325_scf_1306_c1_1248_1532"
        ],
        "product": [
          "L-threonylcarbamoyladenylate synthase"
        ],
        "cath_funfam": [
          "3.90.870.10"
        ],
        "cog": [
          "COG0009"
        ],
        "ko": [
          "KO:K07566"
        ],
        "ec_number": [
          "EC:2.7.7.87"
        ],
        "pfam": [
          "Sua5_yciO_yrd"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1307_c1": {
    "1781_100325_scf_1307_c1_12_1532": {
      "seqid": "NMDC:1781_100325_scf_1307_c1",
      "start": 11,
      "end": 1532,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1307_c1_12_1532",
      "annotations": {
        "id": [
          "1781_100325_scf_1307_c1_12_1532"
        ],
        "product": [
          "NADH-quinone oxidoreductase subunit L"
        ],
        "cog": [
          "COG1009"
        ],
        "ko": [
          "KO:K00341"
        ],
        "ec_number": [
          "EC:1.6.5.3"
        ],
        "pfam": [
          "Proton_antipo_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1308_c1": {
    "1781_100325_scf_1308_c1_2_1060": {
      "seqid": "NMDC:1781_100325_scf_1308_c1",
      "start": 1,
      "end": 1060,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1308_c1_2_1060",
      "annotations": {
        "id": [
          "1781_100325_scf_1308_c1_2_1060"
        ],
        "product": [
          "phosphoribosylaminoimidazolecarboxamide formyltransferase/IMP cyclohydrolase"
        ],
        "cath_funfam": [
          "3.40.140.20"
        ],
        "cog": [
          "COG0138"
        ],
        "ko": [
          "KO:K00602"
        ],
        "ec_number": [
          "EC:2.1.2.3",
          "EC:3.5.4.10"
        ],
        "pfam": [
          "AICARFT_IMPCHa"
        ],
        "superfamily": [
          "SM00798"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1308_c1_1116_1532": {
      "seqid": "NMDC:1781_100325_scf_1308_c1",
      "start": 1115,
      "end": 1532,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1308_c1_1116_1532",
      "annotations": {
        "id": [
          "1781_100325_scf_1308_c1_1116_1532"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1309_c1": {
    "1781_100325_scf_1309_c1_325_1038": {
      "seqid": "NMDC:1781_100325_scf_1309_c1",
      "start": 324,
      "end": 1038,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1309_c1_325_1038",
      "annotations": {
        "id": [
          "1781_100325_scf_1309_c1_325_1038"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG3826"
        ],
        "ko": [
          "KO:K09990"
        ],
        "pfam": [
          "2OG-FeII_Oxy_",
          "Oxygenase-N"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1309_c1_1341_1532": {
      "seqid": "NMDC:1781_100325_scf_1309_c1",
      "start": 1340,
      "end": 1532,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1309_c1_1341_1532",
      "annotations": {
        "id": [
          "1781_100325_scf_1309_c1_1341_1532"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_130_c1": {
    "1781_100325_scf_130_c1_2_1312": {
      "seqid": "NMDC:1781_100325_scf_130_c1",
      "start": 1,
      "end": 1312,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_130_c1_2_1312",
      "annotations": {
        "id": [
          "1781_100325_scf_130_c1_2_1312"
        ],
        "product": [
          "glycine hydroxymethyltransferase"
        ],
        "cath_funfam": [
          "3.40.640.10",
          "3.90.1150.10"
        ],
        "cog": [
          "COG0112"
        ],
        "ko": [
          "KO:K00600"
        ],
        "ec_number": [
          "EC:2.1.2.1"
        ],
        "pfam": [
          "Aminotran_1_",
          "Beta_elim_lyas",
          "SHM"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_130_c1_1529_1633": {
      "seqid": "NMDC:1781_100325_scf_130_c1",
      "start": 1528,
      "end": 1633,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_130_c1_1529_1633",
      "annotations": {
        "id": [
          "1781_100325_scf_130_c1_1529_1633"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_130_c1_1731_2189": {
      "seqid": "NMDC:1781_100325_scf_130_c1",
      "start": 1730,
      "end": 2189,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_130_c1_1731_2189",
      "annotations": {
        "id": [
          "1781_100325_scf_130_c1_1731_2189"
        ],
        "product": [
          "small subunit ribosomal protein S9"
        ],
        "cath_funfam": [
          "3.30.230.10"
        ],
        "cog": [
          "COG0103"
        ],
        "ko": [
          "KO:K02996"
        ],
        "pfam": [
          "Ribosomal_S"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_130_c1_2167_2649": {
      "seqid": "NMDC:1781_100325_scf_130_c1",
      "start": 2166,
      "end": 2649,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_130_c1_2167_2649",
      "annotations": {
        "id": [
          "1781_100325_scf_130_c1_2167_2649"
        ],
        "product": [
          "large subunit ribosomal protein L13"
        ],
        "cath_funfam": [
          "3.90.1180.10"
        ],
        "cog": [
          "COG0102"
        ],
        "ko": [
          "KO:K02871"
        ],
        "pfam": [
          "Ribosomal_L1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_130_c1_2642_2989": {
      "seqid": "NMDC:1781_100325_scf_130_c1",
      "start": 2641,
      "end": 2989,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_130_c1_2642_2989",
      "annotations": {
        "id": [
          "1781_100325_scf_130_c1_2642_2989"
        ],
        "product": [
          "large subunit ribosomal protein L18e"
        ],
        "cath_funfam": [
          "3.100.10.10"
        ],
        "cog": [
          "COG1727"
        ],
        "ko": [
          "KO:K02883"
        ],
        "pfam": [
          "Ribosomal_L1",
          "Ribosomal_L27"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_130_c1_3031_3453": {
      "seqid": "NMDC:1781_100325_scf_130_c1",
      "start": 3030,
      "end": 3453,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_130_c1_3031_3453",
      "annotations": {
        "id": [
          "1781_100325_scf_130_c1_3031_3453"
        ],
        "product": [
          "DNA-directed RNA polymerase subunit D"
        ],
        "cath_funfam": [
          "2.170.120.12"
        ],
        "cog": [
          "COG0202"
        ],
        "ko": [
          "KO:K03047"
        ],
        "ec_number": [
          "EC:2.7.7.6"
        ],
        "pfam": [
          "RNA_pol_",
          "RNA_pol_A_ba"
        ],
        "superfamily": [
          "SM00662"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1310_c1": {
    "1781_100325_scf_1310_c1_1_636": {
      "seqid": "NMDC:1781_100325_scf_1310_c1",
      "start": 0,
      "end": 636,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1310_c1_1_636",
      "annotations": {
        "id": [
          "1781_100325_scf_1310_c1_1_636"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "pfam": [
          "HTH_4"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1310_c1_654_1157": {
      "seqid": "NMDC:1781_100325_scf_1310_c1",
      "start": 653,
      "end": 1157,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1310_c1_654_1157",
      "annotations": {
        "id": [
          "1781_100325_scf_1310_c1_654_1157"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1310_c1_1187_1531": {
      "seqid": "NMDC:1781_100325_scf_1310_c1",
      "start": 1186,
      "end": 1531,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1310_c1_1187_1531",
      "annotations": {
        "id": [
          "1781_100325_scf_1310_c1_1187_1531"
        ],
        "product": [
          "ABC-type multidrug transport system permease subunit"
        ],
        "cog": [
          "COG0842"
        ],
        "pfam": [
          "ABC2_membran",
          "ABC2_membrane_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1311_c1": {
    "1781_100325_scf_1311_c1_2_310": {
      "seqid": "NMDC:1781_100325_scf_1311_c1",
      "start": 1,
      "end": 310,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1311_c1_2_310",
      "annotations": {
        "id": [
          "1781_100325_scf_1311_c1_2_310"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1311_c1_355_1503": {
      "seqid": "NMDC:1781_100325_scf_1311_c1",
      "start": 354,
      "end": 1503,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1311_c1_355_1503",
      "annotations": {
        "id": [
          "1781_100325_scf_1311_c1_355_1503"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG3214"
        ],
        "ko": [
          "KO:K09927"
        ],
        "pfam": [
          "HTH_4"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1312_c1": {
    "1781_100325_scf_1312_c1_1_453": {
      "seqid": "NMDC:1781_100325_scf_1312_c1",
      "start": 0,
      "end": 453,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1312_c1_1_453",
      "annotations": {
        "id": [
          "1781_100325_scf_1312_c1_1_453"
        ],
        "product": [
          "dihydroorotate dehydrogenase (NAD+) catalytic subunit"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "cog": [
          "COG0167"
        ],
        "ko": [
          "KO:K17828"
        ],
        "ec_number": [
          "EC:1.3.1.14"
        ],
        "pfam": [
          "DHO_d"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1312_c1_470_1342": {
      "seqid": "NMDC:1781_100325_scf_1312_c1",
      "start": 469,
      "end": 1342,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1312_c1_470_1342",
      "annotations": {
        "id": [
          "1781_100325_scf_1312_c1_470_1342"
        ],
        "product": [
          "dihydroorotate dehydrogenase electron transfer subunit"
        ],
        "cath_funfam": [
          "2.10.240.10",
          "2.40.30.10",
          "3.40.50.80"
        ],
        "cog": [
          "COG0543"
        ],
        "ko": [
          "KO:K02823"
        ],
        "pfam": [
          "DHODB_Fe-S_bin"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1312_c1_1368_1532": {
      "seqid": "NMDC:1781_100325_scf_1312_c1",
      "start": 1367,
      "end": 1532,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1312_c1_1368_1532",
      "annotations": {
        "id": [
          "1781_100325_scf_1312_c1_1368_1532"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1313_c1": {
    "1781_100325_scf_1313_c1_9_1532": {
      "seqid": "NMDC:1781_100325_scf_1313_c1",
      "start": 8,
      "end": 1532,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1313_c1_9_1532",
      "annotations": {
        "id": [
          "1781_100325_scf_1313_c1_9_1532"
        ],
        "product": [
          "GTP pyrophosphokinase"
        ],
        "cath_funfam": [
          "3.10.20.30",
          "3.30.460.10",
          "3.30.70.260"
        ],
        "cog": [
          "COG0317"
        ],
        "ko": [
          "KO:K00951"
        ],
        "ec_number": [
          "EC:2.7.6.5"
        ],
        "pfam": [
          "AC",
          "ACT_",
          "RelA_Spo",
          "TG"
        ],
        "superfamily": [
          "SM00954"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1314_c1": {
    "1781_100325_scf_1314_c1_523_1008": {
      "seqid": "NMDC:1781_100325_scf_1314_c1",
      "start": 522,
      "end": 1008,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1314_c1_523_1008",
      "annotations": {
        "id": [
          "1781_100325_scf_1314_c1_523_1008"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.40.30.90"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1315_c1": {
    "1781_100325_scf_1315_c1_2_145": {
      "seqid": "NMDC:1781_100325_scf_1315_c1",
      "start": 1,
      "end": 145,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1315_c1_2_145",
      "annotations": {
        "id": [
          "1781_100325_scf_1315_c1_2_145"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1315_c1_145_492": {
      "seqid": "NMDC:1781_100325_scf_1315_c1",
      "start": 144,
      "end": 492,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1315_c1_145_492",
      "annotations": {
        "id": [
          "1781_100325_scf_1315_c1_145_492"
        ],
        "product": [
          "4a-hydroxytetrahydrobiopterin dehydratase"
        ],
        "cath_funfam": [
          "3.30.1360.20"
        ],
        "cog": [
          "COG2154"
        ],
        "ko": [
          "KO:K01724"
        ],
        "ec_number": [
          "EC:4.2.1.96"
        ],
        "pfam": [
          "Pterin_4"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1315_c1_502_1032": {
      "seqid": "NMDC:1781_100325_scf_1315_c1",
      "start": 501,
      "end": 1032,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1315_c1_502_1032",
      "annotations": {
        "id": [
          "1781_100325_scf_1315_c1_502_1032"
        ],
        "product": [
          "methionine-S-sulfoxide reductase"
        ],
        "cath_funfam": [
          "3.30.1060.10"
        ],
        "cog": [
          "COG0225"
        ],
        "pfam": [
          "PMS"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1315_c1_1109_1531": {
      "seqid": "NMDC:1781_100325_scf_1315_c1",
      "start": 1108,
      "end": 1531,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1315_c1_1109_1531",
      "annotations": {
        "id": [
          "1781_100325_scf_1315_c1_1109_1531"
        ],
        "product": [
          "glutamate-1-semialdehyde 2",
          "1-aminomutase"
        ],
        "cath_funfam": [
          "3.90.1150.10"
        ],
        "cog": [
          "COG0001"
        ],
        "ko": [
          "KO:K01845"
        ],
        "ec_number": [
          "EC:5.4.3.8"
        ],
        "pfam": [
          "Aminotran_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1316_c1": {
    "1781_100325_scf_1316_c1_2_115": {
      "seqid": "NMDC:1781_100325_scf_1316_c1",
      "start": 1,
      "end": 115,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1316_c1_2_115",
      "annotations": {
        "id": [
          "1781_100325_scf_1316_c1_2_115"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1316_c1_310_852": {
      "seqid": "NMDC:1781_100325_scf_1316_c1",
      "start": 309,
      "end": 852,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1316_c1_310_852",
      "annotations": {
        "id": [
          "1781_100325_scf_1316_c1_310_852"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1316_c1_961_1419": {
      "seqid": "NMDC:1781_100325_scf_1316_c1",
      "start": 960,
      "end": 1419,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1316_c1_961_1419",
      "annotations": {
        "id": [
          "1781_100325_scf_1316_c1_961_1419"
        ],
        "product": [
          "prefoldin alpha subunit"
        ],
        "cath_funfam": [
          "1.10.287.370"
        ],
        "cog": [
          "COG1730"
        ],
        "ko": [
          "KO:K04797"
        ],
        "pfam": [
          "Prefoldi"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1317_c1": {
    "1781_100325_scf_1317_c1_1_207": {
      "seqid": "NMDC:1781_100325_scf_1317_c1",
      "start": 0,
      "end": 207,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1317_c1_1_207",
      "annotations": {
        "id": [
          "1781_100325_scf_1317_c1_1_207"
        ],
        "product": [
          "phosphoglycerol geranylgeranyltransferase"
        ],
        "cath_funfam": [
          "3.20.20.390"
        ],
        "cog": [
          "COG1646"
        ],
        "ko": [
          "KO:K17104"
        ],
        "ec_number": [
          "EC:2.5.1.41"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1317_c1_276_638": {
      "seqid": "NMDC:1781_100325_scf_1317_c1",
      "start": 275,
      "end": 638,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1317_c1_276_638",
      "annotations": {
        "id": [
          "1781_100325_scf_1317_c1_276_638"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1317_c1_765_1340": {
      "seqid": "NMDC:1781_100325_scf_1317_c1",
      "start": 764,
      "end": 1340,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1317_c1_765_1340",
      "annotations": {
        "id": [
          "1781_100325_scf_1317_c1_765_1340"
        ],
        "product": [
          "predicted transcriptional regulator"
        ],
        "cath_funfam": [
          "1.10.10.10"
        ],
        "cog": [
          "COG3432"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1317_c1_1421_1528": {
      "seqid": "NMDC:1781_100325_scf_1317_c1",
      "start": 1420,
      "end": 1528,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1317_c1_1421_1528",
      "annotations": {
        "id": [
          "1781_100325_scf_1317_c1_1421_1528"
        ],
        "product": [
          "bifunctional DNA-binding transcriptional regulator/antitoxin component of YhaV-PrlF toxin-antitoxin module"
        ],
        "cath_funfam": [
          "2.10.260.10"
        ],
        "cog": [
          "COG2002"
        ],
        "superfamily": [
          "SM00966"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1318_c1": {
    "1781_100325_scf_1318_c1_396_1157": {
      "seqid": "NMDC:1781_100325_scf_1318_c1",
      "start": 395,
      "end": 1157,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1318_c1_396_1157",
      "annotations": {
        "id": [
          "1781_100325_scf_1318_c1_396_1157"
        ],
        "product": [
          "chromosome partitioning protein"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG1192"
        ],
        "ko": [
          "KO:K03496"
        ],
        "pfam": [
          "AAA_3",
          "ArsA_ATPas",
          "CBP_Bcs",
          "Cbi",
          "Fer4_Nif",
          "Mip",
          "Par",
          "VirC"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1318_c1_1154_1507": {
      "seqid": "NMDC:1781_100325_scf_1318_c1",
      "start": 1153,
      "end": 1507,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1318_c1_1154_1507",
      "annotations": {
        "id": [
          "1781_100325_scf_1318_c1_1154_1507"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1319_c1": {
    "1781_100325_scf_1319_c1_3_155": {
      "seqid": "NMDC:1781_100325_scf_1319_c1",
      "start": 2,
      "end": 155,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1319_c1_3_155",
      "annotations": {
        "id": [
          "1781_100325_scf_1319_c1_3_155"
        ],
        "product": [
          "DNA invertase Pin-like site-specific DNA recombinase"
        ],
        "cath_funfam": [
          "3.40.50.1390"
        ],
        "cog": [
          "COG1961"
        ],
        "pfam": [
          "Resolvas"
        ],
        "superfamily": [
          "SM00857"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1319_c1_288_1529": {
      "seqid": "NMDC:1781_100325_scf_1319_c1",
      "start": 287,
      "end": 1529,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1319_c1_288_1529",
      "annotations": {
        "id": [
          "1781_100325_scf_1319_c1_288_1529"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DUF415"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_131_c1": {
    "1781_100325_scf_131_c1_199_1971": {
      "seqid": "NMDC:1781_100325_scf_131_c1",
      "start": 198,
      "end": 1971,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_131_c1_199_1971",
      "annotations": {
        "id": [
          "1781_100325_scf_131_c1_199_1971"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG5421"
        ],
        "pfam": [
          "DDE_Tnp_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_131_c1_2149_3486": {
      "seqid": "NMDC:1781_100325_scf_131_c1",
      "start": 2148,
      "end": 3486,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_131_c1_2149_3486",
      "annotations": {
        "id": [
          "1781_100325_scf_131_c1_2149_3486"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DDE_Tnp_1_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1320_c1": {
    "1781_100325_scf_1320_c1_31_855": {
      "seqid": "NMDC:1781_100325_scf_1320_c1",
      "start": 30,
      "end": 855,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1320_c1_31_855",
      "annotations": {
        "id": [
          "1781_100325_scf_1320_c1_31_855"
        ],
        "product": [
          "ubiquinol-cytochrome c reductase cytochrome b subunit"
        ],
        "cath_funfam": [
          "1.20.810.10"
        ],
        "cog": [
          "COG1290"
        ],
        "ko": [
          "KO:K00412"
        ],
        "pfam": [
          "Cytochrom_B_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1320_c1_797_1027": {
      "seqid": "NMDC:1781_100325_scf_1320_c1",
      "start": 796,
      "end": 1027,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1320_c1_797_1027",
      "annotations": {
        "id": [
          "1781_100325_scf_1320_c1_797_1027"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1320_c1_1163_1528": {
      "seqid": "NMDC:1781_100325_scf_1320_c1",
      "start": 1162,
      "end": 1528,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1320_c1_1163_1528",
      "annotations": {
        "id": [
          "1781_100325_scf_1320_c1_1163_1528"
        ],
        "product": [
          "plastocyanin"
        ],
        "cog": [
          "COG3794"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1321_c1": {
    "1781_100325_scf_1321_c1_1_561": {
      "seqid": "NMDC:1781_100325_scf_1321_c1",
      "start": 0,
      "end": 561,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1321_c1_1_561",
      "annotations": {
        "id": [
          "1781_100325_scf_1321_c1_1_561"
        ],
        "product": [
          "alanine-synthesizing transaminase"
        ],
        "cath_funfam": [
          "3.40.640.10"
        ],
        "cog": [
          "COG0436"
        ],
        "ko": [
          "KO:K14261"
        ],
        "ec_number": [
          "EC:2.6.1.-"
        ],
        "pfam": [
          "Aminotran_1_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1321_c1_875_1528": {
      "seqid": "NMDC:1781_100325_scf_1321_c1",
      "start": 874,
      "end": 1528,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1321_c1_875_1528",
      "annotations": {
        "id": [
          "1781_100325_scf_1321_c1_875_1528"
        ],
        "product": [
          "PAS domain S-box-containing protein"
        ],
        "cath_funfam": [
          "3.30.450.20"
        ],
        "cog": [
          "COG2202"
        ],
        "pfam": [
          "PA",
          "PAS_"
        ],
        "superfamily": [
          "SM00086",
          "SM00091"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1322_c1": {
    "1781_100325_scf_1322_c1_195_368": {
      "seqid": "NMDC:1781_100325_scf_1322_c1",
      "start": 194,
      "end": 368,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1322_c1_195_368",
      "annotations": {
        "id": [
          "1781_100325_scf_1322_c1_195_368"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1322_c1_652_1527": {
      "seqid": "NMDC:1781_100325_scf_1322_c1",
      "start": 651,
      "end": 1527,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1322_c1_652_1527",
      "annotations": {
        "id": [
          "1781_100325_scf_1322_c1_652_1527"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.70.270"
        ],
        "pfam": [
          "RVT_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1323_c1": {
    "1781_100325_scf_1323_c1_3_1529": {
      "seqid": "NMDC:1781_100325_scf_1323_c1",
      "start": 2,
      "end": 1529,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1323_c1_3_1529",
      "annotations": {
        "id": [
          "1781_100325_scf_1323_c1_3_1529"
        ],
        "product": [
          "polyribonucleotide nucleotidyltransferase"
        ],
        "cath_funfam": [
          "3.30.1370.10",
          "3.30.230.70"
        ],
        "cog": [
          "COG1185"
        ],
        "ko": [
          "KO:K00962"
        ],
        "ec_number": [
          "EC:2.7.7.8"
        ],
        "pfam": [
          "KH_",
          "RNase_P",
          "RNase_PH_"
        ],
        "superfamily": [
          "SM00322"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1324_c1": {
    "1781_100325_scf_1324_c1_3_281": {
      "seqid": "NMDC:1781_100325_scf_1324_c1",
      "start": 2,
      "end": 281,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1324_c1_3_281",
      "annotations": {
        "id": [
          "1781_100325_scf_1324_c1_3_281"
        ],
        "product": [
          "nitrogen fixation NifU-like protein"
        ],
        "cath_funfam": [
          "3.90.1010.10"
        ],
        "cog": [
          "COG0822"
        ],
        "ko": [
          "KO:K04488"
        ],
        "pfam": [
          "NifU_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1324_c1_278_1522": {
      "seqid": "NMDC:1781_100325_scf_1324_c1",
      "start": 277,
      "end": 1522,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1324_c1_278_1522",
      "annotations": {
        "id": [
          "1781_100325_scf_1324_c1_278_1522"
        ],
        "product": [
          "cysteine desulfurase/selenocysteine lyase"
        ],
        "cath_funfam": [
          "3.40.640.10"
        ],
        "cog": [
          "COG0520"
        ],
        "ko": [
          "KO:K11717"
        ],
        "ec_number": [
          "EC:2.8.1.7",
          "EC:4.4.1.16"
        ],
        "pfam": [
          "Aminotran_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1325_c1": {
    "1781_100325_scf_1325_c1_28_789": {
      "seqid": "NMDC:1781_100325_scf_1325_c1",
      "start": 27,
      "end": 789,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1325_c1_28_789",
      "annotations": {
        "id": [
          "1781_100325_scf_1325_c1_28_789"
        ],
        "product": [
          "predicted deacetylase"
        ],
        "cog": [
          "COG3233"
        ],
        "pfam": [
          "DUF233",
          "Polysacc_deac_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1325_c1_782_1522": {
      "seqid": "NMDC:1781_100325_scf_1325_c1",
      "start": 781,
      "end": 1522,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1325_c1_782_1522",
      "annotations": {
        "id": [
          "1781_100325_scf_1325_c1_782_1522"
        ],
        "product": [
          "glycosyltransferase involved in cell wall biosynthesis"
        ],
        "cath_funfam": [
          "3.40.50.2000"
        ],
        "cog": [
          "COG0438"
        ],
        "pfam": [
          "Glyco_trans_1_",
          "Glycos_transf_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1326_c1": {
    "1781_100325_scf_1326_c1_2_430": {
      "seqid": "NMDC:1781_100325_scf_1326_c1",
      "start": 1,
      "end": 430,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1326_c1_2_430",
      "annotations": {
        "id": [
          "1781_100325_scf_1326_c1_2_430"
        ],
        "product": [
          "peptide-methionine (R)-S-oxide reductase"
        ],
        "cath_funfam": [
          "2.170.150.20"
        ],
        "cog": [
          "COG0229"
        ],
        "ko": [
          "KO:K07305"
        ],
        "ec_number": [
          "EC:1.8.4.12"
        ],
        "pfam": [
          "Sel"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1326_c1_1032_1325": {
      "seqid": "NMDC:1781_100325_scf_1326_c1",
      "start": 1031,
      "end": 1325,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1326_c1_1032_1325",
      "annotations": {
        "id": [
          "1781_100325_scf_1326_c1_1032_1325"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1327_c1": {
    "1781_100325_scf_1327_c1_25_558": {
      "seqid": "NMDC:1781_100325_scf_1327_c1",
      "start": 24,
      "end": 558,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1327_c1_25_558",
      "annotations": {
        "id": [
          "1781_100325_scf_1327_c1_25_558"
        ],
        "product": [
          "glycosyltransferase involved in cell wall biosynthesis"
        ],
        "cath_funfam": [
          "3.40.50.2000"
        ],
        "cog": [
          "COG0438"
        ],
        "pfam": [
          "Glyco_trans_1_",
          "Glycos_transf_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1327_c1_555_1526": {
      "seqid": "NMDC:1781_100325_scf_1327_c1",
      "start": 554,
      "end": 1526,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1327_c1_555_1526",
      "annotations": {
        "id": [
          "1781_100325_scf_1327_c1_555_1526"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1328_c1": {
    "1781_100325_scf_1328_c1_2_1456": {
      "seqid": "NMDC:1781_100325_scf_1328_c1",
      "start": 1,
      "end": 1456,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1328_c1_2_1456",
      "annotations": {
        "id": [
          "1781_100325_scf_1328_c1_2_1456"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1329_c1": {
    "1781_100325_scf_1329_c1_200_1525": {
      "seqid": "NMDC:1781_100325_scf_1329_c1",
      "start": 199,
      "end": 1525,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1329_c1_200_1525",
      "annotations": {
        "id": [
          "1781_100325_scf_1329_c1_200_1525"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "DDE_Tnp_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_132_c1": {
    "1781_100325_scf_132_c1_16_654": {
      "seqid": "NMDC:1781_100325_scf_132_c1",
      "start": 15,
      "end": 654,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_132_c1_16_654",
      "annotations": {
        "id": [
          "1781_100325_scf_132_c1_16_654"
        ],
        "product": [
          "acetyl-CoA synthetase"
        ],
        "cath_funfam": [
          "2.30.38.10",
          "3.30.300.30"
        ],
        "cog": [
          "COG0365"
        ],
        "ko": [
          "KO:K01895"
        ],
        "ec_number": [
          "EC:6.2.1.1"
        ],
        "pfam": [
          "AMP-bindin",
          "AMP-binding_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_132_c1_697_1173": {
      "seqid": "NMDC:1781_100325_scf_132_c1",
      "start": 696,
      "end": 1173,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_132_c1_697_1173",
      "annotations": {
        "id": [
          "1781_100325_scf_132_c1_697_1173"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG1430"
        ],
        "ko": [
          "KO:K09005"
        ],
        "pfam": [
          "DUF19"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_132_c1_1338_1631": {
      "seqid": "NMDC:1781_100325_scf_132_c1",
      "start": 1337,
      "end": 1631,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_132_c1_1338_1631",
      "annotations": {
        "id": [
          "1781_100325_scf_132_c1_1338_1631"
        ],
        "product": [
          "formate hydrogenlyase subunit 6/NADH:ubiquinone oxidoreductase subunit I"
        ],
        "cath_funfam": [
          "3.30.70.20"
        ],
        "cog": [
          "COG1143"
        ],
        "pfam": [
          "Fer",
          "Fer4_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_132_c1_1751_2032": {
      "seqid": "NMDC:1781_100325_scf_132_c1",
      "start": 1750,
      "end": 2032,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_132_c1_1751_2032",
      "annotations": {
        "id": [
          "1781_100325_scf_132_c1_1751_2032"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_132_c1_2167_3195": {
      "seqid": "NMDC:1781_100325_scf_132_c1",
      "start": 2166,
      "end": 3195,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_132_c1_2167_3195",
      "annotations": {
        "id": [
          "1781_100325_scf_132_c1_2167_3195"
        ],
        "product": [
          "flap endonuclease-1"
        ],
        "cath_funfam": [
          "3.40.50.1010"
        ],
        "cog": [
          "COG0258"
        ],
        "ko": [
          "KO:K04799"
        ],
        "ec_number": [
          "EC:3.-"
        ],
        "pfam": [
          "XPG_"
        ],
        "superfamily": [
          "SM00279",
          "SM00484",
          "SM00485"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_132_c1_3221_3508": {
      "seqid": "NMDC:1781_100325_scf_132_c1",
      "start": 3220,
      "end": 3508,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_132_c1_3221_3508",
      "annotations": {
        "id": [
          "1781_100325_scf_132_c1_3221_3508"
        ],
        "product": [
          "thymidylate synthase ThyX"
        ],
        "cog": [
          "COG1351"
        ],
        "pfam": [
          "Thy"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1330_c1": {
    "1781_100325_scf_1330_c1_3_1475": {
      "seqid": "NMDC:1781_100325_scf_1330_c1",
      "start": 2,
      "end": 1475,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1330_c1_3_1475",
      "annotations": {
        "id": [
          "1781_100325_scf_1330_c1_3_1475"
        ],
        "product": [
          "K+-sensing histidine kinase KdpD"
        ],
        "cath_funfam": [
          "1.10.287.130"
        ],
        "cog": [
          "COG2205"
        ],
        "pfam": [
          "HisK"
        ],
        "superfamily": [
          "SM00388"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1331_c1": {
    "1781_100325_scf_1331_c1_2_259": {
      "seqid": "NMDC:1781_100325_scf_1331_c1",
      "start": 1,
      "end": 259,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1331_c1_2_259",
      "annotations": {
        "id": [
          "1781_100325_scf_1331_c1_2_259"
        ],
        "product": [
          "chaperonin GroEL"
        ],
        "cath_funfam": [
          "1.10.560.10"
        ],
        "cog": [
          "COG0459"
        ],
        "ko": [
          "KO:K04077"
        ],
        "pfam": [
          "Cpn60_TCP"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1331_c1_290_565": {
      "seqid": "NMDC:1781_100325_scf_1331_c1",
      "start": 289,
      "end": 565,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1331_c1_290_565",
      "annotations": {
        "id": [
          "1781_100325_scf_1331_c1_290_565"
        ],
        "product": [
          "chaperonin GroES"
        ],
        "cath_funfam": [
          "2.30.33.40"
        ],
        "cog": [
          "COG0234"
        ],
        "ko": [
          "KO:K04078"
        ],
        "pfam": [
          "Cpn1"
        ],
        "superfamily": [
          "SM00883"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1331_c1_782_1009": {
      "seqid": "NMDC:1781_100325_scf_1331_c1",
      "start": 781,
      "end": 1009,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1331_c1_782_1009",
      "annotations": {
        "id": [
          "1781_100325_scf_1331_c1_782_1009"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.30.420.40"
        ],
        "cog": [
          "COG2952"
        ],
        "pfam": [
          "DUF50"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1331_c1_1054_1329": {
      "seqid": "NMDC:1781_100325_scf_1331_c1",
      "start": 1053,
      "end": 1329,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1331_c1_1054_1329",
      "annotations": {
        "id": [
          "1781_100325_scf_1331_c1_1054_1329"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "1.20.1440.100"
        ],
        "cog": [
          "COG2952"
        ],
        "pfam": [
          "DUF50"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1332_c1": {
    "1781_100325_scf_1332_c1_6_524": {
      "seqid": "NMDC:1781_100325_scf_1332_c1",
      "start": 5,
      "end": 524,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1332_c1_6_524",
      "annotations": {
        "id": [
          "1781_100325_scf_1332_c1_6_524"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cog": [
          "COG1628"
        ],
        "ko": [
          "KO:K09120"
        ],
        "pfam": [
          "DUF9"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1332_c1_631_834": {
      "seqid": "NMDC:1781_100325_scf_1332_c1",
      "start": 630,
      "end": 834,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1332_c1_631_834",
      "annotations": {
        "id": [
          "1781_100325_scf_1332_c1_631_834"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "4.10.280.10"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1332_c1_965_1372": {
      "seqid": "NMDC:1781_100325_scf_1332_c1",
      "start": 964,
      "end": 1372,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1332_c1_965_1372",
      "annotations": {
        "id": [
          "1781_100325_scf_1332_c1_965_1372"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1333_c1": {
    "1781_100325_scf_1333_c1_2_166": {
      "seqid": "NMDC:1781_100325_scf_1333_c1",
      "start": 1,
      "end": 166,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1333_c1_2_166",
      "annotations": {
        "id": [
          "1781_100325_scf_1333_c1_2_166"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1333_c1_153_1382": {
      "seqid": "NMDC:1781_100325_scf_1333_c1",
      "start": 152,
      "end": 1382,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1333_c1_153_1382",
      "annotations": {
        "id": [
          "1781_100325_scf_1333_c1_153_1382"
        ],
        "product": [
          "predicted transposase YbfD/YdcC"
        ],
        "cog": [
          "COG5433"
        ],
        "pfam": [
          "DDE_Tnp_",
          "DDE_Tnp_1_asso"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1334_c1": {
    "1781_100325_scf_1334_c1_3_392": {
      "seqid": "NMDC:1781_100325_scf_1334_c1",
      "start": 2,
      "end": 392,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1334_c1_3_392",
      "annotations": {
        "id": [
          "1781_100325_scf_1334_c1_3_392"
        ],
        "product": [
          "pyrimidine operon attenuation protein/uracil phosphoribosyltransferase"
        ],
        "cath_funfam": [
          "3.40.50.2020"
        ],
        "cog": [
          "COG2065"
        ],
        "ko": [
          "KO:K02825"
        ],
        "ec_number": [
          "EC:2.4.2.9"
        ],
        "pfam": [
          "Pribosyltra"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1334_c1_385_1383": {
      "seqid": "NMDC:1781_100325_scf_1334_c1",
      "start": 384,
      "end": 1383,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1334_c1_385_1383",
      "annotations": {
        "id": [
          "1781_100325_scf_1334_c1_385_1383"
        ],
        "product": [
          "aspartate carbamoyltransferase catalytic subunit"
        ],
        "cath_funfam": [
          "3.40.50.1370"
        ],
        "cog": [
          "COG0540"
        ],
        "ko": [
          "KO:K00609"
        ],
        "ec_number": [
          "EC:2.1.3.2"
        ],
        "pfam": [
          "OTCac",
          "OTCace_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1334_c1_1439_1525": {
      "seqid": "NMDC:1781_100325_scf_1334_c1",
      "start": 1438,
      "end": 1525,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1334_c1_1439_1525",
      "annotations": {
        "id": [
          "1781_100325_scf_1334_c1_1439_1525"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1335_c1": {
    "1781_100325_scf_1335_c1_62_301": {
      "seqid": "NMDC:1781_100325_scf_1335_c1",
      "start": 61,
      "end": 301,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1335_c1_62_301",
      "annotations": {
        "id": [
          "1781_100325_scf_1335_c1_62_301"
        ],
        "product": [
          "LmbE family N-acetylglucosaminyl deacetylase"
        ],
        "cath_funfam": [
          "3.40.50.10320"
        ],
        "cog": [
          "COG2120"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1335_c1_844_1506": {
      "seqid": "NMDC:1781_100325_scf_1335_c1",
      "start": 843,
      "end": 1506,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1335_c1_844_1506",
      "annotations": {
        "id": [
          "1781_100325_scf_1335_c1_844_1506"
        ],
        "product": [
          "large subunit ribosomal protein L1"
        ],
        "cath_funfam": [
          "3.40.50.790"
        ],
        "cog": [
          "COG0081"
        ],
        "ko": [
          "KO:K02863"
        ],
        "pfam": [
          "Ribosomal_L"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1336_c1": {
    "1781_100325_scf_1336_c1_36_1523": {
      "seqid": "NMDC:1781_100325_scf_1336_c1",
      "start": 35,
      "end": 1523,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1336_c1_36_1523",
      "annotations": {
        "id": [
          "1781_100325_scf_1336_c1_36_1523"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.60.40.10"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1337_c1": {
    "1781_100325_scf_1337_c1_1_81": {
      "seqid": "NMDC:1781_100325_scf_1337_c1",
      "start": 0,
      "end": 81,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1337_c1_1_81",
      "annotations": {
        "id": [
          "1781_100325_scf_1337_c1_1_81"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1337_c1_199_1479": {
      "seqid": "NMDC:1781_100325_scf_1337_c1",
      "start": 198,
      "end": 1479,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1337_c1_199_1479",
      "annotations": {
        "id": [
          "1781_100325_scf_1337_c1_199_1479"
        ],
        "product": [
          "transposase"
        ],
        "cog": [
          "COG3335",
          "COG3415"
        ],
        "pfam": [
          "DDE_",
          "HTH_2",
          "HTH_3"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1338_c1": {
    "1781_100325_scf_1338_c1_1_360": {
      "seqid": "NMDC:1781_100325_scf_1338_c1",
      "start": 0,
      "end": 360,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1338_c1_1_360",
      "annotations": {
        "id": [
          "1781_100325_scf_1338_c1_1_360"
        ],
        "product": [
          "small subunit ribosomal protein S13"
        ],
        "cath_funfam": [
          "1.10.8.50",
          "4.10.910.10"
        ],
        "cog": [
          "COG0099"
        ],
        "ko": [
          "KO:K02952"
        ],
        "pfam": [
          "Ribosomal_S1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1338_c1_572_928": {
      "seqid": "NMDC:1781_100325_scf_1338_c1",
      "start": 571,
      "end": 928,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1338_c1_572_928",
      "annotations": {
        "id": [
          "1781_100325_scf_1338_c1_572_928"
        ],
        "product": [
          "small subunit ribosomal protein S11"
        ],
        "cath_funfam": [
          "3.30.420.80"
        ],
        "cog": [
          "COG0100"
        ],
        "ko": [
          "KO:K02948"
        ],
        "pfam": [
          "Ribosomal_S1"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1338_c1_976_1524": {
      "seqid": "NMDC:1781_100325_scf_1338_c1",
      "start": 975,
      "end": 1524,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1338_c1_976_1524",
      "annotations": {
        "id": [
          "1781_100325_scf_1338_c1_976_1524"
        ],
        "product": [
          "small subunit ribosomal protein S4"
        ],
        "cath_funfam": [
          "1.10.1050.10",
          "3.10.290.10"
        ],
        "cog": [
          "COG0522"
        ],
        "ko": [
          "KO:K02986"
        ],
        "pfam": [
          "Ribosomal_S",
          "S"
        ],
        "superfamily": [
          "SM00363"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1339_c1": {
    "1781_100325_scf_1339_c1_28_387": {
      "seqid": "NMDC:1781_100325_scf_1339_c1",
      "start": 27,
      "end": 387,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1339_c1_28_387",
      "annotations": {
        "id": [
          "1781_100325_scf_1339_c1_28_387"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1339_c1_542_991": {
      "seqid": "NMDC:1781_100325_scf_1339_c1",
      "start": 541,
      "end": 991,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1339_c1_542_991",
      "annotations": {
        "id": [
          "1781_100325_scf_1339_c1_542_991"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1339_c1_1083_1262": {
      "seqid": "NMDC:1781_100325_scf_1339_c1",
      "start": 1082,
      "end": 1262,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1339_c1_1083_1262",
      "annotations": {
        "id": [
          "1781_100325_scf_1339_c1_1083_1262"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1339_c1_1268_1378": {
      "seqid": "NMDC:1781_100325_scf_1339_c1",
      "start": 1267,
      "end": 1378,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1339_c1_1268_1378",
      "annotations": {
        "id": [
          "1781_100325_scf_1339_c1_1268_1378"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1339_c1_1402_1524": {
      "seqid": "NMDC:1781_100325_scf_1339_c1",
      "start": 1401,
      "end": 1524,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1339_c1_1402_1524",
      "annotations": {
        "id": [
          "1781_100325_scf_1339_c1_1402_1524"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_133_c1": {
    "1781_100325_scf_133_c1_179_409": {
      "seqid": "NMDC:1781_100325_scf_133_c1",
      "start": 178,
      "end": 409,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_133_c1_179_409",
      "annotations": {
        "id": [
          "1781_100325_scf_133_c1_179_409"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_133_c1_530_742": {
      "seqid": "NMDC:1781_100325_scf_133_c1",
      "start": 529,
      "end": 742,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_133_c1_530_742",
      "annotations": {
        "id": [
          "1781_100325_scf_133_c1_530_742"
        ],
        "product": [
          "colicin import membrane protein"
        ],
        "ko": [
          "KO:K03646"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_133_c1_870_2411": {
      "seqid": "NMDC:1781_100325_scf_133_c1",
      "start": 869,
      "end": 2411,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_133_c1_870_2411",
      "annotations": {
        "id": [
          "1781_100325_scf_133_c1_870_2411"
        ],
        "product": [
          "acetyl-CoA/propionyl-CoA carboxylase"
        ],
        "cath_funfam": [
          "3.90.226.10"
        ],
        "cog": [
          "COG4799"
        ],
        "ko": [
          "KO:K18604"
        ],
        "ec_number": [
          "EC:6.4.1.2",
          "EC:6.4.1.3"
        ],
        "pfam": [
          "Carboxyl_tran",
          "Mdc"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_133_c1_2424_3521": {
      "seqid": "NMDC:1781_100325_scf_133_c1",
      "start": 2423,
      "end": 3521,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_133_c1_2424_3521",
      "annotations": {
        "id": [
          "1781_100325_scf_133_c1_2424_3521"
        ],
        "product": [
          "acetyl-CoA/propionyl-CoA carboxylase"
        ],
        "cath_funfam": [
          "3.30.470.20"
        ],
        "cog": [
          "COG4770"
        ],
        "ko": [
          "KO:K18603"
        ],
        "ec_number": [
          "EC:6.4.1.2",
          "EC:6.4.1.3"
        ],
        "pfam": [
          "ATP-gras",
          "ATP-grasp_",
          "Biotin_carb_",
          "CPSase_L_D",
          "Dala_Dala_lig_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1340_c1": {
    "1781_100325_scf_1340_c1_1_627": {
      "seqid": "NMDC:1781_100325_scf_1340_c1",
      "start": 0,
      "end": 627,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1340_c1_1_627",
      "annotations": {
        "id": [
          "1781_100325_scf_1340_c1_1_627"
        ],
        "product": [
          "adenylosuccinate synthase"
        ],
        "cath_funfam": [
          "3.40.440.10"
        ],
        "cog": [
          "COG0104"
        ],
        "ko": [
          "KO:K01939"
        ],
        "ec_number": [
          "EC:6.3.4.4"
        ],
        "pfam": [
          "Adenylsucc_syn"
        ],
        "superfamily": [
          "SM00788"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1340_c1_710_1171": {
      "seqid": "NMDC:1781_100325_scf_1340_c1",
      "start": 709,
      "end": 1171,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1340_c1_710_1171",
      "annotations": {
        "id": [
          "1781_100325_scf_1340_c1_710_1171"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1340_c1_1168_1440": {
      "seqid": "NMDC:1781_100325_scf_1340_c1",
      "start": 1167,
      "end": 1440,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1340_c1_1168_1440",
      "annotations": {
        "id": [
          "1781_100325_scf_1340_c1_1168_1440"
        ],
        "product": [
          "NAD-dependent SIR2 family protein deacetylase"
        ],
        "cath_funfam": [
          "1.10.3880.10"
        ],
        "cog": [
          "COG0846"
        ],
        "pfam": [
          "Iron_traffi"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1341_c1": {
    "1781_100325_scf_1341_c1_3_92": {
      "seqid": "NMDC:1781_100325_scf_1341_c1",
      "start": 2,
      "end": 92,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1341_c1_3_92",
      "annotations": {
        "id": [
          "1781_100325_scf_1341_c1_3_92"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1341_c1_73_921": {
      "seqid": "NMDC:1781_100325_scf_1341_c1",
      "start": 72,
      "end": 921,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1341_c1_73_921",
      "annotations": {
        "id": [
          "1781_100325_scf_1341_c1_73_921"
        ],
        "product": [
          "pimeloyl-ACP methyl ester carboxylesterase"
        ],
        "cath_funfam": [
          "3.40.50.1820"
        ],
        "cog": [
          "COG0596"
        ],
        "pfam": [
          "Abhydrolase_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1341_c1_1017_1208": {
      "seqid": "NMDC:1781_100325_scf_1341_c1",
      "start": 1016,
      "end": 1208,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1341_c1_1017_1208",
      "annotations": {
        "id": [
          "1781_100325_scf_1341_c1_1017_1208"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1341_c1_1283_1522": {
      "seqid": "NMDC:1781_100325_scf_1341_c1",
      "start": 1282,
      "end": 1522,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1341_c1_1283_1522",
      "annotations": {
        "id": [
          "1781_100325_scf_1341_c1_1283_1522"
        ],
        "product": [
          "N-carbamoylputrescine amidase"
        ],
        "cath_funfam": [
          "3.60.110.10"
        ],
        "cog": [
          "COG0388"
        ],
        "ko": [
          "KO:K12251"
        ],
        "ec_number": [
          "EC:3.5.1.53"
        ],
        "pfam": [
          "CN_hydrolas"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1342_c1": {
    "1781_100325_scf_1342_c1_2_799": {
      "seqid": "NMDC:1781_100325_scf_1342_c1",
      "start": 1,
      "end": 799,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1342_c1_2_799",
      "annotations": {
        "id": [
          "1781_100325_scf_1342_c1_2_799"
        ],
        "product": [
          "twitching motility protein PilT"
        ],
        "cath_funfam": [
          "3.40.50.300"
        ],
        "cog": [
          "COG2805"
        ],
        "ko": [
          "KO:K02669"
        ],
        "pfam": [
          "T2SS"
        ],
        "superfamily": [
          "SM00382"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1342_c1_815_1183": {
      "seqid": "NMDC:1781_100325_scf_1342_c1",
      "start": 814,
      "end": 1183,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1342_c1_815_1183",
      "annotations": {
        "id": [
          "1781_100325_scf_1342_c1_815_1183"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1342_c1_1236_1523": {
      "seqid": "NMDC:1781_100325_scf_1342_c1",
      "start": 1235,
      "end": 1523,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1342_c1_1236_1523",
      "annotations": {
        "id": [
          "1781_100325_scf_1342_c1_1236_1523"
        ],
        "product": [
          "poly(A) polymerase"
        ],
        "cath_funfam": [
          "3.30.460.10"
        ],
        "cog": [
          "COG0617"
        ],
        "ko": [
          "KO:K00970"
        ],
        "ec_number": [
          "EC:2.7.7.19"
        ],
        "pfam": [
          "PolyA_po"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1343_c1": {
    "1781_100325_scf_1343_c1_208_1503": {
      "seqid": "NMDC:1781_100325_scf_1343_c1",
      "start": 207,
      "end": 1503,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1343_c1_208_1503",
      "annotations": {
        "id": [
          "1781_100325_scf_1343_c1_208_1503"
        ],
        "product": [
          "leucyl-tRNA synthetase"
        ],
        "cath_funfam": [
          "1.10.730.10",
          "3.40.50.620"
        ],
        "cog": [
          "COG0495"
        ],
        "ko": [
          "KO:K01869"
        ],
        "ec_number": [
          "EC:6.1.1.4"
        ],
        "pfam": [
          "Anticodon_",
          "tRNA-synt_",
          "tRNA-synt_1"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1344_c1": {
    "1781_100325_scf_1344_c1_21_1385": {
      "seqid": "NMDC:1781_100325_scf_1344_c1",
      "start": 20,
      "end": 1385,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1344_c1_21_1385",
      "annotations": {
        "id": [
          "1781_100325_scf_1344_c1_21_1385"
        ],
        "product": [
          "NRAMP (natural resistance-associated macrophage protein)-like metal ion transporter"
        ],
        "cog": [
          "COG1914"
        ],
        "pfam": [
          "Nram"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1344_c1_1357_1521": {
      "seqid": "NMDC:1781_100325_scf_1344_c1",
      "start": 1356,
      "end": 1521,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1344_c1_1357_1521",
      "annotations": {
        "id": [
          "1781_100325_scf_1344_c1_1357_1521"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1345_c1": {
    "1781_100325_scf_1345_c1_67_288": {
      "seqid": "NMDC:1781_100325_scf_1345_c1",
      "start": 66,
      "end": 288,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1345_c1_67_288",
      "annotations": {
        "id": [
          "1781_100325_scf_1345_c1_67_288"
        ],
        "product": [
          "translation initiation factor IF-1"
        ],
        "cath_funfam": [
          "2.40.50.140"
        ],
        "cog": [
          "COG0361"
        ],
        "ko": [
          "KO:K02518"
        ],
        "pfam": [
          "eIF-1"
        ],
        "superfamily": [
          "SM00316"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1345_c1_300_671": {
      "seqid": "NMDC:1781_100325_scf_1345_c1",
      "start": 299,
      "end": 671,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1345_c1_300_671",
      "annotations": {
        "id": [
          "1781_100325_scf_1345_c1_300_671"
        ],
        "product": [
          "catechol 2",
          "3-dioxygenase-like lactoylglutathione lyase family enzyme"
        ],
        "cog": [
          "COG0346"
        ],
        "pfam": [
          "Glyoxalas"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1345_c1_668_1522": {
      "seqid": "NMDC:1781_100325_scf_1345_c1",
      "start": 667,
      "end": 1522,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1345_c1_668_1522",
      "annotations": {
        "id": [
          "1781_100325_scf_1345_c1_668_1522"
        ],
        "product": [
          "hypothetical protein"
        ],
        "pfam": [
          "LT"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1346_c1": {
    "1781_100325_scf_1346_c1_1_279": {
      "seqid": "NMDC:1781_100325_scf_1346_c1",
      "start": 0,
      "end": 279,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1346_c1_1_279",
      "annotations": {
        "id": [
          "1781_100325_scf_1346_c1_1_279"
        ],
        "product": [
          "ethanolamine permease"
        ],
        "ko": [
          "KO:K16238"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1346_c1_395_1522": {
      "seqid": "NMDC:1781_100325_scf_1346_c1",
      "start": 394,
      "end": 1522,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1346_c1_395_1522",
      "annotations": {
        "id": [
          "1781_100325_scf_1346_c1_395_1522"
        ],
        "product": [
          "glutamine synthetase"
        ],
        "cath_funfam": [
          "3.10.20.70",
          "3.30.590.10"
        ],
        "cog": [
          "COG0174"
        ],
        "ko": [
          "KO:K01915"
        ],
        "ec_number": [
          "EC:6.3.1.2"
        ],
        "pfam": [
          "Gln-synt_"
        ],
        "superfamily": [
          "SM01230"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1347_c1": {
    "1781_100325_scf_1347_c1_1_1203": {
      "seqid": "NMDC:1781_100325_scf_1347_c1",
      "start": 0,
      "end": 1203,
      "strand": "+",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_1347_c1_1_1203",
      "annotations": {
        "id": [
          "1781_100325_scf_1347_c1_1_1203"
        ],
        "product": [
          "16S ribosomal RNA"
        ]
      }
    },
    "1781_100325_scf_1347_c1_1355_1521": {
      "seqid": "NMDC:1781_100325_scf_1347_c1",
      "start": 1354,
      "end": 1521,
      "strand": "+",
      "type": "SO:0000252",
      "encodes": "NMDC:1781_100325_scf_1347_c1_1355_1521",
      "annotations": {
        "id": [
          "1781_100325_scf_1347_c1_1355_1521"
        ],
        "product": [
          "23S ribosomal RNA"
        ]
      }
    }
  },
  "1781_100325_scf_1348_c1": {
    "1781_100325_scf_1348_c1_3_290": {
      "seqid": "NMDC:1781_100325_scf_1348_c1",
      "start": 2,
      "end": 290,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1348_c1_3_290",
      "annotations": {
        "id": [
          "1781_100325_scf_1348_c1_3_290"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "2.30.40.10"
        ],
        "cog": [
          "COG1574"
        ],
        "ko": [
          "KO:K07047"
        ],
        "pfam": [
          "Amidohydro_"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1348_c1_420_1520": {
      "seqid": "NMDC:1781_100325_scf_1348_c1",
      "start": 419,
      "end": 1520,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1348_c1_420_1520",
      "annotations": {
        "id": [
          "1781_100325_scf_1348_c1_420_1520"
        ],
        "product": [
          "aminomethyltransferase"
        ],
        "cath_funfam": [
          "3.30.1360.120"
        ],
        "cog": [
          "COG0404"
        ],
        "ko": [
          "KO:K00605"
        ],
        "ec_number": [
          "EC:2.1.2.10"
        ],
        "pfam": [
          "GCV_",
          "GCV_T_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_1349_c1": {
    "1781_100325_scf_1349_c1_73_948": {
      "seqid": "NMDC:1781_100325_scf_1349_c1",
      "start": 72,
      "end": 948,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1349_c1_73_948",
      "annotations": {
        "id": [
          "1781_100325_scf_1349_c1_73_948"
        ],
        "product": [
          "hypothetical protein"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_1349_c1_1075_1509": {
      "seqid": "NMDC:1781_100325_scf_1349_c1",
      "start": 1074,
      "end": 1509,
      "strand": "-",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_1349_c1_1075_1509",
      "annotations": {
        "id": [
          "1781_100325_scf_1349_c1_1075_1509"
        ],
        "product": [
          "lipoprotein-anchoring transpeptidase ErfK/SrfK"
        ],
        "cath_funfam": [
          "2.40.440.10"
        ],
        "cog": [
          "COG1376"
        ],
        "pfam": [
          "Yku"
        ],
        "phase": [
          "0"
        ]
      }
    }
  },
  "1781_100325_scf_134_c1": {
    "1781_100325_scf_134_c1_135_1754": {
      "seqid": "NMDC:1781_100325_scf_134_c1",
      "start": 134,
      "end": 1754,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_134_c1_135_1754",
      "annotations": {
        "id": [
          "1781_100325_scf_134_c1_135_1754"
        ],
        "product": [
          "hypothetical protein"
        ],
        "cath_funfam": [
          "3.20.20.70"
        ],
        "cog": [
          "COG1964"
        ],
        "ko": [
          "KO:K06937"
        ],
        "ec_number": [
          "EC:2.1.1.-"
        ],
        "pfam": [
          "Fer4_1",
          "Radical_SA"
        ],
        "phase": [
          "0"
        ]
      }
    },
    "1781_100325_scf_134_c1_1911_2762": {
      "seqid": "NMDC:1781_100325_scf_134_c1",
      "start": 1910,
      "end": 2762,
      "strand": "+",
      "type": "SO:0000316",
      "encodes": "NMDC:1781_100325_scf_134_c1_1911_2762",
      "annotations": {
        "id": [
          "1781_100325_scf_134_c1_1911_2762"
        ],
        "product": [
          "3-hydroxypropionyl-coenzyme A dehydratase"
        ],
        "cath_funfam": [
          "1.10.12.10",
          "3.90.226.10"
        ],
        "cog": [
          "COG1024"
        ],
        "ko": [
          "KO:K15019"
        ],
        "ec_number": [
          "EC:4.2.1.116"
        ],
        "pfam": [
          "ECH_"
        ],
        "phase": [
          "0"
        ]
      }
    }
  }
}
```
# About pynmdc

PyNMDC is a Python package to work with NMDC data.

More about NMDC: https://microbiomedata.org/

## Install (for developers only):
1 `git clone git@github.com:microbiomedata/pynmdc.gitc.git`

2 Go to the pynmdc package root dir

3 Run this command: `pip install -e .`

4 Test Command line interface:
```
$nmdc --help
Usage: nmdc [OPTIONS] COMMAND [ARGS]...

  NMDC Tools v0.1.

Options:
  --help  Show this message and exit.

Commands:
  gff2json  Convert GFF3 to NMDC JSON format.
```

5 Run gff2json:

```
$nmdc gff2json test_data/metaT/metaT.gff
```

Output:

'''javascript
{
  "seqid": "NMDC:1781_100346_scf_10000_c1",
  "start": 1,
  "end": 454,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10000_c1_2_454"
}
{
  "seqid": "NMDC:1781_100346_scf_10001_c1",
  "start": 2,
  "end": 431,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10001_c1_3_431"
}
{
  "seqid": "NMDC:1781_100346_scf_10002_c1",
  "start": 2,
  "end": 218,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10002_c1_3_218"
}
{
  "seqid": "NMDC:1781_100346_scf_10002_c1",
  "start": 230,
  "end": 452,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10002_c1_231_452"
}
{
  "seqid": "NMDC:1781_100346_scf_10003_c1",
  "start": 0,
  "end": 372,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10003_c1_1_372"
}
{
  "seqid": "NMDC:1781_100346_scf_10004_c1",
  "start": 0,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10004_c1_1_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10005_c1",
  "start": 0,
  "end": 278,
  "strand": "+",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_10005_c1_1_278"
}
{
  "seqid": "NMDC:1781_100346_scf_10006_c1",
  "start": 0,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10006_c1_1_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10007_c1",
  "start": 81,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10007_c1_82_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10008_c1",
  "start": 0,
  "end": 450,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10008_c1_1_450"
}
{
  "seqid": "NMDC:1781_100346_scf_10009_c1",
  "start": 2,
  "end": 452,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10009_c1_3_452"
}
{
  "seqid": "NMDC:1781_100346_scf_1000_c1",
  "start": 36,
  "end": 459,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_1000_c1_37_459"
}
{
  "seqid": "NMDC:1781_100346_scf_1000_c1",
  "start": 455,
  "end": 1289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_1000_c1_456_1289"
}
{
  "seqid": "NMDC:1781_100346_scf_1000_c1",
  "start": 1297,
  "end": 1399,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_1000_c1_1298_1399"
}
{
  "seqid": "NMDC:1781_100346_scf_10010_c1",
  "start": 2,
  "end": 431,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10010_c1_3_431"
}
{
  "seqid": "NMDC:1781_100346_scf_10011_c1",
  "start": 2,
  "end": 452,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10011_c1_3_452"
}
{
  "seqid": "NMDC:1781_100346_scf_10012_c1",
  "start": 5,
  "end": 452,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10012_c1_6_452"
}
{
  "seqid": "NMDC:1781_100346_scf_10013_c1",
  "start": 0,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10013_c1_1_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10014_c1",
  "start": 1,
  "end": 451,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10014_c1_2_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10015_c1",
  "start": 2,
  "end": 221,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10015_c1_3_221"
}
{
  "seqid": "NMDC:1781_100346_scf_10015_c1",
  "start": 217,
  "end": 451,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10015_c1_218_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10016_c1",
  "start": 2,
  "end": 452,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10016_c1_3_452"
}
{
  "seqid": "NMDC:1781_100346_scf_10017_c1",
  "start": 30,
  "end": 249,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10017_c1_31_249"
}
{
  "seqid": "NMDC:1781_100346_scf_10018_c1",
  "start": 0,
  "end": 402,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10018_c1_1_402"
}
{
  "seqid": "NMDC:1781_100346_scf_10019_c1",
  "start": 0,
  "end": 207,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10019_c1_1_207"
}
{
  "seqid": "NMDC:1781_100346_scf_10019_c1",
  "start": 211,
  "end": 451,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10019_c1_212_451"
}
{
  "seqid": "NMDC:1781_100346_scf_1001_c1",
  "start": 1,
  "end": 967,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_1001_c1_2_967"
}
{
  "seqid": "NMDC:1781_100346_scf_1001_c1",
  "start": 963,
  "end": 1320,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_1001_c1_964_1320"
}
{
  "seqid": "NMDC:1781_100346_scf_10020_c1",
  "start": 0,
  "end": 261,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10020_c1_1_261"
}
{
  "seqid": "NMDC:1781_100346_scf_10020_c1",
  "start": 310,
  "end": 451,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10020_c1_311_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10021_c1",
  "start": 0,
  "end": 174,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10021_c1_1_174"
}
{
  "seqid": "NMDC:1781_100346_scf_10022_c1",
  "start": 1,
  "end": 427,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10022_c1_2_427"
}
{
  "seqid": "NMDC:1781_100346_scf_10023_c1",
  "start": 51,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10023_c1_52_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10024_c1",
  "start": 45,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10024_c1_46_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10025_c1",
  "start": 1,
  "end": 268,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10025_c1_2_268"
}
{
  "seqid": "NMDC:1781_100346_scf_10025_c1",
  "start": 306,
  "end": 405,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10025_c1_307_405"
}
{
  "seqid": "NMDC:1781_100346_scf_10026_c1",
  "start": 0,
  "end": 315,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10026_c1_1_315"
}
{
  "seqid": "NMDC:1781_100346_scf_10027_c1",
  "start": 2,
  "end": 452,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10027_c1_3_452"
}
{
  "seqid": "NMDC:1781_100346_scf_10028_c1",
  "start": 1,
  "end": 130,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10028_c1_2_130"
}
{
  "seqid": "NMDC:1781_100346_scf_10028_c1",
  "start": 247,
  "end": 349,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10028_c1_248_349"
}
{
  "seqid": "NMDC:1781_100346_scf_10028_c1",
  "start": 345,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10028_c1_346_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10029_c1",
  "start": 2,
  "end": 104,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10029_c1_3_104"
}
{
  "seqid": "NMDC:1781_100346_scf_10029_c1",
  "start": 23,
  "end": 236,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10029_c1_24_236"
}
{
  "seqid": "NMDC:1781_100346_scf_10029_c1",
  "start": 343,
  "end": 451,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10029_c1_344_451"
}
{
  "seqid": "NMDC:1781_100346_scf_1002_c1",
  "start": 7,
  "end": 223,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_1002_c1_8_223"
}
{
  "seqid": "NMDC:1781_100346_scf_1002_c1",
  "start": 235,
  "end": 1378,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_1002_c1_236_1378"
}
{
  "seqid": "NMDC:1781_100346_scf_10030_c1",
  "start": 1,
  "end": 388,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10030_c1_2_388"
}
{
  "seqid": "NMDC:1781_100346_scf_10031_c1",
  "start": 15,
  "end": 321,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10031_c1_16_321"
}
{
  "seqid": "NMDC:1781_100346_scf_10031_c1",
  "start": 326,
  "end": 452,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10031_c1_327_452"
}
{
  "seqid": "NMDC:1781_100346_scf_10032_c1",
  "start": 1,
  "end": 451,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10032_c1_2_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10033_c1",
  "start": 96,
  "end": 453,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10033_c1_97_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10034_c1",
  "start": 0,
  "end": 453,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10034_c1_1_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10035_c1",
  "start": 1,
  "end": 106,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10035_c1_2_106"
}
{
  "seqid": "NMDC:1781_100346_scf_10035_c1",
  "start": 216,
  "end": 438,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10035_c1_217_438"
}
{
  "seqid": "NMDC:1781_100346_scf_10036_c1",
  "start": 84,
  "end": 453,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10036_c1_85_453"
}
{
  "seqid": "NMDC:1781_100346_scf_10037_c1",
  "start": 0,
  "end": 255,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10037_c1_1_255"
}
{
  "seqid": "NMDC:1781_100346_scf_10037_c1",
  "start": 325,
  "end": 451,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10037_c1_326_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10038_c1",
  "start": 1,
  "end": 451,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_10038_c1_2_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10145_c1",
  "start": 77,
  "end": 451,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_10145_c1_78_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10159_c1",
  "start": 0,
  "end": 451,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_10159_c1_1_451"
}
{
  "seqid": "NMDC:1781_100346_scf_10268_c1",
  "start": 219,
  "end": 336,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_10268_c1_220_336"
}
{
  "seqid": "NMDC:1781_100346_scf_10280_c1",
  "start": 210,
  "end": 448,
  "strand": "",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_10280_c1_211_448"
}
{
  "seqid": "NMDC:1781_100346_scf_10325_c1",
  "start": 2,
  "end": 122,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_10325_c1_3_122"
}
{
  "seqid": "NMDC:1781_100346_scf_10362_c1",
  "start": 245,
  "end": 320,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_10362_c1_246_320"
}
{
  "seqid": "NMDC:1781_100346_scf_10480_c1",
  "start": 124,
  "end": 200,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_10480_c1_125_200"
}
{
  "seqid": "NMDC:1781_100346_scf_10514_c1",
  "start": 0,
  "end": 126,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_10514_c1_1_126"
}
{
  "seqid": "NMDC:1781_100346_scf_10528_c1",
  "start": 223,
  "end": 310,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_10528_c1_224_310"
}
{
  "seqid": "NMDC:1781_100346_scf_10556_c1",
  "start": 179,
  "end": 434,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_10556_c1_180_434"
}
{
  "seqid": "NMDC:1781_100346_scf_10573_c1",
  "start": 0,
  "end": 444,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_10573_c1_1_444"
}
{
  "seqid": "NMDC:1781_100346_scf_1078_c1",
  "start": 706,
  "end": 842,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_1078_c1_707_842"
}
{
  "seqid": "NMDC:1781_100346_scf_10793_c1",
  "start": 0,
  "end": 440,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_10793_c1_1_440"
}
{
  "seqid": "NMDC:1781_100346_scf_10817_c1",
  "start": 351,
  "end": 439,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_10817_c1_352_439"
}
{
  "seqid": "NMDC:1781_100346_scf_11028_c1",
  "start": 0,
  "end": 436,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_11028_c1_1_436"
}
{
  "seqid": "NMDC:1781_100346_scf_11151_c1",
  "start": 233,
  "end": 353,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_11151_c1_234_353"
}
{
  "seqid": "NMDC:1781_100346_scf_11224_c1",
  "start": 2,
  "end": 432,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_11224_c1_3_432"
}
{
  "seqid": "NMDC:1781_100346_scf_11239_c1",
  "start": 24,
  "end": 388,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_11239_c1_25_388"
}
{
  "seqid": "NMDC:1781_100346_scf_11325_c1",
  "start": 0,
  "end": 431,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_11325_c1_1_431"
}
{
  "seqid": "NMDC:1781_100346_scf_11358_c1",
  "start": 123,
  "end": 395,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_11358_c1_124_395"
}
{
  "seqid": "NMDC:1781_100346_scf_11389_c1",
  "start": 0,
  "end": 430,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_11389_c1_1_430"
}
{
  "seqid": "NMDC:1781_100346_scf_1138_c1",
  "start": 0,
  "end": 92,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_1138_c1_1_92"
}
{
  "seqid": "NMDC:1781_100346_scf_11505_c1",
  "start": 25,
  "end": 376,
  "strand": "+",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_11505_c1_26_376"
}
{
  "seqid": "NMDC:1781_100346_scf_11526_c1",
  "start": 258,
  "end": 426,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_11526_c1_259_426"
}
{
  "seqid": "NMDC:1781_100346_scf_11529_c1",
  "start": 0,
  "end": 428,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_11529_c1_1_428"
}
{
  "seqid": "NMDC:1781_100346_scf_11537_c1",
  "start": 0,
  "end": 354,
  "strand": "",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_11537_c1_1_354"
}
{
  "seqid": "NMDC:1781_100346_scf_1157_c1",
  "start": 64,
  "end": 1300,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1157_c1_65_1300"
}
{
  "seqid": "NMDC:1781_100346_scf_1170_c1",
  "start": 0,
  "end": 946,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1170_c1_1_946"
}
{
  "seqid": "NMDC:1781_100346_scf_1175_c1",
  "start": 47,
  "end": 1293,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1175_c1_48_1293"
}
{
  "seqid": "NMDC:1781_100346_scf_11791_c1",
  "start": 0,
  "end": 122,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_11791_c1_1_122"
}
{
  "seqid": "NMDC:1781_100346_scf_11834_c1",
  "start": 0,
  "end": 423,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_11834_c1_1_423"
}
{
  "seqid": "NMDC:1781_100346_scf_11877_c1",
  "start": 0,
  "end": 422,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_11877_c1_1_422"
}
{
  "seqid": "NMDC:1781_100346_scf_12016_c1",
  "start": 0,
  "end": 420,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12016_c1_1_420"
}
{
  "seqid": "NMDC:1781_100346_scf_120_c1",
  "start": 0,
  "end": 340,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_120_c1_1_340"
}
{
  "seqid": "NMDC:1781_100346_scf_12125_c1",
  "start": 91,
  "end": 355,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_12125_c1_92_355"
}
{
  "seqid": "NMDC:1781_100346_scf_12133_c1",
  "start": 0,
  "end": 418,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12133_c1_1_418"
}
{
  "seqid": "NMDC:1781_100346_scf_12336_c1",
  "start": 214,
  "end": 318,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_12336_c1_215_318"
}
{
  "seqid": "NMDC:1781_100346_scf_12377_c1",
  "start": 0,
  "end": 415,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12377_c1_1_415"
}
{
  "seqid": "NMDC:1781_100346_scf_12395_c1",
  "start": 0,
  "end": 415,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12395_c1_1_415"
}
{
  "seqid": "NMDC:1781_100346_scf_123_c1",
  "start": 106,
  "end": 389,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_123_c1_107_389"
}
{
  "seqid": "NMDC:1781_100346_scf_12546_c1",
  "start": 234,
  "end": 311,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_12546_c1_235_311"
}
{
  "seqid": "NMDC:1781_100346_scf_12549_c1",
  "start": 0,
  "end": 191,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_12549_c1_1_191"
}
{
  "seqid": "NMDC:1781_100346_scf_12630_c1",
  "start": 0,
  "end": 411,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12630_c1_1_411"
}
{
  "seqid": "NMDC:1781_100346_scf_12674_c1",
  "start": 0,
  "end": 411,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12674_c1_1_411"
}
{
  "seqid": "NMDC:1781_100346_scf_12692_c1",
  "start": 202,
  "end": 283,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_12692_c1_203_283"
}
{
  "seqid": "NMDC:1781_100346_scf_12776_c1",
  "start": 0,
  "end": 410,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12776_c1_1_410"
}
{
  "seqid": "NMDC:1781_100346_scf_12892_c1",
  "start": 0,
  "end": 408,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12892_c1_1_408"
}
{
  "seqid": "NMDC:1781_100346_scf_12964_c1",
  "start": 0,
  "end": 407,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_12964_c1_1_407"
}
{
  "seqid": "NMDC:1781_100346_scf_13365_c1",
  "start": 115,
  "end": 225,
  "strand": "",
  "type": "SO:0001459",
  "encodes": "NMDC:1781_100346_scf_13365_c1_116_225"
}
{
  "seqid": "NMDC:1781_100346_scf_13393_c1",
  "start": 133,
  "end": 304,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_13393_c1_134_304"
}
{
  "seqid": "NMDC:1781_100346_scf_13463_c1",
  "start": 0,
  "end": 400,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_13463_c1_1_400"
}
{
  "seqid": "NMDC:1781_100346_scf_13633_c1",
  "start": 0,
  "end": 360,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_13633_c1_1_360"
}
{
  "seqid": "NMDC:1781_100346_scf_13645_c1",
  "start": 0,
  "end": 397,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_13645_c1_1_397"
}
{
  "seqid": "NMDC:1781_100346_scf_13654_c1",
  "start": 0,
  "end": 298,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_13654_c1_1_298"
}
{
  "seqid": "NMDC:1781_100346_scf_1369_c1",
  "start": 0,
  "end": 1198,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1369_c1_1_1198"
}
{
  "seqid": "NMDC:1781_100346_scf_13920_c1",
  "start": 0,
  "end": 395,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_13920_c1_1_395"
}
{
  "seqid": "NMDC:1781_100346_scf_13950_c1",
  "start": 0,
  "end": 395,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_13950_c1_1_395"
}
{
  "seqid": "NMDC:1781_100346_scf_13951_c1",
  "start": 0,
  "end": 395,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_13951_c1_1_395"
}
{
  "seqid": "NMDC:1781_100346_scf_14034_c1",
  "start": 0,
  "end": 393,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_14034_c1_1_393"
}
{
  "seqid": "NMDC:1781_100346_scf_14098_c1",
  "start": 54,
  "end": 325,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_14098_c1_55_325"
}
{
  "seqid": "NMDC:1781_100346_scf_14175_c1",
  "start": 0,
  "end": 392,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_14175_c1_1_392"
}
{
  "seqid": "NMDC:1781_100346_scf_1419_c1",
  "start": 183,
  "end": 1178,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1419_c1_184_1178"
}
{
  "seqid": "NMDC:1781_100346_scf_14295_c1",
  "start": 0,
  "end": 188,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_14295_c1_1_188"
}
{
  "seqid": "NMDC:1781_100346_scf_14295_c1",
  "start": 267,
  "end": 384,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_14295_c1_268_384"
}
{
  "seqid": "NMDC:1781_100346_scf_1436_c1",
  "start": 0,
  "end": 1030,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1436_c1_1_1030"
}
{
  "seqid": "NMDC:1781_100346_scf_1436_c1",
  "start": 1085,
  "end": 1171,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1436_c1_1086_1171"
}
{
  "seqid": "NMDC:1781_100346_scf_14379_c1",
  "start": 63,
  "end": 331,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_14379_c1_64_331"
}
{
  "seqid": "NMDC:1781_100346_scf_14384_c1",
  "start": 0,
  "end": 390,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_14384_c1_1_390"
}
{
  "seqid": "NMDC:1781_100346_scf_14619_c1",
  "start": 0,
  "end": 387,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_14619_c1_1_387"
}
{
  "seqid": "NMDC:1781_100346_scf_14701_c1",
  "start": 0,
  "end": 166,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_14701_c1_1_166"
}
{
  "seqid": "NMDC:1781_100346_scf_1475_c1",
  "start": 104,
  "end": 1154,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1475_c1_105_1154"
}
{
  "seqid": "NMDC:1781_100346_scf_15023_c1",
  "start": 0,
  "end": 383,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_15023_c1_1_383"
}
{
  "seqid": "NMDC:1781_100346_scf_15217_c1",
  "start": 0,
  "end": 176,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_15217_c1_1_176"
}
{
  "seqid": "NMDC:1781_100346_scf_15455_c1",
  "start": 0,
  "end": 378,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_15455_c1_1_378"
}
{
  "seqid": "NMDC:1781_100346_scf_15473_c1",
  "start": 0,
  "end": 378,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_15473_c1_1_378"
}
{
  "seqid": "NMDC:1781_100346_scf_15527_c1",
  "start": 51,
  "end": 127,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_15527_c1_52_127"
}
{
  "seqid": "NMDC:1781_100346_scf_15613_c1",
  "start": 74,
  "end": 243,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_15613_c1_75_243"
}
{
  "seqid": "NMDC:1781_100346_scf_15695_c1",
  "start": 0,
  "end": 376,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_15695_c1_1_376"
}
{
  "seqid": "NMDC:1781_100346_scf_15799_c1",
  "start": 0,
  "end": 226,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_15799_c1_1_226"
}
{
  "seqid": "NMDC:1781_100346_scf_15864_c1",
  "start": 0,
  "end": 375,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_15864_c1_1_375"
}
{
  "seqid": "NMDC:1781_100346_scf_15971_c1",
  "start": 156,
  "end": 313,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_15971_c1_157_313"
}
{
  "seqid": "NMDC:1781_100346_scf_15976_c1",
  "start": 61,
  "end": 200,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_15976_c1_62_200"
}
{
  "seqid": "NMDC:1781_100346_scf_16005_c1",
  "start": 0,
  "end": 374,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_16005_c1_1_374"
}
{
  "seqid": "NMDC:1781_100346_scf_16046_c1",
  "start": 31,
  "end": 116,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_16046_c1_32_116"
}
{
  "seqid": "NMDC:1781_100346_scf_16219_c1",
  "start": 211,
  "end": 291,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_16219_c1_212_291"
}
{
  "seqid": "NMDC:1781_100346_scf_1622_c1",
  "start": 1056,
  "end": 1098,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_1622_c1_1057_1098"
}
{
  "seqid": "NMDC:1781_100346_scf_16297_c1",
  "start": 0,
  "end": 371,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_16297_c1_1_371"
}
{
  "seqid": "NMDC:1781_100346_scf_16327_c1",
  "start": 0,
  "end": 371,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_16327_c1_1_371"
}
{
  "seqid": "NMDC:1781_100346_scf_16667_c1",
  "start": 76,
  "end": 368,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_16667_c1_77_368"
}
{
  "seqid": "NMDC:1781_100346_scf_1680_c1",
  "start": 45,
  "end": 258,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_1680_c1_46_258"
}
{
  "seqid": "NMDC:1781_100346_scf_17014_c1",
  "start": 148,
  "end": 260,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_17014_c1_149_260"
}
{
  "seqid": "NMDC:1781_100346_scf_17101_c1",
  "start": 0,
  "end": 364,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_17101_c1_1_364"
}
{
  "seqid": "NMDC:1781_100346_scf_17225_c1",
  "start": 0,
  "end": 363,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_17225_c1_1_363"
}
{
  "seqid": "NMDC:1781_100346_scf_1725_c1",
  "start": 373,
  "end": 1063,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1725_c1_374_1063"
}
{
  "seqid": "NMDC:1781_100346_scf_17362_c1",
  "start": 0,
  "end": 362,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_17362_c1_1_362"
}
{
  "seqid": "NMDC:1781_100346_scf_17427_c1",
  "start": 0,
  "end": 362,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_17427_c1_1_362"
}
{
  "seqid": "NMDC:1781_100346_scf_1774_c1",
  "start": 0,
  "end": 1049,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1774_c1_1_1049"
}
{
  "seqid": "NMDC:1781_100346_scf_17876_c1",
  "start": 266,
  "end": 358,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_17876_c1_267_358"
}
{
  "seqid": "NMDC:1781_100346_scf_18029_c1",
  "start": 254,
  "end": 357,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_18029_c1_255_357"
}
{
  "seqid": "NMDC:1781_100346_scf_18223_c1",
  "start": 0,
  "end": 356,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_18223_c1_1_356"
}
{
  "seqid": "NMDC:1781_100346_scf_18271_c1",
  "start": 0,
  "end": 356,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_18271_c1_1_356"
}
{
  "seqid": "NMDC:1781_100346_scf_18543_c1",
  "start": 0,
  "end": 354,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_18543_c1_1_354"
}
{
  "seqid": "NMDC:1781_100346_scf_18594_c1",
  "start": 69,
  "end": 287,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_18594_c1_70_287"
}
{
  "seqid": "NMDC:1781_100346_scf_185_c1",
  "start": 1541,
  "end": 1839,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_185_c1_1542_1839"
}
{
  "seqid": "NMDC:1781_100346_scf_18601_c1",
  "start": 58,
  "end": 215,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_18601_c1_59_215"
}
{
  "seqid": "NMDC:1781_100346_scf_19633_c1",
  "start": 0,
  "end": 347,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_19633_c1_1_347"
}
{
  "seqid": "NMDC:1781_100346_scf_1971_c1",
  "start": 0,
  "end": 993,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1971_c1_1_993"
}
{
  "seqid": "NMDC:1781_100346_scf_1973_c1",
  "start": 0,
  "end": 993,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1973_c1_1_993"
}
{
  "seqid": "NMDC:1781_100346_scf_19769_c1",
  "start": 233,
  "end": 346,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_19769_c1_234_346"
}
{
  "seqid": "NMDC:1781_100346_scf_19773_c1",
  "start": 0,
  "end": 65,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_19773_c1_1_65"
}
{
  "seqid": "NMDC:1781_100346_scf_19886_c1",
  "start": 0,
  "end": 345,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_19886_c1_1_345"
}
{
  "seqid": "NMDC:1781_100346_scf_1994_c1",
  "start": 0,
  "end": 988,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_1994_c1_1_988"
}
{
  "seqid": "NMDC:1781_100346_scf_19999_c1",
  "start": 0,
  "end": 345,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_19999_c1_1_345"
}
{
  "seqid": "NMDC:1781_100346_scf_20072_c1",
  "start": 0,
  "end": 345,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_20072_c1_1_345"
}
{
  "seqid": "NMDC:1781_100346_scf_20079_c1",
  "start": 0,
  "end": 101,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_20079_c1_1_101"
}
{
  "seqid": "NMDC:1781_100346_scf_202_c1",
  "start": 55,
  "end": 131,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_202_c1_56_131"
}
{
  "seqid": "NMDC:1781_100346_scf_202_c1",
  "start": 2661,
  "end": 2882,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_202_c1_2662_2882"
}
{
  "seqid": "NMDC:1781_100346_scf_20419_c1",
  "start": 0,
  "end": 343,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_20419_c1_1_343"
}
{
  "seqid": "NMDC:1781_100346_scf_20573_c1",
  "start": 0,
  "end": 342,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_20573_c1_1_342"
}
{
  "seqid": "NMDC:1781_100346_scf_20867_c1",
  "start": 0,
  "end": 340,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_20867_c1_1_340"
}
{
  "seqid": "NMDC:1781_100346_scf_20961_c1",
  "start": 0,
  "end": 340,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_20961_c1_1_340"
}
{
  "seqid": "NMDC:1781_100346_scf_212_c1",
  "start": 0,
  "end": 1521,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_212_c1_1_1521"
}
{
  "seqid": "NMDC:1781_100346_scf_21938_c1",
  "start": 0,
  "end": 247,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_21938_c1_1_247"
}
{
  "seqid": "NMDC:1781_100346_scf_22076_c1",
  "start": 79,
  "end": 262,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_22076_c1_80_262"
}
{
  "seqid": "NMDC:1781_100346_scf_22239_c1",
  "start": 74,
  "end": 156,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_22239_c1_75_156"
}
{
  "seqid": "NMDC:1781_100346_scf_22291_c1",
  "start": 0,
  "end": 333,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_22291_c1_1_333"
}
{
  "seqid": "NMDC:1781_100346_scf_22804_c1",
  "start": 147,
  "end": 222,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_22804_c1_148_222"
}
{
  "seqid": "NMDC:1781_100346_scf_232_c1",
  "start": 0,
  "end": 1556,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_232_c1_1_1556"
}
{
  "seqid": "NMDC:1781_100346_scf_232_c1",
  "start": 1774,
  "end": 2731,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_232_c1_1775_2731"
}
{
  "seqid": "NMDC:1781_100346_scf_2337_c1",
  "start": 727,
  "end": 835,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_2337_c1_728_835"
}
{
  "seqid": "NMDC:1781_100346_scf_23420_c1",
  "start": 55,
  "end": 203,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_23420_c1_56_203"
}
{
  "seqid": "NMDC:1781_100346_scf_23667_c1",
  "start": 7,
  "end": 122,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_23667_c1_8_122"
}
{
  "seqid": "NMDC:1781_100346_scf_23776_c1",
  "start": 112,
  "end": 327,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_23776_c1_113_327"
}
{
  "seqid": "NMDC:1781_100346_scf_23871_c1",
  "start": 65,
  "end": 163,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_23871_c1_66_163"
}
{
  "seqid": "NMDC:1781_100346_scf_24099_c1",
  "start": 0,
  "end": 326,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_24099_c1_1_326"
}
{
  "seqid": "NMDC:1781_100346_scf_2414_c1",
  "start": 0,
  "end": 890,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_2414_c1_1_890"
}
{
  "seqid": "NMDC:1781_100346_scf_2448_c1",
  "start": 434,
  "end": 701,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_2448_c1_435_701"
}
{
  "seqid": "NMDC:1781_100346_scf_2453_c1",
  "start": 71,
  "end": 218,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_2453_c1_72_218"
}
{
  "seqid": "NMDC:1781_100346_scf_25065_c1",
  "start": 0,
  "end": 321,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_25065_c1_1_321"
}
{
  "seqid": "NMDC:1781_100346_scf_26099_c1",
  "start": 1,
  "end": 267,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_26099_c1_2_267"
}
{
  "seqid": "NMDC:1781_100346_scf_2610_c1",
  "start": 460,
  "end": 854,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_2610_c1_461_854"
}
{
  "seqid": "NMDC:1781_100346_scf_26238_c1",
  "start": 0,
  "end": 317,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_26238_c1_1_317"
}
{
  "seqid": "NMDC:1781_100346_scf_26389_c1",
  "start": 18,
  "end": 316,
  "strand": "",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_26389_c1_19_316"
}
{
  "seqid": "NMDC:1781_100346_scf_26571_c1",
  "start": 0,
  "end": 316,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_26571_c1_1_316"
}
{
  "seqid": "NMDC:1781_100346_scf_2664_c1",
  "start": 665,
  "end": 742,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_2664_c1_666_742"
}
{
  "seqid": "NMDC:1781_100346_scf_26753_c1",
  "start": 0,
  "end": 219,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_26753_c1_1_219"
}
{
  "seqid": "NMDC:1781_100346_scf_2690_c1",
  "start": 569,
  "end": 731,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_2690_c1_570_731"
}
{
  "seqid": "NMDC:1781_100346_scf_2706_c1",
  "start": 239,
  "end": 358,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_2706_c1_240_358"
}
{
  "seqid": "NMDC:1781_100346_scf_27266_c1",
  "start": 0,
  "end": 218,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_27266_c1_1_218"
}
{
  "seqid": "NMDC:1781_100346_scf_27290_c1",
  "start": 0,
  "end": 313,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_27290_c1_1_313"
}
{
  "seqid": "NMDC:1781_100346_scf_27339_c1",
  "start": 86,
  "end": 250,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_27339_c1_87_250"
}
{
  "seqid": "NMDC:1781_100346_scf_2762_c1",
  "start": 689,
  "end": 808,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_2762_c1_690_808"
}
{
  "seqid": "NMDC:1781_100346_scf_27715_c1",
  "start": 0,
  "end": 311,
  "strand": "",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_27715_c1_1_311"
}
{
  "seqid": "NMDC:1781_100346_scf_27744_c1",
  "start": 121,
  "end": 312,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_27744_c1_122_312"
}
{
  "seqid": "NMDC:1781_100346_scf_2794_c1",
  "start": 0,
  "end": 755,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_2794_c1_1_755"
}
{
  "seqid": "NMDC:1781_100346_scf_28063_c1",
  "start": 0,
  "end": 273,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_28063_c1_1_273"
}
{
  "seqid": "NMDC:1781_100346_scf_28065_c1",
  "start": 0,
  "end": 310,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_28065_c1_1_310"
}
{
  "seqid": "NMDC:1781_100346_scf_2823_c1",
  "start": 0,
  "end": 825,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_2823_c1_1_825"
}
{
  "seqid": "NMDC:1781_100346_scf_28393_c1",
  "start": 51,
  "end": 281,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_28393_c1_52_281"
}
{
  "seqid": "NMDC:1781_100346_scf_28497_c1",
  "start": 0,
  "end": 218,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_28497_c1_1_218"
}
{
  "seqid": "NMDC:1781_100346_scf_28646_c1",
  "start": 37,
  "end": 113,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_28646_c1_38_113"
}
{
  "seqid": "NMDC:1781_100346_scf_28838_c1",
  "start": 128,
  "end": 308,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_28838_c1_129_308"
}
{
  "seqid": "NMDC:1781_100346_scf_28949_c1",
  "start": 0,
  "end": 291,
  "strand": "+",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_28949_c1_1_291"
}
{
  "seqid": "NMDC:1781_100346_scf_2898_c1",
  "start": 53,
  "end": 222,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_2898_c1_54_222"
}
{
  "seqid": "NMDC:1781_100346_scf_29166_c1",
  "start": 0,
  "end": 270,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_29166_c1_1_270"
}
{
  "seqid": "NMDC:1781_100346_scf_29371_c1",
  "start": 205,
  "end": 306,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_29371_c1_206_306"
}
{
  "seqid": "NMDC:1781_100346_scf_29648_c1",
  "start": 80,
  "end": 270,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_29648_c1_81_270"
}
{
  "seqid": "NMDC:1781_100346_scf_29737_c1",
  "start": 0,
  "end": 305,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_29737_c1_1_305"
}
{
  "seqid": "NMDC:1781_100346_scf_2997_c1",
  "start": 0,
  "end": 803,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_2997_c1_1_803"
}
{
  "seqid": "NMDC:1781_100346_scf_3025_c1",
  "start": 0,
  "end": 356,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_3025_c1_1_356"
}
{
  "seqid": "NMDC:1781_100346_scf_30653_c1",
  "start": 0,
  "end": 302,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_30653_c1_1_302"
}
{
  "seqid": "NMDC:1781_100346_scf_31124_c1",
  "start": 38,
  "end": 300,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_31124_c1_39_300"
}
{
  "seqid": "NMDC:1781_100346_scf_3179_c1",
  "start": 479,
  "end": 697,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_3179_c1_480_697"
}
{
  "seqid": "NMDC:1781_100346_scf_32172_c1",
  "start": 210,
  "end": 296,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_32172_c1_211_296"
}
{
  "seqid": "NMDC:1781_100346_scf_32361_c1",
  "start": 71,
  "end": 297,
  "strand": "",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_32361_c1_72_297"
}
{
  "seqid": "NMDC:1781_100346_scf_3245_c1",
  "start": 662,
  "end": 736,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_3245_c1_663_736"
}
{
  "seqid": "NMDC:1781_100346_scf_32581_c1",
  "start": 0,
  "end": 295,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_32581_c1_1_295"
}
{
  "seqid": "NMDC:1781_100346_scf_3258_c1",
  "start": 0,
  "end": 770,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_3258_c1_1_770"
}
{
  "seqid": "NMDC:1781_100346_scf_32711_c1",
  "start": 0,
  "end": 295,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_32711_c1_1_295"
}
{
  "seqid": "NMDC:1781_100346_scf_32923_c1",
  "start": 55,
  "end": 227,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_32923_c1_56_227"
}
{
  "seqid": "NMDC:1781_100346_scf_33038_c1",
  "start": 0,
  "end": 252,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_33038_c1_1_252"
}
{
  "seqid": "NMDC:1781_100346_scf_33130_c1",
  "start": 0,
  "end": 294,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_33130_c1_1_294"
}
{
  "seqid": "NMDC:1781_100346_scf_33692_c1",
  "start": 52,
  "end": 146,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_33692_c1_53_146"
}
{
  "seqid": "NMDC:1781_100346_scf_33909_c1",
  "start": 120,
  "end": 292,
  "strand": "+",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_33909_c1_121_292"
}
{
  "seqid": "NMDC:1781_100346_scf_33955_c1",
  "start": 0,
  "end": 292,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_33955_c1_1_292"
}
{
  "seqid": "NMDC:1781_100346_scf_34150_c1",
  "start": 172,
  "end": 291,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_34150_c1_173_291"
}
{
  "seqid": "NMDC:1781_100346_scf_34209_c1",
  "start": 41,
  "end": 220,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_34209_c1_42_220"
}
{
  "seqid": "NMDC:1781_100346_scf_34291_c1",
  "start": 216,
  "end": 291,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_34291_c1_217_291"
}
{
  "seqid": "NMDC:1781_100346_scf_34557_c1",
  "start": 0,
  "end": 124,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_34557_c1_1_124"
}
{
  "seqid": "NMDC:1781_100346_scf_34567_c1",
  "start": 2,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34567_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34568_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34568_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34569_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34569_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34570_c1",
  "start": 213,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34570_c1_214_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34571_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34571_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34572_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34572_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34573_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34573_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34574_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34574_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34575_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34575_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34576_c1",
  "start": 92,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34576_c1_93_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34577_c1",
  "start": 1,
  "end": 118,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34577_c1_2_118"
}
{
  "seqid": "NMDC:1781_100346_scf_34577_c1",
  "start": 125,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34577_c1_126_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34578_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34578_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34579_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34579_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34580_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34580_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34581_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34581_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34582_c1",
  "start": 3,
  "end": 138,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34582_c1_4_138"
}
{
  "seqid": "NMDC:1781_100346_scf_34583_c1",
  "start": 2,
  "end": 164,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34583_c1_3_164"
}
{
  "seqid": "NMDC:1781_100346_scf_34584_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34584_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34585_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34585_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34586_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34586_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34587_c1",
  "start": 2,
  "end": 215,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34587_c1_3_215"
}
{
  "seqid": "NMDC:1781_100346_scf_34588_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34588_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34589_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34589_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34590_c1",
  "start": 2,
  "end": 290,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34590_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34591_c1",
  "start": 53,
  "end": 290,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34591_c1_54_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34592_c1",
  "start": 29,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34592_c1_30_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34593_c1",
  "start": 2,
  "end": 290,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34593_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34594_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34594_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34595_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34595_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34596_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34596_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34597_c1",
  "start": 120,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34597_c1_121_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34598_c1",
  "start": 2,
  "end": 290,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34598_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34599_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34599_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34601_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34601_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34603_c1",
  "start": 2,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34603_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34604_c1",
  "start": 23,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34604_c1_24_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34605_c1",
  "start": 1,
  "end": 100,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34605_c1_2_100"
}
{
  "seqid": "NMDC:1781_100346_scf_34605_c1",
  "start": 138,
  "end": 273,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34605_c1_139_273"
}
{
  "seqid": "NMDC:1781_100346_scf_34606_c1",
  "start": 1,
  "end": 274,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34606_c1_2_274"
}
{
  "seqid": "NMDC:1781_100346_scf_34607_c1",
  "start": 1,
  "end": 103,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34607_c1_2_103"
}
{
  "seqid": "NMDC:1781_100346_scf_34607_c1",
  "start": 16,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34607_c1_17_283"
}
{
  "seqid": "NMDC:1781_100346_scf_34608_c1",
  "start": 7,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34608_c1_8_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34609_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34609_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34610_c1",
  "start": 1,
  "end": 172,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34610_c1_2_172"
}
{
  "seqid": "NMDC:1781_100346_scf_34612_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34612_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34613_c1",
  "start": 2,
  "end": 290,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34613_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34614_c1",
  "start": 88,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34614_c1_89_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34615_c1",
  "start": 54,
  "end": 285,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34615_c1_55_285"
}
{
  "seqid": "NMDC:1781_100346_scf_34616_c1",
  "start": 2,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34616_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34617_c1",
  "start": 2,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34617_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34618_c1",
  "start": 2,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34618_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34619_c1",
  "start": 1,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34619_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34620_c1",
  "start": 0,
  "end": 249,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34620_c1_1_249"
}
{
  "seqid": "NMDC:1781_100346_scf_34621_c1",
  "start": 0,
  "end": 267,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34621_c1_1_267"
}
{
  "seqid": "NMDC:1781_100346_scf_34622_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34622_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34623_c1",
  "start": 2,
  "end": 290,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34623_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34624_c1",
  "start": 11,
  "end": 233,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34624_c1_12_233"
}
{
  "seqid": "NMDC:1781_100346_scf_34625_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34625_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34626_c1",
  "start": 9,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34626_c1_10_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34627_c1",
  "start": 2,
  "end": 209,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34627_c1_3_209"
}
{
  "seqid": "NMDC:1781_100346_scf_34628_c1",
  "start": 2,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34628_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34629_c1",
  "start": 35,
  "end": 290,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34629_c1_36_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34630_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34630_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34631_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34631_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34632_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34632_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34633_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34633_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34634_c1",
  "start": 105,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34634_c1_106_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34635_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34635_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34636_c1",
  "start": 24,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34636_c1_25_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34637_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34637_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34638_c1",
  "start": 1,
  "end": 289,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34638_c1_2_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34639_c1",
  "start": 4,
  "end": 289,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34639_c1_5_289"
}
{
  "seqid": "NMDC:1781_100346_scf_34640_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34640_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34641_c1",
  "start": 2,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34641_c1_3_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34642_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34642_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34643_c1",
  "start": 11,
  "end": 290,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34643_c1_12_290"
}
{
  "seqid": "NMDC:1781_100346_scf_34644_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_34644_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_34653_c1",
  "start": 4,
  "end": 270,
  "strand": "",
  "type": "SO:0001459",
  "encodes": "NMDC:1781_100346_scf_34653_c1_5_270"
}
{
  "seqid": "NMDC:1781_100346_scf_3483_c1",
  "start": 139,
  "end": 256,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_3483_c1_140_256"
}
{
  "seqid": "NMDC:1781_100346_scf_34920_c1",
  "start": 169,
  "end": 274,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_34920_c1_170_274"
}
{
  "seqid": "NMDC:1781_100346_scf_35177_c1",
  "start": 6,
  "end": 84,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_35177_c1_7_84"
}
{
  "seqid": "NMDC:1781_100346_scf_3563_c1",
  "start": 244,
  "end": 443,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_3563_c1_245_443"
}
{
  "seqid": "NMDC:1781_100346_scf_35648_c1",
  "start": 0,
  "end": 289,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_35648_c1_1_289"
}
{
  "seqid": "NMDC:1781_100346_scf_3575_c1",
  "start": 0,
  "end": 734,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_3575_c1_1_734"
}
{
  "seqid": "NMDC:1781_100346_scf_365_c1",
  "start": 33,
  "end": 172,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_365_c1_34_172"
}
{
  "seqid": "NMDC:1781_100346_scf_36737_c1",
  "start": 0,
  "end": 152,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_36737_c1_1_152"
}
{
  "seqid": "NMDC:1781_100346_scf_36892_c1",
  "start": 0,
  "end": 288,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_36892_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_36915_c1",
  "start": 0,
  "end": 288,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_36915_c1_1_288"
}
{
  "seqid": "NMDC:1781_100346_scf_36965_c1",
  "start": 0,
  "end": 287,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_36965_c1_1_287"
}
{
  "seqid": "NMDC:1781_100346_scf_37006_c1",
  "start": 0,
  "end": 287,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_37006_c1_1_287"
}
{
  "seqid": "NMDC:1781_100346_scf_37588_c1",
  "start": 161,
  "end": 278,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_37588_c1_162_278"
}
{
  "seqid": "NMDC:1781_100346_scf_37646_c1",
  "start": 75,
  "end": 170,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_37646_c1_76_170"
}
{
  "seqid": "NMDC:1781_100346_scf_3780_c1",
  "start": 0,
  "end": 712,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_3780_c1_1_712"
}
{
  "seqid": "NMDC:1781_100346_scf_37942_c1",
  "start": 0,
  "end": 213,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_37942_c1_1_213"
}
{
  "seqid": "NMDC:1781_100346_scf_38089_c1",
  "start": 91,
  "end": 286,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_38089_c1_92_286"
}
{
  "seqid": "NMDC:1781_100346_scf_38128_c1",
  "start": 168,
  "end": 262,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_38128_c1_169_262"
}
{
  "seqid": "NMDC:1781_100346_scf_38190_c1",
  "start": 0,
  "end": 286,
  "strand": "",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_38190_c1_1_286"
}
{
  "seqid": "NMDC:1781_100346_scf_382_c1",
  "start": 2012,
  "end": 2149,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_382_c1_2013_2149"
}
{
  "seqid": "NMDC:1781_100346_scf_38610_c1",
  "start": 0,
  "end": 247,
  "strand": "",
  "type": "SO:0001459",
  "encodes": "NMDC:1781_100346_scf_38610_c1_1_247"
}
{
  "seqid": "NMDC:1781_100346_scf_38671_c1",
  "start": 0,
  "end": 133,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_38671_c1_1_133"
}
{
  "seqid": "NMDC:1781_100346_scf_38_c1",
  "start": 974,
  "end": 4368,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_38_c1_975_4368"
}
{
  "seqid": "NMDC:1781_100346_scf_38_c1",
  "start": 4604,
  "end": 4760,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_38_c1_4605_4760"
}
{
  "seqid": "NMDC:1781_100346_scf_38_c1",
  "start": 4980,
  "end": 5244,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_38_c1_4981_5244"
}
{
  "seqid": "NMDC:1781_100346_scf_39036_c1",
  "start": 25,
  "end": 100,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_39036_c1_26_100"
}
{
  "seqid": "NMDC:1781_100346_scf_39413_c1",
  "start": 151,
  "end": 277,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_39413_c1_152_277"
}
{
  "seqid": "NMDC:1781_100346_scf_39482_c1",
  "start": 199,
  "end": 285,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_39482_c1_200_285"
}
{
  "seqid": "NMDC:1781_100346_scf_39854_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39854_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39855_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39855_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39856_c1",
  "start": 67,
  "end": 172,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39856_c1_68_172"
}
{
  "seqid": "NMDC:1781_100346_scf_39857_c1",
  "start": 2,
  "end": 233,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39857_c1_3_233"
}
{
  "seqid": "NMDC:1781_100346_scf_39858_c1",
  "start": 60,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39858_c1_61_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39859_c1",
  "start": 20,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39859_c1_21_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39860_c1",
  "start": 126,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39860_c1_127_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39861_c1",
  "start": 2,
  "end": 281,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39861_c1_3_281"
}
{
  "seqid": "NMDC:1781_100346_scf_39862_c1",
  "start": 0,
  "end": 165,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39862_c1_1_165"
}
{
  "seqid": "NMDC:1781_100346_scf_39863_c1",
  "start": 1,
  "end": 271,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39863_c1_2_271"
}
{
  "seqid": "NMDC:1781_100346_scf_39864_c1",
  "start": 3,
  "end": 195,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39864_c1_4_195"
}
{
  "seqid": "NMDC:1781_100346_scf_39864_c1",
  "start": 191,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39864_c1_192_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39865_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39865_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39866_c1",
  "start": 0,
  "end": 264,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39866_c1_1_264"
}
{
  "seqid": "NMDC:1781_100346_scf_39867_c1",
  "start": 76,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39867_c1_77_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39868_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39868_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39869_c1",
  "start": 93,
  "end": 249,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39869_c1_94_249"
}
{
  "seqid": "NMDC:1781_100346_scf_39870_c1",
  "start": 2,
  "end": 83,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39870_c1_3_83"
}
{
  "seqid": "NMDC:1781_100346_scf_39870_c1",
  "start": 97,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39870_c1_98_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39871_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39871_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39872_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39872_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39873_c1",
  "start": 6,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39873_c1_7_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39874_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39874_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39875_c1",
  "start": 173,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39875_c1_174_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39876_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39876_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39877_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39877_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39878_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39878_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39879_c1",
  "start": 49,
  "end": 220,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39879_c1_50_220"
}
{
  "seqid": "NMDC:1781_100346_scf_39880_c1",
  "start": 2,
  "end": 263,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39880_c1_3_263"
}
{
  "seqid": "NMDC:1781_100346_scf_39881_c1",
  "start": 60,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39881_c1_61_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39882_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39882_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39883_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39883_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39884_c1",
  "start": 4,
  "end": 268,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39884_c1_5_268"
}
{
  "seqid": "NMDC:1781_100346_scf_39885_c1",
  "start": 0,
  "end": 261,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39885_c1_1_261"
}
{
  "seqid": "NMDC:1781_100346_scf_39886_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39886_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39887_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39887_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39888_c1",
  "start": 1,
  "end": 127,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39888_c1_2_127"
}
{
  "seqid": "NMDC:1781_100346_scf_39888_c1",
  "start": 123,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39888_c1_124_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39889_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39889_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39890_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39890_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39891_c1",
  "start": 1,
  "end": 268,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39891_c1_2_268"
}
{
  "seqid": "NMDC:1781_100346_scf_39892_c1",
  "start": 1,
  "end": 262,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39892_c1_2_262"
}
{
  "seqid": "NMDC:1781_100346_scf_39893_c1",
  "start": 0,
  "end": 207,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39893_c1_1_207"
}
{
  "seqid": "NMDC:1781_100346_scf_39893_c1",
  "start": 206,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39893_c1_207_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39894_c1",
  "start": 0,
  "end": 252,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39894_c1_1_252"
}
{
  "seqid": "NMDC:1781_100346_scf_39895_c1",
  "start": 1,
  "end": 271,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39895_c1_2_271"
}
{
  "seqid": "NMDC:1781_100346_scf_39896_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39896_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39897_c1",
  "start": 27,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39897_c1_28_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39898_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39898_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39899_c1",
  "start": 2,
  "end": 119,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39899_c1_3_119"
}
{
  "seqid": "NMDC:1781_100346_scf_39899_c1",
  "start": 171,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39899_c1_172_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39900_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39900_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39901_c1",
  "start": 0,
  "end": 102,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39901_c1_1_102"
}
{
  "seqid": "NMDC:1781_100346_scf_39901_c1",
  "start": 12,
  "end": 102,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39901_c1_13_102"
}
{
  "seqid": "NMDC:1781_100346_scf_39901_c1",
  "start": 98,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39901_c1_99_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39902_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39902_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39903_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39903_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39904_c1",
  "start": 1,
  "end": 181,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39904_c1_2_181"
}
{
  "seqid": "NMDC:1781_100346_scf_39904_c1",
  "start": 177,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39904_c1_178_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39905_c1",
  "start": 129,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39905_c1_130_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39906_c1",
  "start": 55,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39906_c1_56_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39907_c1",
  "start": 2,
  "end": 203,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39907_c1_3_203"
}
{
  "seqid": "NMDC:1781_100346_scf_39908_c1",
  "start": 2,
  "end": 185,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39908_c1_3_185"
}
{
  "seqid": "NMDC:1781_100346_scf_39909_c1",
  "start": 2,
  "end": 239,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39909_c1_3_239"
}
{
  "seqid": "NMDC:1781_100346_scf_39910_c1",
  "start": 9,
  "end": 165,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39910_c1_10_165"
}
{
  "seqid": "NMDC:1781_100346_scf_39910_c1",
  "start": 164,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39910_c1_165_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39911_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39911_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39912_c1",
  "start": 7,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39912_c1_8_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39913_c1",
  "start": 64,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39913_c1_65_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39914_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39914_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39915_c1",
  "start": 15,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39915_c1_16_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39916_c1",
  "start": 24,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39916_c1_25_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39917_c1",
  "start": 14,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39917_c1_15_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39918_c1",
  "start": 1,
  "end": 238,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39918_c1_2_238"
}
{
  "seqid": "NMDC:1781_100346_scf_39919_c1",
  "start": 2,
  "end": 269,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39919_c1_3_269"
}
{
  "seqid": "NMDC:1781_100346_scf_39920_c1",
  "start": 2,
  "end": 281,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39920_c1_3_281"
}
{
  "seqid": "NMDC:1781_100346_scf_39921_c1",
  "start": 2,
  "end": 221,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39921_c1_3_221"
}
{
  "seqid": "NMDC:1781_100346_scf_39922_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39922_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39923_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39923_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39924_c1",
  "start": 28,
  "end": 277,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39924_c1_29_277"
}
{
  "seqid": "NMDC:1781_100346_scf_39925_c1",
  "start": 17,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39925_c1_18_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39926_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39926_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39927_c1",
  "start": 68,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39927_c1_69_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39928_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39928_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39929_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39929_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39930_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39930_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39931_c1",
  "start": 3,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39931_c1_4_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39932_c1",
  "start": 11,
  "end": 236,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39932_c1_12_236"
}
{
  "seqid": "NMDC:1781_100346_scf_39932_c1",
  "start": 199,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39932_c1_200_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39933_c1",
  "start": 1,
  "end": 268,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39933_c1_2_268"
}
{
  "seqid": "NMDC:1781_100346_scf_39934_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39934_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39935_c1",
  "start": 2,
  "end": 119,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39935_c1_3_119"
}
{
  "seqid": "NMDC:1781_100346_scf_39936_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39936_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39937_c1",
  "start": 12,
  "end": 255,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39937_c1_13_255"
}
{
  "seqid": "NMDC:1781_100346_scf_39938_c1",
  "start": 158,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39938_c1_159_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39939_c1",
  "start": 10,
  "end": 136,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39939_c1_11_136"
}
{
  "seqid": "NMDC:1781_100346_scf_39939_c1",
  "start": 139,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39939_c1_140_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39940_c1",
  "start": 37,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39940_c1_38_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39941_c1",
  "start": 11,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39941_c1_12_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39942_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39942_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39943_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39943_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39944_c1",
  "start": 124,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39944_c1_125_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39945_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39945_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39946_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39946_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39947_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39947_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39948_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39948_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39949_c1",
  "start": 54,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39949_c1_55_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39950_c1",
  "start": 1,
  "end": 238,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39950_c1_2_238"
}
{
  "seqid": "NMDC:1781_100346_scf_39951_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39951_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39952_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39952_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39953_c1",
  "start": 0,
  "end": 105,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39953_c1_1_105"
}
{
  "seqid": "NMDC:1781_100346_scf_39954_c1",
  "start": 33,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39954_c1_34_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39955_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39955_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39956_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39956_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39957_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39957_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39958_c1",
  "start": 0,
  "end": 90,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39958_c1_1_90"
}
{
  "seqid": "NMDC:1781_100346_scf_39958_c1",
  "start": 95,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39958_c1_96_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39959_c1",
  "start": 35,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39959_c1_36_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39960_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39960_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39961_c1",
  "start": 2,
  "end": 278,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39961_c1_3_278"
}
{
  "seqid": "NMDC:1781_100346_scf_39962_c1",
  "start": 94,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39962_c1_95_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39963_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39963_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39964_c1",
  "start": 18,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39964_c1_19_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39965_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39965_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39966_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39966_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39967_c1",
  "start": 2,
  "end": 80,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39967_c1_3_80"
}
{
  "seqid": "NMDC:1781_100346_scf_39967_c1",
  "start": 86,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39967_c1_87_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39968_c1",
  "start": 0,
  "end": 168,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39968_c1_1_168"
}
{
  "seqid": "NMDC:1781_100346_scf_39968_c1",
  "start": 184,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39968_c1_185_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39969_c1",
  "start": 21,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39969_c1_22_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39970_c1",
  "start": 2,
  "end": 266,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39970_c1_3_266"
}
{
  "seqid": "NMDC:1781_100346_scf_39971_c1",
  "start": 1,
  "end": 226,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39971_c1_2_226"
}
{
  "seqid": "NMDC:1781_100346_scf_39972_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39972_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39973_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39973_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39974_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39974_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39975_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39975_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39976_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39976_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39977_c1",
  "start": 0,
  "end": 240,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39977_c1_1_240"
}
{
  "seqid": "NMDC:1781_100346_scf_39978_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39978_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39979_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39979_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39980_c1",
  "start": 0,
  "end": 216,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39980_c1_1_216"
}
{
  "seqid": "NMDC:1781_100346_scf_39981_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39981_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39982_c1",
  "start": 1,
  "end": 265,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39982_c1_2_265"
}
{
  "seqid": "NMDC:1781_100346_scf_39983_c1",
  "start": 0,
  "end": 195,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39983_c1_1_195"
}
{
  "seqid": "NMDC:1781_100346_scf_39984_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39984_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39985_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39985_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39986_c1",
  "start": 101,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39986_c1_102_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39987_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39987_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39988_c1",
  "start": 0,
  "end": 267,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39988_c1_1_267"
}
{
  "seqid": "NMDC:1781_100346_scf_39989_c1",
  "start": 84,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39989_c1_85_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39990_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39990_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39991_c1",
  "start": 0,
  "end": 267,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39991_c1_1_267"
}
{
  "seqid": "NMDC:1781_100346_scf_39992_c1",
  "start": 29,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39992_c1_30_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39993_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39993_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_39995_c1",
  "start": 1,
  "end": 253,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39995_c1_2_253"
}
{
  "seqid": "NMDC:1781_100346_scf_39996_c1",
  "start": 33,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39996_c1_34_282"
}
{
  "seqid": "NMDC:1781_100346_scf_39997_c1",
  "start": 21,
  "end": 243,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39997_c1_22_243"
}
{
  "seqid": "NMDC:1781_100346_scf_39998_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39998_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_39999_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_39999_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40000_c1",
  "start": 105,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40000_c1_106_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40001_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40001_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40002_c1",
  "start": 1,
  "end": 139,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40002_c1_2_139"
}
{
  "seqid": "NMDC:1781_100346_scf_40002_c1",
  "start": 139,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40002_c1_140_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40003_c1",
  "start": 2,
  "end": 218,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40003_c1_3_218"
}
{
  "seqid": "NMDC:1781_100346_scf_40004_c1",
  "start": 96,
  "end": 222,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40004_c1_97_222"
}
{
  "seqid": "NMDC:1781_100346_scf_40005_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40005_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40006_c1",
  "start": 0,
  "end": 237,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40006_c1_1_237"
}
{
  "seqid": "NMDC:1781_100346_scf_40007_c1",
  "start": 2,
  "end": 275,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40007_c1_3_275"
}
{
  "seqid": "NMDC:1781_100346_scf_40008_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40008_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40009_c1",
  "start": 2,
  "end": 212,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40009_c1_3_212"
}
{
  "seqid": "NMDC:1781_100346_scf_40010_c1",
  "start": 76,
  "end": 187,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40010_c1_77_187"
}
{
  "seqid": "NMDC:1781_100346_scf_40010_c1",
  "start": 186,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40010_c1_187_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40011_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40011_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40012_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40012_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40014_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40014_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40015_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40015_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40016_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40016_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40017_c1",
  "start": 1,
  "end": 280,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40017_c1_2_280"
}
{
  "seqid": "NMDC:1781_100346_scf_40018_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40018_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40019_c1",
  "start": 15,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40019_c1_16_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40020_c1",
  "start": 1,
  "end": 244,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40020_c1_2_244"
}
{
  "seqid": "NMDC:1781_100346_scf_40021_c1",
  "start": 1,
  "end": 193,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40021_c1_2_193"
}
{
  "seqid": "NMDC:1781_100346_scf_40022_c1",
  "start": 12,
  "end": 279,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40022_c1_13_279"
}
{
  "seqid": "NMDC:1781_100346_scf_40023_c1",
  "start": 162,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40023_c1_163_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40024_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40024_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40025_c1",
  "start": 1,
  "end": 274,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40025_c1_2_274"
}
{
  "seqid": "NMDC:1781_100346_scf_40026_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40026_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40027_c1",
  "start": 1,
  "end": 163,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40027_c1_2_163"
}
{
  "seqid": "NMDC:1781_100346_scf_40028_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40028_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40029_c1",
  "start": 1,
  "end": 268,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40029_c1_2_268"
}
{
  "seqid": "NMDC:1781_100346_scf_40030_c1",
  "start": 2,
  "end": 221,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40030_c1_3_221"
}
{
  "seqid": "NMDC:1781_100346_scf_40031_c1",
  "start": 10,
  "end": 241,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40031_c1_11_241"
}
{
  "seqid": "NMDC:1781_100346_scf_40032_c1",
  "start": 28,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40032_c1_29_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40033_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40033_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40034_c1",
  "start": 28,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40034_c1_29_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40035_c1",
  "start": 2,
  "end": 215,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40035_c1_3_215"
}
{
  "seqid": "NMDC:1781_100346_scf_40036_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40036_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40037_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40037_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40038_c1",
  "start": 2,
  "end": 101,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40038_c1_3_101"
}
{
  "seqid": "NMDC:1781_100346_scf_40039_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40039_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40040_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40040_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40041_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40041_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40042_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40042_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40043_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40043_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40044_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40044_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40045_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40045_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40046_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40046_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40047_c1",
  "start": 0,
  "end": 117,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40047_c1_1_117"
}
{
  "seqid": "NMDC:1781_100346_scf_40048_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40048_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40049_c1",
  "start": 2,
  "end": 134,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40049_c1_3_134"
}
{
  "seqid": "NMDC:1781_100346_scf_40049_c1",
  "start": 133,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40049_c1_134_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40050_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40050_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40051_c1",
  "start": 35,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40051_c1_36_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40052_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40052_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40053_c1",
  "start": 59,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40053_c1_60_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40054_c1",
  "start": 17,
  "end": 257,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40054_c1_18_257"
}
{
  "seqid": "NMDC:1781_100346_scf_40055_c1",
  "start": 0,
  "end": 213,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40055_c1_1_213"
}
{
  "seqid": "NMDC:1781_100346_scf_40056_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40056_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40057_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40057_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40058_c1",
  "start": 1,
  "end": 274,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40058_c1_2_274"
}
{
  "seqid": "NMDC:1781_100346_scf_40059_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40059_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40061_c1",
  "start": 2,
  "end": 275,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40061_c1_3_275"
}
{
  "seqid": "NMDC:1781_100346_scf_40062_c1",
  "start": 50,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40062_c1_51_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40063_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40063_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40064_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40064_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40065_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40065_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40066_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40066_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40067_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40067_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40068_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40068_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40069_c1",
  "start": 150,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40069_c1_151_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40070_c1",
  "start": 4,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40070_c1_5_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40071_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40071_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40072_c1",
  "start": 20,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40072_c1_21_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40073_c1",
  "start": 38,
  "end": 227,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40073_c1_39_227"
}
{
  "seqid": "NMDC:1781_100346_scf_40074_c1",
  "start": 2,
  "end": 179,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40074_c1_3_179"
}
{
  "seqid": "NMDC:1781_100346_scf_40074_c1",
  "start": 204,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40074_c1_205_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40075_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40075_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40076_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40076_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40077_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40077_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40078_c1",
  "start": 31,
  "end": 163,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40078_c1_32_163"
}
{
  "seqid": "NMDC:1781_100346_scf_40078_c1",
  "start": 159,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40078_c1_160_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40079_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40079_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40080_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40080_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40081_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40081_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40082_c1",
  "start": 82,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40082_c1_83_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40083_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40083_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40084_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40084_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40085_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40085_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40086_c1",
  "start": 2,
  "end": 119,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40086_c1_3_119"
}
{
  "seqid": "NMDC:1781_100346_scf_40087_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40087_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40088_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40088_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40089_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40089_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40090_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40090_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40091_c1",
  "start": 119,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40091_c1_120_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40092_c1",
  "start": 201,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40092_c1_202_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40093_c1",
  "start": 62,
  "end": 203,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40093_c1_63_203"
}
{
  "seqid": "NMDC:1781_100346_scf_40094_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40094_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40095_c1",
  "start": 5,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40095_c1_6_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40096_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40096_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40097_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40097_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40098_c1",
  "start": 2,
  "end": 257,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40098_c1_3_257"
}
{
  "seqid": "NMDC:1781_100346_scf_40099_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40099_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40100_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40100_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40101_c1",
  "start": 57,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40101_c1_58_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40102_c1",
  "start": 0,
  "end": 219,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40102_c1_1_219"
}
{
  "seqid": "NMDC:1781_100346_scf_40103_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40103_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40104_c1",
  "start": 2,
  "end": 269,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40104_c1_3_269"
}
{
  "seqid": "NMDC:1781_100346_scf_40105_c1",
  "start": 22,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40105_c1_23_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40106_c1",
  "start": 1,
  "end": 271,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40106_c1_2_271"
}
{
  "seqid": "NMDC:1781_100346_scf_40107_c1",
  "start": 76,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40107_c1_77_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40108_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40108_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40109_c1",
  "start": 20,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40109_c1_21_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40110_c1",
  "start": 185,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40110_c1_186_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40111_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40111_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40112_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40112_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40113_c1",
  "start": 28,
  "end": 232,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40113_c1_29_232"
}
{
  "seqid": "NMDC:1781_100346_scf_40114_c1",
  "start": 1,
  "end": 259,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40114_c1_2_259"
}
{
  "seqid": "NMDC:1781_100346_scf_40115_c1",
  "start": 1,
  "end": 235,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40115_c1_2_235"
}
{
  "seqid": "NMDC:1781_100346_scf_40116_c1",
  "start": 1,
  "end": 283,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40116_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40117_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40117_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40118_c1",
  "start": 1,
  "end": 283,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40118_c1_2_283"
}
{
  "seqid": "NMDC:1781_100346_scf_40119_c1",
  "start": 6,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40119_c1_7_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40120_c1",
  "start": 2,
  "end": 149,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40120_c1_3_149"
}
{
  "seqid": "NMDC:1781_100346_scf_40120_c1",
  "start": 160,
  "end": 274,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40120_c1_161_274"
}
{
  "seqid": "NMDC:1781_100346_scf_40121_c1",
  "start": 11,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40121_c1_12_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40122_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40122_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40123_c1",
  "start": 2,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40123_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40124_c1",
  "start": 45,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40124_c1_46_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40125_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40125_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40126_c1",
  "start": 0,
  "end": 279,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40126_c1_1_279"
}
{
  "seqid": "NMDC:1781_100346_scf_40127_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40127_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40128_c1",
  "start": 2,
  "end": 281,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40128_c1_3_281"
}
{
  "seqid": "NMDC:1781_100346_scf_40129_c1",
  "start": 21,
  "end": 282,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40129_c1_22_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40130_c1",
  "start": 14,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40130_c1_15_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40131_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40131_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40132_c1",
  "start": 1,
  "end": 238,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40132_c1_2_238"
}
{
  "seqid": "NMDC:1781_100346_scf_40133_c1",
  "start": 2,
  "end": 284,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40133_c1_3_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40134_c1",
  "start": 0,
  "end": 282,
  "strand": "",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40134_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_40135_c1",
  "start": 164,
  "end": 284,
  "strand": "+",
  "type": "SO:0000316",
  "encodes": "NMDC:1781_100346_scf_40135_c1_165_284"
}
{
  "seqid": "NMDC:1781_100346_scf_40540_c1",
  "start": 0,
  "end": 284,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_40540_c1_1_284"
}
{
  "seqid": "NMDC:1781_100346_scf_4055_c1",
  "start": 0,
  "end": 689,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_4055_c1_1_689"
}
{
  "seqid": "NMDC:1781_100346_scf_4080_c1",
  "start": 0,
  "end": 687,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_4080_c1_1_687"
}
{
  "seqid": "NMDC:1781_100346_scf_41031_c1",
  "start": 214,
  "end": 282,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_41031_c1_215_282"
}
{
  "seqid": "NMDC:1781_100346_scf_410_c1",
  "start": 354,
  "end": 2135,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_410_c1_355_2135"
}
{
  "seqid": "NMDC:1781_100346_scf_41114_c1",
  "start": 134,
  "end": 283,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_41114_c1_135_283"
}
{
  "seqid": "NMDC:1781_100346_scf_41486_c1",
  "start": 0,
  "end": 283,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_41486_c1_1_283"
}
{
  "seqid": "NMDC:1781_100346_scf_41754_c1",
  "start": 0,
  "end": 282,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_41754_c1_1_282"
}
{
  "seqid": "NMDC:1781_100346_scf_41942_c1",
  "start": 25,
  "end": 130,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_41942_c1_26_130"
}
{
  "seqid": "NMDC:1781_100346_scf_42131_c1",
  "start": 3,
  "end": 263,
  "strand": "",
  "type": "SO:0001459",
  "encodes": "NMDC:1781_100346_scf_42131_c1_4_263"
}
{
  "seqid": "NMDC:1781_100346_scf_4218_c1",
  "start": 23,
  "end": 149,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_4218_c1_24_149"
}
{
  "seqid": "NMDC:1781_100346_scf_42538_c1",
  "start": 42,
  "end": 156,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_42538_c1_43_156"
}
{
  "seqid": "NMDC:1781_100346_scf_42662_c1",
  "start": 0,
  "end": 281,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_42662_c1_1_281"
}
{
  "seqid": "NMDC:1781_100346_scf_42712_c1",
  "start": 131,
  "end": 281,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_42712_c1_132_281"
}
{
  "seqid": "NMDC:1781_100346_scf_42773_c1",
  "start": 125,
  "end": 254,
  "strand": "",
  "type": "SO:0001459",
  "encodes": "NMDC:1781_100346_scf_42773_c1_126_254"
}
{
  "seqid": "NMDC:1781_100346_scf_4292_c1",
  "start": 350,
  "end": 476,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_4292_c1_351_476"
}
{
  "seqid": "NMDC:1781_100346_scf_43410_c1",
  "start": 0,
  "end": 280,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_43410_c1_1_280"
}
{
  "seqid": "NMDC:1781_100346_scf_43456_c1",
  "start": 0,
  "end": 176,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_43456_c1_1_176"
}
{
  "seqid": "NMDC:1781_100346_scf_43800_c1",
  "start": 170,
  "end": 280,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_43800_c1_171_280"
}
{
  "seqid": "NMDC:1781_100346_scf_43870_c1",
  "start": 0,
  "end": 162,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_43870_c1_1_162"
}
{
  "seqid": "NMDC:1781_100346_scf_44014_c1",
  "start": 0,
  "end": 280,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_44014_c1_1_280"
}
{
  "seqid": "NMDC:1781_100346_scf_44194_c1",
  "start": 0,
  "end": 279,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_44194_c1_1_279"
}
{
  "seqid": "NMDC:1781_100346_scf_45125_c1",
  "start": 0,
  "end": 181,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_45125_c1_1_181"
}
{
  "seqid": "NMDC:1781_100346_scf_45339_c1",
  "start": 99,
  "end": 278,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_45339_c1_100_278"
}
{
  "seqid": "NMDC:1781_100346_scf_4538_c1",
  "start": 0,
  "end": 609,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_4538_c1_1_609"
}
{
  "seqid": "NMDC:1781_100346_scf_45800_c1",
  "start": 55,
  "end": 135,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_45800_c1_56_135"
}
{
  "seqid": "NMDC:1781_100346_scf_46101_c1",
  "start": 0,
  "end": 256,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_46101_c1_1_256"
}
{
  "seqid": "NMDC:1781_100346_scf_4611_c1",
  "start": 0,
  "end": 151,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_4611_c1_1_151"
}
{
  "seqid": "NMDC:1781_100346_scf_4726_c1",
  "start": 11,
  "end": 87,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_4726_c1_12_87"
}
{
  "seqid": "NMDC:1781_100346_scf_4819_c1",
  "start": 449,
  "end": 526,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_4819_c1_450_526"
}
{
  "seqid": "NMDC:1781_100346_scf_4859_c1",
  "start": 52,
  "end": 629,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_4859_c1_53_629"
}
{
  "seqid": "NMDC:1781_100346_scf_4877_c1",
  "start": 0,
  "end": 628,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_4877_c1_1_628"
}
{
  "seqid": "NMDC:1781_100346_scf_4890_c1",
  "start": 33,
  "end": 244,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_4890_c1_34_244"
}
{
  "seqid": "NMDC:1781_100346_scf_5017_c1",
  "start": 0,
  "end": 619,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_5017_c1_1_619"
}
{
  "seqid": "NMDC:1781_100346_scf_5108_c1",
  "start": 256,
  "end": 335,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5108_c1_257_335"
}
{
  "seqid": "NMDC:1781_100346_scf_5114_c1",
  "start": 0,
  "end": 614,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_5114_c1_1_614"
}
{
  "seqid": "NMDC:1781_100346_scf_5192_c1",
  "start": 52,
  "end": 405,
  "strand": "+",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_5192_c1_53_405"
}
{
  "seqid": "NMDC:1781_100346_scf_5200_c1",
  "start": 453,
  "end": 610,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5200_c1_454_610"
}
{
  "seqid": "NMDC:1781_100346_scf_5214_c1",
  "start": 359,
  "end": 602,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5214_c1_360_602"
}
{
  "seqid": "NMDC:1781_100346_scf_5324_c1",
  "start": 106,
  "end": 182,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5324_c1_107_182"
}
{
  "seqid": "NMDC:1781_100346_scf_5485_c1",
  "start": 71,
  "end": 148,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5485_c1_72_148"
}
{
  "seqid": "NMDC:1781_100346_scf_550_c1",
  "start": 0,
  "end": 1431,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_550_c1_1_1431"
}
{
  "seqid": "NMDC:1781_100346_scf_5569_c1",
  "start": 247,
  "end": 367,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5569_c1_248_367"
}
{
  "seqid": "NMDC:1781_100346_scf_5622_c1",
  "start": 273,
  "end": 347,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5622_c1_274_347"
}
{
  "seqid": "NMDC:1781_100346_scf_5662_c1",
  "start": 16,
  "end": 586,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_5662_c1_17_586"
}
{
  "seqid": "NMDC:1781_100346_scf_571_c1",
  "start": 1678,
  "end": 1798,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_571_c1_1679_1798"
}
{
  "seqid": "NMDC:1781_100346_scf_5726_c1",
  "start": 59,
  "end": 298,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5726_c1_60_298"
}
{
  "seqid": "NMDC:1781_100346_scf_5805_c1",
  "start": 301,
  "end": 579,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_5805_c1_302_579"
}
{
  "seqid": "NMDC:1781_100346_scf_58_c1",
  "start": 1909,
  "end": 2220,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_58_c1_1910_2220"
}
{
  "seqid": "NMDC:1781_100346_scf_5959_c1",
  "start": 0,
  "end": 572,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_5959_c1_1_572"
}
{
  "seqid": "NMDC:1781_100346_scf_5982_c1",
  "start": 0,
  "end": 571,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_5982_c1_1_571"
}
{
  "seqid": "NMDC:1781_100346_scf_6085_c1",
  "start": 11,
  "end": 87,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_6085_c1_12_87"
}
{
  "seqid": "NMDC:1781_100346_scf_6283_c1",
  "start": 47,
  "end": 124,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_6283_c1_48_124"
}
{
  "seqid": "NMDC:1781_100346_scf_6309_c1",
  "start": 242,
  "end": 390,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_6309_c1_243_390"
}
{
  "seqid": "NMDC:1781_100346_scf_6443_c1",
  "start": 0,
  "end": 554,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_6443_c1_1_554"
}
{
  "seqid": "NMDC:1781_100346_scf_6458_c1",
  "start": 0,
  "end": 553,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_6458_c1_1_553"
}
{
  "seqid": "NMDC:1781_100346_scf_6504_c1",
  "start": 0,
  "end": 551,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_6504_c1_1_551"
}
{
  "seqid": "NMDC:1781_100346_scf_6536_c1",
  "start": 0,
  "end": 549,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_6536_c1_1_549"
}
{
  "seqid": "NMDC:1781_100346_scf_6625_c1",
  "start": 0,
  "end": 83,
  "strand": "",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_6625_c1_1_83"
}
{
  "seqid": "NMDC:1781_100346_scf_676_c1",
  "start": 0,
  "end": 1399,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_676_c1_1_1399"
}
{
  "seqid": "NMDC:1781_100346_scf_676_c1",
  "start": 1455,
  "end": 1574,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_676_c1_1456_1574"
}
{
  "seqid": "NMDC:1781_100346_scf_6778_c1",
  "start": 57,
  "end": 150,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_6778_c1_58_150"
}
{
  "seqid": "NMDC:1781_100346_scf_6867_c1",
  "start": 0,
  "end": 537,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_6867_c1_1_537"
}
{
  "seqid": "NMDC:1781_100346_scf_6880_c1",
  "start": 0,
  "end": 536,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_6880_c1_1_536"
}
{
  "seqid": "NMDC:1781_100346_scf_6900_c1",
  "start": 10,
  "end": 104,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_6900_c1_11_104"
}
{
  "seqid": "NMDC:1781_100346_scf_6938_c1",
  "start": 0,
  "end": 534,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_6938_c1_1_534"
}
{
  "seqid": "NMDC:1781_100346_scf_7310_c1",
  "start": 457,
  "end": 521,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_7310_c1_458_521"
}
{
  "seqid": "NMDC:1781_100346_scf_7490_c1",
  "start": 0,
  "end": 374,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7490_c1_1_374"
}
{
  "seqid": "NMDC:1781_100346_scf_7570_c1",
  "start": 0,
  "end": 285,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7570_c1_1_285"
}
{
  "seqid": "NMDC:1781_100346_scf_7596_c1",
  "start": 0,
  "end": 257,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7596_c1_1_257"
}
{
  "seqid": "NMDC:1781_100346_scf_7628_c1",
  "start": 165,
  "end": 511,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7628_c1_166_511"
}
{
  "seqid": "NMDC:1781_100346_scf_7785_c1",
  "start": 0,
  "end": 506,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7785_c1_1_506"
}
{
  "seqid": "NMDC:1781_100346_scf_7815_c1",
  "start": 172,
  "end": 505,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7815_c1_173_505"
}
{
  "seqid": "NMDC:1781_100346_scf_7930_c1",
  "start": 0,
  "end": 501,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7930_c1_1_501"
}
{
  "seqid": "NMDC:1781_100346_scf_7961_c1",
  "start": 418,
  "end": 494,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_7961_c1_419_494"
}
{
  "seqid": "NMDC:1781_100346_scf_7963_c1",
  "start": 345,
  "end": 464,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_7963_c1_346_464"
}
{
  "seqid": "NMDC:1781_100346_scf_7972_c1",
  "start": 3,
  "end": 198,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_7972_c1_4_198"
}
{
  "seqid": "NMDC:1781_100346_scf_7990_c1",
  "start": 320,
  "end": 500,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_7990_c1_321_500"
}
{
  "seqid": "NMDC:1781_100346_scf_8130_c1",
  "start": 0,
  "end": 496,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_8130_c1_1_496"
}
{
  "seqid": "NMDC:1781_100346_scf_8165_c1",
  "start": 57,
  "end": 174,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_8165_c1_58_174"
}
{
  "seqid": "NMDC:1781_100346_scf_8165_c1",
  "start": 298,
  "end": 496,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_8165_c1_299_496"
}
{
  "seqid": "NMDC:1781_100346_scf_8401_c1",
  "start": 0,
  "end": 489,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_8401_c1_1_489"
}
{
  "seqid": "NMDC:1781_100346_scf_8434_c1",
  "start": 0,
  "end": 456,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_8434_c1_1_456"
}
{
  "seqid": "NMDC:1781_100346_scf_8502_c1",
  "start": 138,
  "end": 252,
  "strand": "+",
  "type": null,
  "encodes": "NMDC:1781_100346_scf_8502_c1_139_252"
}
{
  "seqid": "NMDC:1781_100346_scf_8605_c1",
  "start": 197,
  "end": 484,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_8605_c1_198_484"
}
{
  "seqid": "NMDC:1781_100346_scf_8650_c1",
  "start": 0,
  "end": 168,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_8650_c1_1_168"
}
{
  "seqid": "NMDC:1781_100346_scf_8749_c1",
  "start": 177,
  "end": 321,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_8749_c1_178_321"
}
{
  "seqid": "NMDC:1781_100346_scf_9171_c1",
  "start": 0,
  "end": 471,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9171_c1_1_471"
}
{
  "seqid": "NMDC:1781_100346_scf_9183_c1",
  "start": 55,
  "end": 173,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_9183_c1_56_173"
}
{
  "seqid": "NMDC:1781_100346_scf_918_c1",
  "start": 0,
  "end": 1270,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_918_c1_1_1270"
}
{
  "seqid": "NMDC:1781_100346_scf_9191_c1",
  "start": 0,
  "end": 471,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9191_c1_1_471"
}
{
  "seqid": "NMDC:1781_100346_scf_9199_c1",
  "start": 0,
  "end": 198,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_9199_c1_1_198"
}
{
  "seqid": "NMDC:1781_100346_scf_9413_c1",
  "start": 230,
  "end": 347,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9413_c1_231_347"
}
{
  "seqid": "NMDC:1781_100346_scf_9430_c1",
  "start": 0,
  "end": 110,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_9430_c1_1_110"
}
{
  "seqid": "NMDC:1781_100346_scf_9430_c1",
  "start": 166,
  "end": 258,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_9430_c1_167_258"
}
{
  "seqid": "NMDC:1781_100346_scf_9465_c1",
  "start": 0,
  "end": 465,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9465_c1_1_465"
}
{
  "seqid": "NMDC:1781_100346_scf_947_c1",
  "start": 950,
  "end": 1363,
  "strand": "",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_947_c1_951_1363"
}
{
  "seqid": "NMDC:1781_100346_scf_9507_c1",
  "start": 0,
  "end": 464,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9507_c1_1_464"
}
{
  "seqid": "NMDC:1781_100346_scf_9721_c1",
  "start": 0,
  "end": 459,
  "strand": "",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9721_c1_1_459"
}
{
  "seqid": "NMDC:1781_100346_scf_9744_c1",
  "start": 77,
  "end": 329,
  "strand": "+",
  "type": "SO:0000655",
  "encodes": "NMDC:1781_100346_scf_9744_c1_78_329"
}
{
  "seqid": "NMDC:1781_100346_scf_9773_c1",
  "start": 0,
  "end": 458,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9773_c1_1_458"
}
{
  "seqid": "NMDC:1781_100346_scf_9817_c1",
  "start": 32,
  "end": 389,
  "strand": "+",
  "type": "SO:0000584",
  "encodes": "NMDC:1781_100346_scf_9817_c1_33_389"
}
{
  "seqid": "NMDC:1781_100346_scf_9987_c1",
  "start": 0,
  "end": 454,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9987_c1_1_454"
}
{
  "seqid": "NMDC:1781_100346_scf_9996_c1",
  "start": 0,
  "end": 454,
  "strand": "+",
  "type": "SO:0000252",
  "encodes": "NMDC:1781_100346_scf_9996_c1_1_454"
}
'''
"""Module of example data.

See Also
--------
pyranges.random : generate random PyRanges

Examples
--------
>>> pr.example_data.f1
Chromosome      Start      End  Name         Score  Strand
category        int64    int64  object       int64  category
------------  -------  -------  ---------  -------  ----------
chr1                3        6  interval1        0  +
chr1                5        7  interval2        0  -
chr1                8        9  interval3        0  +
PyRanges with 3 rows and 6 columns.
Contains 1 chromosomes and 2 strands.

"""
import tempfile
from functools import cached_property
from importlib.resources import files
from pathlib import Path
from typing import ClassVar

import pyranges as pr
from pyranges.pyranges_main import PyRanges


class ExampleData:
    """"""

    _files: ClassVar[dict[str, Path]] = {}

    @classmethod
    @property
    def files(cls: "ExampleData") -> dict[str, Path]:
        """Return a dict of the basenames to full paths of the example data in the project.

        Examples
        --------
        >>> bam = ExampleData.files["smaller.bam"]
        >>> bam.exists()
        True
        >>> import importlib
        >>> bam == importlib.resources.files().joinpath("data/smaller.bam")
        True
        """
        if cls._files:
            return cls._files
        cls._files = {f.name: f for f in files("pyranges").joinpath("data").iterdir() if "__" not in f.name}
        return cls._files

    @staticmethod
    def _read_bed_from_string(contents: str) -> "PyRanges":
        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as f:
            f.write(contents)
            f.flush()
            return pr.read_bed(f.name)

    @staticmethod
    def _read_gtf_from_string(contents: str) -> "PyRanges":
        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as f:
            f.write(contents)
            f.flush()
            return pr.read_gtf(f.name)

    @cached_property
    def chipseq(self) -> "pr.PyRanges":
        contents = """chr8	28510032	28510057	U0	0	-
chr7	107153363	107153388	U0	0	-
chr5	135821802	135821827	U0	0	-
chr14	19418999	19419024	U0	0	-
chr12	106679761	106679786	U0	0	-
chr21	40099618	40099643	U0	0	+
chr8	22714402	22714427	U0	0	-
chr19	19571102	19571127	U0	0	+
chr3	140986358	140986383	U0	0	-
chr10	35419784	35419809	U0	0	-
chr4	98488749	98488774	U0	0	+
chr11	22225193	22225218	U0	0	+
chr1	38457520	38457545	U0	0	+
chr1	80668132	80668157	U0	0	-
chr2	152562484	152562509	U0	0	-
chr4	153155301	153155326	U0	0	+
chr9	120803448	120803473	U0	0	+
chr6	89296757	89296782	U0	0	-
chr1	194245558	194245583	U0	0	+
chr8	57916061	57916086	U0	0	+"""
        return self._read_bed_from_string(contents)

    @property
    def chipseq_background(self) -> "pr.PyRanges":
        contents = """chr7	20246668	20246693	U0	0	+
chr1	39036822	39036847	U0	0	+
chr19	47109000	47109025	U0	0	-
chr10	90059861	90059886	U0	0	-
chr3	55648137	55648162	U0	0	+
chr7	91135110	91135135	U0	0	+
chr13	100938475	100938500	U0	0	+
chr3	115816130	115816155	U0	0	+
chr19	43528773	43528798	U0	0	+
chr10	73781101	73781126	U0	0	+"""
        return self._read_bed_from_string(contents)

    @cached_property
    def chromsizes(self) -> "pr.PyRanges":
        contents = """chr1	0	249250621
chr2	0	243199373
chr3	0	198022430
chr4	0	191154276
chr5	0	180915260
chr6	0	171115067
chr7	0	159138663
chrX	0	155270560
chr8	0	146364022
chr9	0	141213431
chr10	0	135534747
chr11	0	135006516
chr12	0	133851895
chr13	0	115169878
chr14	0	107349540
chr15	0	102531392
chr16	0	90354753
chr17	0	81195210
chr18	0	78077248
chr20	0	63025520
chrY	0	59373566
chr19	0	59128983
chr22	0	51304566
chr21	0	48129895
chrM	0	16571"""
        return self._read_bed_from_string(contents)

    @cached_property
    def ensembl_gtf(self) -> "pr.PyRanges":
        """Example gtf file from Ensembl."""
        contents = """#!genome-build GRCh38.p10
#!genome-version GRCh38
#!genome-date 2013-12
#!genome-build-accession NCBI:GCA_000001405.25
#!genebuild-last-updated 2017-06
1	havana	gene	11869	14409	.	+	.	gene_id "ENSG00000223972"; gene_version "5"; gene_name "DDX11L1"; gene_source "havana"; gene_biotype "transcribed_unprocessed_pseudogene";
1	havana	transcript	11869	14409	.	+	.	gene_id "ENSG00000223972"; gene_version "5"; transcript_id "ENST00000456328"; transcript_version "2"; gene_name "DDX11L1"; gene_source "havana"; gene_biotype "transcribed_unprocessed_pseudogene"; transcript_name "DDX11L1-202"; transcript_source "havana"; transcript_biotype "processed_transcript"; tag "basic"; transcript_support_level "1";
1	havana	exon	11869	12227	.	+	.	gene_id "ENSG00000223972"; gene_version "5"; transcript_id "ENST00000456328"; transcript_version "2"; exon_number "1"; gene_name "DDX11L1"; gene_source "havana"; gene_biotype "transcribed_unprocessed_pseudogene"; transcript_name "DDX11L1-202"; transcript_source "havana"; transcript_biotype "processed_transcript"; exon_id "ENSE00002234944"; exon_version "1"; tag "basic"; transcript_support_level "1";
1	havana	exon	12613	12721	.	+	.	gene_id "ENSG00000223972"; gene_version "5"; transcript_id "ENST00000456328"; transcript_version "2"; exon_number "2"; gene_name "DDX11L1"; gene_source "havana"; gene_biotype "transcribed_unprocessed_pseudogene"; transcript_name "DDX11L1-202"; transcript_source "havana"; transcript_biotype "processed_transcript"; exon_id "ENSE00003582793"; exon_version "1"; tag "basic"; transcript_support_level "1";
1	havana	exon	13221	14409	.	+	.	gene_id "ENSG00000223972"; gene_version "5"; transcript_id "ENST00000456328"; transcript_version "2"; exon_number "3"; gene_name "DDX11L1"; gene_source "havana"; gene_biotype "transcribed_unprocessed_pseudogene"; transcript_name "DDX11L1-202"; transcript_source "havana"; transcript_biotype "processed_transcript"; exon_id "ENSE00002312635"; exon_version "1"; tag "basic"; transcript_support_level "1";
1	havana	exon	112700	112804	.	-	.	gene_id "ENSG00000238009"; gene_version "6"; transcript_id "ENST00000471248"; transcript_version "1"; exon_number "2"; gene_name "AL627309.1"; gene_source "ensembl_havana"; gene_biotype "lincRNA"; transcript_name "AL627309.1-203"; transcript_source "havana"; transcript_biotype "lincRNA"; exon_id "ENSE00001957285"; exon_version "1"; transcript_support_level "5";
1	havana	exon	110953	111357	.	-	.	gene_id "ENSG00000238009"; gene_version "6"; transcript_id "ENST00000471248"; transcript_version "1"; exon_number "3"; gene_name "AL627309.1"; gene_source "ensembl_havana"; gene_biotype "lincRNA"; transcript_name "AL627309.1-203"; transcript_source "havana"; transcript_biotype "lincRNA"; exon_id "ENSE00001879696"; exon_version "1"; transcript_support_level "5";
1	ensembl	transcript	120725	133723	.	-	.	gene_id "ENSG00000238009"; gene_version "6"; transcript_id "ENST00000610542"; transcript_version "1"; gene_name "AL627309.1"; gene_source "ensembl_havana"; gene_biotype "lincRNA"; transcript_name "AL627309.1-205"; transcript_source "ensembl"; transcript_biotype "lincRNA"; tag "basic"; transcript_support_level "5";
1	ensembl	exon	133374	133723	.	-	.	gene_id "ENSG00000238009"; gene_version "6"; transcript_id "ENST00000610542"; transcript_version "1"; exon_number "1"; gene_name "AL627309.1"; gene_source "ensembl_havana"; gene_biotype "lincRNA"; transcript_name "AL627309.1-205"; transcript_source "ensembl"; transcript_biotype "lincRNA"; exon_id "ENSE00003748456"; exon_version "1"; tag "basic"; transcript_support_level "5";
1	ensembl	exon	129055	129223	.	-	.	gene_id "ENSG00000238009"; gene_version "6"; transcript_id "ENST00000610542"; transcript_version "1"; exon_number "2"; gene_name "AL627309.1"; gene_source "ensembl_havana"; gene_biotype "lincRNA"; transcript_name "AL627309.1-205"; transcript_source "ensembl"; transcript_biotype "lincRNA"; exon_id "ENSE00003734824"; exon_version "1"; tag "basic"; transcript_support_level "5";
1	ensembl	exon	120874	120932	.	-	.	gene_id "ENSG00000238009"; gene_version "6"; transcript_id "ENST00000610542"; transcript_version "1"; exon_number "3"; gene_name "AL627309.1"; gene_source "ensembl_havana"; gene_biotype "lincRNA"; transcript_name "AL627309.1-205"; transcript_source "ensembl"; transcript_biotype "lincRNA"; exon_id "ENSE00003740919"; exon_version "1"; tag "basic"; transcript_support_level "5";"""
        return self._read_gtf_from_string(contents)

    @property
    def f1(self) -> "pr.PyRanges":
        contents = """chr1	3	6	interval1	0	+
chr1	5	7	interval2	0	-
chr1	8	9	interval3	0	+"""
        return self._read_bed_from_string(contents)

    @property
    def f2(self) -> "pr.PyRanges":
        contents = """chr1	1	2	a	0	+
chr1	6	7	b	0	-"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as f:
            f.write(contents)
            f.flush()
            return pr.read_bed(f.name)

    @property
    def aorta(self) -> "pr.PyRanges":
        return pr.read_bed(self.files["aorta.bed"])

    @property
    def aorta2(self) -> "pr.PyRanges":
        return pr.read_bed(self.files["aorta2.bed"])

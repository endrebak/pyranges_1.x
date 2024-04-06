from pyranges import genomicfeatures  # noqa: F401
from pyranges import statistics as stats  # noqa: F401
from pyranges.core.random import random  # noqa: F401
from pyranges.core.version import __version__  # noqa: F401
from pyranges.example_data_manager import example_data  # noqa: F401
from pyranges.get_fasta import get_sequence, get_transcript_sequence  # noqa: F401
from pyranges.methods.concat import concat  # noqa: F401
from pyranges.multioverlap import count_overlaps  # noqa: F401
from pyranges.option_manager import options  # noqa: F401
from pyranges.pyranges_main import PyRanges  # noqa: F401
from pyranges.range_frame.range_frame import RangeFrame  # noqa: F401
from pyranges.readers import from_string, read_bam, read_bed, read_bigwig, read_gff3, read_gtf  # NOQA: F401

read_gff = read_gtf

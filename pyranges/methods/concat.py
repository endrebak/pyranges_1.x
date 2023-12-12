"""Module for PyRanges concat method."""
import typing
from collections.abc import Iterable
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from pyranges import RangeFrame


def concat(grs: Iterable["RangeFrame"], *args, **kwargs) -> "RangeFrame":
    """Concatenate PyRanges.

    Parameters
    ----------
    grs: iterable of PyRanges
        PyRanges to concatenate.

    args:
        Arguments passed to pandas.concat.

    kwargs:
        Keyword arguments passed to pandas.concat.

    Returns
    -------
    pyranges.PyRanges

    Examples
    --------
    >>> import pyranges as pr
    >>> gr1 = pr.example_data.f2
    >>> gr2 = pr.example_data.f1
    >>> pr.concat([gr1, gr2])
      index  |    Chromosome      Start      End  Name         Score  Strand
      int64  |    category        int64    int64  object       int64  category
    -------  ---  ------------  -------  -------  ---------  -------  ----------
          0  |    chr1                1        2  a                0  +
          1  |    chr1                6        7  b                0  -
          0  |    chr1                3        6  interval1        0  +
          1  |    chr1                5        7  interval2        0  -
          2  |    chr1                8        9  interval3        0  +
    PyRanges with 5 rows, 6 columns, and 1 index columns.
    Contains 1 chromosomes and 2 strands.

    >>> pr.concat([gr1, gr2.remove_strand()])
      index  |    Chromosome      Start      End  Name         Score  Strand
      int64  |    category        int64    int64  object       int64  category
    -------  ---  ------------  -------  -------  ---------  -------  ----------
          0  |    chr1                1        2  a                0  +
          1  |    chr1                6        7  b                0  -
          0  |    chr1                3        6  interval1        0  nan
          1  |    chr1                5        7  interval2        0  nan
          2  |    chr1                8        9  interval3        0  nan
    PyRanges with 5 rows, 6 columns, and 1 index columns.
    Contains 1 chromosomes and 2 strands (including non-genomic strands: nan).
    """
    return typing.cast("RangeFrame", list(grs)[0].__class__(pd.concat([pd.DataFrame(gr) for gr in grs], *args, **kwargs)))

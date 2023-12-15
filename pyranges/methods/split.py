from typing import TYPE_CHECKING

import pandas as pd

from pyranges.names import CHROM_COL, END_COL, RANGE_COLS, START_COL, STRAND_COL, VALID_USE_STRAND_TYPE
from pyranges.pyranges_helpers import mypy_ensure_pyranges, validate_and_convert_strand

if TYPE_CHECKING:
    from pyranges import PyRanges


def _split(
    df: "PyRanges",
    strand: VALID_USE_STRAND_TYPE = "auto",
    **_,
) -> "PyRanges":
    dtype = df[START_COL].dtype

    starts = df[START_COL]
    ends = df[END_COL]
    points = [starts, ends]

    _points = pd.concat(points).sort_values().drop_duplicates()

    _ends = _points.shift(-1)

    _points = _points.iloc[:-1]
    _ends = _ends.iloc[:-1]
    _features = pd.concat([_points, _ends], axis=1).astype(dtype)
    _features.columns = pd.Index(RANGE_COLS)

    _features.insert(0, CHROM_COL, df[CHROM_COL].iloc[0])
    if validate_and_convert_strand(df, strand):
        _features.insert(_features.shape[1], STRAND_COL, df[STRAND_COL].iloc[0])

    return mypy_ensure_pyranges(_features.reset_index(drop=True))

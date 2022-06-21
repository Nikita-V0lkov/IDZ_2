import pandas as pd


def series_fill_nan(series):
    """
    The function returns a series in which the nans are filled

    Parameters
    ----------
    :param series : series
        Generated series

    Returns
    -------
    :return reindex_series : series
        Reindexed series

    Examples
    --------
    >>>series_fill_nan(series)
    0    9\n
    3    4\n
    6    7\n
    dtype: int64\n
    0    9\n
    1    9\n
    2    4\n
    3    4\n
    4    4\n
    5    7\n
    6    7\n
    7    7\n
    8    7\n
    9    7\n
    dtype: int64
    """

    if not isinstance(series, pd.Series):
        raise TypeError('Only series type accepted')

    reindex_series = series.reindex(range(10), method='nearest')
    return reindex_series

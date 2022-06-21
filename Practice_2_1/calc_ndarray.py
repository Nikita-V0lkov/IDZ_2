import numpy as np
from statistics import geometric_mean


def arithmetic_avg(gen_ndarray):
    """
    Function takes a ndarray array and returns the arithmetic mean

    Parameters
    ----------
    :param gen_ndarray : ndarray
        Array from the values of which the arithmetic mean will be calculated

    Returns
    -------
    :return avg_arf : int, float
        Arithmetical mean

    Examples
    --------
    >>>arithmetic_avg([61 78 26 50  8  7 64 30 53 19])
    39.6
    """
    avg_arf = gen_ndarray.mean()
    return avg_arf


def geometric_avg(gen_ndarray):
    """
    Function takes a ndarray array and returns the geometric mean

    Parameters
    ----------
    :param gen_ndarray : ndarray
        Array from the values of which the geometric mean will be calculated

    Returns
    -------
    :return avg_geom : int, float
        Geometric mean

    Examples
    --------
    >>>geometric_avg([61 78 26 50  8  7 64 30 53 19])
    30.380061705220317
    """
    avg_geom = geometric_mean(gen_ndarray)
    return avg_geom


def frequent_values(gen_ndarray):
    """
    Function takes a ndarray array and returns the most frequent values

    Parameters
    ----------
    :param gen_ndarray : ndarray
        Array from the values of which the frequent values will be searched

    Returns
    -------
    :return freq_val : int
        Frequent value

    Examples
    --------
    >>>frequent_values([61 78 26 50  8  7 64 30 53 19])
    7
    """
    freq_val = np.bincount(gen_ndarray).argmax()
    return freq_val


def median_calc(gen_ndarray):
    """
    Function takes a ndarray array and returns the median

    Parameters
    ----------
    :param gen_ndarray : ndarray
        Array from the values of which the median will be calculated

    Returns
    -------
    :return median_result : int, float
        Median

    Examples
    --------
    >>>median_calc([61 78 26 50  8  7 64 30 53 19])
    40.0
    """
    median_result = np.median(gen_ndarray)
    return median_result

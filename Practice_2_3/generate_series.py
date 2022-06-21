import random as r
import pandas as pd


def generate_series():
    """
    The function returns the generated series

    Returns
    -------
    :return: generated_series : series
    """
    indexes = r.sample(range(10), 3)  # Generate 10 random indexes
    elements = r.sample(range(10), 3)  # Generate 10 random elements
    generated_series = pd.Series(elements, index=sorted(indexes))  # Create sorted Series
    return generated_series

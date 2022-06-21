from series_fill_nan import *
from generate_series import *


def main_menu():
    generated_series = generate_series()
    print(generated_series)
    print(series_fill_nan(generated_series))

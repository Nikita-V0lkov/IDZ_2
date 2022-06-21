from calc_ndarray import *


def main_menu():
    gen_ndarray = np.random.randint(1, 100, size=10)
    print("Generated ndarray: {} \n Avg: {} Geom: {} Median: {} Freq val: {}"
          .format(gen_ndarray, arithmetic_avg(gen_ndarray), geometric_avg(gen_ndarray),
                  median_calc(gen_ndarray), frequent_values(gen_ndarray)))

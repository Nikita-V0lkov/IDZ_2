from dataframe_filter import *
from tournament_table_gen import *


def main_menu():
    name_list = ['Olivia', 'Emil', 'Beta', 'Jim', 'Beam', 'Jack', 'Daniels']
    grade_list = ['A', 'B', 'C', 'D', 'FX', 'F']
    class_list = [1, 2, 3, 4, 5]
    generated_ttable = tournament_table_gen(name_list, grade_list, class_list)
    print("Generated tournament table \n", generated_ttable)
    print("Filtered by bigger than grade \n", filter_bigger_than_grade(generated_ttable, 'C'))
    print("Filtered by smaller than grade \n", filter_smaller_than_grade(generated_ttable, 'A'))
    print("Filtered by bigger than class \n", filter_bigger_than_class(generated_ttable, 1))
    print("Filtered by smaller than class \n", filter_smaller_than_class(generated_ttable, 3))

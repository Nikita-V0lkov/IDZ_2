import pandas as pd
import random


def tournament_table_gen(names_list, grade_list, class_list):
    """
    Function generates the tournament table

    Parameters
    ----------
    :param names_list : list
        Athlete names list
    :param grade_list : list
        Athlete grades list
    :param class_list : list
        Athlete class list

    Returns
    -------
    :return standings_frame : DataFrame
        Generated tournament table
    """
    if not isinstance(names_list, list):
        raise TypeError('Names list accept only list variable type')

    if not isinstance(grade_list, list):
        raise TypeError('Grades list accept only list variable type')

    if not isinstance(class_list, list):
        raise TypeError('Class list accept only list variable type')

    standings = {'Name': random.choices(names_list, k=5),
                 'Grade': random.choices(grade_list, k=5),
                 'Class': random.choices(class_list, k=5)}
    standings_frame = pd.DataFrame(standings, columns=['Name', 'Grade', 'Class'])
    return standings_frame

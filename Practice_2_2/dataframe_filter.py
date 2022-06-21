import pandas as pd


def filter_bigger_than_grade(ttable_frame, grade):
    """
    Function returns the tournament table where the input value is bigger than grade

    Parameters
    ----------
    :param ttable_frame : DataFrame
        The DataFrame we will be filtering
    :param grade : str
        Grade by which we will filter

    Returns
    -------
    :return standings_frame : DataFrame
        Tournament table filtered by grade
    """
    if not isinstance(ttable_frame, pd.DataFrame) or not isinstance(grade, str):
        raise TypeError

    filtered_by_grade = ttable_frame[ttable_frame['Grade'] < grade]
    return filtered_by_grade


def filter_bigger_than_class(ttable_frame, filter_class):
    """
    Function returns the tournament table where the input value is bigger than filter_class

    Parameters
    ----------
    :param ttable_frame : DataFrame
        The DataFrame we will be filtering
    :param filter_class : int
        Athlete class by which we will filter

    Returns
    -------
    :return standings_frame : DataFrame
        Tournament table filtered by class
    """

    if not isinstance(ttable_frame, pd.DataFrame) or not isinstance(filter_class, int):
        raise TypeError

    filtered_by_class = ttable_frame[ttable_frame.Class > filter_class]
    return filtered_by_class


def filter_smaller_than_grade(ttable_frame, grade):
    """
    Function returns the tournament table where the input value is less than grade

    Parameters
    ----------
    :param ttable_frame : DataFrame
        The DataFrame we will be filtering
    :param grade : str
        Grade by which we will filter

    Returns
    -------
    :return standings_frame : DataFrame
        Standing filtered by grade
    """

    if not isinstance(ttable_frame, pd.DataFrame) or not isinstance(grade, str):
        raise TypeError

    filtered_by_grade = ttable_frame[ttable_frame['Grade'] > grade]
    return filtered_by_grade


def filter_smaller_than_class(ttable_frame, filter_class):
    """
    Function returns the tournament table where the input value is less than filter_class

    Parameters
    ----------
    :param ttable_frame : DataFrame
        The DataFrame we will be filtering
    :param filter_class : int
        Athlete class by which we will filter

    Returns
    -------
    :return ttable_frame : DataFrame
        Tournament table filtered by class
    """

    if not isinstance(ttable_frame, pd.DataFrame) or not isinstance(filter_class, int):
        raise TypeError

    filtered_by_class = ttable_frame[ttable_frame.Class < filter_class]
    return filtered_by_class

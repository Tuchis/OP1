"""
LAB 10 Module 2 Docstring
"""

import pandas as pd


def read_data(path_to_file):
    """
    Reads data
    @param path_to_file:
    @return:
    """
    df = pd.read_csv(path_to_file)
    return df
# print(read_data("census.csv"))

def max_counties(df):
    """
    Return the biggest counties state
    @param df:
    @return:
    >>> max_counties(read_data("census.csv"))
    'Texas'
    """
    return df['STNAME'].value_counts().idxmax()


def max_difference(df):
    """
    Function with maximum difference
    @param df:
    @return:
    """
    alpha_dif = 0
    alpha_index = 0
    for index_col, row in df.iterrows():
        if row["SUMLEV"] == 50:
            pass
        else:
            continue
        variabla = (row["POPESTIMATE2010"], row["POPESTIMATE2011"], row["POPESTIMATE2012"],\
                    row["POPESTIMATE2013"], row["POPESTIMATE2014"], row["POPESTIMATE2015"])
        maxim = max(variabla)
        minim = min(variabla)
        differ = abs(maxim - minim)
        if differ > alpha_dif:
            alpha_dif, alpha_index = differ, index_col
    return df["CTYNAME"][alpha_index]

def conditional_counties(df):
    """
    Function with counties and conditions
    @param df:
    @return:
    """
    stnames = []
    ctynames = []
    for _, row in df.iterrows():
        if (row["REGION"] == 1 or row["REGION"] == 2) and row["CTYNAME"].startswith("Washington")\
                and row["POPESTIMATE2015"] > row["POPESTIMATE2014"]:
            stnames.append(row["STNAME"])
            ctynames.append(row["CTYNAME"])
    return pd.DataFrame({'STNAME': stnames, 'CTYNAME': ctynames})
print(conditional_counties(read_data()))
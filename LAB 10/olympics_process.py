"""
LAB 10 Module 1 Docstring
"""

import pandas as pd


def read_data():
    """
    Function to read data
    @return:
    """
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(') # split the index by '('

    df.index = names_ids.str[0] # the [0] element is the country name (new index)
    df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID \
    # (take first 3 characters from that)

    df = df.drop('Totals')
    # print(df)
    # print(df.dtypes)

    return df
read_data()

def first_country(df):
    """
    Function to find first country in table
    @param df:
    @return:
    """
    contr = df.iloc[0]
    return contr
# print(first_country(read_data()))

def summer_biggest(df):
    """
    Find country with biggest amount of summer gold
    @param df:
    @return:
    >>> summer_biggest(read_data())
    'United States'
    """
    column = df["Gold"]
    max_index = column.idxmax()
    return max_index
# print(summer_biggest(read_data()))


def difference_biggest(df):
    """
    Find the biggest difference
    @param df:
    @return:
    """
    summer = df["Gold"]
    winter = df["Gold.1"]
    difference = abs(summer - winter)
    max_index = difference.idxmax()
    return max_index
# print(difference_biggest(read_data()))

def difference_biggest_relative(df):
    """
    Find the beggest relative difference
    @param df:
    @return:
    """
    for index_col, row in df.iterrows():
        if row["Gold"] == 0 or row["Gold.1"] == 0:
            df = df.drop(index = index_col)
    summer = df["Gold"]
    winter = df["Gold.1"]
    all_med = df["Gold.2"]
    difference = abs(summer - winter)
    relative = difference / all_med
    max_index = relative.idxmax()
    return max_index
print(difference_biggest_relative(read_data()))


def get_points(df):
    """
    Find points
    @param df:
    @return:
    """
    gold = df["Gold.2"]
    silver = df["Silver.2"]
    bronze = df["Bronze.2"]
    ser = gold * 3 + silver * 2 + bronze * 1
    df['Points'] = ser
    return ser

"""
Module for Laboratory 9, First exercise
"""
def find_film_keywords(film_keywords: dict, film_name: str):
    """
    Function to find all keywords in certain film
    """
    list_of_keys = set()
    for key in film_keywords:
        if film_name in film_keywords[key]:
            list_of_keys.add(key)
    return list_of_keys


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    The function to find number of keys for every movie
    >>> find_films_with_keywords(({'job-application-abroad': ['nOfficially Yours (2012)']}), 1)
    [('nOfficially Yours (2012)', 1)]
    """
    tuples_of_films = []
    films_dict = {}
    for key in film_keywords:
        for film in film_keywords[key]:
            if film in films_dict:
                value = films_dict[film]
                value += 1
                films_dict[film] = value
            else:
                films_dict[film] = 1
    for _ in range(num_of_films):
        max_key = max(films_dict, key=films_dict.get)
        tuples_of_films.append((max_key, films_dict[max_key]))
        films_dict.pop(max_key)
    return tuples_of_films

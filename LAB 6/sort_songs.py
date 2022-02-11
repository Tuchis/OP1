"""Lab 6 2
"""
from typing import List, Tuple, Callable, Union

def song_length(variable: Tuple[str]) -> float:
    """ Checks song length
    >>> song_length({('Той день', '3.58'), ('Янанебібув', '3.19')})
    [('Янанебібув', '3.19'), ('Той день', '3.58')]
    """
    songs_sorted = sorted(variable, key=lambda tup: tup[1])
    return songs_sorted

def title_length(variable: Tuple[str]) -> int:
    """ Sorts by title length

    >>> title_length({('Той день', '3.58'), ('Янанебібув', '3.19')})
    [('Той день', '3.58'), ('Янанебібув', '3.19')]
    """
    songs_sorted = sorted(variable, key=lambda tup: (len(tup[0]), tup[0]))
    return songs_sorted

def last_word(variable: Tuple[str]) -> str:
    """ Sorts by last word

    >>> last_word({('Той день', '3.58'), ('Янанебібув', '3.19')})
    [('Той день', '3.58'), ('Янанебібув', '3.19')]
    """
    words = []
    words_sorted = []
    for a_tuple in variable:
        words.append(a_tuple[0])
    for word in words:
        timed = word.split()
        words_sorted.append(timed[len(timed) - 1].lower())
    words_sorted.sort()
    songs_sorted = []
    for elem in words_sorted:
        for song in variable:
            if elem in song[0].lower():
                songs_sorted.append(song)
    return songs_sorted


def sort_songs(
    song_titles: List[str],
    length_songs: List[str],
    key: Callable[[tuple], Union[int, str, float]]) -> List[tuple]:
    """ Sorts songs by keys

    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай',\
         'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'], \
             ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', \
                 '3.43', '3.17', '2.21'], last_word)
    [('Африка', '4.24'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Етюд', \
'2.21'), ('Кавачай', '4.39'), ('Мало мені', '5.06'), ('Коли тебе нема'\
, '3.17'), ('Поясни', '3.39'), ('Сосни', '4.31'), ('Фіалки', '3.43\
'), ('Янанебібув', '3.19')]
    """
    if len(song_titles) != len(length_songs):
        return None
    file = set(zip(song_titles, length_songs))
    return key(file)

"""Program for inserting word "диво" before every word that starts
with certain character or characters
"""
def dyvo_insert(sentence, flag):
    """Inserting word "диво" before every word that starts with flag.

    Args:
        sentence (str): the sentence
        flag (str): flag, we are searching for

    Returns:
        str: sentence, with inserted "диво"
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті"\
    , "ки")
    'дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    """
    sentence = sentence.lower().replace(flag, "диво" + flag)
    return sentence

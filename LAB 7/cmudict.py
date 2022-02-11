"""
Lab 7 Docstring
"""
def dict_reader_tuple(file_dict):
    """
    Documentation to function
    """
    tuples = []
    with open(file_dict) as file:
        for line in file:
            line = line.strip().split()
            tuples.append((line[0], int(line[1]), line[2:][:]))
    return tuples


def dict_reader_dict(file_dict):
    """
    The second function to make dictionary
    """
    dict_of_words = {}
    with open(file_dict) as tuples:
        for set_of_words in tuples:
            set_of_words = set_of_words.strip().split()
            prons = set()
            for element in [set_of_words[2:]]:
                vouls = ()
                for voul in element:
                    voul = (voul,)
                    vouls = vouls + voul
                prons.add(vouls)
            try:
                value = dict_of_words[set_of_words[0]]
                value.add(vouls)
                dict_of_words[set_of_words[0]] = value
            except (KeyError, ValueError, IndexError):
                dict_of_words[set_of_words[0]] = prons
    return dict_of_words

def dict_reader_dict_from_list(inp_list):
    """
    Function to make dictionary from list
    """
    dict_of_words = {}
    for elem in inp_list:
        prons = set()
        vouls = ()
        for word in elem[2]:
            voul = (word,)
            vouls = vouls + voul
        prons.add(vouls)
        try:
            value = dict_of_words[elem[0]]
            value.add(vouls)
            dict_of_words[elem[0]] = value
        except (KeyError, ValueError, IndexError):
            dict_of_words[elem[0]] = prons
    return dict_of_words


def dict_invert(dct):
    """
    Inverts function and creates dictionary with keys
    >>> dict_invert({'AABERG': {('AA1', 'B', 'ER0', 'G')}})
    {1: {('AABERG', ('AA1', 'B', 'ER0', 'G'))}}
    """
    def dict_dict_invert(dct):
        result = {}
        for name in dct:
            try:
                value = result[len(dct[name])]
                for pronon in dct[name]:
                    prononcuat = ()
                    for elem in pronon:
                        prononcuat = prononcuat + (elem,)
                    minus = (name, prononcuat)
                # value = [((x) for x in value), minus]
                value.append(minus)
                result[len(dct[name])] = value
            except KeyError:
                plus = []
                for pronon in dct[name]:
                    prononcuat = ()
                    for elem in pronon:
                        prononcuat = prononcuat + (elem, )
                    minus = (name, prononcuat)
                    plus.append((minus))
                result[len(dct[name])] = plus
        for key in result:
            value = result[key]
            final = set(value)
            # for elem in value:
            #     big_tuple += (elem)
            #     final.add(elem)
            result[key] = final
        return result

    if type(dct) == list:
        dct = dict_reader_dict_from_list(dct)
        return dict_dict_invert(dct)

    if type(dct) == dict:
        return dict_dict_invert(dct)
print(dict_reader_dict("cmudict"))
"""
Common names
"""

def common_names(female_names, male_names):
    r"""
    Compares names
    >>> common_names(names_read("female.txt"), names_read("male.txt")) #doctest: +ELLIPSIS
    {...
    """
    name_set = set()
    common_name = set()
    for name in female_names:
        name_set.add(name)
    for name in male_names:
        if name in name_set and name.startswith(("A", "E", "I", "O", "U")):
            common_name.add(name)
    return common_name

def names_read(file_name):
    """
    Reads names from files
    """
    names = []
    with open(file_name) as file:
        for line in file:
            line.strip()
            line = line[:-1]
            names.append(line)
    return names

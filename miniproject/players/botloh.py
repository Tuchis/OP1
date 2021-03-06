#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from logging import DEBUG, debug, getLogger
# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can however do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


# plateau = Figures()
# plateau.height = 10
# plateau.width = 100
# print(plateau.width, plateau.height)
# fig = Figures()
# fig.height = 12
# fig.width = 123
# print(fig.width, fig.height)

# def check_moves(platea, figur, player):
#     plateau = []
#     for i in platea:
#         plateau.append([m for m in i])
#     figure = []
#     for i in figur:
#         figure.append([m for m in i])
#     debug(plateau)
#     for i in range(len(plateau)):
#         for j in range(len(plateau[0])):
#             for f in range(len(figure)):
#                 for m in range(len(figure[f])):
#                     if figure[m] == '*':
# def givezero(plateau, new_plateau, player):
#     elem = ("O" if player == 1 else "X")
#     for i in range(len(plateau)):
#         for j in range(len(plateau[0])):
#             if plateau[i][j] == elem:
#                 if new_plateau[i][j] == '.':
#                     new_plateau[i] = new_plateau[i][:j] + elem + new_plateau[i][j+1:]
#     return new_plateau
#
# # print(givezero(['   01234567890123456,', '000 .................','001 .................', '002 .................','003 .................','004 .................','005 .................','006 .................','007 ..O..............','008 ..OOO............','009 .................','010 .................','011 .................','012 ..............X..','013 .................','014 .................]'], ['   01234567890123456,', '000 .................','001 .................', '002 .................','003 .................','004 .................','005 .................','006 .................','007 .*.*.............','008 ..OOO............','009 .................','010 .................','011 .................','012 ..............X..','013 .................','014 .................]'], 1))
#
#
# def check_available_moves(plateau: list, figure: list, player: int, heigth: int, width: int):
#     oldfigs = 0
#     opp_count = 0
#     my_count = 0
#
#     for i in plateau:
#         oldfigs += i.count('.')
#         opp_count += i.count("O" if player == 2 else "X")
#         my_count += i.count("O" if player == 1 else "X")
#     figc = 0
#     for i in figure:
#         figc += i.count('*')
#     possible = []
#     for i in range(1, heigth + 1):
#         for j in range(3, len(plateau[1]) - len(figure) + 1):
#             newplateau = plateau.copy()
#             for f in range(len(figure)):
#                 if i + len(figure) <= len(plateau) - 1:
#                     newplateau[i+f] = newplateau[i+f][:j] + figure[f] + newplateau[i+f][j + len(figure[f]):]
#                 # print(newplateau)
#                 newplateau = givezero(plateau, newplateau, player)
#                 new_opp_count = 0
#                 new_my_count = 0
#                 for fig in newplateau:
#                     new_opp_count += fig.count("O" if player == 2 else "X")
#                     new_my_count += fig.count("O" if player == 1 else "X")
#                 if new_opp_count == opp_count and new_my_count == my_count - 1:
#                     # print(plateau)
#                     # print(newplateau, j-4, i-1)
#                     if i - 1 <= len(plateau) - len(figure) - 2:
#                         if j - 4 >= 0:
#                             debug(newplateau)
#                             possible.append(tuple((i - 1, j - 4)))
#     return possible


def givezero(plateau, new_plateau, player):
    elem = ("O" if player == 1 else "X")
    opp_elem = ("O" if player == 2 else "X")
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j] == elem:
                if new_plateau[i][j] == '.':
                    new_plateau[i] = new_plateau[i][:j] + elem + new_plateau[i][j+1:]
            elif plateau[i][j] == opp_elem:
                if new_plateau[i][j] == '.':
                    new_plateau[i] = new_plateau[i][:j] + opp_elem + new_plateau[i][j + 1:]
    return new_plateau


def dist(x1, y1, x2, y2):
    return ((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2)**0.5


def dominance(plateau, player, i, j):
    """
    Get as close as possible to the opponent
    :param plateau:
    :param possible:
    :param player:
    :return:
    """
    distances = []
    mine = '*'
    notmine = ("O" if player == 2 else "X")
    for string in range(len(plateau)):
        for elem in range(len(plateau[string])):
            if plateau[string][elem] == notmine:
                distances.append(dist(int(i), int(j), string, elem))
    return min(distances)


def check_available_moves(plateau: list, figure: list, player: int, heigth: int, width: int):
    # debug(plateau)
    # debug(figure)
    opp_count = 0
    my_count = 0
    for i in range(len(plateau)):
        plateau[i] = plateau[i].replace('x', 'X').replace('o', 'O')
        opp_count += plateau[i].count("O" if player == 2 else "X")
        my_count += plateau[i].count("O" if player == 1 else "X")
    possible = []
    for i in range(1, heigth + 1 - len(figure)):
        for j in range(4, len(plateau[1]) - len(figure[0])):
                newplateau = plateau.copy()
                for f in range(len(figure)):
                    if i + f <= len(plateau) - 1:
                        newplateau[i+f] = newplateau[i+f][:j] + figure[f] + newplateau[i+f][j + len(figure[f]):]
                # print(newplateau)
                newplateau = givezero(plateau, newplateau, player)
                new_opp_count = 0
                new_my_count = 0
                for fig in newplateau:
                    new_opp_count += fig.count("O" if player == 2 else "X")
                    new_my_count += fig.count("O" if player == 1 else "X")
                if new_opp_count == opp_count and new_my_count == my_count - 1:
                    # debug(newplateau)
                    distance = dominance(newplateau, player, i-1, j-4)
                    possible.append(tuple(((i - 1, j - 4), distance)))
    return possible, new_my_count

# debug(check_available_moves(['   01234567890123456,', '000 .................','001 .................', '002 .................','003 .................','004 .................','005 .................','006 .................','007 ..O..............','008 ..OOO............','009 .................','010 .................','011 .................','012 ..............X..','013 .................','014 .................]'], ['..*.','***.'],1, 15, 17))
# print(check_available_moves(['    0123456789012345678901234567890123456789', '000 ........................................', '001 ........................................', '002 ........................................', '003 ...O....................................', '004 ........................................', '005 ........................................', '006 ........................................', '007 ........................................', '008 ........................................', '009 ........................................', '010 ........................................', '011 ........................................', '012 ........................................', '013 ........................................', '014 ........................................', '015 ........................................', '016 ........................................', '017 ........................................', '018 ........................................', '019 ...............................XX.......', '020 ...............................X........', '021 ........................................', '022 ........................................', '023 ........................................'], ['.*..', '....', '....'], 2, 23, 40))


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    info = input()
    width = info[:-1].split()[-1]
    height = info.split()[-2]
    debug(f"Description of the field: {info}")
    return height, width




def parse_field(player: int, height, width):
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowercase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player int: Represents whether we're the first or second player
    """
    # move = None
    plateau = []
    for i in range(height + 1):
        line = input()
        plateau.append(line)
        # debug(f"Field: {l}")
        # if move is None:
        #     c = l.lower().find("o" if player == 1 else "x")
        #     if c != -1:
        #         move = i - 1, c - 4
    # assert move is not None
    return plateau


# def closest_opposite(plateau, figure, possible, player):
#     if player == 1:
#         for i in range(len(plateau) - 1, 0, -1):
#             plateau[i] = plateau[i].replace('.', (str(len(plateau) - i) if i >= 8 else str(9)))
#     else:
#         for i in range(len(plateau)):
#             plateau[i] = plateau[i].replace('.', str(9) if i >= 9 else str(i))
#     # for i in range(len(plateau)):
#     #     if player == 1:
#     #         plateau[i] = plateau[i].replace('.', )
#     debug(plateau)
#     for move in possible:
#         pass
# debug(closest_opposite(['   01234567890123456,', '000 .................','001 .................', '002 .................','003 .................','004 .................','005 .................','006 .................','007 ..O..............','008 ..OOO............','009 .................','010 .................','011 .................','012 ..............X..','013 .................','014 .................]'], ['..*.','***.'],[(6, 0), (6, 1), (6, 2), (7, 4), (8, 0), (8, 1), (8, 2)], 2))


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    l = input()
    debug(f"Piece: {l}")
    fig_height = int(l.split()[-2])
    fig_width = int(l[:-1].split()[-1])
    figure = []
    for _ in range(fig_height):
        l = input()
        figure.append(l)
        debug(f"Piece: {l}")
    return figure


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    height, width = parse_field_info()
    plateau = parse_field(player, int(height), int(width))
    figure = parse_figure()
    available_moves, count = check_available_moves(plateau, figure, player, int(height), int(width))
    debug(available_moves)
    # best_move = find_distance(plateau, figure, available_moves)
    if len(available_moves) == 0:
        print(1, 1)
        quit()
    # elif len(available_moves) >= 2:
    #     best_move = (available_moves[-(len(available_moves) - 3)])
    # else:
    #     best_move = available_moves[-1]
    # best_move = random.choice(available_moves)
    # best_move = available_moves[len(available_moves) // 2]
    # if player == 1:
    #     if count > int(height) * 4:
    #         best_move = available_moves[0]
    #     else:
    #         best_move = available_moves[-1]
    # else:
    #     if count > int(height) * 4:
    #         best_move = available_moves[-1]
    #     else:
    #         best_move = available_moves[0]
    if count < int(height) // 2:
        if player == 2:
            best_move = available_moves[-1][0]
        elif player == 1:
            best_move = available_moves[0][0]
    elif count < int(height) * 3:
        if player == 2:
            best_move = available_moves[0][0]
        else:
            best_move = available_moves[-1][0]
    else:
        available_moves.sort(key=lambda x: x[1])
        best_move = available_moves[0][0]

    return best_move


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()

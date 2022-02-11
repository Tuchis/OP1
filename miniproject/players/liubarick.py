#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
My bot, version 1.1
"""

from logging import DEBUG, debug, getLogger

getLogger().setLevel(DEBUG)

symbols = [["o", "O"], ["x", "X"]]


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 0 if "p1 :" in i else 1


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    move = None
    height, width = parse_field_info()
    field = parse_field(height, width)
    piece = parse_figure()
    move = move_decision(player, field, piece)
    return move


def parse_field_info():
    """
    Parse the info about the field.

    Returns height and width of the field

    The input may look like this:

    Plateau 15 17:
    """
    l = input()
    h, w = int(l.split()[1]), int(l.split()[2][:-1])
    debug(f"Description of the field: {l}")
    debug(f"height: {h}, width: {w}")
    return h, w


def parse_field(height: int, width: int):
    """
    Parse the field.

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
    field = [0]*height
    for i in range(-1, height):
        inp = input()
        debug(f"Field: {inp}")
        if i != -1:
            field[i] = inp[-width:]
    return field


def parse_figure():
    """
    Parse the figure.

    The function parses the height and the width of the figure.
    Returns it for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    piece = []
    inp = input()
    debug(f"Piece: {inp}")
    height, width = int(inp.split()[1]), int(inp.split()[2][:-1])
    for _ in range(height):
        inp = input()
        debug(f"Piece: {inp}")
        piece.append(inp)
    return piece


def imaginary_board_conflicts(pos, field, piece, gs, bs):

    """corner = 0

    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == "*" and corner == 0:
                corner = (row, col)
    debug(corner)"""
    count = 0
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if field[pos[0]+row][pos[1] + col] in gs and piece[row][col] !=".":
                count += 1
            if (field[pos[0]+row][pos[1] + col] in bs or (field[pos[0]+row][pos[1] + col] in gs and count >1)) and piece[row][col] != ".":
                return False
    if count == 1:
        return True
    return False


def move_decision(player, field, piece):
    """
    Function for decision, which move to make.
    """
    def appropriate_moves(good_s, bad_s):
        moves = []
        for row_count, row in enumerate(field):
            for pos_num, position in enumerate(row):
                # here i can add some initial test to exclude some definitely bad positions
                if (row_count + len(piece) <= len(field))\
                        and (pos_num + len(piece[0]) <= len(field[0])):
                    if imaginary_board_conflicts((row_count,pos_num), field, piece, good_s, bad_s):
                        moves.append((row_count,pos_num))

        return moves

    if player == 1:
        gs = symbols[1]
        bs = symbols[0]
    else:
        gs = symbols[1]
        bs = symbols[0]
    moves = appropriate_moves(gs, bs)

    if moves != []:
        return moves[0] if player == 1 else moves[-1]
    else:

        return (0, 0)


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError as error:
        print(error)
        debug("Cannot get input. Seems that we've lost ):!!!!!!!1")


if __name__ == "__main__":
    debug("GG")
    main()
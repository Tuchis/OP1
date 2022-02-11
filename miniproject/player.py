#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

import random

from logging import DEBUG, debug, getLogger

# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can hovever do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    _, height, width = input().split()
    height, width = int(height), int(width[:-1])
    # debug(height+ width)
    # debug(f"Description of the field: {height, width}")
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

    Also, it might be useful to distinguish between lowecase (the most recent piece)
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
    move = None
    l = input()
    hostile_pos = []
    team_pos = []
    for i in range(height):
        line = input()[4:]
        # debug(f"Field: {line}")
        for j in range(width):
            if line[j] == ("X" if player == 1 else "O"):
                hostile_pos.append((i,j))
            elif line[j] == ("O" if player == 1 else "X"):
                team_pos.append((i,j))
    # debug("Hostile pos:" + str(hostile_pos))
    # debug("Team pos: " + str(team_pos))
    return hostile_pos, team_pos


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
    line = input()
    # debug(f"Piece: {line}")
    height, width = int(line.split()[1]), int(line.split()[2][:-1])
    signs = []
    for hei in range(height):
        line = input()
        for symb in range(len(line)):
            if line[symb] == "*":
                signs.append((hei, symb))
    # debug(f"Piece: {signs}")
    return signs, height, width


def mover(height, width, hostile, team, figure, figure_height, figure_width):
    positions = []
    # debug(height)
    # debug(width)
    # debug(team)
    # debug(hostile)
    for h in range(height - figure_height + 1):
        for w in range(width - figure_width + 1):
            count = 0
            for star in figure:
                # debug("0: " + str(star[0])+ " 1: " + str(star[1]))
                if star[0] + h > height or star[1] + w > width:
                    count += 2
                if (star[0] + h, star[1] + w) in hostile:
                    count += 2
                elif (star[0] + h, star[1] + w) in team:
                    count += 1
            if count == 1:
                # debug("YES")
                positions.append((h, w))
    # debug("Postions:" + str(positions))
    return random.choice(positions)


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    move = None
    heigth , width = parse_field_info()
    hostile_pos, team_pos = parse_field(player, heigth, width)
    figure, fig_hei, fig_wid = parse_figure()
    # debug("Start")
    move = mover(heigth, width, hostile_pos, team_pos, figure, fig_hei, fig_wid)
    # debug("End" + str(move))
    return move


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

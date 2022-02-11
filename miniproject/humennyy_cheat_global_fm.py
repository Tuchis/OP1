#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""
import copy
import random
import time
import sys
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
    l = input()
    # debug(f"Description of the field: {l}")
    height = int(l.split()[1])
    width = int(l.split()[2][:-1])
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
    field = []
    for i in range(height + 1):
        line = input()
        if line.startswith(" "):
            pass
        else:
            line = line[4:]
            # debug(line)
            liner = []
            for letter in range(len(line)):
                if line[letter] == "X":
                    liner.append("X")
                elif line[letter] == "O":
                    liner.append("O")
                else:
                    liner.append("_")
            field.append(liner)
    for line_index in range(height):
        try:
            posit = field[line_index].index(("X" if player == 1 else "O"))
            position = (posit, line_index)
        except:
            pass
    enemy_positions = set()
    enemy_positions_done = set()
    enemy_positions.add(position)
    # debug(position)
    # debug(enemy_positions.difference(enemy_positions_done))
    while enemy_positions != enemy_positions_done:
        pos = random.choice(list(enemy_positions.difference(enemy_positions_done)))
        for xer in range(3):
            for yer in range(3):
                try:
                    if field[pos[1] + yer - 1][pos[0] + xer - 1] == "_":
                        field[pos[1] + yer - 1][pos[0] + xer - 1] = "1"
                    elif field[pos[1] + yer - 1][pos[0] + xer - 1] == (("X" if player == 1 else "O")):
                        enemy_positions.add((pos[0] + xer - 1, pos[1] + yer -1))
                    else:
                        pass
                except:
                    pass
        enemy_positions_done.add(pos)
    number = 0
    # debug(field)
    while True:
        number += 1
        status = True
        nums_positions = set()
        nums_positions_done = set()
        for line_index in range(height):
            for elem_index in range(width):
                if field[line_index][elem_index] == str(number):
                    nums_positions.add((elem_index, line_index))
        nums_positions.add(position)
        # debug(nums_positions)
        while nums_positions != nums_positions_done:
            pos = random.choice(list(nums_positions.difference(nums_positions_done)))
            # for xer in range(3):
            #     for yer in range(3):
            for xer,yer in [(1,0), (1,2), (0,1), (2,1)]:
                try:
                    if field[pos[1] + yer - 1][pos[0] + xer - 1] == "_":
                        field[pos[1] + yer - 1][pos[0] + xer - 1] = str(number + 1)
                        status = False
                    elif field[pos[1] + yer - 1][pos[0] + xer - 1] == (str(number)):
                        nums_positions.add((pos[0] + xer - 1, pos[1] + yer - 1))
                    else:
                        pass
                except:
                    pass
            nums_positions_done.add(pos)
        # debug(field)
        if status is True:
            break

    # debug(field)
    # with open("debug", "a") as file:
    #     file.write(str(field) + "\n")
    # print(field, file=sys.stderr)
    return field


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
    # debug(f"Piece: {l}")
    height = int(l.split()[1])
    width = int(l.split()[2][:-1])
    figure = []
    for i in range(height):
        l = input()
        # debug(f"Piece: {l}")
        liner = []
        for letter in l:
            if letter == "*":
                liner.append("*")
            else:
                liner.append("_")
        figure.append(liner)
    # debug(figure)
    return figure, height, width


def checker(player, field, field_height, field_width, xer, yer, figure, height, width):
    """
    Checker of correct position
    @param player:
    @param field:
    @param field_height:
    @param field_width:
    @param xer:
    @param yer:
    @param figure:
    @param height:
    @param width:
    @return:
    """
    price = 0
    zone = []
    for heighter in range(height):
        line = []
        for elem in range(xer, xer + width):
            try:
                line.append(field[yer + heighter][elem])
            except:
                line.append(".")
        zone.append(line)
    # debug(zone)
    counter = 0
    for line in range(height):
        for widther in range(width):
            try:
                if figure[line][widther] == "*" and zone[line][widther] == ".":
                    return False,price
                elif figure[line][widther] == "*" and (zone[line][widther] == (("O" or "o") if player == 1 else ("X" or "x"))):
                    counter += 1
                elif figure[line][widther] == "*" and (zone[line][widther] == (("X" or "x") if player == 1 else ("O" or "o"))):
                    return False, price
                elif figure[line][widther] == "*":
                    try:
                        price += int(field[yer + line][xer + widther])
                    except:
                        price += 100
            except IndexError:
                return False, price
    if counter != 1:
        return False, price
    else:
        temp_field = copy.deepcopy(field)
        for hei in range(field_height):
            for wid in range(field_width):
                if temp_field[hei][wid] == (("O" or "o") if player == 1 else ("X" or "x")):
                    temp_field[hei][wid] = "_"
        for hei in range(height):
            for wid in range(width):
                try:
                    temp_field[xer + hei][yer + wid] = figure[hei][wid]
                except IndexError:
                    pass
        # debug(field)
        # debug(temp_field)
        # debug("PRICE:" + str(price))
        return 1, price


def mover(player, field, field_height, field_width,\
         figure, figure_height, figure_width):
    """
    The function to check possibility of the move
    @param player:
    @param field:
    @param field_height:
    @param field_width:
    @param figure:
    @param figure_height:
    @param figure_width:
    @return:
    """

    moves = []

    for heighter in range(-figure_height, field_height):
        for elem_index in range(-figure_width, field_width):
            status, price = checker(player, field, field_height, field_width, elem_index, heighter, figure, figure_height, figure_width)
            if status == 1:
                moves.append([(heighter, elem_index), price])
            else:
                pass
    # debug("MOVES:" + str(moves))

    def qsort_index(lst, index):
        if len(lst) == 0:
            return []
        else:
            pivot = lst[0]
            lesser = qsort_index([x for x in lst[1:] if x[index] < pivot[index]], index)
            greater = qsort_index([x for x in lst[1:] if x[index] >= pivot[index]], index)
            return lesser + [pivot] + greater
    moves = qsort_index(moves, 1)
    # debug(moves)
    # print(moves, file=sys.stderr)

    try:
        move = moves[0][0]
        return move[0], move[1]
    except IndexError:
        return "No moves. Kolya is the best assistant"



def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    move = None
    height, width = parse_field_info()
    field = parse_field(player, height, width)
    figure, figure_height, figure_width = parse_figure()
    move = mover(player, field, height, width,\
                 figure, figure_height, figure_width)
    # debug(type(move))
    return move


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        time.sleep(0.5)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    # debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()

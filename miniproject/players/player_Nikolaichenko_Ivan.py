#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logging import DEBUG, debug, getLogger
import math
import copy


getLogger().setLevel(DEBUG)

opponent_coords = ()

def parse_field_info():
    """
    Parsing the info about the field.

    The input may look like this:

    Plateau 15 17:
    """
    size_info = input()
    size_info = size_info.split(" ")
    size_info[2] = size_info[2].replace(":", "")
    return int(size_info[1]), int(size_info[2])

def parse_field(times_to_repeat, map_len):
    """
    Parsing the field.

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

    """
    map = []
    for i in range(times_to_repeat):
        line = input()
        line = line.strip()
        line_lst = []
        for i in range(len(line)):
            line_lst.append(line[i])
        remove_value = len(line) - map_len
        line_lst = line_lst[remove_value:]

        map.append(line_lst)       
    map.pop(0)
    return map

def parse_figure():
    """
    Parsing the figure.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    piece = input()
    piece = piece.split(" ")
    piece[2] = piece[2].replace(":", "")
    figure = []
    for i in range(int(piece[1])):
        size_info = input()
        size_info = size_info.strip()
        figure_list = []
        for i in range(len(size_info)):
            figure_list.append(size_info[i])
        figure.append(figure_list)
    return figure

def cut_figure(figure):
    """
    Stripping the figure for more convinient processing
    """
    left_shift = 0
    right_shift = 0
    down_shift = 0
    up_shift = 0

    figure = copy.deepcopy(figure)

    # up cut
    for i in range(len(figure)):
        current_line_empty = True
        for j in range(len(figure[0])):
            if (figure[i][j] != "."):
                current_line_empty = False
                break
        if current_line_empty:
            up_shift += 1
        else:
            break
    for _ in range(up_shift):
        figure.pop(0)

    # down cut
    for i in range(len(figure) - 1, -1, -1):
        current_line_empty = True
        for j in range(len(figure[0])):
            if (figure[i][j] != "."):
                current_line_empty = False
                break
        if current_line_empty:
            down_shift += 1
        else:
            break
    for _ in range(down_shift):
        figure.pop(-1)
    
    # left cut
    for i in range(len(figure[0])):
        current_col_empty = True
        for j in range(len(figure)):
            if (figure[j][i] != "."):
                current_col_empty = False
                break
        if current_col_empty:
            left_shift += 1
        else:
            break
    for _ in range(left_shift):
        for line in figure:
            line.pop(0)

    # right cut
    for i in range(len(figure[0]) - 1, -1, -1):
        current_col_empty = True
        for j in range(len(figure)):
            if (figure[j][i] != "."):
                current_col_empty = False
                break
        if current_col_empty:
            right_shift += 1
        else:
            break
    for _ in range(right_shift):
        for line in figure:
            line.pop(-1)

    return (figure, left_shift, up_shift)

def figure_fits(mapp, zero, star, figure):
    """
    Checks if the figure fits or not 
    """
    left = 0
    right = 0
    down = 0
    up = 0
    for _ in range(0, star[1] + 1):
        left = left + 1
    for _ in range(star[1], len(figure[star[0]])):
        right = right + 1
    for _ in range(0, star[0] + 1,):
        up = up + 1
    for _ in range(star[0], len(figure)):
        down = down + 1
    if down != 0:
        down = down -1
    if up != 0:
        up = up - 1
    if left != 0:
        left = left - 1
    if right != 0:
        right = right - 1
    if zero[0] - up < 0:
        return False, ()
    if zero[0] + down >= len(mapp):
        return False, ()
    if zero[1] - left < 0:
        return False, ()
    if zero[1] + right >= len(mapp[zero[0]]):
        return False, ()
    for k in range(up + down + 1):
        if  (zero[0] - up + k, zero[1]) != (zero[0], zero[1]):
            if mapp[zero[0] - up + k][zero[1]] != ".":
                if figure[star[0] - up + k][star[1]] != ".":
                    return False, ()
        for i in range(left):
            if mapp[zero[0] - up + k][zero[1] - i - 1] != ".":
                if figure[star[0] - up + k][star[1] - i - 1] != ".":
                    return False, ()
        for i in range(right):
            if mapp[zero[0] - up + k][zero[1] + i + 1] != ".":
                if figure[star[0] - up + k][star[1] + i + 1] != ".":
                    return False, ()
    return True, (left, up)


def step(player, mapp, figure):
    """
    Finding all possible places to put a figure
    """

    figure, left_shift, up_shift = cut_figure(figure)
    
    all_variants = []
    if player == 1:
        mark = "o"
    else:
        mark = "x"
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            if mapp[i][j].lower() == mark:
                for k in range(len(figure)):
                    for l in range(len(figure[k])):
                        if figure[k][l] == "*":
                            result = figure_fits(mapp, (i, j), (k, l), figure)
                            fits = result[0]
                            shift = result[1]
                            if fits:
                                left = shift[0]
                                up = shift[1]
                                coord = (i - up - up_shift, j - left - left_shift)                                
                                all_variants.append(coord)
    if all_variants == []:
        return []
    return all_variants

def best_variant(all_variants, mapp, player):
    """
    Finding the best place to put a figure according to the strategy 
    """
    global opponent_coords
    if player == 2:
        mark = "o"
    else:
        mark = "x"
    if opponent_coords == ():
        opponent_coords = find_first_position(mark, mapp)
    all_distances = {}
    for i in range(len(all_variants)):
        katet_1 = abs(all_variants[i][0] - opponent_coords[0])
        katet_2 = abs(all_variants[i][1] - opponent_coords[1])

        distance = math.sqrt((math.pow(katet_1, 2)) + (math.pow(katet_2, 2)))
        distance = round(distance, 4)
        all_distances[all_variants[i]] = distance
    values_list = list(all_distances.values())
    min_dist = 1000000
    for elem in values_list:
        if elem < min_dist:
            min_dist = elem
    for coords, dist in all_distances.items():  
        if dist == min_dist:
            return coords

def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    info = input()
    return 1 if "p1 :" in info else 2


def play(player):
    """
    Calling all sub-functions and gets the final coords
    """
    map_details = parse_field_info()
    times_to_repeat = map_details[0] + 1
    map_len = map_details[1]

    map = parse_field(times_to_repeat, map_len)
    figure = parse_figure()
    all_variants = step(player, map, figure)
    if all_variants == []:
        return all_variants
    output  = best_variant(all_variants, map, player)
    coord = []
    coord.append(output[0])
    coord.append(output[1])
    return coord

def moving(player):
    """
    Main game loop.
    """
    while True:
        move = play(player)
        print(*move)

def find_first_position(mark, mapp):
    """
    Finding the position of the first opponnent's cell
    """
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            if mapp[i][j].lower() == mark:
                return (i, j)

def main():
    player = parse_info_about_player()
    try:
        moving(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()

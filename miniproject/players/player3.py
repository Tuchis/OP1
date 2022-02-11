#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logging import debug, DEBUG, getLogger
from math import sqrt

getLogger().setLevel(DEBUG)
# logging.basicConfig(filename='file1', level=logging.DEBUG)

def parse_player():
    '''
    returns 1 if player is 1 else returns 2
    '''
    info=input()
    if 'p1 :' in info:
        player=2
    else:
        player=1
    return player


def parse_field_info():
    '''
    returns sizes of the field
    '''
    field=input()
    # debug(f"Field info: {field}")
    return int(field.split()[1]), int(field.split()[2][:-1])


def parse_field(height):
    '''
    returns field
    '''
    field=[]
    for _ in range(height+1):
        line=input()
        # debug(f"{column_index%10}: {line}")
        field.append(line[4:])
    return field[1:]

def parse_figure_info():
    '''
    returns sizes of the figure
    '''
    info=input()
    # debug(f'Figure info: {int(info.split()[1]), int(info.split()[2][:-1])}')
    return int(info.split()[1]), int(info.split()[2][:-1])


def parse_figure(height):
    '''
    returns list of relative figure's stars coordinates
    '''
    figure=[]
    for column_index in range(height):
        column=input()
        # debug(f'{column_index%10}: {column}')
        for element_index in range(len(column)):
            if column[element_index]!='.':
                figure.append((column_index,element_index))
    # debug(f'Figure: {figure}')
    return figure

def figure_options(figure):
    '''
    returns the relative coordinates of points of figure, where
    the one point have coordinate (0,0)
    '''
    options=[]
    for current_point in figure:
        option=[]
        for point in figure:
            option.append((point[0]-current_point[0], point[1]-current_point[1]))
        options.append(option)
    # debug(f'Options: {options}')
    return options




def move_checker(step, figure, coordinats, field_info):
    '''
    returns all available places, where the first star of the figure
    can be fit
    '''
    #return the places were first point from figure can be placed
    # debug(f'Step: {step}')
    first_point_places=[]
    options=figure_options(figure)
    for option in options:
        newset=set() #set of coordinates of figure on the field
        for point in option:
            if abs(step[0]+point[0])>field_info[0]-1 or abs(step[1]\
                +point[1])>field_info[1]-1 or step[0]+point[0]<0 or step[1]+point[1]<0:
                newset=set()
                break#if doesnt go under field border
            newset.add((step[0]+point[0], step[1]+point[1]))
        # debug(f'newset: {newset}')
        commonset=coordinats[0]|coordinats[1]
        # debug(f'commonset: {commonset}')
        if len(commonset&newset)==1:
            first_point_places.append((step[0]+option[0][0],step[1]+option[0][1]))
    # debug(f'first point places: {first_point_places}')
    return first_point_places


def coordinates(field):
    '''
    returns sets of coordinates O and X
    '''
    # coord_olist, coord_xlist = [], []
    coord_x,coord_o=set(),set()
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j].lower() == 'o':
                # coord_olist.append((i,j))
                coord_o.add((i,j))
            elif field[i][j].lower() == 'x':
                # coord_xlist.append((i,j))
                coord_x.add((i,j))
    # debug(f'x: {coord_xlist}')
    # debug(f'o: {coord_olist}')
    return coord_x, coord_o


def move(player):
    '''
    returns all available moves of the player
    '''
    moves=[]
    field_info=parse_field_info()
    field=parse_field(field_info[0])
    coordinats=coordinates(field)
    figure_info=parse_figure_info()
    figure=parse_figure(figure_info[0])
    for coordinate in (coordinats[0] if player==1 else coordinats[1]):
        for point in move_checker(coordinate, figure, coordinats, field_info):
            moves.append((point[0]-figure[0][0],point[1]-figure[0][1]))
            # debug(f'move: {coordinate}')
    # debug(f'moves: {moves}')
    return moves


def select_move(moves, last_move):
    farest=0
    best_move=None
    for move in moves:
        if sqrt((move[0]-last_move[0])**2+(move[1]-last_move[1])**2)>farest:
            best_move=move
            farest=sqrt((move[0]-last_move[0])**2+(move[1]-last_move[1])**2)
    return best_move

def main():
    '''
    main function of the bot. Prints the move
    '''
    player=parse_player()
    # debug(f'player:{player}')
    last_move=(0,0)
    flag=True
    while flag:
        moves=move(player)
        if moves!=[]:
            last_move=select_move(moves, last_move)
        else:
            print(0,0)
            flag=False
        print(last_move[0],last_move[1])

if __name__ == "__main__":
    main()

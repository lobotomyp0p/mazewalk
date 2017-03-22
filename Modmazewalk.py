#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:08:55 2017

Mazewalk V. 2 : Better, Bigger, more Amazing
a 2d random walk through a maze
with benefit of some BATSRUS knowledge

@author: camilla
"""

import random
import matplotlib.pyplot as plt
import numpy as np

def set_cell_face(cells,i,j,bi,bval):
    # for changing a cell boundary
    cells[i][j][bi] = bval

    return cells
    

def init_field(xdim, ydim):
    # initializes the field cells
    # all of them with open boundaries
    cells = []
    for i in np.arange(xdim):
        cells.append([])
    for i in np.arange(xdim):
        for j in np.arange(ydim):
            cells[i].append([0,0,0,0])

    return cells
    
    
def init_maze(cells, xdim, ydim):
    # initializes the maze boundaries
    # 0 is pass-through
    # 1 is solid
    
    # West boundary
    for j in np.arange(ydim):
        cells = set_cell_face(cells,0,j,0,1)

    # East boundary
    for j in np.arange(ydim):
        cells = set_cell_face(cells,xdim-1,j,1,1)
    
    # North boundary
    for i in np.arange(xdim):
        cells = set_cell_face(cells,i,0,2,1)
    
    # South boundary
    for i in np.arange(xdim):
        cells = set_cell_face(cells,i,ydim-1,3,1)

    return cells
    
    
def build_exit(cells, i1,j1, i2,j2, bi):
    # defines the exit in the specified cells
    # on the face specified by bi
    if i1 == i2 :
        for j in np.arange(j1,j2):
            cells = set_cell_face(cells, i1,j,bi,3)
    elif j1 == j2 :
        for i in np.arange(i1,i2):
            cells = set_cell_face(cells, i,j1,bi,3)
    else:
        print('!!! Problem with build_exit!')
    
    return cells
    
    
def build_inner_wall(cells, i1,j1, i2,j2):
    # places a wall on the East boundary of a line of cells
    # and the West boundary on the cells to the east of the line
    # or South, and North on the cells to the south
    if i1 == i2 :
        for j in np.arange(j1,j2+1):
            cells = set_cell_face(cells, i1,j, 1,1)
            cells = set_cell_face(cells, i1+1,j, 0,1)
    elif j1 == j2 :
        for i in np.arange(i1,i2+1):
            cells = set_cell_face(cells, i,j1,3,1)
            cells = set_cell_face(cells, i,j1+1,2,1)
    else:
        print('!!! Problem with build_inner_wall!')

    return cells
    
    
def particle_step(i,j, s):
    # pushes a particle to the next cell in direction s
    
    # to the West
    if s == 0: i = i-1
    # to the East
    if s == 1: i = i+1
    # to the North
    if s == 2: j = j-1
    # to the South
    if s == 3: j = j+1
    
    return [i,j]
    

def maze_walk(cells, starti, startj):
    # returns the steps of a random walk through the maze
    # as a list of lists (the indices of where the particle
    # is at this step)
    steps = []
    particle_exit = False

    # the start
    steps.append([starti, startj])
    
    # the loop
    while particle_exit == False:
        # what direction does the particle move? (bi)
        s = random.randint(0,3)
        k = len(steps)-1
        i = steps[k][0]
        j = steps[k][1]
        
        # does it strike the exit?
        if cells[i][j][s] == 3 :
            particle_exit = True
        # does it strike a wall?
        elif cells[i][j][s] == 1 :
            continue
        # does it pass to the next cell?
        elif cells[i][j][s] == 0 :
            steps.append(particle_step(i,j, s))
        else:
            print('!!! Problem with maze_walk!')
            break
            
    return steps
    
def print_maze(cells, si = 0, sj = 0):
    # to print the maze
    # start cell is shaded \u2592
    # no boundary cells are whitespace
    # corners are 3-quadrant blocks
    #   southwest \u2599
    #   southeast \u259F
    #   northwest \u259B
    #   northeast \u259C
    # sides are half blocks
    #   west  \u258C
    #   east  \u2590
    #   north \u2580
    #   south \u2584
    # exits are thin half blocks
    #   west  \u258F
    #   east  \u2595
    #   north \u2594
    #   south \u2581
    field = ''
    for j in np.arange(len(cells[0])):
        row = ''
        for i in np.arange(len(cells)):
            if cells[i][j] == [0,0,0,0]: a = " "
            # sides
            if cells[i][j] == [1,0,0,0]: a = "\u258C"
            if cells[i][j] == [0,1,0,0]: a = "\u2590"
            if cells[i][j] == [0,0,1,0]: a = "\u2580"
            if cells[i][j] == [0,0,0,1]: a = "\u2584"
            # corners
            if cells[i][j] == [1,0,0,1]: a = "\u2599"
            if cells[i][j] == [0,1,0,1]: a = "\u259F"
            if cells[i][j] == [1,0,1,0]: a = "\u259B"
            if cells[i][j] == [0,1,1,0]: a = "\u259C"
            # exits (sides)
            if cells[i][j] == [3,0,0,0]: a = "\u258F"
            if cells[i][j] == [0,3,0,0]: a = "\u2595"
            if cells[i][j] == [0,0,3,0]: a = "\u2594"
            if cells[i][j] == [0,0,0,3]: a = "\u2581"
            if i == si and j == sj: a = "\u2592"
            row = row + a
        field = field + "\n" + row
    
    return field
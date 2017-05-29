#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:46:41 2017

@author: camilla
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import Modmazewalk as mz

# initiate a 10x10 field
xdim = 10
ydim = 10
cells = mz.init_field(xdim,ydim)

# print the initial empty field
print(mz.print_maze(cells))

# bound a 10x10 maze
mxdim = xdim
mydim = ydim
cells = mz.init_maze(cells,mxdim,mydim)

# print the maze walls
print(mz.print_maze(cells))

# put the 2 cell exit in the northwest corner
cells = mz.build_exit(cells, mxdim-1,1, mxdim-1,3, 1)

# print the maze with its exit
print(mz.print_maze(cells))

# place an internal wall
cells = mz.build_inner_wall(cells, 3,0, 3,4)
# cells = mz.build_inner_wall(cells, 0,3, 3,3)

# print the maze with its internal wall
print(mz.print_maze(cells))

# walk a particle through the maze, beginning at the cell
# indicated by "start", until it reaches the exit
start = [0,4]
steps = mz.maze_walk(cells, start[0], start[1])
print('This particle took {} steps to finish the maze.'.format(len(steps)))

# print the maze and highlight the initial position
printi = True
print(mz.print_maze(cells, printi, start[0], start[1]))

# print the maze and highlight some later position
step = steps[50]
print(mz.print_maze(cells, printi, step[0], step[1]))

# walk many particles through the maze
n = 5000
ttx = np.zeros(n) # ttx -> time to exit. sorry.
for i in np.arange(n):
    ttx[i] = len(mz.maze_walk(cells, start[0], start[1]))

# make a histogram of how long it took them to get through
n, bins, patches = plt.hist(ttx, 70, facecolor='green', alpha=0.75)
plt.xlabel('Steps to exit maze')
plt.ylabel('Number of Particles')
plt.grid(True)

plt.show()

# questions we can address with this then
# how does maze size affect time to completion dist
# how does exit placement affect time to completion dist
# how does a wall affect time to completion dist
# how does exit size affect time to completion dist
# can we determine a mean, stdev for these dists (yes) (how)
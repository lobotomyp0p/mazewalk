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

# initiate a 6x6 field
xdim = 10
ydim = 10
cells = mz.init_field(xdim,ydim)

# bound a 6x6 maze
mxdim = xdim
mydim = ydim
cells = mz.init_maze(cells,mxdim,mydim)

# put the length = 2 exit in the northwest corner
cells = mz.build_exit(cells, mxdim-1,1, mxdim-1,3, 1)

# place an internal wall
cells = mz.build_inner_wall(cells, 3,0, 3,4)
# cells = mz.build_inner_wall(cells, 0,3, 3,3)

# walk a particle through the maze, beginning at the cell
# indicated by "start", until it reaches the exit
start = [0,4]
steps = mz.maze_walk(cells, start[0], start[1])
print(len(steps))

# print the maze
print(mz.print_maze(cells, start[0], start[1]))

## walk many particles through the maze
#n = 5000
#ttx = np.zeros(n)
#for i in np.arange(n):
#    ttx[i] = len(mz.maze_walk(cells, start[0], start[1]))

## make a histogram of how long it took them to get through
#n, bins, patches = plt.hist(ttx, 50, facecolor='green', alpha=0.75)
#plt.xlabel('Time to exit maze')
#plt.ylabel('# Particles')
##plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
#
#plt.show()

# questions we can address here then
# how does maze size affect time to completion dist
# how does exit placement affect time to completion dist
# how does a wall affect time to completion dist
# how does exit size affect time to completion dist
# can we determine a mean, stdev for these dists (yes) (how)
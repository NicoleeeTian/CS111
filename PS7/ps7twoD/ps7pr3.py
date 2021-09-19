#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *

def alive_neighbors(posnr, posnc, grid):
    """return the number of neighbors that still alive around posnr posnc
    input: grid is a 2-D list. We assume that all of the cell
        values are integers 1 and 0.
        posnr and posnc represents inner element of the gird
    """
    total=0
    for r in range(posnr-1, posnr+2):
        for c in range(posnc-1, posnc+2):
            if grid[r][c]==1:
                total+=1
    if grid[posnr][posnc]==1:
        return total-1
    else:
        return total


def next_gen(grid):
    """ create and retrun a new 2-D list representing the next generaton of cells
    input: grid is a 2-D list. We assume that all of the cell
        values are integers 1 and 0.
    """
    new_grid=copy(grid)
    for r in range(1,len(grid)-1):
        for c in range(1, len(grid[0])-1):
            if new_grid[r][c]==1:
                if alive_neighbors(r, c, grid)<2:
                    new_grid[r][c]=0
                elif alive_neighbors(r, c, grid)>3:
                    new_grid[r][c]=0
            else:
                if alive_neighbors(r, c, grid)==3:
                    new_grid[r][c]=1
    return new_grid
### Author: Sam Delaney
### Modified by Sebastius for the SHA2017 Badge
### (made during prototype phase, may not work on release software)
### Description: Game of Life
### Category: Games
### License: MIT
### Appname: GoL
### Built-in: no

import math
import array
import os
import badge
import urandom

def game_of_life():
    badge.eink_init()
    badge.ugfx_init()
    badge.clear(badge.WHITE)
    badge.flush()
    width = 37
    height = 16
    cell_width = 8
    cell_height = 8
    grid = [[0 for x in range(height)] for y in range(width)]

    def seed():
        for x in range(0, width-1):
            for y in range(0, height-1):
                if urandom.getrandbits(30) % 2 == 1:
                    grid[x][y] = 1
                else:
                    grid[x][y] = 0

    def display():
        for x in range(0, width):
            for y in range(0, height):
                if grid[x][y] == 1:
                    badge.area(x*cell_width,y*cell_height, cell_width, cell_height, badge.BLACK)
                else:
                    badge.area(x*cell_width,y*cell_height, cell_width, cell_height, badge.WHITE)
        badge.flush()

    def step():
        changed = 0
        for x in range(1, width):
            for y in range(1, height):
                n = 0
                # 1. tl
                if x > 0 and y > 0 and grid[x-1][y-1] == 1:
                    n += 1
                # 2. t
                if y > 0 and grid[x][y-1] == 1:
                    n += 1
                # 3. tr
                if x < width-1 and y > 0 and grid[x+1][y-1] == 1:
                    n += 1
                # 4. l
                if x > 0 and grid[x-1][y] == 1:
                    n += 1
                # 5. r
                if x < width-1 and grid[x+1][y] == 1:
                    n += 1
                # 6. bl
                if x > 0 and y < height-1 and grid[x-1][y+1] == 1:
                    n += 1
                # 7. b
                if y < height-1 and grid[x][y-1] == 1:
                    n += 1
                # 8. br
                if x < width-1 and y < height-1 and grid[x+1][y+1] == 1:
                    n += 1

                if grid[x][y] == 1:
                    changed  += 1
                    if n < 2:
                        grid[x][y] = 0
                    elif n > 3 :
                        grid[x][y] = 0
                    else:
                        grid[x][y] = 1
                elif n == 3:
                    grid[x][y] = 1
                    changed += 1

        if changed > 0:
            return True
        else:
            return False

    seed()
    g = 0
    while True:
        g += 1
        display()
        if step() is False or g > 50:
            seed()
            g = 0

game_of_life()

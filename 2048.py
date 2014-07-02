"""
Clone of 2048 game.
"""

import poc_2048_gui        
from random import randint

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    count_merge = 0
    count_line_after = 0
    line_after = [0] * len(line)

    for count_line in range(len(line)):
        if line[count_line] != 0:
            if count_line_after > 0 and count_merge == 0 and line_after[count_line_after-1] == line[count_line]:
                line_after[count_line_after-1] += line[count_line]
                count_merge += 1
            else:
                line_after[count_line_after] = line[count_line]
                count_line_after += 1
                count_merge = 0
    return line_after

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width  = grid_width
        self.reset()
        self.initial_dict = {UP: [], DOWN: [], LEFT: [], RIGHT: []}      
        for i in range(grid_width):
            self.initial_dict[UP].append([0, i])
            self.initial_dict[DOWN].append([grid_height - 1, i])
        for i in range(grid_height):
            self.initial_dict[LEFT].append([i, 0])
            self.initial_dict[RIGHT].append([i, grid_width - 1])
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.cell = [[0 for _col in range(self.grid_width)] for _row in range(self.grid_height)]       
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in range(self.grid_width):
            print self.cell[row]

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        movedcell = [[0 for _col in range(self.grid_width)] for _row in range(self.grid_height)]       
        for inital_tile in self.initial_dict[direction]:
            if direction == UP or direction == DOWN:
                temp_list = [0] * self.grid_height
                for i in range(self.grid_height):
                    temp_list[i] = self.cell[inital_tile[0] + i*OFFSETS[direction][0]][inital_tile[1] + i*OFFSETS[direction][1]]
            else:
                temp_list = [0] * self.grid_width
                for i in range(self.grid_width):
                    temp_list[i] = self.cell[inital_tile[0] + i*OFFSETS[direction][0]][inital_tile[1] + i*OFFSETS[direction][1]]
            merge_list = merge(temp_list)
            if direction == UP or direction == DOWN:
                for i in range(self.grid_height):
                    movedcell[inital_tile[0] + i*OFFSETS[direction][0]][inital_tile[1] + i*OFFSETS[direction][1]] = merge_list[i]
            else:
                for i in range(self.grid_width):
                    movedcell[inital_tile[0] + i*OFFSETS[direction][0]][inital_tile[1] + i*OFFSETS[direction][1]] = merge_list[i]
        if movedcell != self.cell:
            self.cell = movedcell
            self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        zeros = sum([1 for sublist in self.cell for item in sublist if item == 0])
        new_tile_position =  randint(0, zeros-1)
        count_zero = 0
        for width in range(self.grid_width):
            for height in range(self.grid_height):
                if count_zero != new_tile_position and self.cell[height][width] == 0:
                   count_zero += 1
                elif  self.cell[height][width] == 0:
                    self.cell[height][width] = 2 if randint(0,9) > 0 else 4
                    return
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.cell[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.cell[row][col]
 
    
poc_2048_gui.run_gui(TwentyFortyEight(2, 3))
#foo = TwentyFortyEight(4, 4)
#foo.set_tile(3, 2, 2)
#foo.set_tile(2, 0, 2)
#foo.__str__()
#foo.move(UP);foo.__str__()

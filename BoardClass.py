'''
Gameplay logic for CS 5001 Final Project
Game 2048
Author: Kate Saslow
'''

import random
import numpy as np

class Board:
    '''
    This class represents a 2048 Board. It allows you to construct
    a new Board for the 2048 game and represents all the logic involved
    with actually playing the game, such as shifting the board either
    up/down/left/right, adding a random 2/4 on the board, and keeping
    score until the game is over. 
    Attributes:
    - array: the 2D matrix (nested lists) that represents the game board
    - score: the user's score while playing the game
    Methods:
    - initialize_array(): this method initializes the game board (an empty
    matrix save for either a random 2 and 4 or 2 random 2s)
    - merge_up(): this method merges the board up, combining any like numbers
    shifted into each other
    - merge_down(): this method merges the board down, combining any like
    numbers shifted into each other
    - merge_right(): this method merges the board right, combining any like
    numbers shifted into each other
    - merge_left(): this method merges the board left, combining any like
    numbers shifted into each other
    - add_2or4(): this method randomly places either a 2 or 4 in an empty
    spot on the board after each merge_() method is called
    - get_array(): this method returns the state of the array of the board
    - get_score(): this method returns the current score of the gameboard
    - game_over(): this method tracks the status of the game with a Bool
    depending on whether the game is over or not.
    '''

    def __init__(self):
        '''
        This method is the constructor. It initiates the game board
        with an empty array, save 2 randomly initiated numbers. Either
        2 and 2 or 2 and 4.
        The necessary attributes for class Board are array and score.
        Preconditions:
        - The values within the array must be integer values.
        - The values within the array must be a factor of 2, from 0 (empty)
        to 2048 (when the game ends).
        - The board must be a 4x4 grid with exactly 4 rows and exactly 4
        columns. 
        '''
        # initialize the starting array of game board 
        self.array = self.initialize_array()
        self.score = 0
               

    def __str__(self):
        '''
        This method determines what printing the object should return
        and how the output should look (e.g. matrix, not nested lists)
        '''
        array_as_str = ""
        for row in self.array:
            row_contents = ""
            for item in row:
                row_contents += "|" + str(item)
            array_as_str += row_contents + "\n"
            
        return array_as_str

        
    def initialize_array(self):
        '''
        This function initiatlizes the array to initiate the
        Board object. The array must start as an empty array, save for
        2 randomly placed numbers. Either 2 and 2 or 2 and 4.
        Returns:
        - The starting game matrix for the Board __init__ method to use
        '''
        array = []
        # initiate a 4x4 matrix
        for i in range(4):
            array.append(([0] * 4))

        # place numbers at random row/col
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        r2 = random.randint(0, 3)
        c2 = random.randint(0, 3)
        r3 = random.randint(0, 3)
        c3 = random.randint(0, 3)
        # potential starting values on board either 2 and 2 or 2 and 4
        starters = [2, 4]

        if array[r][c] == 0:
            array[r][c] = 2
        if array[r2][c2] == 0:  
            array[r2][c2] = random.choice(starters)
        # in case a random element is chosen twice, do it a third time.
        else: 
            array[r3][c3] = random.choice(starters)

        return array
    
    # HELPER FUNCTION for all vertical movement in game
    def get_columns(self):
        '''
        This method is a helper function that accesses the self.array
        matrix and reads the column-wise values to return as a
        2D, flattened array. 
        Returns:
        - The column-wise values as a new nested list.
        '''
        columns = []
        col0 = [row[0] for row in self.array]
        col1 = [row[1] for row in self.array]
        col2 = [row[2] for row in self.array]
        col3 = [row[3] for row in self.array]
        columns.append(col0)
        columns.append(col1)
        columns.append(col2)
        columns.append(col3)

        return columns

    # HELPER FUNCTION for merge_up
    def shift_up(self, array):
        '''
        This method is a helper function to merge the elements in the grid.
        Parameters:
        - Inputs: an array (nested lists)
        - Returns: the shifted up COLUMNS of the 2-D array. The columns will
        be further manipulated in the merge_up() function before being
        transposed back to rows 
        '''
        # SWAP the non-zero values with the zero values in the columns
        # remove zeros from columns and append them to end
        columns = self.get_columns()
        shifted_vals = []
        temp_zeros = []
        for column in columns:
            for val in column:
                # add vals to shift to temporary list
                shifted_vals_temp = [val for val in column if val != 0]
                # add zeros to temporary list
                temp_zeros = [val for val in column if val == 0]
                # append zeros to end of shifted_vals list
                shifted_vals_temp.extend(temp_zeros)
            # append each shifted sublist back to nested list
            shifted_vals.append(shifted_vals_temp)

        return shifted_vals

    # HELPER FUNCTION for merge grid
    def shift_down(self, array):
        '''
        This method is a helper function to merge the elements in the grid.
        Parameters:
        - Inputs: an array (nested lists)
        - Returns: the shifted down COLUMNS (nested lists) of the 2-D array.
        The columns will be further manipulated in the merge_down() function
        before being transposed back rows. 
        ''' 

        # same logic as shift_up but reversed: remove non-zeros and reappend
        columns = self.get_columns()
        shifted_vals = []
        for column in columns:
            for val in column:
                shifted_zeros = [val for val in column if val == 0]
                temp_vals = [val for val in column if val != 0]

                shifted_zeros.extend(temp_vals)
            shifted_vals.append(shifted_zeros)
    
        return shifted_vals

    # HELPER FUNCTION for merge grid
    def shift_left(self, array):
        '''
        This method is a helper function to merge the elements in the grid.
        Parameters:
        - Inputs: an array (nested lists)
        - Returns: the shifted left rows (nested lists) of the matrix.
        '''

        shifted_vals = []
        for row in array:
            for val in row:
                # add non-zero vals to temporary list
                shifted_vals_temp = [val for val in row if val != 0]
                # add zero vals to temporary list
                temp_zeros = [val for val in row if val == 0]
                # append zeros to end of shifted-vals list
                shifted_vals_temp.extend(temp_zeros)
            shifted_vals.append(shifted_vals_temp)

        return shifted_vals

    # HELPER FUNCTION for merge grid
    def shift_right(self, array):
        '''
        This method is a helper function to merge the elements in the grid.
        Parameters:
        - Inputs: an array (nested lists)
        - Returns: the shifted right rows (nested lists) of the matrix.
        '''

        # similar logic to shift_left, just reversed
        shifted_vals = []
        for row in array:
            for val in row:
                shifted_zeros = [val for val in row if val == 0]
                temp_vals = [val for val in row if val != 0]

                shifted_zeros.extend(temp_vals)
            shifted_vals.append(shifted_zeros)
            result = shifted_vals
        return result

    def merge_up(self):
        '''
        This method merges the game board in the upward direction.
        All values shift up in their columns, and where any value merges
        upward into an equal value, those 2 values merge, turning into
        double that value. The score also increases by that doubled
        value. Example: If a 4 and a 4 are adjacent in a column and
        the board is merged up, those two 4 tiles become one 8 tile
        and the score increases by 8 points. 
        '''
        score = self.score
        # put array in shifted-up state
        array_shifted = self.shift_up(self.array)
        # similar logic to merge right/left, but use columns instead of rows
        # helper func shift_up() returns COLUMNS in array, not rows.
        merged_vals = []
        for row in array_shifted:
            # iterate left to right to compare vals
            for i in range(1, len(row)):
                # compare to val on LEFT
                if row[i] == row[i - 1]:
                    # 2 like values merging together become twice that value
                    row[i - 1] = 2 * (row[i])
                    # score increases by that doubled val
                    score += (2 * (row[i]))
                    # replace 1 of merged tiles with empty val
                    row[i] = 0
            merged_vals.append(row)
        # shift again to remove the 0 that replaced the merged value
        result = self.shift_left(merged_vals)
        # transpose to turn columns into rows 
        result = np.transpose(result)
        self.array = result
        self.score = score

            
    def merge_down(self):
        '''
        This method merges the game board in the downward direction.
        All values shift down in their columns, and where any value
        merges downward into an equal value, those 2 values merge, turning
        into double that value. The score also increases by that doubled
        value. 
        '''
        score = self.score
        # put array in shifted-down state
        array_shifted = self.shift_down(self.array)
        # similar logic to merge_right/left, but use columns instead of rows
        # shift_down() returns COLUMNS in array, not rows. 
        merged_vals = []
        for row in array_shifted:
            # iterate from right to left so that vals on right side merge
            for i in reversed(range(0, len(row) - 1)):
                # compare to value on the RIGHT
                if row[i] == row[i + 1]:
                    row[i + 1] = 2 * (row[i])
                    score += (2 * (row[i]))
                    row[i] = 0
            merged_vals.append(row)
        # shift_right again to remove 0s from merged tiles
        result = self.shift_right(merged_vals)
        # transpose to turn columns into rows
        result = np.transpose(result)
        self.array = result
        self.score = score

    def merge_right(self):
        '''
        This method merges the game board in the rightward direction.
        All values shift right in their rows, and where any value merges
        rightward into an equal value, those 2 values merge, turning into
        double that value. The score also increases by that doubled
        value.
        '''
        score = self.score
        # put array in shifted-right state
        array = self.shift_right(self.array)
        merged_vals = []
        for row in array:
            # iterate from right to left so vals on right side merge
            for i in reversed(range(len(row) - 1)):
                # compare to value on the right
                if row[i] == row[i + 1]:
                    row[i + 1] = 2 * (row[i])
                    # add merged vals to score
                    score += (2 * (row[i]))
                    row[i] = 0
            merged_vals.append(row)
        # need to shift_right again to remove 0s from merged tiles
        result = self.shift_right(merged_vals)
        self.array = result
        self.score = score

    def merge_left(self):
        '''
        This method merges the game board in the leftward direction.
        All values shift left in their rows, and where any value merges
        leftward into an equal value, those 2 values merge, turning into
        double that value. The score also increases by that doubles value
        '''
        score = self.score
        # similar logic to merge_right, but compare to the left side:
        array = self.shift_left(self.array)
        merged_vals = []
        for row in array:
            pos = 0
            for i in range(1, len(row)):
                # compare to value on the left
                if row[i] == row[i - 1]:
                    row[i - 1] = 2 * (row[i])
                    score += (2 * (row[i]))
                    row[i] = 0
            merged_vals.append(row)
        # need to shift_left again to remove 0s from merged tiles 
        result = self.shift_left(merged_vals)
        self.array = result
        self.score = score

    # HELPER FUNCTION to determine status of game
    def right_move_possible(self):
        '''
        This method is a helper function that determines if there is a
        possible merge_right move left on the board.
        An array can be merged right iff:
        - there exists an empty space in the row
        - there are 2 numbers next to each other that can be merged
        Method returns Bool: True if right_move_possible
        '''

        for i in range(0, 3):
            for j in range(0, 3):
                # if 2 non-zero numbers next to each other
                if self.array[i][j] == self.array[i][j + 1] \
                    and self.array[i][j] != 0:
                    return True
                elif self.array[i][j] != 0 and self.array[i][j + 1] == 0:
                    return True
        return False

    # HELPER FUNCTION to determine status of game
    def left_move_possible(self):
        '''
        This method is a helper function that determines if there is a
        possible merge_left move left on the board.
        An array can be merged left iff:
        - there exists an empty space in the row
        - there are 2 numbers next to each other that can be merged
        Method returns Bool: True if left_move_possible
        '''
        
        for i in range(0, 3):
            for j in range(0, 3):
                # if 2 non-zero numbers next to each other
                if self.array[i][j] == self.array[i][j + 1] \
                   and self.array[i][j] != 0:
                    return True
                elif self.array[i][j] == 0 and self.array[i][j + 1] != 0:
                    return True
        return False
    
    # HELPER FUNCTION to determine status of game
    def up_move_possible(self):
        '''
        This method is a helper function that determines if there is a
        possible merge_up move left on the board.
        An array can be merged up iff:
        - there exists an empty space in the column
        - there are 2 numbers adjacent in column that can be merged
        Method returns Bool: True if up_move_possible
        '''
        
        columns = self.get_columns()
        for i in range(0, 3):
            for j in range(0, 3):
                # if 2 non-zero numbers next to each other
                if columns[i][j] == columns[i][j + 1] \
                   and columns[i][j] != 0:
                    return True
                elif columns[i][j] == 0 and columns[i][j + 1] != 0:
                    return True
        return False

    # HELPER FUNCTION  to determine status of game
    def down_move_possible(self):
        '''
        This method is a helper function that determines if there is a
        possible merge_down move left on the board.
        An array can be merged up iff:
        - there exists an empty space in the column
        - there are 2 numbers adjacent in column that can be merged
        Method returns Bool: True if down_move_possible
        '''
        
        columns = self.get_columns()
        for i in range(0, 3):
            for j in range(0, 3):
                # if 2 non-zero numbers next to each other
                if columns[i][j] == columns[i][j + 1] \
                    and columns[i][j] != 0:
                    return True
                elif columns[i][j] != 0 and columns[i][j + 1] == 0:
                    return True
        return False
                

    
    def add_2or4(self):
        '''
        This function adds a new 2 or 4 to the board after each move.
        In the game, the 2 should be added after 2 numbers merged into
        each other have already been combined.
        Parameters:
        Inputs: array (nested lists)
        Returns: the same array with an additional 2 or 4 added to a
        previously empty cell. 
        '''
        # after each move, a new 2 or 4 is added to an empty spot in board 
        choices = [2, 4]
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        # while loop to only add 2/4 to an empty spot in array
        while self.array[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.array[row][col] = random.choice(choices)


    def get_array(self):
        '''
        This method gets and returns the current game board
        '''
        return self.array

    def get_score(self):
        '''
        This method gets and returns the current score of the game
        '''
        return self.score

    def game_over(self):
        '''
        This method helps see the status of the game. If 2048 on board,
        the user wins and the game is over. If no 2048, no empty spaces
        left on board, and no possible shift in any direction,
        the user loses and the game is over
        '''
        # initiate game_over to False until specific conditions met
        game_over = False

        # if 2048 on board: user wins
        for row in self.array:
            for val in row:
                if val == 2048:
                    print("YOU WIN!!")
                    game_over = True
                    return game_over

        # if merge up/down/left/right still possible: game not over
        # if merges not possible, game over: user loses
        if not self.right_move_possible() and \
           not self.left_move_possible() and \
           not self.up_move_possible() and \
           not self.down_move_possible():
            print("Game Over! You lose ...")
            game_over = True
            return game_over
        
        else:
            game_over = False
            return game_over

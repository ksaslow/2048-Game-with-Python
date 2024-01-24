'''
Testing Board:
Create BoardTest class that tests Board.
Inherits from unittest.TestCase

Author: Kate Saslow
'''

from BoardClass import Board
import unittest
import numpy as np

class BoardTest(unittest.TestCase):
    '''
    Class BoardTest, uses PyUnit framework.
    Inherits from unittest.TestCase
    '''

    def test_constructor(self):
        '''
        This method tests the constructor of the
        Board class. It tests that the attributes of the class
        to make sure they are updated accordingly as the game
        is played.
        '''
        
        board = Board()
        
        # test attribute board.array
        # test that 16 values are initiated to 4 lists:
        self.assertEqual(len(board.array), 4)
        for row in board.array:
            # test that each sublist has 4 values
            self.assertEqual(len(row), 4)

        # test attribute board.score
        # score must be initialized to 0
        self.assertEqual(board.score, 0)

    def test_str(self):
        '''
        This tests that the __str__ method prints the output of the
        object instance correctly. 
        '''
        # make sure output is equal
        board = Board()
        # create empty array just to test that formatting is correct
        board.array = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        expected_output = "|0|0|0|0\n|0|0|0|0\n|0|0|0|0\n|0|0|0|0\n"
                        
        self.assertEqual(board.__str__(), expected_output)

    def test_initialize_array(self):
        '''
        This method tests the helper function that initializes the board
        matrix within the __init__ constructor. The array that is initialized
        at the start of a game, and when the object instance is called, must
        have exactly 2 non-zero values, and those values can only be either
        2 or 4
        '''
        board = Board()
        # test that only 2 values are initialized to the board.array:
        non_zero_vals = []
        for row in board.array:
            for val in row:
                if val != 0:
                    non_zero_vals.append(val)
        self.assertEqual(len(non_zero_vals), 2)

        # test that only 2s and 4s are initialized to board.array:
        chars_accepted = [2, 4]
        for val in non_zero_vals:
            self.assertIn(val, chars_accepted)

    def test_merge_up(self):
        '''
        This method tests the merge_up method of the Board class that
        shifts the values in the matrix upward. All non-zero values in
        the 4 columns of the matrix are shifted to the top of the columns.
        If any 2 values are adjacent in the columns and shifted into each
        other, those two values are merged together, and the value doubles.
        For example, if there are two 2s adjacent in a column, the uppermost 2
        will become a 4, and the lower 2 is replaced by the values below it
        in the column.
        '''
        
        board = Board()
        # test normal instance of merge_up() to make sure functions correctly
        board.array = [[0,0,0,0],[2,0,0,0],[0,0,0,2],[0,0,0,0]]
        board.merge_up()
        # merge_up result is an array, change to list to assertEqual
        test_list = board.array.tolist()
        self.assertEqual(test_list,
                         [[2,0,0,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

        # test case where 2 like values merge into each other and combine
        board.array = [[2,0,2,0],[4,0,0,16],[2,4,8,16],[2,4,8,16]]
        board.merge_up()
        test_list = board.array.tolist()
        self.assertEqual(test_list,
                         [[2,8,2,32],[4,0,16,16],[4,0,0,0],[0,0,0,0]])

        # test case where 3 like values adjacent
        # the uppermost 2 values should be merged together, not lowest val
        board.array = [[2,0,0,0],[2,0,0,0],[2,0,0,0],[0,0,0,0]]
        board.merge_up()
        test_list = board.array.tolist()
        self.assertEqual(test_list,
                         [[4,0,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]])

        # test case where no merge_up possible - no change
        board.array = [[4,8,2,16],[8,32,4,8],[2,64,16,4],[4,16,512,8]]
        # make copy to test if it stays the same
        copy = board.array
        board.merge_up()
        test_list = board.array.tolist()
        self.assertEqual(copy, test_list)

        # test helper method up_move_possible() where no merge_up possible
        self.assertFalse(board.up_move_possible())

    def test_merge_down(self):
        '''
        This method tests the merge_down method of the Board class that
        shifts the values in the matrix downward. All non-zero values in
        the 4 columns of the matrix are shifted to the bottom of the columns.
        If any 2 values are adjacent in the columns and shifted into each
        other, those two values are merged together, and the value doubles.
        For example, if there are two 2s adjacent in a column, the lowermost
        2 will become a 4, and the uppermost 2 is replaced by the values
        above it in the column.
        '''

        board = Board()
        # test normal instance of merge_down() to make sure works correctly
        board.array = [[0,0,0,0],[2,0,0,0],[0,0,0,2],[0,0,0,0]]
        board.merge_down()
        # merge_down result is an array, change to list to assertEqual
        test_list = board.array.tolist()
        self.assertEqual(test_list, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[2,0,0,2]])

        # test case where 2 like values merge into each other and combine
        board.array = [[2,0,2,0],[4,0,0,16],[2,4,8,16],[2,4,8,16]]
        board.merge_down()
        test_list = board.array.tolist()
        self.assertEqual(test_list,
                         [[0,0,0,0],[2,0,0,0],[4,0,2,16],[4,8,16,32]])

        # test case where 3 like values adjacent
        # the lowermost 2 values should be merged together, not upper val
        board.array = [[2,2,0,0],[2,4,0,0],[2,4,0,0],[0,0,0,0]]
        board.merge_down()
        test_list = board.array.tolist()
        self.assertEqual(test_list, [[0,0,0,0],[0,0,0,0],[2,2,0,0],[4,8,0,0]])

        # test case where no merge_down possible - no change
        board.array = [[4,8,2,16],[8,32,4,8],[2,64,16,4],[4,16,512,8]]
        copy = board.array
        board.merge_down()
        test_list = board.array.tolist()
        self.assertEqual(copy, test_list)

        # test helper method down_move_possible() where no merge_down possible
        self.assertFalse(board.down_move_possible())

    def test_merge_right(self):
        '''
        This method tests the merge_right method of the Board class that
        shifts the values in the matrix rightward. All non-zero values in
        the 4 rows of the matrix are shifted to the right of the rows.
        If any 2 values are adjacent in the rows and shifted into each other,
        those two values are merged together, and the value doubles.
        For example, if there are two 2s adjacent in a row, the right most
        2 will become a 4, and the left most 2 is replaced by the values
        next to it in the row.
        '''

        board = Board()
        # test normal instance of merge_right() to make sure works correctly
        board.array = [[0,0,0,0],[0,0,2,0],[2,0,0,0],[0,0,0,0]]
        board.merge_right()
        self.assertEqual(board.array,
                         [[0,0,0,0],[0,0,0,2],[0,0,0,2],[0,0,0,0]])

        # test case where 2 like values merge into each other and combine
        board.array = [[0,0,0,0],[2,2,0,0],[0,0,4,0],[8,4,0,0]]
        board.merge_right()
        self.assertEqual(board.array,
                         [[0,0,0,0],[0,0,0,4],[0,0,0,4],[0,0,8,4]])

        # test case where 3 like values adjacent
        # the right-most 2 values should be merged together, not left most val
        board.array = [[2,2,2,2],[2,2,2,4],[0,0,0,0],[0,0,0,0]]
        board.merge_right()
        self.assertEqual(board.array,
                         [[0,0,4,4],[0,2,4,4],[0,0,0,0],[0,0,0,0]])

        # test case where no merge_right possible - no change
        board.array = [[4,8,2,16],[8,32,4,8],[2,64,16,4],[4,16,512,8]]
        copy = board.array
        board.merge_right()
        self.assertEqual(board.array, copy)

        # test helper method right_move_possible where no merge_right possible
        self.assertFalse(board.right_move_possible())

    def test_merge_left(self):
        '''
        This method tests the merge_left method of the Board class that
        shifts the values in the matrix leftward. All non-zero values in
        the 4 rows of the matrix are shifted to the left of the rows.
        If any 2 values are adjacent in the rows and shifted into each other,
        those two values are merged together, and the value doubles.
        For example, if there are two 2s adjacent in a row, the left most
        2 will become a 4, and the right most 2 is replaced by the values
        next to it in the row.
        '''

        board = Board()
        # test normal instance of merge_left() to make sure works correctly
        board.array = [[0,0,0,0],[0,0,2,0],[0,0,0,2],[0,0,0,0]]
        board.merge_left()
        self.assertEqual(board.array,
                         [[0,0,0,0],[2,0,0,0],[2,0,0,0],[0,0,0,0]])

        # test case where 2 like values merge into each other and combine
        board.array = [[0,0,0,0],[2,2,0,0],[0,0,4,0],[8,4,0,0]]
        board.merge_left()
        self.assertEqual(board.array,
                         [[0,0,0,0],[4,0,0,0],[4,0,0,0],[8,4,0,0]])

        # test where 3 like values adjacent
        # the left-most 2 values should be merged together, not right most val
        board.array = [[2,2,2,2],[2,2,2,4],[0,0,0,0],[0,0,0,0]]
        board.merge_left()
        self.assertEqual(board.array,
                         [[4,4,0,0],[4,2,4,0],[0,0,0,0],[0,0,0,0]])

        # test where no merge_left possible - no change
        board.array = [[4,8,2,16],[8,32,4,8],[2,64,16,4],[4,16,512,8]]
        copy = board.array
        board.merge_left()
        self.assertEqual(board.array, copy)

        # test helper method left_move_possible where no merge_left possible
        self.assertFalse(board.left_move_possible())

    def test_add_2or4(self):
        '''
        This method test the add_2or4() method of the Board class. After each
        move, a 2 or 4 should be added to the board randomly in one of the
        "empty" spaces (where val = 0). 

        '''

        board = Board()
        board.array = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        board.add_2or4()

        # test that only 2 or 4 added
        chars_accepted = [2, 4]
        for row in board.array:
            for val in row:
                if val != 0:
                    self.assertIn(val, chars_accepted)

        # test that only one new val added
        non_zeros = []
        for row in board.array:
            for val in row:
                if val != 0:
                    non_zeros.append(val)
        self.assertEqual(len(non_zeros), 1)

    def test_get_array(self):
        '''
        This tests the get_array() method from Board
        '''
        board = Board()
        self.assertEqual(board.get_array(), board.array)

    def test_get_score(self):
        '''
        This tests the get_score() method from the Board
        '''
        board = Board()
        self.assertEqual(board.get_score(), board.score)

        # test that the score is being counted correctly
        # if two 4s merge into each other, score = 8
        board.array = [[4,4,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        board.merge_left()
        score = board.get_score()
        self.assertEqual(score, 8)

        # if multiple values merge/double, score captures all merged vals
        # array below should ADD 28 points to the score
        # since board.score attribute not reset, this will add 28 points to 8
        board.array = [[4,4,8,8],[2,2,0,0],[0,0,0,0],[0,0,0,0]]
        board.merge_right()
        score = board.get_score()
        self.assertEqual(score, 36)

    def test_game_over(self):
        '''
        This method tests the game_over() methof from the Board class.
        The game_over() determines the status of the game at every play
        of the board. This method should return True/False depending
        on whether the game is over.
        '''
        board = Board()

        # test that game_over == True if 2048 on board:
        board.array = [[64,32,4,4],[512,16,8,2],[2048,64,32,16],[2,2,0,0]]
        self.assertTrue(board.game_over())

        # test that game_over == True if no more moves are possible
        board.array = [[4,8,2,16],[8,32,4,8],[2,64,16,4],[4,16,512,8]]
        self.assertTrue(board.game_over())

        # test that game_over == False if moves are still possible
        board.array = [[2,2,4,0],[8,4,4,0],[16,2,8,4],[32,8,2,4]]
        self.assertFalse(board.game_over())


def main():
    unittest.main(verbosity=3)

if __name__ == "__main__":
    main()

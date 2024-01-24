'''
Main game driver for CS 5001 Final Project
Includes all Turtle functions 
Game 2048
Author: Kate Saslow
'''
import turtle
import random
import numpy as np
from functools import partial
from BoardClass import Board

# initiate global Turtle instance
t = turtle.Turtle()
# initiate global Board instance
board = Board()
     
def draw_tile(t, val):
    '''
    This function draws a single tile on the game board.
    Input:
    - t: the Turtle instance to draw the board/tile
    - val: value in the array that belongs in that tile
    Returns:
    - a tile on the game board with the appropriate value
    and the appropriate color.
    '''
    # setting color code for tiles
    if val == 0:
        color = 'WhiteSmoke'
    elif val == 2:
        color = '#b3d9ff'
    elif val == 4:
        color = '#B9D1EB'
    elif val == 8:
        color = '#e6e6ff'
    elif val == 16:
        color = '#ccccff'
    elif val == 32:
        color = '#b3b3ff'
    elif val == 64:
        color = '#9999ff'
    elif val == 128:
        color = '#e6ccff'
    elif val == 256:
        color = '#d9b3ff'
    elif val == 512:
        color = '#cc99ff'
    elif val == 1024:
        color = '#ffb3ff'
    elif val == 2048:
        color = '#ff4dff'
    t.pen(fillcolor=color, pencolor = 'gray60', pensize = 5)
    t.fillcolor(color)
    t.fillcolor()
    t.begin_fill()

    # draw border of tile
    for i in range(4):
        t.forward(100)
        t.left(90)
    # change color of turtle pen for darker colors so visible
    if val <= 16:
        t.pen(fillcolor=color, pencolor = 'gray60', pensize = 5)
    else:
        t.pen(fillcolor=color, pencolor='white', pensize=5)
    # position the turtle within square to write 
    t.up()
    t.forward(50)
    t.left(90)
    t.forward(40)
    t.down()
    # don't write 0 on tile, just leave empty if 0
    if val == 0:
        val = ''
    else:
        t.write(val, align='center', font=('Arial', 24, 'bold'))
    t.up()
    t.forward(-40)
    t.left(-90)
    t.forward(-50)
    t.down()

    t.end_fill()


def initiate_board(t, score, array):
    '''
    This function initiates the 2048 game board and draws it with Turtle
    Inputs:
    - score: (int) with the updating score to track on the screen
    - array: (nested list) with the updating array to be drawn at
    each stage of the game. The board updates as the user inputs
    different arrow keys to move the tiles.
    Returns:
    - a new representation of the game board, reflecting the changes
    made to the Board object and the game state
    '''
    t.clear()
    screen = t.getscreen()
    screen.title("2048 BY KATE")
    # add background picture, uploaded to Gradescope with code
    screen.bgpic("turtle_background_new.001.png")
    # adjust the default size of screen
    screen.setup(1000, 1000)
    screen.tracer(0)
    
    x = 0
    y = 0
    val = ""
    
    # iterate through array to set tile's position on screen 
    for rows in range(0, len(array)):
        if rows == 0:
            y = 100
        elif rows == 1:
            y = 0
        elif rows == 2:
            y = -100
        elif rows == 3:
            y = -200

        for col in range(0, len(array[rows])):
            if col == 0:
                x = -200
            elif col == 1:
                x = -100
            elif col == 2:
                x = 0
            elif col == 3:
                x = 100
            
            # set appropriate values to be drawn in specific tile
            val = array[rows][col]
            t.up()
            t.goto(x, y)
            t.down()
            draw_tile(t, val)
    # update score on the board after each move
    draw_score(t, score)
    t.hideturtle()

def end_game(t):
    '''
    This function prints a "GAME OVER!" message to the screen when
    either the game is ended because the game is over, or when the
    user quits the game in the middle of game play.
    Inputs: the global Turtle object defined at beginning of program
    '''
    t.up()
    # print message in the middle of the screen
    t.goto(0, 0)
    t.down()
    t.pen(fillcolor="", pencolor='#ff4dff', pensize=10)
    t.write("GAME OVER!", align="center", font=("Arial Black", 75, "bold"))


def draw_score(t, score):
    '''
    This function draws the score on the board.
    Inputs:
    - t: the global Turtle object defined at beginning of program
    - score: Board.score is the attribute of the Board class that gets
    updated with every change made to the board via user input and should
    be printed to the screen so the user can see the current score.
    '''
    t.speed(0)
    t.pen(fillcolor='white', pencolor= '#ff4dff', pensize=5)
    t.up()
    # print message at top right corner of the screen
    t.goto(280, 280)
    t.write("SCORE: " + str(score), align="center",
            font=("Arial Black", 30, "bold"))
    t.hideturtle()
    

def u(board):
    '''
    This function accepts user input of the up arrow on the keyboard
    and shits/merges the game board upward. The function then adds a new
    2 or 4 randomly to the screen after the move is made to advance the
    game. After a move is made, the function updates the Board object
    and prints the new state of the board to the screen.
    Inputs: the board object, whose array/score attributes are being
    continuously updated
    Returns: This function also prints the current array and score to the
    shell running the game, so that the user can track the moves made
    and progress of the game alongside the Turtle drawing.
    Postcondition: If the game is over after that specific move, the
    game ends by the end_game() function being called and a "GAME OVER"
    message printed to the screen.
    '''
    board.merge_up()
    board.add_2or4()
    initiate_board(t, board.score, board.array)
    print(board)
    print("Score = ", board.get_score())
    if board.game_over() == True:
        end_game(t)
    
    
def d(board):
    '''
    This function accepts user input of the down arrow on the keyboard
    and shits/merges the game board downward. The function then adds a new
    2 or 4 randomly to the screen after the move is made to advance the
    game. After a move is made, the function updates the Board object
    and prints the new state of the board to the screen.
    Inputs: the board object, whose array/score attributes are being
    continuously updated
    Returns: This function also prints the current array and score to the
    shell running the game, so that the user can track the moves made
    and progress of the game alongside the Turtle drawing.
    Postcondition: If the game is over after that specific move, the
    game ends by the end_game() function being called and a "GAME OVER"
    message printed to the screen.
    '''
    board.merge_down()
    board.add_2or4()
    initiate_board(t, board.score, board.array)
    print(board)
    print("Score = ", board.get_score())
    if board.game_over() == True:
        end_game(t)

def l(board):
    '''
    This function accepts user input of the left arrow on the keyboard
    and shits/merges the game board leftward. The function then adds a new
    2 or 4 randomly to the screen after the move is made to advance the
    game. After a move is made, the function updates the Board object
    and prints the new state of the board to the screen.
    Inputs: the board object, whose array/score attributes are being
    continuously updated
    Returns: This function also prints the current array and score to the
    shell running the game, so that the user can track the moves made
    and progress of the game alongside the Turtle drawing.
    Postcondition: If the game is over after that specific move, the
    game ends by the end_game() function being called and a "GAME OVER"
    message printed to the screen.
    '''
    board.merge_left()
    board.add_2or4()
    initiate_board(t, board.score, board.array)
    print(board)
    print("Score = ", board.get_score())
    if board.game_over() == True:
        end_game(t)

def r(board):
    '''
    This function accepts user input of the right arrow on the keyboard
    and shits/merges the game board rightward. The function then adds a new
    2 or 4 randomly to the screen after the move is made to advance the
    game. After a move is made, the function updates the Board object
    and prints the new state of the board to the screen.
    Inputs: the board object, whose array/score attributes are being
    continuously updated
    Returns: This function also prints the current array and score to the
    shell running the game, so that the user can track the moves made
    and progress of the game alongside the Turtle drawing.
    Postcondition: If the game is over after that specific move, the
    game ends by the end_game() function being called and a "GAME OVER"
    message printed to the screen.
    '''
    board.merge_right()
    board.add_2or4()
    initiate_board(t, board.score, board.array)
    print(board)
    print("Score = ", board.get_score())
    if board.game_over() == True:
        end_game(t)

def n(board):
    '''
    This function accepts user input of the "n" key on the keyboard
    and starts a new game. If the "n" key is pressed by the user, the
    array of the Board instance is re-initialized to a starting array,
    and the score gets reset to 0. The board is updated and the user
    can continue playing with the new board/game.
    Inputs: the board object, whose array/score will be reset to start
    setting.
    Returns: A reset game board, score reset to 0, and prints to the shell
    that the user started a new game.
    Preconditions: the user must select the lowercase "n" key to
    start a new game. 
    '''
    board.array = board.initialize_array()
    board.score = 0
    initiate_board(t, board.score, board.array)
    print(board)
    print(board.score)
    print("You chose to start a new game!")


def q(board):
    '''
    This function accepts user input of the "q" key on the keyboard
    and quits the current game. If the "q" key is pressed by the user,
    the end_game() function is called, and the "GAME OVER!" message is
    printed to the Turtle screen to let the user know the game has ended.
    The function also prints to the shell that the game is quitting.
    Inputs: the board object
    Returns: the "GAME OVER!" message to the turtle screen.
    Preconditions: the user must select the lowercase "q" key to
    quit the game.
    '''
    screen = t.getscreen()
    end_game(t)
    print("Quitting ... Bye!")

def main():

    screen  = t.getscreen()
    initiate_board(t, board.score, board.array)
    print(board)
    
    screen.onkeypress(partial(u, board), "Up")

    screen.onkeypress(partial(d, board), "Down")

    screen.onkeypress(partial(l, board), "Left")

    screen.onkeypress(partial(r, board), "Right")
    
    screen.onkeypress(partial(q, board), "q")

    screen.onkeypress(partial(n, board), "n")

    screen.listen()

if __name__ == "__main__":
    main()

# 2048-Game-with-Python
## Author: Kate Saslow

Popular 2048 game designed and built with Python and Turtle, using functional programming for the game logic and OO-design for the GUI

### Introduction

For the final project in CS 5001, I had to write a program to play the 2048 game with Python. 

I chose to build a class Board that implements the logic of the game: shifting the board in the specified direction, merging any like values that are merged into each other, adding a new 2 or 4 to the game after every move, updating the array continuously, updating the score continuously, and tracking the status of the game (whether the game is over or not). 

For all Turtle code, I chose functional design, and passed the Board object to the functions to be manipulated and continuously drawn. 

### Files Uploaded

- BoardClass.py
This file contains all the game logic and design. 
Functions in this file include:
	- \__init\__ to initiate the object instance and game board
	- initialize_array to initialize the 4x4 grid of the game board
	- all directions merge_up/down/left/right functions to shift and merge the values on board
	- add_2or4 to add a new 2 or 4 randomly to an empty space in the board to advance game
	- get_score to find the current score at any stage in game
	- game_over to determine the status of the game, whether over or not

- main.py
This file is the main game driver and contains all Turtle functions. This file contains all of the user interface features of the game.
Functions in this file include:
	- draw_tile to draw a single tile on the screen. This function also keeps the color code for the different vals
	- initiate_board to take the current Board and draw it on the turtle screen. This function is called in order to update the game after each move. Within this function is the Turtle background screen "turtle_background_new.001.png" which was uploaded in the zip to Gradescope
	- end_game to draw "GAME OVER!" on the screen when the game ends, either organically or if the user quits
	- draw_score to update and draw the current score of the game to the Turtle screen
	- u to take the user input from the up arrow on keyboard and merge the game board up
	- d to take the user input from the down arrow on keyboard and merge the game board down
	- l to take the user input from left arrow on keyboard and merge the game board left
	- r to take the user input from the right arrow on the keyboard and merge the game board right
	- n to take the user input from the lowercase "n" key and to start a new game
	- q to take the user input from the lowercase "q" key and to quit the current game
	
- turtle_background_new.001.png
This file contains the background image that is printed to the turtle screen

- TestBoardClass.py
This file contains all the tests for the board logic and game design

### How to run the program 
In order to start playing the game, the user must open the file "main.py" and execute the code. Once the code is executed, a turtle screen will open and the board will be visible. The controls for the game are the 4 arrows on the keyboard. Up, down, left, or right. The user can select which direction to shift the board by pressing said arrow. As the board explains, the user can start a new game at any time by selecting key "n", or the user can quit the current game by pressing the "q" key. The game simultaneously prints the new board to the turtle screen, and tracks the game in the IDLE shell/terminal. In the terminal, you can see all previous states of the board, as well as the score after each move. This functionality was kept not only to ensure that the game runs as planned, but also to give the user a bit more insight into the flow of the game. Messages are also printed to the terminal when the user wins/loses, decides to start a new game, or quits. 

### Features 
This program contains all features laid out in the project descriptions including:
- the screen draws the board with numbers in visible color combinations. Once the tiles are darker (larger values), the number is printed in white instead of grey so that they remain visible
- the player is able to control the game with the arrow keys on the keyboard
- the game keeps track of the score and displays it on the board at all times
- there is a way to end the game at any time ("q"), and this is displayed on the screen at all times
- there is a way to start the game at any time without having to exit and re-run the program ("n"), and this is displayed on the screen at all times
- if the user presses any keys other that the 4 arrows, "n" or "q", the game is not affected
- the program does not crash when the board fills up, instead a "GAME OVER!" message is displayed on the screen so that the user knows that the game has ended and there are no moves left
- this program prints the different values in different colors, so that merges on the board are easily visible and distinguishable

### Thank you for reading and playing! Have fun! 

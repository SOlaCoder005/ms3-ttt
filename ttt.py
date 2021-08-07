# Tic-Tac-Toe Game

"""
Imported Libraries and Modules 
"""
import emoji # Credit: Unicode
import time # Credit: Guru99
import random
# https://www.youtube.com/watch?v=7Djh-Cbgi0E
import os
os.system("clear")


"""
CONST variables
"""

# X = ()
# O = ()
PlayerWon = ""
PlayerLost = ""
PlayerDraw = "DRAW"
BLANK_SPACE = " "
BOARD_SQUARES = 9
GAMEPIECES = {
    "a":"\U0001F9DE", #mermaid
    "b":"\U0001F9D1", #cook
    "c":"\U0001F444", #mouth
    "d":"\U0001F63B", #cat love
    "e":"\U0001F47B", #ghost
    "f":"\U0001F916", #robot head
    "g":"\U0001F47D", #alien
    "h":"\U0001F9E0", #brain
    "i":"\U0001F4A3", #bomb          
}

# - Reference Source: Dawson (2010, pp.181-82)
WINNING_INSTANCES = (
    (0, 1, 2), #horizontal instances
    (3, 4, 5), #horizontal instances
    (6, 7, 8),  #horizontal instances
    (0, 3, 6), #vertical instances
    (1, 4, 7),  #vertical instances
    (2, 5, 8), #vertical instances
    (0, 4, 8),  #diagonal instances
    (2, 4, 6) #diagonal instances
)

def welcome():

    """
    Greets user when they initially run the game.
    """

    print("\nWELCOME TO TIC-TAC-TOE! \U0001F609\n")
    print("This is a place to engage in digital strategic sparing!\n")
    print("Can you put AI in it's place to show it who's boss?\n")
    time.sleep(2)
    print("I hope so...\U0001F914\n")
    time.sleep(3)
    
def r_u_ready_to_play():

    """
    Asks user if they are ready to play.
    """

    yes = "y"
    no = "n" 
    
    while True: 
        
        try: 
            answer = input("\nAre you ready to play (y/n)?:\n")

            if answer == yes:
                print("\nOkay! Here's how to play... \U0001F60E\n")
                return game_guides()
                time.sleep(1.5)

            elif answer == no: 
                print("\n\U0001F92F What! Why not?\n")
                print("\n\U0001F612 Okay, maybe next time.\n")
                time.sleep(1)
                return exit()

            else: 
                raise ValueError()

        except ValueError:
            print(
                f"\nSorry, didn't recognise yourt respnse '{answer}'. Try again..."
            )
 
def game_guides():
    
    """
    Tells user how to play the game.
    """

    print(
    
        """
        \U0001F4DC How it works
        -----------------------
        """
    )
    print(
        """ 
        Your battle-ground is formed of 9 squares and looks like this: 

                            0  |  1  |  2
                            --------------
                            3  |  4  |  5
                            --------------
                            6  |  7  |  8

      
        \U0001F449  You can play either as X or O.\n
        \U0001F449  You must align three Xs (or Os).\n
        \U0001F449  They can be aligned horizontally, verticaly or diagonally.\n
        \U0001F449  Do this before the computer and you win the game!\n
        \U0001F449  If both of you run out of moves it you shall daraw a tie!\n
        """
    )
    time.sleep(3)

def game_pieces(): 

    """
    Tells player how to select the piece that they want to use on the game board.
    """

    print("Wait! Before we start, you need to pick a game board piece.\n")
    print(
        """
        \U0001F449 Each piece is assigned to a respective letter.
        """
    )
    print(
        """
        \U0001F4DC For Instance:
        -----------------------
        """
    )
    print(
        """
                            a = \U0001F9DE 
                            b = \U0001F9D1
                            c = \U0001F444
                            d = \U0001F63B
        """
    )
    time.sleep(3)

    print(
        """
        \U0001F449 Using the chart below, please select your game piece:
        """
    )
    print(
        # Do not chnage spacing as this aligns eefectivily in the terminal
        """
                            a  |  b  | c  
                            -------------
                            \U0001F9DE | \U0001F9D1  | \U0001F444

                            d  |  e  | f  
                            -------------
                            \U0001F63B | \U0001F47B  | \U0001F916

                            g  |  h  | i  
                            -------------
                            \U0001F47D | \U0001F9E0  | \U0001F4A3

        """
    )

def human_picks_game_piece(): 

    """
    Allows user to select game piece.
    """  

    human_game_piece_picked = input("\n\U0001F3B2 Please pick your game piece:\n")

    if human_game_piece_picked in GAMEPIECES:
        print(f"\nOkay, your game piece is '{ GAMEPIECES[human_game_piece_picked] }'.\n")
        X = GAMEPIECES[human_game_piece_picked]

    else:  
        print(f"\nSorry, didn't recognise yourt respnse '{ human_game_piece_picked }'.\n")
        return human_picks_game_piece()
        time.sleep(1)
         
def ai_picks_game_piece():
    #NEED TO DO A LOOP SO AI DOES NOT PICK THE SAME PIECE AS PLAYER

    """
    - Allows computer ('AI') to select game piece.
    - The AI's Game piece is selected at random.
    """

    games_piece_list = list(GAMEPIECES.values())
    ai_game_piece_picked = random.choice(games_piece_list)
    print(f"\nGreat, the AI has picked '{ai_game_piece_picked}' as it's game piece.\n")
    O = ai_game_piece_picked
    time.sleep(1)
    print("\nOkay let's play! \U0001F60E\n")
    time.sleep(1.5)
    # return game_play()

def game_play():
    """
    - Holds the primary fucntions of the game. 
    - Refreshesd the board everytime a move is made 
    - Reference Source: @TokyoEdtech
    """
    #clears the screen
    os.system("clear")

    #loading message
    print("\n\U0001F3B2 Game board loading...\n")
    time.sleep(1)

def BLANK_SPACE_board():
    """
    - Initialises new game board
    - Reference Source: Dawson (2010, p.180)
    """
    board = []
    for square in range(BOARD_SQUARES):
        board.append(BLANK_SPACE)
    return board
    
def present_board(board):

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def board_moves(board):
    """
    - Returns a list of viable moves on the board
    - Reference Source: Dawson (2010, p.180)
    """

    moves = []
    for square in range(BOARD_SQUARES):
        if board[square] == BLANK_SPACE:
            moves.append(square)
    return moves

def game_winner_analysis(board):
    WINNING_INSTANCES

    for row in WINNING_INSTANCES:
        if board[row[0]] == board[row[1]] == board[row[2]] != BLANK_SPACE:
            winner = board[row[0]]
            return PlayerWon

        elif BLANK_SPACE not in board:
            return PlayerDraw




def exit():
    print(input("\nPlease press ENTER on your keyboard to exit:\n"))
    time.sleep(.5) 
    print("Exiting Game mode...\n") 
    time.sleep(1)
    #clears the terminal viewport 
    return clear_screen()
    

def clear_screen():
    #clears the screen
    os.system("clear")

    #welcome message
    return welcome()

   
def main(): 
    """
    Contains key functions that allows the game to run. 
    """
    # welcome()
    # r_u_ready_to_play()
    # game_pieces()
    human_picks_game_piece()
    ai_picks_game_piece()
    game_play()
    board = BLANK_SPACE_board() 
    present_board(board)
    board_moves(board)
    game_winner_analysis(board)
    # exit()
    # clear_screen()
     
main()

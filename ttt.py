# Tic-Tac-Toe Game

"""
Imported Libraries and Modules 
"""
import emoji # Credit Unicode
import time #Credit: Guru99


"""
CONST variables
"""
X = "\U0001F4AA" # human arm symbol 
O = "\U0001F9BE"  # mechanical arm symbol
PlayerWon = ""
PlayerLost = ""
PlayerTie = ""
BOARD_SQUARES = 9
GAME_NAME = "\ntic-tac-toe!\n"


def welcome():
    """
    TGreets user when they initially run the game.
    """
    print("\nWELCOME TO TIC-TAC-TOE! \U0001F609\n")
    print("This is a place where great minds meet to engage in digital strategic sparing!\n")
    print("This is one of the last places where you are able to put AI in it's place and show it whos boss.\n")
    time.sleep(2.5)


def game_guides():
    """
    Tells user how to play the game
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

      
        \U0001F449 You can play either as X or O\n
        \U0001F449 You must align three Xs or Os in a row in order to win the game\n
        \U0001F449 If you and the computer run out of moves it you shall daraw a tie!\n
        """
    )
    time.sleep(1.5)


def r_u_ready_to_play():
    """
    Asks user if they are ready to play
    """
    yes = "y"
    no = "n"
    
    while True: 
        
        try: 
            answer = input("\nAre you ready to play (y/n)?: ")

            if answer == yes:
                print("\nOkay! lets play \U0001F60E")
                return present_game_board()
                time.sleep(1.5)

            elif answer == no: 
                print("\n\U0001F92F What! Why not?\n")
                print("\n\U0001F612 Okay, maybe next time.\n")
                time.sleep(1.5)
                return welcome()

            else: 
                raise ValueError()

        except ValueError:
            print(
                f"\nSorry, didn't recognise yourt respnse '{answer}'. Please try again..."
            )
        #OUTSTANDING ACTION(s)- Create statementent that times out/ allows only 3 incorrect repsonses 


# def game_board():
#     board = [] 
#     for square in range(BOARD_SQUARES):
#         board.append(EMPTY)
#         return board

# def present_game_board(board):
#     """
#     - Creates new game board. 
#     - This is presented to user.
#     """
#     print("\n\t",board[0],"|",board[1],"|",board[2])
#     print("\t", "-----------")
#     print("\n\t",board[3],"|",board[4],"|",board[5])
#     print("\t", "-----------")
#     print("\n\t",board[6],"|",board[7],"|",board[8],"\n")



        
    
def main(): 
    """
    Contains key functions that allows the game to run. 
    """

    welcome()
    game_guides()
    r_u_ready_to_play()
    present_game_board()

print(GAME_NAME.upper())
main()







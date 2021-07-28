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
GREETING_MESSAGE = "\nBasically, T*3 is a game of Tic-Tac-Toe. \U0001F609 \n"


def welcome():
    """
    This message greets the user when they initially run the game.
    """
    print("This is a place where great minds meet to engage in digital strategic sparing!\n")
    print("This is one of the last places where you are able to put AI in it's place and show it whos boss.\n")
    time.sleep(2.5)


def game_guides():
    """
    This message tell the user how to play the game
    """
    print(
    
        """
        \U0001F4DC The Instuctions:
        ---------------
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

    
        """
    )
    
   




def main(): 

    welcome()
    game_guides()

print(GREETING_MESSAGE.upper())
main()







# Tic-Tac-Toe Game
import emoji


# X = "\U0001F607" # angel symbol 
# O = "\U0001F608" # devil symbol
# print(X, O)

X = "\U0001F4AA" # human arm symbol 
O = "\U0001F9BE" # mechanical arm symbol
PlayerWon = ""
PlayerLost = ""
PlayerTie = ""
# print(X, O)

def welcome_message():
    """
    This message greets the user when they initially run the game.
    """
    print("\nHello, and Welocome to the T*3 game!\n")
    print("Basically, T*3 is a game of Tic-Tac-Toe.\n")
    print("This is a place where great minds meet to engage in digital strategic sparing!\n")
    print("This is one of the last places where you are able to put AI in it's place and show it whos boss.\n")
    # print("Are you ready to play?")


welcome_message()


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
   

game_guides()


def take_turns():
    """
    This allows game to switch turns between users
    """
    if user_turn == X:
        return O
    else: 
        return X

take_turns() 



# def main(): 


# main()
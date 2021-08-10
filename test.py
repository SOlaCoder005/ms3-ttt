# Tic-Tac-Toe Game

"""
Imported Libraries and Modules
"""
import emoji
# Credit: Unicode
import time 
# Credit: Guru99
import random
# https://www.youtube.com/watch?v=7Djh-Cbgi0E
import os
os.system("clear")


"""
CONST variables
"""
GAMEPIECES = {
    # mermaid
    "a": "\U0001F9DE",
    # cook
    "b": "\U0001F9D1",
    # mouth
    "c": "\U0001F444",
    # cat love
    "d": "\U0001F63B",
    # ghost
    "e": "\U0001F47B",
    # robot head
    "f": "\U0001F916",
    # alien
    "g": "\U0001F47D",
    # brain
    "h": "\U0001F9E0",
    # bomb
    "i": "\U0001F4A3",
    }
    
# WINNING_INSTANCES = (
#     # horizontal instance
#     (1, 2, 3),
#     # horizontal instance
#     (4, 5, 6),
#     # horizontal instance
#     (7, 8, 9),
#     # vertical instance
#     (1, 4, 7),
#     # vertical instance
#     (2, 5, 8),
#     # vertical instance
#     (3, 6, 9),
#     # diagonal instance
#     (1, 5, 9),
#     # diagonal instance
#     (3, 5, 7)
# )

# Ref: Dawson (2010, p.184)
OPTIMAL_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)


def welcome():
    """
    Greets user when they initially run the game.
    """
    print("\nWELCOME TO TIC-TAC-TOE! \U0001F609\n")
    print("This is a place to engage in digital strategic sparing!\n")
    print("Can you put AI in it's place to show it who's boss?\n")
    time.sleep(2)
    print("\nI hope so...\U0001F914\n")
    print("\n\U0001F3B2 Instructions loading...")
    time.sleep(1.5)


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

                            1  |  2  |  3
                            --------------
                            4  |  5  |  6
                            --------------
                            7  |  8  |  9

      
        \U0001F449  You can play either as X or O.\n
        \U0001F449  You must align three Xs (or Os).\n
        \U0001F449  They can be aligned horizontally, verticaly or diagonally.\n
        \U0001F449  Do this before the computer and you win the game!\n
        \U0001F449  If both of you run out of moves it you shall daraw a tie!\n
        """
    )
    time.sleep(3)


def r_u_ready_to_play():
    """
    Asks user if they are ready to play.
    """
    yes = "y"
    no = "n"
    while True:
        try:
            answer = input("\n\U0001F3B2 Are you ready to play (y/n)?:\n")

            if answer == yes:
                print("\nOkay, let's go! \U0001F60E\n")
                return game_pieces_overview()
                time.sleep(1)
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


def game_pieces_overview():
    """
    - Tells player how to select the game piece that they want to use.
    """
    print("\n\U0001F449 Before we start, you need to pick a game board piece.\n")
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
        # Do not chnage spacing as this aligns effectivily in the terminal
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
    pp.player_picks_game_piece()
    time.sleep(1)


class PickGamePiece():
    def player_picks_game_piece(self):
        """
        Allows user to select game piece.
        This shall be used later and assigned to the player
        """
        # Hss been assigned 'gloabal' as piece will be called in the game play
        global PlayerGamePiece
        while True:
            try:
                PlayerGamePiece = input("\U0001F3B2 Pick your piece (a-i):\n")           
                if PlayerGamePiece in GAMEPIECES:
                    print(
                        f"\nYou've picked '  {GAMEPIECES[PlayerGamePiece]}  '.\n"
                    )
                    return pp.ai_picks_game_piece()
                else:
                    raise ValueError()
            except ValueError:
                print(
                    f"\n'{PlayerGamePiece}' is not vaild. Try again.\n"
                )                  

    def ai_picks_game_piece(self):
        """
        - Allows computer ('AI') to select game piece.
        - The AI's Game piece is selected at random.
        """
        # Hss been assigned 'gloabal' as piece will be called in the game play
        global AiGamePiece
        games_piece_list = list(GAMEPIECES.values())
        AiGamePiece = random.choice(games_piece_list)#AI sometimes picks the same icon as player, WHY?
        # AI selects a random game piece except from one chosen by player
        # AiGamePiece = random.choice([x for x in games_piece_list if x != PlayerGamePiece]) #AI sometimes picks the same icon as player, WHY?
        print(
            f"\nGreat, the AI has picked '  {AiGamePiece}  ' as it's game piece.\n"
        )
        time.sleep(1)
        print("\nOkay let's play! \U0001F60E\n")
        time.sleep(1.5)


pp = PickGamePiece()
# You dont need to call in main() as this statement calls the class
pp.player_picks_game_piece()
# pp.ai_picks_game_piece()


class Board():
    """
    Initialises game board
    Reference Source: @TokyoEdtech - # https://www.youtube.com/watch?v=7Djh-Cbgi0E
    """
    def __init__(self):
        self.squares = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def board_structure(self):
        print("\n")
        print(" %s | %s | %s " % (self.squares[1], self.squares[2], self.squares[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.squares[4], self.squares[5], self.squares[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.squares[7], self.squares[8], self.squares[9]))
        print("\n")

    def update_square(self, board_space, player):
        """
        This updates the Player's and / or AI's move
        Function PlayerGamePiece or AiGame Pieces needs to be called to trigger the update
        """
     
        try: 
            if self.squares[board_space] == " ":
                self.squares[board_space] = player
            elif self.squares[board_space] != " ":
                pass
                print("\n\U0001F449 Space is filled! A turn is missed.\n")
                time.sleep(2)
            else: 
                raise ValueError() 
        except ValueError:
            print("\nDid not recognise response. Please try again!\n")
            time.sleep(1)
            
    # Ref: TokyoEdtech pt3
    def new_game_board(self):
        """
        This creates a new empty gameboard.
        This game board is activated if the player wants to play again.
        """
        self.squares = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    # Ref: TokyoEdtech pt3
    def winning_instances(self, player):
        """
        This lists all the possible ways for the play or AI to win the game. 
        """
        if self.squares[1] == player and self.squares[2] == player and self.squares[3] == player:
            return True
        elif self.squares[4] == player and self.squares[5] == player and self.squares[6] == player:
            return True
        elif self.squares[7] == player and self.squares[8] == player and self.squares[9] == player:
            return True
        elif self.squares[1] == player and self.squares[4] == player and self.squares[7] == player:
            return True
        elif self.squares[2] == player and self.squares[5] == player and self.squares[8] == player:
            return True
        elif self.squares[3] == player and self.squares[6] == player and self.squares[9] == player:
            return True
        elif self.squares[1] == player and self.squares[5] == player and self.squares[9] == player:
            return True
        elif self.squares[3] == player and self.squares[5] == player and self.squares[7] == player:
            return True
        return False
        # might be able to call array
        # if self.squares[i] in WINNING_INSTANCES == player:
       

    # Ref: TokyoEdtech pt4
    def game_tie(self):
        """
        Checks for a tie after a win is checked
        """
        occupied_squares = 0
        for square in self.squares:
            if square != " ":
                # going through each space to check if it's full
                occupied_squares += 1
        # Checks if the 9 squares are occupied
        if occupied_squares == 9:
            return True
        else:
            return False 

    
board = Board()
# board.board_structure()


def refresh_game_board():
    """
    - Holds the primary fucntions of the game.
    - Refreshesd the board everytime a move is made.
    - Reference Source: @TokyoEdtech
    """
    # clears the screen
    os.system("clear")

    # loading message
    print("\n\U0001F3B2 Loading game...\n")
    time.sleep(1)
    os.system("clear")
    print("\n\U0001F3B2 Game loaded.\n")
    time.sleep(1)

    # presents board
    board.board_structure()


def player_moves():
    """
    - Player and AI will alternate turns until the board is filled
    - If incorrect answer is entered, by Player, ther are asked to play again.
    - If AI makes the wrong turn, it will lose a turn
    """
    while True:
        try:
            # Player Turn
            player_move = int(input("\n\U0001F449 Human, Please choose a space between 1-9: \n"))

            # Wherever player places move, put game piece
            board.update_square(player_move, GAMEPIECES[PlayerGamePiece])

            # Once placed, board refreshes
            refresh_game_board()

            # Check Player's moves for winner
            # No 'else statement' is needed as this only needs to run if True
            if board.winning_instances(GAMEPIECES[PlayerGamePiece]) is True:
                print("\n\U0001F973  Well Done! You've beaten the AI!\n")
                yes = "y"
                no = "n"
                question = input("\n\U0001F3B2 Do you want to play again? (y/n):\n") 
                if question == yes:
                    print("\n\U0001F449 Don't get full of yourself...\n")
                    print("\n\U0001F449 You may not win this time!\n")
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\n\U0001F449 Fine i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                    return welcome()
                else:
                    break

            # Check Player's moves for tie
            if board.game_tie():
                print("\n Well, this is awkward. You've tied.\n")
                time.sleep(0.25)
                print("\n Seems like you both play the same.\n")
                yes = "y"
                no = "n"
                question = input("\n\U0001F3B2 Do you want to play again? (y/n):\n") 
                if question == yes:
                    print("\n\U0001F449 Let's see if we can get a winner.\n")
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\n\U0001F449 Fine i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                    return welcome()
                else:
                    break
    
            # AI Turn
            print("\n\U0001F449 The AI will now make a move... \n")
            time.sleep(1)
            ai_move = random.randint(0, 9)
            # Wherever AI places move, put game piece
            board.update_square(ai_move, AiGamePiece)
            time.sleep(.5)
              
            # Once placed, board refreshes
            refresh_game_board() 

            # Check AI's moves for winner    
            if board.winning_instances(AiGamePiece) is True:
                print("\n\U0001F629 Well, the machine won! Oh Dear...\n")
                yes = "y"
                no = "n"
                question = input("\n\U0001F449 Do you want to play again? (y/n):\n") 
                if question == yes: 
                    print("\n\U0001F4AA Ahhh the will is strong with this one...\n")
                    time.sleep(1)
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\n\U0001F449 Fine, i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                    return welcome()
                else: 
                    break

            # Check AI's moves for tie
            if board.game_tie():
                print("\n\U0001F973 Well, this is awkward. You've tied.\n")
                time.sleep(0.25)
                print("\n\U0001F973 Seems like you both play the same.")
                yes = "y"
                no = "n"
                question = input("\n\U0001F3B2 Do you want to play again? (y/n):\n") 
                if question == yes:
                    print("\n Let's see if we can get a winner.\n")
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\nFine i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                    return welcome()
                else:
                    break

        except ValueError:
            # If value invalid, this message will activate 
            print("\n\U0001F449 Uuuummm, that's not a right value. Try again!\n")
            time.sleep(1) 


        
def exit():
    """
    - Activated when player no longer wants to play
    """
    print(input("\nPlease press ENTER on your keyboard to exit:\n"))
    time.sleep(.5) 
    print("Exiting Game mode...\n") 
    time.sleep(1)
    return clear_screen()


def clear_screen():
    """
    - Clears the terminal
    """
    # clears the screen
    os.system("clear")
    # loops back to programme's welcome message
    return welcome()


def main():
    
    # welcome()
    # game_guides()
    # r_u_ready_to_play()
    refresh_game_board()
    player_moves()
    exit()

main()
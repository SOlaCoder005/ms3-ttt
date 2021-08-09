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
PlayerWon = ""
PlayerLost = ""
PlayerDraw = "DRAW"
BLANK_SPACE = " "
BOARD_SQUARES = 9
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
    
WINNING_INSTANCES = (
    # horizontal instance
    (1, 2, 3),
    # horizontal instance
    (4, 5, 6),
    # horizontal instance
    (7, 8, 9),
    # vertical instance
    (1, 4, 7),
    # vertical instance
    (2, 5, 8),
    # vertical instance
    (3, 6, 9),
    # diagonal instance
    (1, 5, 9),
    # diagonal instance
    (3, 5, 7)
)

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
        global AiGamePiece
        games_piece_list = list(GAMEPIECES.values())
        AiGamePiece = random.choice(games_piece_list) #AI sometimes picks the same icon as player, WHY?
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
# pp.player_picks_game_piece()
# pp.ai_picks_game_piece()


class Board():
    """
    - Initialises game board
    - Reference Source: @TokyoEdtech - # https://www.youtube.com/watch?v=7Djh-Cbgi0E
    """
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def board_structure(self):
        print("\n")
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))
        print("\n")

    def update_cell(self, board_space, player):
        """
        """
        if self.cells[board_space] == " ":
            self.cells[board_space] = player
    
    # Ref: TokyoEdtech pt3
    def winning_instances(self, player):
        """
        """
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        elif self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        elif self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        elif self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        elif self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        return False
        # if self.cells[i] in WINNING_INSTANCES == player:
        # might be able to call array
    
    def new_game_board(self):
        """
        This creates a new empty gameboard.
        This game board is activated if the player wants to play again.
        """
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


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
            player_move = int(input("\n\U0001F3B2 Human, Please choose a space between 1-9: \n"))

            # Wherever player places move, put game piece
            board.update_cell(player_move, GAMEPIECES[PlayerGamePiece])

            # Once placed, board refreshes
            refresh_game_board()

            # Check Player's move for winner
            # No else statement as this only needs to run if True
            if board.winning_instances(GAMEPIECES[PlayerGamePiece]) == True:
                print("\n\U0001F973 Well Done! You've beaten the AI!\n")
                yes = "y"
                no = "n"
                question = input("\n\U0001F3B2 Do you want to play again? (y/n):\n") 
                if question == yes:
                    print("\n Don't get full of yourself...\n")
                    print("\n You may not win this time!\n")
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\nFine i'm bored anyway!\n")
                    time.sleep(.5)
                    return exit()
                else:
                    break
        
            # AI Turn
            print("\n\U0001F3B2 The AI will now make a move... \n")
            time.sleep(1)
            ai_move = random.randint(0, 9)

            # Wherever AI places move, put game piece
            board.update_cell(ai_move, AiGamePiece)
            time.sleep(.5)

            # Once placed, board refreshes
            refresh_game_board() 

            # Check AI's move for winner    
            if board.winning_instances(AiGamePiece) == True:
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
                    return exit()
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
    
    welcome()
    game_guides()
    r_u_ready_to_play()
    refresh_game_board()
    player_moves()
    exit()

main()
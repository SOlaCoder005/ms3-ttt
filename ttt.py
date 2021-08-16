# TIC-TAC-TOE GAME - Programme script

# Imported Libraries and Modules
import emoji
import time
import random
import sys
import os
os.system("clear")

# CONST VARIABLES

# Dictionary of icons that the player and AI can choose from
GAMEPIECES = {
    "a": "\U0001F984",  # unicorn
    "b": "\U0001F47E",  # alien monster
    "c": "\U0001F444",  # mouth
    "d": "\U0001F49B",  # yellow heart
    "e": "\U0001F47B",  # ghost
    "f": "\U0001F916",  # robot head
    "g": "\U0001F47D",  # alien
    "h": "\U0001F596",  # vulcan salute
    "i": "\U0001F649",  # hear no evil monkey
}


# Instances where player or AI can win
WINNING_INSTANCES = [
    [1, 2, 3],  # horizontal instance
    [4, 5, 6],  # horizontal instance
    [7, 8, 9],  # horizontal instance
    [1, 4, 7],  # vertical instance
    [2, 5, 8],  # vertical instance
    [3, 6, 9],  # vertical instance
    [1, 5, 9],  # diagonal instance
    [3, 5, 7]   # diagonal instance
]


def welcome_header():
    """
    - Presents welcome message to player
    """
    print("\nWELCOME TO TIC-TAC-TOE! \U0001F609\n")
    time.sleep(1)


def welcome_description():
    """
    - Greets user when they initially run the game.
    """
    print("This is a place to engage in digital strategic sparing!\n")
    time.sleep(1)
    print("Can you put AI in it's place to show it who's boss?\n")
    time.sleep(1)
    print("\nI hope so...\n")
    time.sleep(2)

    yes = "y"
    no = "n"

    while True:
        try:
            answer = input("\n\U0001F3B2 Do you want to play (y/n)?:\n")
            if answer == yes:
                print("\n\U0001F449 Great!\n")
                time.sleep(1.5)
                return game_guides()
            elif answer == no:
                print("\n\U0001F449 Okay no worries!\n")
                time.sleep(1)
                print("Exiting...\n")
                time.sleep(1)
                return restart_program()
            else:
                raise ValueError()
        except ValueError:
            print(
                f"\nDidn't recognise your respnse '{answer}'. Try again..."
            )


def game_guides():
    """
    - Tells user how to play the game.
    """
    print("\n\U0001F3B2 Instructions loading...")
    time.sleep(1.5)
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

        \U0001F449  You can pick the game piece you want to use on the board.\n
        \U0001F449  To win, you must align your pieces in a row.\n
        \U0001F449  The row can be horizontally, verticaly or diagonally.\n
        \U0001F449  Do this before the AI and you win the game!\n
        \U0001F449  If both of you run out of moves you shall daraw a tie!\n
        """
    )
    time.sleep(3)


def r_u_ready_to_play():
    """
    - Asks user if they are ready to play.
    """
    yes = "y"
    no = "n"

    while True:
        try:
            answer = input("\n\U0001F3B2 Are you ready to play (y/n)?:\n")

            if answer == yes:
                print("\nOkay, let's go! \U0001F60E\n")
                time.sleep(1.5)
                return game_pieces_overview()
            elif answer == no:
                print("\n\U0001F92F What! Why not?\n")
                print("\n\U0001F612 Okay, maybe next time.\n")
                time.sleep(1)
                return exit()
            else:
                raise ValueError()
        except ValueError:
            print(
                f"\nDidn't recognise your respnse ' {answer} '. Try again..."
            )


def game_pieces_overview():
    """
    - Tells player how to select the game piece that they want to use.
    """
    print("\n\U0001F449 Wait! You need to pick a game board piece.\n")
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
                            a = \U0001F984
                            b = \U0001F47E
                            c = \U0001F444
                            d = \U0001F49B
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
                            \U0001F984  | \U0001F47E  | \U0001F444

                            d  |  e  | f
                            -------------
                            \U0001F49B  | \U0001F47B  | \U0001F916

                            g  |  h  | i
                            -------------
                            \U0001F47D  | \U0001F596  | \U0001F649

        """
    )
    pp.player_picks_game_piece()
    time.sleep(1)


def refresh_game_board():
    """
    - Holds the primary fucntions of the game.
    - Refreshesd the board everytime a move is made.
    """
    # clears the screen
    os.system("clear")

    # loading message
    print("\n\U0001F3B2 Loading board...\n")
    time.sleep(1)
    os.system("clear")
    print("\n\U0001F3B2 Board loaded.\n")
    time.sleep(1)

    # presents board
    board.board_structure()


def moves():
    """
    - Player and AI will alternate turns until the board is filled
    - If incorrect answer is ned by Player, they are asked to play again.
    - If AI makes the wrong turn, it will lose a turn
    """
    while True:
        try:
            # Player's Turn
            player_move = int(input("\n\U0001F449 Human, make a move(1-9):\n"))
            if 0 < player_move < 10:

                # Wherever player places move, put game piece
                board.update_square(player_move, GAMEPIECES[PlayerGamePiece])

                # Once placed, board refreshes
                refresh_game_board()
            else:
                print("\nDid not recognise response. Please try again!\n")
                time.sleep(.5)
                continue

            # Check Player's moves for winner
            # No 'else statement' is needed as this only needs to run if True
            if board.winning_instances(GAMEPIECES[PlayerGamePiece]) is True:
                print("\n\U0001F973  Well Done! You've beaten the AI!\n")
                yes = "y"
                no = "n"
                question = input("\n\U0001F3B2 Play again? (y/n):\n")
                if question == yes:
                    print("\n\U0001F449 Don't get full of yourself...\n")
                    time.sleep(1)
                    print("\n\U0001F449 You may not win this time!\n")
                    time.sleep(1)
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\n\U0001F449 Fine i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                elif question != yes or no:
                    print("\n\U0001F449 Sorry, that response is not vaild.\n")
                    time.sleep(.5)
                    print("\n\U0001F449 The game will now end\n")
                    time.sleep(.5)
                    exit()
                else:
                    break

            # Check Player's moves for tie
            if board.game_tie():
                print("\n Well, this is awkward. You've tied.\n")
                time.sleep(0.25)
                print("\n Seems like you both play the same.\n")
                yes = "y"
                no = "n"
                question = input("\n\U0001F3B2 Play again? (y/n):\n")
                if question == yes:
                    print("\n\U0001F449 Let's see if we can get a winner.\n")
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\n\U0001F449 Fine i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                elif question != yes or no:
                    print("\n\U0001F449 Sorry, that response is not vaild.\n")
                    time.sleep(.5)
                    print("\n\U0001F449 The game will now end...\n")
                    time.sleep(.5)
                    exit()
                else:
                    break

            # AI's Turn
            print("\n\U0001F449 The AI will now make a move... \n")
            time.sleep(1)

            # Wherever AI places move, put game piece
            board.ai_move(AiGamePiece)
            time.sleep(.5)

            # Once placed, board refreshes
            refresh_game_board()

            # Check AI's moves for winner
            if board.winning_instances(AiGamePiece) is True:
                print("\n\U0001F629 Well, the machine won! Oh Dear...\n")
                yes = "y"
                no = "n"
                question = input("\n\U0001F449 Play again? (y/n):\n")
                if question == yes:
                    print("\n\U0001F4AA  Ahhh, your will is strong!\n")
                    time.sleep(1)
                    print("\n\U0001F4AA  But, will it be enough?\n")
                    time.sleep(1.5)
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\n\U0001F449 Fine, i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                elif question != yes or no:
                    print("\n\U0001F449 Sorry, that response is not vaild.\n")
                    time.sleep(.5)
                    print("\n\U0001F449 The game will now end\n")
                    time.sleep(.5)
                    exit()
                else:
                    break

            # Check AI's moves for tie
            if board.game_tie():
                print("\n\U0001F449 Well, this is awkward. You've tied.\n")
                time.sleep(0.25)
                print("\n\U0001F449 Seems like you both play the same.")
                yes = "y"
                no = "n"
                question = input("\n\U0001F449  Play again? (y/n):\n")
                if question == yes:
                    print("\n Let's see if we can get a winner.\n")
                    board.new_game_board()
                    refresh_game_board()
                    time.sleep(1)
                elif question == no:
                    print("\nFine i'm bored anyway!\n")
                    time.sleep(.5)
                    exit()
                elif question != yes or no:
                    print("\n\U0001F449 Sorry, that response is not vaild.\n")
                    time.sleep(.5)
                    print("\n\U0001F449 The game will now end\n")
                    time.sleep(.5)
                    exit()
                else:
                    break

        except ValueError:
            print("\n\U0001F449 That's not a right value. Try again!\n")
            time.sleep(1)


def exit():
    """
    - Activated when player no longer wants to play the game or programme
    """
    print(input("\n\U0001F449 Press ENTER on your keyboard to exit:\n"))
    time.sleep(.5)
    print("Exiting Game mode...\n")
    time.sleep(1)
    clear_screen()


def clear_screen():
    """
    - Clears the terminal
    """
    # clears the screen
    os.system("clear")
    return restart_program()


def restart_program():
    """
    - This clears the terminal and restarts the programme.
    """
    os.system("clear")
    python = sys.executable
    os.execl(python, python, * sys.argv)
    return welcome_header()


class PickGamePiece():
    def player_picks_game_piece(self):
        """
        - Allows user to select game piece.
        - This shall be used later and assigned to the player
        """
        # PlayerGamePiece has been assigned 'gloabal'
        # This piece will be called in the gameplay
        global PlayerGamePiece

        while True:
            try:
                PlayerGamePiece = input("\U0001F3B2 Pick your piece (a-i):\n")
                if PlayerGamePiece in GAMEPIECES:
                    print(
                        f"\nYou've picked ' {GAMEPIECES[PlayerGamePiece]} '.\n"
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
        - Conditional has been used to make the AI
          pick a different piece to the PlayerGamePiece
        """
        # AiGamePiece has been assigned 'gloabal'
        # This piece will be called in the gameplay
        global AiGamePiece

        # Where the AI will pick the piece from
        games_piece_list = list(GAMEPIECES.values())

        # The AI will select piece at random
        AiGamePiece = random.choice(games_piece_list)
        if AiGamePiece != GAMEPIECES[PlayerGamePiece]:
            print(
                f"\nThe AI has picked ' {AiGamePiece} ' as it's game piece.\n"
            )
            time.sleep(1)
            print("\nOkay let's play! \U0001F60E\n")
            time.sleep(1.5)
            return board
        else:
            print("\n\U0001F449 Sorry an error occured\n")
            return pp.ai_picks_game_piece()

pp = PickGamePiece()


class Board():
    """
    - Initialises game board
    """
    def __init__(self):
        self.squares = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def board_structure(self):
        """
        - Code creates the board structure.
        - This will be displayed in the terminal.
        - The print statements have been formatted in this way to
          meet line length requirements on PEP8 Validator checks
        """
        print("\n")
        print(
            "  %s  |  %s  |  %s  " %
            (self.squares[1], self.squares[2], self.squares[3])
        )
        print("-----------------")
        print(
            "  %s  |  %s  |  %s  " %
            (self.squares[4], self.squares[5], self.squares[6])
        )
        print("-----------------")
        print(
            "  %s  |  %s  |  %s  " %
            (self.squares[7], self.squares[8], self.squares[9])
        )
        print("\n")

    def update_square(self, board_space, player):
        """
        - This updates the Player's and / or AI's move
        -  When PlayerGamePiece or AiGamePiece are called,
          they trigger the update on the board sqaure
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

    def new_game_board(self):
        """
        - This creates a new empty gameboard.
        - This game board is activated if the player wants to play again.
        """
        self.squares = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def winning_instances(self, player):
        """
        - This lists all the possible ways for the play or AI to win the game.
        """
        for instances in WINNING_INSTANCES:
            outcome = True
            for board_space in instances:
                if self.squares[board_space] != player:
                    outcome = False
            if outcome is True:
                return True

    def ai_move(self, player):
        """
        - Dictates the AI's move
        - The AI will search for the next available space
        """
        chance = list(range(1, 10))
        random.shuffle(chance)
        for i in chance:
            if self.squares[i] == " ":
                self.update_square(i, player)
                break

    def game_tie(self):
        """
        - Checks for a tie after a win is checked
        """
        occupied_squares = 0
        for square in self.squares:
            if square != " ":
                # Going through each space to check if it's full
                occupied_squares += 1
        # Checks if the 9 squares are occupied
        if occupied_squares == 9:
            return True
        else:
            return False


board = Board()


def main():
    welcome_header()
    welcome_description()
    r_u_ready_to_play()
    refresh_game_board()
    moves()
    exit()


main()

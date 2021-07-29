"""
Refs below (will move to Readme.md later):
- https://unicode.org/emoji/charts/emoji-list.html - list of emoji unicodes
- https://medium.com/analytics-vidhya/how-to-print-emojis-using-python-2e4f93443f7e - article explaining how to use unicode with Python    
- Dawson 2010, pp. 157-58 and pp.175-187
"""

# Ref: Dawson, 2010 pp. 169-70 

def birthday1(name, age):
 
    print(f"Happy birthday ,", name, "! You are ", age, " today.\n" )

# birthday1(name = "Jack", age = 4) | Happy birthday , Jack ! You are  4  today. | Default values
# birthday1("Jack", 4) | Happy birthday , Jack ! You are  4  today. | Positional Parameters

# X = "\U0001F607" # angel symbol 
# O = "\U0001F608" # devil symbol
# print(X, O)


"""
OLD CODE BELOW:

def r_u_ready_to_play():
    """
    #Asks the user if they are ready to play
    """
    yes = "y"
    no = "n"
    
    #TO DO!!!! - You need to create an error catacher for this fucntion so it doen't take invalid response
    answer = input("\nAre you ready to play? (y/n): ")
    
    if answer == yes:
        print("\nOkay! lets play")
        return present_game_board()
        time.sleep(1.5)
    else: 
        print("\nWhy not? Okay, maybe next time.\n")
        time.sleep(1.5)
        return welcome()
"""

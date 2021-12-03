from files.Board import *

# prints the main menu
def main_menu():

    menu = ["Welcome, Mayor of Simp City!", "----------------------------", 
        "1. Start new game", "2. Load saved game", "", "0. Exit", "Your choice? "]
    
    for item in menu:
        if item == "Your choice? ":
            option = input(item)
            print("")

        else:
            print(item)

    return option

# prints the game menu
def game_menu(currentBoard):

    menu1 = ["1. Build a ", "2. Build a "]

    menu2 = ["3. See remaining buildings", "4. See current score", "", 
            "5. Save game", "0. Exit to main menu", "Your choice? "]

    print("Turn ", currentBoard.turn)

    # build the board
    for items in currentBoard.board:
        for item in items:
            print(item, end =" ")
        print("")

    # TODO creates build option
    for line in menu1:
        print(line)

    # create the other option from 3 to 5 and 0
    for line in menu2:
        if line == "Your choice? ":
            option = input(line)
            print("")

        else:
            print(line)

    return option


    

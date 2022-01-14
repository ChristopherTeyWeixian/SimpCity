from files.Board import *
import random

from files.Game_Options import check_building_left

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
    OptionBuildingList= []
    UpdatedBuildingList = []
    UpdatedBuildingList = check_building_left(currentBoard)

    menu1 = ["1. Build a ", "2. Build a "]

    menu2 = ["3. See remaining buildings", "4. See current score", "", 
                "5. Save game", "0. Exit to main menu", "Your choice? "]

    print("Turn ", currentBoard.turn)

    i = 0
    # build the board
    for items in currentBoard.board:
        for item in items:
            print(item, end =" ")
        display_remaining_building(currentBoard, i)
        i += 1
        print("")

    # TODO creates build option
    for line in menu1:
        #If building type have more than 1 building left to place
        #if check_building_left return true
        RandBuilding=random.randint(0,len(UpdatedBuildingList)-1)
        OptionBuildingList.append(UpdatedBuildingList[RandBuilding])
        print(line+UpdatedBuildingList[RandBuilding])
        #Else do not append building with 0 build amt

    # create the other option from 3 to 5 and 0
    for line in menu2:
        if line == "Your choice? ":
            option = input(line)
            print("")

        else:
            print(line)

    if option == "1" or option == "2":
        return option,OptionBuildingList[int(option)-1]
    else:
        return option, None

def EndGame(currentBoard):

    print("\nFinal layout of Simp City:")

    # build the board
    i = 0
    # build the board
    for items in currentBoard.board:
        for item in items:
            print(item, end =" ")
        display_remaining_building(currentBoard, i)
        i += 1
        print("")

    # puts a spacing away from the main menu that would appear after the game.
    print("")

    #TODO: show total scores

def display_remaining_building(currentBoard, i): #Game option 3
    match i:
        case 0:
            print("\t\tBuilding          Remaining", end =" ")
        case 1:
            print("\t\t--------          ---------", end =" ")
        case 2:
            print("\t\tBCH              ",currentBoard.Beach, end =" ")
        case 3:
            print("\t\tFAC              ",currentBoard.Factory, end =" ")
        case 4:
            print("\t\tHSE              ",currentBoard.House, end =" ")
        case 5:
            print("\t\tSHP              ",currentBoard.Shop, end =" ")
        case 6:
            print("\t\tHWY              ",currentBoard.Highway, end =" ")
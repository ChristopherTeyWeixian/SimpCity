from files.Board import *
import random

from files.Game_Options import check_building_left

# prints the main menu
def main_menu():

    menu = ["Welcome, Mayor of Simp City!", "----------------------------", 
        "1. Start new game", "2. Load saved game", "3. Options", "", "0. Exit", "Your choice? "]
    
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

    menu2 = ["3. See current score", "", "4. Save game", 
                "0. Exit to main menu", "Your choice? "]

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
            if currentBoard.BuildingState[0] == "True":
                print("\t\tBCH              ",currentBoard.Beach, end =" ")
            else:
                print("\t\t--Inactive--", end =" ")
        case 3:
            if currentBoard.BuildingState[1] == "True":
                print("\t\tFAC              ",currentBoard.Factory, end =" ")
            else:
                print("\t\t--Inactive--", end =" ")
        case 4:
            if currentBoard.BuildingState[2] == "True":
                print("\t\tHSE              ",currentBoard.House, end =" ")
            else:
                print("\t\t--Inactive--", end =" ")                
        case 5:
            if currentBoard.BuildingState[3] == "True":
                print("\t\tSHP              ",currentBoard.Shop, end =" ")
            else:
                print("\t\t--Inactive--", end =" ")                
        case 6:
            if currentBoard.BuildingState[4] == "True":
                print("\t\tHWY              ",currentBoard.Highway, end =" ")
            else:
                print("\t\t--Inactive--", end =" ")                
        case 7:
            if currentBoard.BuildingState[5] == "True":
                print("\t\tPRK              ",currentBoard.Park, end =" ")
            else:
                print("\t\t--Inactive--", end =" ")                
        case 8:
            if currentBoard.BuildingState[6] == "True":
                print("\t\tMON              ",currentBoard.Monument, end =" ")
            else:
                print("\t\t--Inactive--", end =" ")                

def Option_Building(currentBoard):
    option_menu = ["Current Building Pool",
                    "1) Beach\t | " + str(currentBoard.BuildingState[0]), 
                    "2) Factory\t | " + str(currentBoard.BuildingState[1]),
                    "3) House\t | " + str(currentBoard.BuildingState[2]),
                    "4) Shop\t\t | " + str(currentBoard.BuildingState[3]),
                    "5) HighWay\t | " + str(currentBoard.BuildingState[4]),
                    "6) Park\t\t | " + str(currentBoard.BuildingState[5]),
                    "7) Monument\t | " + str(currentBoard.BuildingState[6]),
                    "\n0) Exit Option"]

    for line in option_menu:
        print(line)
    
    print("\nType in the number that you want to change the state of the building pool")
    print("Maximum only 5 types of building can be chosen (True)")
    option = input("Select Building Pool: ")

    try:
        option = int(option)
        if option >= 0 and option < 8:
            return option
        else:
            return "Out of Range"
    except:
        return "Wrong Input"
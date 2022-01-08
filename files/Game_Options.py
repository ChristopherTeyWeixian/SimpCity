from files.Board import *

#Game Options 1 & 2, Build a building
def place_building(currentBoard, building, option):
    #Tables to check user input
    column_table = ['a', 'b', 'c', 'd']
    row_table = [1, 2, 3, 4]

    if len(option) == 2 and option[0].isalpha()==True and option[1].isnumeric() ==True:
        
        #Check column
        if option[0].lower() not in column_table:
            column_coord = None
            print("Input a valid column")
            return False

        #Check row
        if int(option[1]) not in row_table:
            row_coord = None
            print("Input a valid row number")
            return False
        
        prevent_overlap(currentBoard, option, building)

    else:
            print("Invalid option")
            return False

def building_choice(currentBoard, option, building): 
    #Modifying row & column selected
    #Building types: HSE, FAC, SHP, HWY, BCH
    column_coord,row_coord=convert_option(option)
    currentBoard.board[row_coord][column_coord-1] = '' 
    currentBoard.board[row_coord][column_coord] = building
    currentBoard.board[row_coord][column_coord+1] = ''
    currentBoard.update_board_building(building)
    currentBoard.Next_Turn()
    return True

def check_adjacent(currentBoard, option, building):

    column_coord,row_coord=convert_option(option)

    #Validation after turn 1
    if currentBoard.turn > 1:
        #Check column 1
        if column_coord == 4:
            #First row
            if row_coord == 2:
                #If slot to the right/below is empty
                if (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False
                
                #If slot to the right/below is taken
                elif (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Second row
            elif row_coord == 4:
                #If slot above/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Third row
            elif row_coord == 6:
                #If slot above/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Fourth row
            elif row_coord == 8:
                 #If slot to the right/up is empty
                if (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord - 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False
                
                #If slot to the right/up is taken
                elif (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord - 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

        #-------------------------------------------------------------------
        #Check column 2
        elif column_coord == 10:
            #First row
            if row_coord == 2:
                #If slot left/right/below is empty
                if (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot left/right/below is taken
                elif (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Second row
            elif row_coord == 4:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Third row
            elif row_coord == 6:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Fourth row
            elif row_coord == 8:
                #If slot above/left/right is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " "):
                    building_choice(currentBoard, option, building)

        #-------------------------------------------------------------------
        #Check column 3
        elif column_coord == 16:
            #First row
            if row_coord == 2:
                #If slot left/right/below is empty
                if (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot left/right/below is taken
                elif (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Second row
            elif row_coord == 4:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Third row
            elif row_coord == 6:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Fourth row
            elif row_coord == 8:
                #If slot above/left/right is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " "):
                    building_choice(currentBoard, option, building)

        #-------------------------------------------------------------------
        #Check column 4
        elif column_coord == 22:
            #First row
            if row_coord == 2:
                #If slot to the left/below is empty
                if (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False
                
                #If slot to the left/below is taken
                elif (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Second row
            elif row_coord == 4:
                #If slot above/left/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Third row
            elif row_coord == 6:
                #If slot above/left/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, option, building)

            #Fourth row
            elif row_coord == 8:
                #If slot above/left is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " "):
                    print("Must build adjacent to existing building")
                    return False
                
                #If slot to the above/left is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " "):
                    building_choice(currentBoard, option, building)

    else:
        #Only for turn 1
        building_choice(currentBoard, option, building)

def prevent_overlap(currentBoard, option, building):
    #Function to check for overlapping buildings

    column_coord,row_coord=convert_option(option)
    
    if column_coord is not None or row_coord is not None:
        if currentBoard.board[row_coord][column_coord] != " ":
            print("Cannot overlap buildings")
            return False
        else:
            check_adjacent(currentBoard, option, building)

    else:
        print(" ")
        return False

def check_building_left(currentBoard):
    BuildingListShortForm=["BCH","FAC","HSE","SHP","HWY"]
    CheckedBuildingList = []    

    #Check amount of building
    #If no building, then wont display it
    for line in BuildingListShortForm:
        if line == "BCH" and currentBoard.Beach >=1:
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "FAC" and currentBoard.Factory>=1:
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "HSE" and currentBoard.House >=1:
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "SHP" and currentBoard.Shop>=1:
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "HWY" and currentBoard.Highway >=1:
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

    return CheckedBuildingList

def display_remaining_building(currentBoard): #Game option 3
    print("Building          Remaining")
    print("--------          ---------")
    print("BCH              ",currentBoard.Beach)
    print("FAC              ",currentBoard.Factory)
    print("HSE              ",currentBoard.House)
    print("SHP              ",currentBoard.Shop)
    print("HWY              ",currentBoard.Highway)
    print("")

def convert_option(Option):
    #Tables for input conversion
    column_table = ['a', 'b', 'c', 'd']
    actual_columns = [4, 10, 16, 22]
    row_table = [1, 2, 3, 4]
    actual_rows = [2, 4, 6, 8] 

    chosen_column = str.lower(Option[0])
    chosen_row = int(Option[1])

    for line in column_table:
        if line == chosen_column:
            column = actual_columns[column_table.index(chosen_column)]

    for line in row_table:
        if line == chosen_row:
            row = actual_rows[row_table.index(chosen_row)]

    return column,row

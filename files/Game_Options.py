from files.Board import *

#Game Options 1 & 2, Build a building
def place_building(currentBoard,building):
    option = str(input("Build where? "))
    #Translate user input to actual position on table
    column_table = ['a', 'b', 'c', 'd']
    actual_columns = [4, 10, 16, 22]
    row_table = [1, 2, 3, 4]
    actual_rows = [2, 4, 6, 8] 
    if len(option) == 2:
        chosen_column = str.lower(option[0])
        chosen_row = int(option[1])

        #Defining column coordinates
        if chosen_column in column_table:
            for line in column_table:
                if line == chosen_column:
                    modified_column = actual_columns[column_table.index(chosen_column)]
                    column_coord = modified_column
 
        else:
            column_coord = None
            print("Input a valid column")
            return False

        #Defining row coordinates
        if (chosen_row > 0) and (chosen_row < 5):
            for line in row_table:
                if line == chosen_row:
                    modified_row = actual_rows[row_table.index(chosen_row)]
                    row_coord = modified_row

        else:
            row_coord = None
            print("Input a valid row number")
            return False

        prevent_overlap(currentBoard, column_coord, row_coord,building)

    else:
            print("Invalid option")

def building_choice(currentBoard, column_coord, row_coord,building): 
    #Modifying row & column selected
    #Building types: HSE, FAC, SHP, HWY, BCH
    currentBoard.board[row_coord][column_coord-1] = '' 
    currentBoard.board[row_coord][column_coord] = building
    currentBoard.board[row_coord][column_coord+1] = ''
    currentBoard.update_board_building(building)
    currentBoard.Next_Turn()
    return True

def check_adjacent(currentBoard, column_coord, row_coord,building):
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
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Second row
            elif row_coord == 4:
                #If slot above/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Third row
            elif row_coord == 6:
                #If slot above/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Fourth row
            elif row_coord == 8:
                 #If slot to the right/up is empty
                if (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord - 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False
                
                #If slot to the right/up is taken
                elif (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord - 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

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
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Second row
            elif row_coord == 4:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Third row
            elif row_coord == 6:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Fourth row
            elif row_coord == 8:
                #If slot above/left/right is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

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
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Second row
            elif row_coord == 4:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Third row
            elif row_coord == 6:
                #If slot above/left/right/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Fourth row
            elif row_coord == 8:
                #If slot above/left/right is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord][column_coord + 6] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/right is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord][column_coord + 6] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

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
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Second row
            elif row_coord == 4:
                #If slot above/left/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Third row
            elif row_coord == 6:
                #If slot above/left/below is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " ") and (currentBoard.board[row_coord + 2][column_coord] == " "):
                    print("Must build adjacent to existing building")
                    return False

                #If slot above/left/below is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " ") or (currentBoard.board[row_coord + 2][column_coord] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

            #Fourth row
            elif row_coord == 8:
                #If slot above/left is empty
                if (currentBoard.board[row_coord - 2][column_coord] == " ") and (currentBoard.board[row_coord][column_coord - 6] == " "):
                    print("Must build adjacent to existing building")
                    return False
                
                #If slot to the above/left is taken
                elif (currentBoard.board[row_coord - 2][column_coord] != " ") or (currentBoard.board[row_coord][column_coord - 6] != " "):
                    building_choice(currentBoard, column_coord, row_coord,building)

    else:
        #Only for turn 1
        building_choice(currentBoard, column_coord, row_coord,building)

def prevent_overlap(currentBoard, column_coord, row_coord,building):
    #Function to check for overlapping buildings
    if column_coord is not None or row_coord is not None:
        if currentBoard.board[row_coord][column_coord] != " ":
            print("Cannot overlap buildings")
            return False
        else:
            check_adjacent(currentBoard, column_coord, row_coord,building)

    else:
        print(" ")
        return False

def display_remaining_building(currentBoard): #Game option 3
    print("Building          Remaining")
    print("--------          ---------")
    print("BCH              ",currentBoard.Beach)
    print("FAC              ",currentBoard.Factory)
    print("HSE              ",currentBoard.House)
    print("SHP              ",currentBoard.Shop)
    print("HWY              ",currentBoard.Highway)
    print("")

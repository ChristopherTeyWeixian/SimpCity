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
    BuildingListShortForm=["BCH","FAC","HSE","SHP","HWY", "PRK", "MON"]
    CheckedBuildingList = []    

    #Check amount of building
    #If no building, then wont display it
    for line in BuildingListShortForm:
        if line == "BCH" and currentBoard.Beach >=1 and currentBoard.BuildingState[0] == "True":
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "FAC" and currentBoard.Factory>=1 and currentBoard.BuildingState[1] == "True":
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "HSE" and currentBoard.House >=1 and currentBoard.BuildingState[2] == "True":
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "SHP" and currentBoard.Shop>=1 and currentBoard.BuildingState[3] == "True":
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "HWY" and currentBoard.Highway >=1 and currentBoard.BuildingState[4] == "True":
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])
        
        if line == "PRK" and currentBoard.Park >= 1 and currentBoard.BuildingState[5] == "True":
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

        if line == "MON" and currentBoard.Monument >= 1 and currentBoard.BuildingState[6] == "True":
            CheckedBuildingList.append(BuildingListShortForm[BuildingListShortForm.index(line)])

    return CheckedBuildingList

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

def CalculateScore(currentBoard):
    score=0
    # Column A - B - C - D
    actual_columns = [4, 10, 16, 22]
    # Row 1 - 2 - 3 - 4
    actual_rows = [2, 4, 6, 8] 

    prk_activeList = []
    prk_indv_count = []

    hse_count = 0
    fac_count = 0
    shp_count = 0
    hwy_count = 0
    bch_count = 0
    prk_count = 0
    mon_count = 0    
    mon_corner_count = 0

    hse_score = 0
    fac_score = 0
    shp_score = 0
    hwy_score = 0
    bch_score = 0
    prk_score = 0
    mon_score = 0

    hse_line = "HSE: "
    fac_line = "FAC: "
    shp_line = "SHP: "
    hwy_line = "HWY: "
    bch_line = "BCH: "
    prk_line = "PRK: "
    mon_line = "MON: "

    for y in range(0, len(actual_columns)):
        for x in range(0, len(actual_rows)):
            # actual_rows[x]
            # actual_columns[y]

            if currentBoard.board[actual_rows[x]][actual_columns[y]] == "BCH":
                if actual_columns[y] == 4 or actual_columns[y] == 22:
                    bch_score += 3
                    bch_line = Combine_String(bch_line, "3", bch_count)
                    bch_count += 1
                else:
                    bch_score += 1
                    bch_line = Combine_String(bch_line, "1", bch_count)
                    bch_count += 1

            elif currentBoard.board[actual_rows[x]][actual_columns[y]] == "FAC":
                fac_count += 1
                #calculations done after

            elif currentBoard.board[actual_rows[x]][actual_columns[y]] == "HSE":
                check_point = [[actual_rows[x - 1], actual_columns[y]], [actual_rows[x + 1], actual_columns[y]], \
                    [actual_rows[x], actual_columns[y - 1]], [actual_rows[x], actual_columns[y + 1]]]
                have_fac = False
                # checks if there is a factory or not
                # try is used here incase the list count went out of the list, it will not crash
                for point in check_point:
                    try:
                        if currentBoard.board[point[0]][point[1]] == "FAC":
                            hse_score += 1
                            hse_line = Combine_String(hse_line, "1", hse_count)
                            hse_count += 1
                            have_fac = True
                            break
                    except:
                        continue

                #used for individual scoring of the house
                if have_fac == False:
                    temp_score = 0 
                    for point in check_point:
                        try:
                            if currentBoard.board[point[0]][point[1]] == "HSE":
                                temp_score += 1
                            elif currentBoard.board[point[0]][point[1]] == "SHP":
                                temp_score += 2
                        except:
                            continue
                    
                    hse_score += temp_score
                    hse_line = Combine_String(hse_line, str(temp_score), hse_count)
                    hse_count += 1
                

            elif currentBoard.board[actual_rows[x]][actual_columns[y]] == "SHP":
                item_1 = " "
                item_2 = " "
                item_3 = " "
                item_4 = " "

                try:
                    item_1 = currentBoard.board[actual_rows[x - 1]][actual_columns[y]]
                except:
                    item_1 = " "
                try:
                    item_2 = currentBoard.board[actual_rows[x + 1]][actual_columns[y]]
                except:
                    item_2 = " "
                try:
                    item_3 = currentBoard.board[actual_rows[x]][actual_columns[y - 1]]
                except:
                    item_3 = " "
                try:
                    item_4 = currentBoard.board[actual_rows[x]][actual_columns[y + 1]]
                except:
                    item_4 = " "

                temp_score = 0
                if item_1 != " ":
                    temp_score += 1

                if item_2 != item_1 and item_2 != " ":
                    temp_score += 1

                if item_3 != item_1 and item_3 != item_2 and item_3 != " ":
                    temp_score += 1
                    
                if item_4 != item_1 and item_4 != item_2 and item_4 != item_3 and item_4 != " ":
                    temp_score += 1

                shp_score += temp_score    
                shp_line = Combine_String(shp_line, str(temp_score), shp_count)
                shp_count += 1

            elif currentBoard.board[actual_rows[x]][actual_columns[y]] == "HWY":
                temp_score = HWY_Recursive(currentBoard.board, x, y, actual_rows, actual_columns)
                hwy_score += temp_score
                hwy_line = Combine_String(hwy_line, str(temp_score), hwy_count)
                hwy_count += 1

            elif currentBoard.board[actual_rows[x]][actual_columns[y]] == "PRK":
                temp_pos = [x, y]
                prk_activeList.append(temp_pos)

            elif currentBoard.board[actual_rows[x]][actual_columns[y]] == "MON":
                if (x == 0 and y == 0) or (x == 3 and y == 3) or (x == 0 and y == 3) or (x == 3 and y == 0):
                    mon_score += 2
                    mon_line = Combine_String(mon_line, "2", mon_count)
                    mon_count += 1
                    mon_corner_count += 1
                else:
                    mon_score += 1
                    mon_line = Combine_String(mon_line, "1", mon_count)
                    mon_count += 1

    '''
        END OF CHECKING THE BOARD 
=========================================
        START OF PRINTING
    '''            

    #gets BCH score, if there is no count means 0 score
    if bch_count == 0:
        bch_line = Combine_String(bch_line, "0", bch_count)
    #Counts Factory score and change the lines
    if fac_count >= 4:
        for i in range(0, fac_count):
            if i <= 3:
                fac_score += 4
                fac_line = Combine_String(fac_line, "4", i)
            else:
                fac_score += 1
                fac_line = Combine_String(fac_line, "1", i)
    elif fac_count > 0:
        for i in range (0, fac_count):
            fac_score += fac_count
            fac_line = Combine_String(fac_line, str(fac_count), i)
    #gets FAC score, if there is no count means 0 score
    else:
        fac_line = Combine_String(fac_line, "0", fac_count)

    #gets HSE score, if there is no count means 0 score
    if hse_count == 0:
        hse_line = Combine_String(hse_line, "0", hse_count)

    #gets SHP score, if there is no count means 0 score
    if shp_count == 0:
        shp_line = Combine_String(shp_line, "0", shp_count)

    #gets HWY score, if there is no count means 0 score
    if hwy_count == 0:
        hwy_line = Combine_String(hwy_line, "0", hwy_count)

    #for PRK scoring system
    while len(prk_activeList) != 0:
        path  = []
        temp_count, prk_activeList = PRK_Recursive(path, prk_activeList[0] ,prk_activeList)
        prk_indv_count.append(temp_count)

    if len(prk_indv_count) != 0:
        for counter in prk_indv_count:
            value = 0
            if counter == 1:
                value = 1
            elif counter == 2:
                value = 3
            elif counter == 3:
                value = 8
            elif counter == 4:
                value = 16
            elif counter == 5:
                value = 22
            elif counter == 6:
                value = 23
            elif counter == 7:
                value = 24
            elif counter == 8:
                value = 25

            prk_score += value
            prk_line = Combine_String(prk_line, str(value), prk_count)
            prk_count += 1
    #gets PRK score, if there is no count mean 0 score
    if prk_count == 0:
        prk_line = Combine_String(prk_line, "0", prk_count)

    if mon_count == 0:
        mon_line = Combine_String(mon_line, "0", mon_count)
    elif mon_corner_count >= 3:
        mon_score = mon_count * 4
        mon_line = "MON: "
        for i in range(0, mon_count):
            mon_line = Combine_String(mon_line, "4", i)

    if currentBoard.BuildingState[0] == "True" and bch_count != 0:
        print(bch_line + " = " + str(bch_score))
    elif currentBoard.BuildingState[0] == "True" and bch_count == 0:
        print(bch_line)
    
    if currentBoard.BuildingState[1] == "True" and fac_count != 0:
        print(fac_line + " = " + str(fac_score))
    elif currentBoard.BuildingState[1] == "True" and fac_count == 0:
        print(fac_line)

    if currentBoard.BuildingState[2] == "True" and hse_count != 0:
        print(hse_line + " = " + str(hse_score))
    elif currentBoard.BuildingState[2] == "True" and hse_count == 0:
        print(hse_line)

    if currentBoard.BuildingState[3] == "True" and shp_count != 0:
        print(shp_line + " = " + str(shp_score))
    elif currentBoard.BuildingState[3] == "True" and shp_count == 0:
        print(shp_line)

    if currentBoard.BuildingState[4] == "True" and hwy_count != 0:
        print(hwy_line + " = " + str(hwy_score))
    elif currentBoard.BuildingState[4] == "True" and hwy_count == 0:
        print(hwy_line)

    if currentBoard.BuildingState[5] == "True" and prk_count != 0:
        print(prk_line + " = " + str(prk_score))
    elif currentBoard.BuildingState[5] == "True" and prk_count == 0:
        print(prk_line)

    if currentBoard.BuildingState[6] == "True" and mon_count != 0:
       print(mon_line + " = " + str(mon_score))
    elif currentBoard.BuildingState[6] == "True" and mon_count == 0:
        print(mon_line)
    

    score = bch_score + fac_score + hse_score + shp_score + hwy_score + prk_score + mon_score
    print("Total Score: " + str(score) + "\n") 
    return score
    

def Combine_String(main, sub, count):
    if count == 0:
        main = main + sub
    else:
        main = main + " + " + sub

    return main

'''
    Recursive Method for PARK
'''
# Recursive method for PRK
# The base recursive
def PRK_Recursive(path, current, active):
    path.append(current)
    down_count = 0
    up_count = 0
    self_left = 0
    self_right = 0

    #left
    if [current[0], current[1] - 1] in active and [current[0], current[1] - 1] not in path:
        self_left, active = PRK_Recursive(path, [current[0], current[1] - 1], active)
    #right
    if [current[0], current[1] + 1] in active and [current[0], current[1] + 1] not in path:
        self_right, active = PRK_Recursive(path, [current[0], current[1] + 1], active)

    #downwards
    if [current[0]  + 1, current[1]] in active and [current[0]  + 1, current[1]] not in path:
        down_count, active = PRK_Recursive(path, [current[0]  + 1, current[1]], active)
    #upwards
    if [current[0] - 1, current[1]] in active and [current[0] - 1, current[1]] not in path:
        up_count, active = PRK_Recursive(path, [current[0] - 1, current[1]], active)

    counter = 1 + down_count + up_count + self_left + self_right

    for item in active:
        if item == current:
            active.remove(item)
            break

    return counter, active

'''
    Recursive Method for High Way
'''
# Recursive method for Highway
def HWY_Recursive(board, x, y, row, col):
    return 1 + HWY_RecursiveLeft(board, x, y - 1, row, col) + HWY_RecursiveRight(board, x, y + 1, row, col)

def HWY_RecursiveLeft(board, x, y, row, col):
    try:
        if y == -1:
            return 0

        if board[row[x]][col[y]] == "HWY":
            return 1 + HWY_RecursiveLeft(board, x, y - 1, row, col)
        else:
            return 0
    except:
        return 0

def HWY_RecursiveRight(board, x , y, row, col):
    try:
        if board[row[x]][col[y]] == "HWY":
            return 1 + HWY_RecursiveRight(board, x, y + 1, row , col)
        else:
            return 0
    except:
        return 0
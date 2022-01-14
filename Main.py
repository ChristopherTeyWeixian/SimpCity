from io import StringIO
from typing import Match
from files.Menu import *
from files.Game_Options import *

while (True):
    
    option = main_menu()
    match option:
        case "1":#Start new game
            board = Board()
            if board.New_Board() == False:
                continue
            while(True):
                if board.turn >= 17:
                    EndGame(board)
                    break
                else:
                    game_opt,building_to_build = game_menu(board)
                    match game_opt:
                        case "1":
                            choose = str(input("Build where? "))
                            place_building(board,building_to_build,choose)
                        case "2":
                            choose = str(input("Build where? "))
                            place_building(board,building_to_build,choose)
                        case "3":
                            print("see current score, not yet implement")
                        case "4":
                            board.Save_Board()
                        case "0":
                            break

        case "2":#Load saved game
            board = Board()
            if board.Load_Board() == False:
                continue
            while(True):
                game_opt,building_to_build = game_menu(board)
                match game_opt:
                    case "1":
                        choose = str(input("Build where? "))
                        place_building(board, building_to_build, choose)
                    case "2":
                        choose = str(input("Build where? "))
                        place_building(board, building_to_build, choose)
                    case "3":
                        display_remaining_building(board)
                    case "4":
                        print("see current score, not yet implement")
                    case "5":
                        board.Save_Board()
                    case "0":
                        break
        case "3":
            board = Board()
            board.Get_BuildingState()
            while True:
                value = Option_Building(board)
                if value == "0":
                    board.Set_BuildingState()
                    break
                else:
                    board.Change_BuildingState(value)           

        case "0":#Exit
            quit()
    



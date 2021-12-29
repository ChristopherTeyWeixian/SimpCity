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
                game_opt,building_to_build = game_menu(board)
                match game_opt:
                    case "1":
                        place_building(board,building_to_build)
                    case "2":
                        place_building(board,building_to_build)
                    case "3":
                        display_remaining_building(board)
                    case "4":
                        print("see current score, not yet implement")
                    case "5":
                        print("save game.... hmmm")
                    case "0":
                        break

        case "2":#Load saved game
            print("you chose 2")

        case "0":#Exit
            quit()
    



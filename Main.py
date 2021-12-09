from io import StringIO
from typing import Match
from files.Menu import *

while (True):
    
    option = main_menu()
    match option:
        case "1":
            board = Board()
            if board.New_Board() == False:
                continue
            while(True):
                game_opt = game_menu(board)
                match game_opt:
                    case "1":
                        print("building something 1")
                    case "2":
                        print("building something 2")
                    case "3":
                        print("see remaining building ehhhh")
                    case "4":
                        print("see current score, not yet implement")
                    case "5":
                        print("save game.... hmmm")
                    case "0":
                        break

        case "2":
            print("you chose 2")

        case "0":
            quit()
    



# This is a sample Python script.
from ReadFile import ReadFile
from Board import*
from Ship import ShipModels
from Ship import Coordinates


def validate_coords(pos):
    pos = pos.split()
    if len(pos) == 2 and pos[0].isnumeric() and pos[1].isnumeric():
        return int(pos[0]), int(pos[1])
    else:
        return False, False


def fire(atk_board, fire_board: FiringBoard, atk_name, def_board, def_name, ship_model):
    print(f"{atk_name}'s Firing Board")
    fire_board.print()
    print(f"{atk_name}'s Placement Board.")
    atk_board.print()
    location = valid_fire(fire_board, atk_name, def_board)
    if def_board.board[location[0]][location[1]] == "*":
        print(f"{atk_name} missed.")
        def_board.board[location[0]][location[1]] = "O"
        atk_board.board[location[0]][location[1]] = "O"
        return atk_board, def_board
    else:
        print(f"{atk_name} hit {def_name}'s {def_board.board[location[0]][location[1]]}!")
        def_board.board[location[0]][location[1]] = "X"
        atk_board.board[location[0]][location[1]] = "X"
        for key in ship_model.dictionary:
            if def_board.board[location[0]][location[1]] == key:
                ship_model.dictionary[key] = ship_model.dictionary[key] - 1
            if ship_model.dictionary[key] == 0:
                print(f"{atk_name} destroyed {def_name}'s {key}!")
                del ship_model.dictionary[key]
        # counter = 0
        # for key in keys:
        #     for i in range(len(def_board)):
        #         for j in range(len(def_board[0])):
        #             if key == def_board[i][j]:
        #                 counter += 1
        #     if counter == 0:
        #         del keys[key]
        #         print(f"{atk_name} destroyed {def_name}'s {key}!")


def valid_fire(board, name, def_board):
    while True:
        location = input(f"{name}, enter the location you want to fire at in the form row col: ").split(' ')
        if len(location) != 2:
            continue
        elif location[0].isnumeric and location[1].isnumeric:
            location = list(map(int, location))
            if 0 <= location[0] <= board.rows - 1 and 0 <= location[1] <= board.cols - 1:
                if def_board.board[location[0]][location[1]] != "O" or "X":
                    return location
                else:
                    continue
            else:
                continue
        else:
            continue


def game_over(board1, board2, name1, name2):
    for i in range(board1.rows):
        for j in range(board1.cols):
            if board1.board[i][j].isalpha() and board1.board[i][j] != ('X' or 'O'):
                return False
            else:
                print(f"{name2} won!")
                return True
    for i in range(board2.rows):
        for j in range(board2.cols):
            if board2.board[i][j].isalpha() and board2.board[i][j] != ('X' or 'O'):
                return False
            else:
                print(f"{name1} won!")
                return True


def main():
    # get input
    config_file = input("Please enter the path to the configuration file for this game: ")
    player1 = input("Player 1, please enter your name: ")
    player2 = input("Player 2, please enter your name: ")

    # read in config file
    file_in = ReadFile(config_file)
    ship_models = ShipModels(file_in.ship_models_list())
    p1_place = PlacementBoard(file_in.rows, file_in.cols)
    p2_place = PlacementBoard(file_in.rows, file_in.cols)

    # p1 placement
    p1_place.print()
    for model in ship_models.model_list:
        while True:
            orient = input(f"{player1}, enter the orientation of your {model[0]}, which is {model[1]} long: ")
            orient = Board.find_orientation(orient)
            if orient is False:
                continue
            else:
                break
        while True:
            pos = input(f"{player1}, enter the starting location for your {model[0]}, which is {model[1]} long: ")
            x_pos, y_pos = validate_coords(pos)
            if x_pos is False:
                continue
            place_pos = Coordinates(x_pos, y_pos)
            if p1_place.place_ship(place_pos, orient, model[0], int(model[1])):
                break
        p1_place.print()

    # p2 placement
    p2_place.print()
    for model in ship_models.model_list:
        while True:
            orient = input(f"{player2}, enter the orientation of your {model[0]}, which is {model[1]} long: ")
            orient = Board.find_orientation(orient)
            if orient is False:
                continue
            else:
                break
        while True:
            pos = input(f"{player2}, enter the starting location for your {model[0]}, which is {model[1]} long: ")
            x_pos, y_pos = validate_coords(pos)
            if x_pos is False:
                continue
            place_pos = Coordinates(x_pos, y_pos)
            if p2_place.place_ship(place_pos, orient, model[0], int(model[1])):
                break
        p2_place.print()

    p1_firing = FiringBoard(file_in.rows, file_in.cols)
    p2_firing = FiringBoard(file_in.rows, file_in.cols)
    counter = 0
    while not game_over(p1_place, p2_place, player1, player2):
        if counter % 2 == 0:
            fire(p1_place, p1_firing, player1, p2_place, player2, ship_models)
            counter += 1
        else:
            fire(p2_place, p2_firing, player2, p1_place, player1, ship_models)
            counter += 1

    # do firing mechanics

    # read in user coordinates of where to fire
    # x_pos = user x coordinate
    # y_pos = user y coordinate
    # p1_firing.fire(x_pos, y_pos)  <- this should do something meaningful

    # determine winner

main()

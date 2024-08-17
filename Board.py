from Ship import Coordinates


class Board:
    def __init__(self, rows, cols):
        self.board = [["*" for _ in range(cols)] for _ in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        #         self.board[i][j] = '*'
        self.rows = rows
        self.cols = cols

    def print(self):
        self.print_header()
        for i in range(self.rows):
            for j in range(-1, self.cols):
                if j + 1 == self.cols:
                    end_char = ''
                else:
                    end_char = ' '
                if j == -1:
                    print(i, end=end_char)
                elif self.board[i][j] == 0:
                    print('*', end=end_char)
                else:
                    print(self.board[i][j], end=end_char)
            print('')

    def print_header(self):
        print(' ', end=' ')
        for i in range(self.cols):
            print(i, end=' ')
        print('')

    @staticmethod
    def find_orientation(orientation):
        orientation = orientation.lower()
        vert_list = ["v", "ve", "ver", "vert", "verti", "vertica", "vertical"]
        hori_list = ["h", "ho", "hor", "hori", "horiz", "horizo", "horizon", "horizont", "horizonta", "horizontal"]
        if orientation in hori_list:
            return "h"
        elif orientation in vert_list:
            return "v"
        else:
            return False

    def check_coords(self, x_pos, y_pos ):
        if (0 <= x_pos <= self.cols - 1 and 0 <= y_pos <= self.rows - 1) and self.board[x_pos][y_pos] == '*':
            return True
        return False


class PlacementBoard(Board):
    def place_ship(self, pos: Coordinates, orientation, ship_type, ship_len):
        if self.check_coords(pos.x, pos.y):
            orient = Board.find_orientation(orientation)
            if orient == "h":
                for i in range(ship_len):
                    if self.board[pos.x][pos.y + i] != '*':
                        return False
                for i in range(ship_len):
                    self.board[pos.x][pos.y + i] = ship_type[0]
                return True
            elif orient == "v" and self.check_coords(pos.x, pos.y + ship_len):
                for i in range(ship_len):
                    if self.board[pos.x + i][pos.y] != '*':
                        return False
                for i in range(ship_len):
                    self.board[pos.x + i][pos.y] = ship_type[0]
                return True
        return False


class FiringBoard(Board):
    # make other functions as needed
    def fire(self, x_pos, y_pos):

        # do something here and delete return False
        print()
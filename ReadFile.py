from Ship import Ship


class ReadFile:
    # initialize file
    def __init__(self, filename):
        # open the file
        with open(filename) as file:
            lines = file.readlines()
            self.rows = int(lines[0])  # first line is num of rows
            self.cols = int(lines[1])  # second line is num of cols
            self.num_of_ships = int(lines[2])  # third line is num of ships
            self.ship_types = []
            # iterate through the remaining lines of the file
            for i in range(3, 3+self.num_of_ships):
                line = lines[i].split()
                char = line[0]
                length = line[1]
                self.ship_types.append(Ship(char, length))

    def ship_models_list(self):
        return self.ship_types

    def display_ship_types(self):
        for ship_type in self.ship_types:
            ship_type.ship_print()

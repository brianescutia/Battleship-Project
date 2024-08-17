

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, char, length):
        self.char = char
        self.length = length

    def ship_print(self):
        print("Char:", self.char, " Length:", self.length)


class ShipModels:
    def __init__(self, model_lists):
        self.model_list = []
        for model in model_lists:
            self.model_list.append((model.char, model.length))
        self.model_list.sort()  # sort alphabetically
        self.dictionary = {}
        for model in self.model_list:
            self.dictionary.update({model[0]: int(model[1])})
    def get_len(self, model):
        for ship_model in self.model_list:
            if ship_model[0] == model:
                return int(ship_model[1])






class Cell:
    def __init__(self, item):
        self.__item = item

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, item):
        self.__item = item

class Item:
    def __init__(self):
        pass

class Food(Item):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "F"

    def getBit(self):
        return 1

class Piece(Item):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "S"

    def getBit(self):
        return 1

class Empty(Item):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return " "

    def getBit(self):
        return 0

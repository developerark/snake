from Item import *
from threading import Lock
import random
import time

class Game:
    class Direction:
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)

    def __init__(self, rows, cols):
        if rows <= 0 and cols <= 0:
            raise Exception("Cant initialize an emtpy game")

        self.__rows = rows
        self.__cols = cols
        self.__grid = []
        self.__gridMutex = Lock()
        self.__snakePosition = None
        self.__direction = None
        self.__directionMutex = Lock()
        self.__speed = 1                 # Unit per second
        self.__foodPosition = None

        # Initialize the game grid
        for i in range(0, self.__rows):
            row = []
            for j in range(0, self.__cols):
                row.append(Cell(Empty()))
            self.__grid.append(row)

    def initialize(self):
        self.__snakePosition = [(random.randint(0, self.__rows - 1), random.randint(0, self.__cols - 1))]
        directions = [Game.Direction.left, Game.Direction.right, Game.Direction.up, Game.Direction.down]
        self.__directionMutex.acquire()
        self.__direction = directions[random.randint(0, len(directions) - 1)]
        self.__directionMutex.release()
        self.__foodPosition = (random.randint(0, self.__rows - 1), random.randint(0, self.__cols - 1))
        self.__gridMutex.acquire()
        # set Snake
        for position in self.__snakePosition:
            self.__grid[position[0]][position[1]].item = Piece()

        # set Food
        self.__grid[self.__foodPosition[0]][self.__foodPosition[1]].item = Food()
        self.__gridMutex.release()

    def __checkValid(self, nextPosition):
        # Touches itself
        for position in self.__snakePosition:
            if position[0] == nextPosition[0] and position[1] == nextPosition[1]:
                print("Touched itself, game over")
                return False
        # Touches edge
        if nextPosition[0] < 0 or nextPosition[0] >= self.rows or nextPosition[1] < 0 or nextPosition[1] >= self.cols:
            print("Touched the edge, game over")
            return False
        return True

    def __gotFood(self, nextPosition):
        if nextPosition[0] == self.__foodPosition[0] and nextPosition[1] == self.__foodPosition[1]:
            return True
        return False

    def start(self):
        sleepTime = 1 / self.__speed
        while True:
            currentHeadPosition = self.__snakePosition[0]
            self.__directionMutex.acquire()
            nextPosition = (currentHeadPosition[0] + self.__direction[0], currentHeadPosition[1] + self.__direction[1])
            self.__directionMutex.release()
            if (not self.__checkValid(nextPosition)):
                # Game over
                return
            elif (self.__gotFood(nextPosition)):
                self.__snakePosition.insert(0, nextPosition)
                self.__gridMutex.acquire()
                self.__grid[nextPosition[0]][nextPosition[1]].item = Piece()
                self.__gridMutex.release()
                self.__foodPosition = (random.randint(0, self.__rows - 1), random.randint(0, self.__cols - 1))
                self.__gridMutex.acquire()
                self.__grid[self.__foodPosition[0]][self.__foodPosition[1]].item = Food()
                self.__gridMutex.release()
            else:
                self.__snakePosition.insert(0, nextPosition)
                self.__gridMutex.acquire()
                self.__grid[nextPosition[0]][nextPosition[1]].item = Piece()
                self.__grid[self.__snakePosition[-1][0]][self.__snakePosition[-1][1]].item = Empty()
                self.__gridMutex.release()
                del self.__snakePosition[-1]
            time.sleep(sleepTime)

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    @property
    def bits(self):
        self.__gridMutex.acquire()
        bits = []
        for row in self.__grid:
            rowBits = []
            for c in row:
                rowBits.append(c.item.getBit())
            bits.append(rowBits)
        self.__gridMutex.release()
        return bits

    def __str__(self):
        self.__gridMutex.acquire()
        rowStrings = []
        for row in self.__grid:
            rowStrings.append("".join([str(cell.item) for cell in row]))
        self.__gridMutex.release()
        return "\n".join(rowStrings)

    def setCell(self, row, col, item):
        self.__gridMutex.acquire()
        self.__grid[row][col].item = item
        self.__gridMutex.release()

    def moveLeft(self):
        self.__directionMutex.acquire()
        self.__direction = Game.Direction.left
        self.__directionMutex.release()

    def moveRight(self):
        self.__directionMutex.acquire()
        self.__direction = Game.Direction.right
        self.__directionMutex.release()

    def moveUp(self):
        self.__directionMutex.acquire()
        self.__direction = Game.Direction.up
        self.__directionMutex.release()

    def moveDown(self):
        self.__directionMutex.acquire()
        self.__direction = Game.Direction.down
        self.__directionMutex.release()


if __name__ == "__main__":
    game = Game(8, 8)
    print(game)

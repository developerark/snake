from States import *
from Game import Game
import time
from Item import *

class GameController:
    def __init__(self):
        self.__game = Game(20, 20)
        self.idleState = Idle()
        self.gameOnState = GameOn()
        self.gameOverState = GameOver()
        self.__currentState = self.idleState

    @property
    def currentState(self):
        return self.__currentState

    @currentState.setter
    def currentState(self, state):
        self.__currentState = state

    @property
    def game(self):
        return self.__game

    def leftPressed(self):
        self.__currentState.leftPressed(self)

    def rightPressed(self):
        self.__currentState.rightPressed(self)

    def upPressed(self):
        self.__currentState.upPressed(self)

    def downPressed(self):
        self.__currentState.downPressed(self)

    def __animateIdleState(self):
        # Make alternate pixels glow
        while (self.__currentState == self.idleState):
            for row in range(0, self.__game.rows):
                for col in range(0, self.__game.cols):
                    rowtype = (row % 2) == 0
                    coltype = (col % 2) == 0
                    if rowtype == coltype:
                        self.__game.setCell(row=row, col=col, item=Food())
                    else:
                        self.__game.setCell(row=row, col=col, item=Empty())
            time.sleep(0.5)

            for row in range(0, self.__game.rows):
                for col in range(0, self.__game.cols):
                    rowtype = (row % 2) == 0
                    coltype = (col % 2) == 0
                    if rowtype != coltype:
                        self.__game.setCell(row=row, col=col, item=Food())
                    else:
                        self.__game.setCell(row=row, col=col, item=Empty())
            time.sleep(0.5)

    def start(self):
        while True:
            # Game starts here like view did load
            self.__animateIdleState()

            time.sleep(1)
            # Snake food should appear and the snake should start moving
            for row in range(0, self.__game.rows):
                for col in range(0, self.__game.cols):
                    self.__game.setCell(row, col, Empty())
            time.sleep(1)

            self.__game.initialize()
            self.__game.start()
            self.__currentState = self.idleState

def draw(stdscr):
    while True:
        stdscr.addstr(0, 0, "Hello")
        stdscr.refresh()
        time.sleep(1)

if __name__ == "__main__":
    gameController = GameController()

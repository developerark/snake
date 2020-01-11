class GameState:
    def __init__(self):
        pass

    def changeState(self, gameController, state):
        gameController.currentState = state

    def leftPressed(self, gameController):
        print("Left Pressed from super")

    def rightPressed(self, gameController):
        print("Right Pressed from super")

    def upPressed(self, gameController):
        print("Up Pressed from super")

    def downPressed(self, gameController):
        print("Down Pressed from super")

class Idle(GameState):
    def __init__(self):
        super().__init__()

    def leftPressed(self, gameController):
        self.changeState(gameController=gameController, state=gameController.gameOnState)

    def rightPressed(self, gameController):
        self.changeState(gameController=gameController, state=gameController.gameOnState)

    def upPressed(self, gameController):
        self.changeState(gameController=gameController, state=gameController.gameOnState)

    def downPressed(self, gameController):
        self.changeState(gameController=gameController, state=gameController.gameOnState)


class GameOn(GameState):
    def __init__(self):
        super().__init__()

    def leftPressed(self, gameController):
        gameController.game.moveLeft()

    def rightPressed(self, gameController):
        gameController.game.moveRight()

    def upPressed(self, gameController):
        gameController.game.moveUp()

    def downPressed(self, gameController):
        gameController.game.moveDown()

class GameOver(GameState):
    def __init(self):
        super().__init__()

    def leftPressed(self, gameController):
        pass

    def rightPressed(self, gameController):
        pass

    def upPressed(self, gameController):
        pass

    def downPressed(self, gameController):
        pass

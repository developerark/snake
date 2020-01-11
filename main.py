from GameController import GameController
from threading import Thread
from Drawing import Drawing
import time
import EventListener

if __name__ == "__main__":
    gameController = GameController()

    # Start Drawing
    drawingThread = Thread(target=Drawing.start, args=(gameController.game, 4,), daemon=True)
    drawingThread.start()

    EventListener.gameController = gameController
    listenerThread = Thread(target=EventListener.start, daemon=True)
    listenerThread.start()

    try:
        # Go the event stuff
        gameController.start()
    except KeyboardInterrupt as error:
        Drawing.isRunning = False
        drawingThread.join()
        print("Terminating...")

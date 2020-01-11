gameController = None

def start():
    while (True):
        event = input(">>>")
        if event == 'a':
            print("Left Pressed")
            gameController.leftPressed()
        if event == 'd':
            print("Right Pressed")
            gameController.rightPressed()
        if event == 'w':
            print("Up Pressed")
            gameController.upPressed()
        if event == 's':
            print("Down Pressed")
            gameController.downPressed()

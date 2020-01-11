import time
class Drawing:
    isRunning = True
    @classmethod
    def start(cls, game, fps=8):
        sleepTime = 1 / fps
        while (Drawing.isRunning):
            #print(game, end='\r')
            with open("output", 'w') as file:
                file.write(str(game))
            time.sleep(sleepTime)

import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
  if data[1005,210] < 128:
    for i in range(240, 440):
        for j in range(400, 420):
            if data[i, j] < 100:
                hit("up")
                return
  else:
    for i in range(240, 440):
        for j in range(400, 420):
            if data[i, j] > 100:
                hit("up")
                return

  return

if __name__ == "__main__":
    print("Hey!!! Dino game about to start in 3 seconds")
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # for i in range(105, 110):
        #     for j in range(410, 415): 
        #         data[i,j] = 0

        # for i in range(275, 325):
        #     for j in range(300, 370):
        #         data[i,j] = 171
        # image.show()
        # break

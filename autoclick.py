import pynput
import time
import keyboard
from pynput.mouse import Button, Controller
import time
import random
import os
from multiprocessing import Process

lowestcps=input("lowest range cps")
highestcps =input("highest range cps")



cpsdelay = 0
cps = random.randint(int(lowestcps), int(highestcps))
delay = 1 / int(cps)


mouse = Controller()




        
        



while True:
        if keyboard.is_pressed('r'):
            keyboard.release('w')
            cps = random.randint(int(lowestcps), int(highestcps))
            delay = 1 / int(cps)
            mouse.press(Button.left)
            time.sleep(0.00000001)
            mouse.release(Button.left)
            keyboard.press('w')
            time.sleep(delay-0.000001)
            keyboard.release('w')
            time.sleep(000000000000000000000000.00000000000000000000000000001)
            keyboard.press('w')

            





        








input()

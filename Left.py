import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random


print("""          
    __  __________    ________  _____
   / / / / ____/ /   /  _/ __ \/ ___/
  / /_/ / __/ / /    / // / / /\__ \ 
 / __  / /___/ /____/ // /_/ /___/ / 
/_/ /_/_____/_____/___/\____//____/                                                 
                                                                         
   _________      __            
  / ____/ (_)____/ /_____  _____
 / /   / / / ___/ //_/ _ \/ ___/
/ /___/ / / /__/ ,< /  __/ /    
\____/_/_/\___/_/|_|\___/_/

Click with the speed of the sun
""")

destructkey =input("keybind for self destruct ")
togglekey =input("keybind for toggle ")

lowestcps =input("enter lowest cps for range ")

highestcps =input("enter highest cps for range ")

cpsdelay = 0
cps = random.randint(int(lowestcps), int(highestcps))



delay = 1






button = Button.left
start_stop_key = KeyCode(char=togglekey)
exit_key = KeyCode(char=destructkey)



class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                cps = random.randint(int(lowestcps), int(highestcps))
                self.delay = 1 / int(cps)
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

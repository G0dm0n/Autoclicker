import tkinter as tk
from pynput import keyboard
from pynput.mouse import Button, Controller
import threading
import time

with open('config.txt', 'r') as file:
    targetKey = file.read()

def keyButton():
    def sniffTargetKey(key):
        global targetKey
        try:
            targetKey = key.char
            with open('config.txt', 'w') as file:
                file.write(str(targetKey))
        except AttributeError:
            targetKey = key
            with open('config.txt', 'w') as file:
                file.write(str(targetKey))
        return False
    with keyboard.Listener(on_press=sniffTargetKey) as listener:
        listener.join()

def startStop():
    def sniffKeys(key):
        global targetKey, clicking
        try:
            if targetKey == key.char:
                clicking = not clicking
        except AttributeError:
            if targetKey == key:
                clicking = not clicking
    with keyboard.Listener(on_press=sniffKeys) as listener:
        listener.join()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
sss
# Threading
startStopThread = threading.Thread(target=startStop)
clickerThread = threading.Thread(target=clicker)

# Tkinter
root = tk.Tk()
root.title("Autoclicker")
root.minsize(500, 300)
keyButton = tk.Button(root, text="Change", font=("Verdana", 10), command=keyButton)
keyButton.place(x=70, y=80)
keyLabel = tk.Label(root, text=targetKey, font=('Verdana', 14))
keyLabel.place(x=50, y=50)

# Variables
clicking = False
mouse = Controller()

# main func
if __name__ == "__main__":
    clickerThread.start()
    startStopThread.start()
    root.mainloop()
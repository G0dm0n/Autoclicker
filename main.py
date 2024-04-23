import tkinter as tk
from pynput import keyboard
from pynput.mouse import Button, Controller
import threading
import time

def keyButton():
    pauseListener.clear()
    def sniffTargetKey(key):
        global targetKey
        try:
            targetKey = key.char
        except AttributeError:
            targetKey = key
        return False
    with keyboard.Listener(on_press=sniffTargetKey) as listener:
        listener.join()
    updateLabel(keyLabel, str(targetKey))
    pauseListener.set()

def startStop():
    def sniffKeys(key):
        global targetKey, clicking, activeListener
        if pauseListener.is_set():
            try:
                if targetKey == key.char:
                    eventClicking()
            except AttributeError:
                if targetKey == key:
                    eventClicking()
    with keyboard.Listener(on_press=sniffKeys) as listener:
        listener.join()

def clicker():
    while True:
        if clicking.is_set():
            mouse.click(Button.left, 1)
            time.sleep(0.01)
        else:
            time.sleep(0.1)
            
def updateLabel(label, text):
    def textUpdate():
        label.config(text=text)
    root.after(150, textUpdate)
    
def eventClicking():
    if clicking.is_set():
        clicking.clear()
    else:
        clicking.set()
    
# Threading
startStopThread = threading.Thread(target=startStop, daemon=True)
clickerThread = threading.Thread(target=clicker, daemon=True)

# Variables
pauseListener = threading.Event()
pauseListener.set()
clicking = threading.Event()
mouse = Controller()
targetKey = "o"
activeListener = True

# Tkinter
root = tk.Tk()
root.title("Autoclicker")
root.minsize(500, 300)
keyButton = tk.Button(root, text="Change", font=("Verdana", 10), command=keyButton)
keyButton.place(x=70, y=80)
keyLabel = tk.Label(root, text=targetKey, font=('Verdana', 14))
keyLabel.place(x=50, y=50)

# main func
if __name__ == "__main__":
    clickerThread.start()
    startStopThread.start()
    root.mainloop()

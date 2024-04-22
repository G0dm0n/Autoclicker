import tkinter as tk

def set_trigger_key(event):
    global trigger_key
    trigger_key = event.keysym
    trigger_entry.delete(0, tk.END)
    trigger_entry.insert(0, trigger_key)
    print(f"Spouštěcí klávesa nastavena na: {trigger_key}")

def on_key_press(event):
    if event.keysym == trigger_key:
        print(f"Stisknuta spouštěcí klávesa: {trigger_key}")
        trigger_action()

def trigger_action():
    print("Akce spuštěna!")

# Vytvoření GUI
root = tk.Tk()
root.minsize(500, 300)
root.title("Nastavení spouštěcí klávesy")

# Entry pro zobrazení/nastavení klávesy
trigger_entry = tk.Entry(root, font=('Arial', 14), width=12)
trigger_entry.pack(pady=20)

# Nastavení focusu na Entry pro snadné zadání klávesy
trigger_entry.focus_set()

# Button pro potvrzení klávesy
set_button = tk.Button(root, text="Nastavit klávesu", font=('Arial', 14), command=lambda: trigger_entry.bind("<Key>", set_trigger_key))
set_button.pack(pady=10)

# Vazba klávesnice na root okno pro sledování stisku klávesy
root.bind("<Key>", on_key_press)

root.mainloop()
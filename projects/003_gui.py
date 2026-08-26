import tkinter as tk
import random

def getRandom():
  lbl.config(text=random.randint(1, 100))
  return

def greet():
  name = entry1.get().strip()
  if not name:
    name = "Arath"
  lbl.config(text=f"Hello, {name}")


root = tk.Tk()
root.geometry("400x300")

tk.Label(root, text="Name").grid(pady=20, row=0, column=0)
tk.Label(root, text="Incremento").grid(pady=20, row=1, column=0)
tk.Label(root, text="Final").grid(pady=20, row=2, column=0)

lbl = tk.Label(root)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
button1 = tk.Button(root, text="Random", command=getRandom)
button2 = tk.Button(root, text="Close app", command=root.destroy)
button3 = tk.Button(root, text="Greet", command=greet)

entry1.grid(pady=10, row=0, column=1)
entry2.grid(pady=10, row=1, column=1)
entry3.grid(pady=10, row=2, column=1)
button1.grid(pady=10, row=3, column=0)
button2.grid(pady=10, row=3, column=1)
button3.grid(pady=10, row=3, column=2)
lbl.grid(pady=10, row=4, column=1)

root.mainloop()
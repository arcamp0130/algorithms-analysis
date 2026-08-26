import tkinter as tk
import random

def getRandom():
  print(random.randint(1, 100))
  return

root = tk.Tk()

tk.Label(root, text="Inicio").grid(row=0, column=0)
tk.Label(root, text="Incremento").grid(row=1, column=0)
tk.Label(root, text="Final").grid(row=2, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
button1 = tk.Button(root, text="Random", command=getRandom)
button2 = tk.Button(root, text="Close app", command=root.destroy)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)

root.mainloop()
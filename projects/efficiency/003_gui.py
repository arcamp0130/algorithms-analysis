import tkinter as tk
from tkinter import messagebox
import random

class AnalyzerGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Analyzer")
    self.root.geometry("700x400")
    self.root.resizable(False, False)

    self.build()


  def build(self):
    frame = tk.Frame(self.root)

    tk.Label(self.root, text="Start").grid(padx=5, pady=10, row=0, column=0)
    tk.Label(self.root, text="Increment").grid(padx=5, pady=10, row=1, column=0)
    tk.Label(self.root, text="End").grid(padx=5, pady=10, row=2, column=0)

    self.start_var = tk.StringVar(value="10")
    self.entry1 = tk.Entry(self.root, textvariable=self.start_var)
    self.entry1.grid(pady=10, row=0, column=1)
    
    self.inc_var = tk.StringVar(value="10")
    self.entry2 = tk.Entry(self.root, textvariable=self.inc_var)
    self.entry2.grid(pady=10, row=1, column=1)
    
    self.end_var = tk.StringVar(value="10")
    self.entry3 = tk.Entry(self.root, textvariable=self.end_var)
    self.entry3.grid(pady=10, row=2, column=1)
    
    self.button1 = tk.Button(self.root, text="Generate", command=self.validate)
    self.button1.grid(pady=10, row=3, column=0)
    
    self.button2 = tk.Button(self.root, text="Close app", command=self.root.destroy)
    self.button2.grid(pady=10, row=3, column=1)
    
    self.lbl = tk.Label(self.root)
    self.lbl.grid(pady=10, row=4, column=1)

  def getRandom():
    self.lbl.config(text=random.randint(1, 100))
    return

  def greet():
    name = entry1.get().strip()
    if not name:
      name = "Arath"
    self.lbl.config(text=f"Hello, {name}")

  def validate(self):
    try:
      # Fetch and cast inputs to integers
      start_val = int(self.start_var.get())
      inc_val = int(self.inc_var.get())
      end_val = int(self.end_var.get())

      # Basic logic validation
      if start_val <= 0 or inc_val <= 0:
        self.lbl.config(text="Start and Increment must be greater than 0.")
        return
      if end_val <= start_val:
        self.lbl.config(text="End value must be greater than Start value.")
        return

      self.lbl.config(text="Ready to generate")

    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid whole numbers.")

root = tk.Tk()
app = AnalyzerGUI(root)
root.mainloop()
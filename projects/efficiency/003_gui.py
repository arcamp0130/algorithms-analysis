import tkinter as tk
from tkinter import messagebox
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AnalyzerGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Analyzer")
    self.root.geometry("700x400")
    self.root.resizable(False, False)

    self.build()


  def build(self):
    input_frame = tk.Frame(self.root, padx=10, pady=10, width=300)
    input_frame.pack(side=tk.LEFT, fill=tk.Y)

    self.plot_frame = tk.Frame(self.root, padx=10, pady=10)
    self.plot_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(input_frame, text="Start").grid(padx=5, pady=10, row=0, column=0)
    tk.Label(input_frame, text="Increment").grid(padx=5, pady=10, row=1, column=0)
    tk.Label(input_frame, text="End").grid(padx=5, pady=10, row=2, column=0)

    self.start_var = tk.StringVar(value="10")
    self.entry1 = tk.Entry(input_frame, textvariable=self.start_var)
    self.entry1.grid(pady=10, row=0, column=1)
    
    self.inc_var = tk.StringVar(value="10")
    self.entry2 = tk.Entry(input_frame, textvariable=self.inc_var)
    self.entry2.grid(pady=10, row=1, column=1)
    
    self.end_var = tk.StringVar(value="10")
    self.entry3 = tk.Entry(input_frame, textvariable=self.end_var)
    self.entry3.grid(pady=10, row=2, column=1)
    
    self.button1 = tk.Button(input_frame, text="Generate", command=self.validate)
    self.button1.grid(pady=10, row=3, column=0)
    
    self.button2 = tk.Button(input_frame, text="Close app", command=self.root.destroy)
    self.button2.grid(pady=10, row=3, column=1)
    
    self.lbl = tk.Label(input_frame)
    self.lbl.grid(pady=10, row=4, column=1)

    # Create matplot figure
    self.figure = Figure(figsize=(5, 4), dpi=100)
    self.ax = self.figure.add_subplot(111)
    self.setup_chart_formatting()

    # Embed matplot figure
    self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
    self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    self.canvas.draw()

  def setup_chart_formatting(self):
    self.ax.set_title("Algorithm Performance")
    self.ax.set_xlabel("Number of Elements")
    self.ax.set_ylabel("Execution Time (ms)")
    self.ax.grid(True, linestyle='--', alpha=0.7)

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
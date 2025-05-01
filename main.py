import tkinter as tk
from controller import MeasurementController


if __name__ == "__main__":
    root = tk.Tk()
    app = MeasurementController(root)
    root.mainloop()
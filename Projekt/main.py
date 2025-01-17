import tkinter as tk
from Projekt.GUI import LabiryntGUI
from Projekt.Labirynt import Labirynt

if __name__ == "__main__":
    root = tk.Tk()
    app_lab = LabiryntGUI(root)
    root.mainloop()
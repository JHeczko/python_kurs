import tkinter as tk

from numpy.core.defchararray import upper
from tensorflow.python.ops.gen_data_flow_ops import map_incomplete_size


class Application(tk.Frame):
    def __init__(self, parent: tk.Tk, title: str = "Kostki"):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title(title)

        self.pack(fill="both", expand=True)

        self.rowconfigure(0, weight=0)  # Allow row 0 to stretch
        self.rowconfigure(1, weight=0)  # Allow row 0 to stretch
        self.rowconfigure(2, weight=1)  # Allow row 1 to stretch
        self.columnconfigure(0,weight=1)  # Allow column 0 to stretch

        self.createWidgets()

    def createWidgets(self):
        # Create upper and lower frames
        upper_label = tk.Frame(self, height=50, bg="#00394d")
        separator = tk.Frame(self, height=5,bg="#005580")
        lower_label = tk.Frame(self, bg="#00131a", height=800, width=800)
        lower_label.columnconfigure(0, weight=1)
        lower_label.columnconfigure(1, weight=1)

        # Upper label widgets
        welcome_text = tk.Label(upper_label,text="Witam w symulatorze kostki 6 ściennej :)", fg="lightblue", font=("System", 20, "bold"))
        welcome_text.pack(expand=True, fill="both")

        # Lower label widgets


        # Place frames in grid
        upper_label.grid(row=0, column=0, sticky="ew")
        separator.grid(row=1, column=0, sticky="ew")
        lower_label.grid(row=2, column=0, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
import tkinter as tk
import random

import numpy as np

from Labirynt import Labirynt

def validate_input(new_value):
    # Allow empty input (to allow deletion) or digits only
    if new_value == "" or new_value.isdigit():
        return True
    return False


def create_lab(frame :tk.Frame, rows:int,columns:int):

    if type(rows) != int:
        rows = int(rows)
    if type(columns) != int:
        columns = int(columns)

    size_block = 300 / columns

    for widget in frame.winfo_children():
        widget.destroy()

    lab = Labirynt(rows,columns)
    lab.generate_random_labirynt()
    lab_matrix = lab.generate_maze_matrix()
    canvas = tk.Canvas(frame,width=((2*columns)+1) * size_block, height=((rows*2)+1) * size_block)

    for i_row,row in enumerate(lab_matrix):
        for i_col, item in enumerate(row):
            color = "black" if item == 1 else "white"
            x1 = i_col * size_block
            y1 = i_row * size_block
            x2 = x1 + size_block
            y2 = y1 + size_block
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    canvas.pack(side=tk.TOP)


if __name__ == "__main__":
    dark_gray = "#262626"
    darker_gray = "#121211"
    system_font = ("Arial", 10, "bold")


    root = tk.Tk()
    root.title("Labirynt")
    root.geometry("800x800")
    root.config(bg=dark_gray)
    root.columnconfigure(0, minsize=600, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    validate_command = root.register(validate_input)

    frame_placeholder = tk.Frame(root)
    frame1 = tk.Frame(frame_placeholder, bg=dark_gray)
    frame2 = tk.Frame(root, bg=dark_gray)

    frame1.config(bg=dark_gray)
    frame2.config(bg=dark_gray)

    frame_placeholder.grid(row=0, column=0, sticky="nsew")
    frame1.pack(fill=tk.BOTH, expand=True)
    frame2.grid(row=0, column=1, sticky="nsew")

    #creating widgets for frame2
    height_in = tk.Entry(frame2, width=20, font = system_font, bg='gray',validate="key", validatecommand=(validate_command, "%P"))
    width_in = tk.Entry(frame2, width=20, font = system_font, bg='gray',validate="key", validatecommand=(validate_command, "%P"))
    height_label = tk.Label(frame2, text="Ilość wierszy:", bg=dark_gray, fg="white", font=system_font)
    width_label = tk.Label(frame2, text="Ilość kolumn:", bg=dark_gray, fg="white", font=system_font)
    button_generate = tk.Button(frame2, text="Wygeneruj Labirynt", bg='gray', fg="white", font=system_font, command=lambda: create_lab(frame1, width_in.get(),height_in.get()))

    height_in.pack(side =tk.BOTTOM, pady=10)
    height_label.pack(side =tk.BOTTOM, pady=10)
    width_in.pack(side =tk.BOTTOM,pady=5)
    width_label.pack(side=tk.BOTTOM, pady=10)
    button_generate.pack(side =tk.TOP,pady=20)


    root.mainloop()
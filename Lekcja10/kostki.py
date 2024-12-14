import tkinter as tk
import random

from soupsieve.util import lower
from tensorboard.summary.v1 import image


class Application(tk.Frame):
    def __init__(self, parent: tk.Tk, title: str = "Kostki"):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title(title)
        parent.geometry("800x800")

        self.text_font = ("System", 20, "bold")
        self.output_text = tk.StringVar(value="Kliknij guzik na dole, aby rzucić kostką!")
        self.image_dice = tk.PhotoImage(file="")

        self.pack(fill="both", expand=True)

        self.rowconfigure(0, weight=0)  # Allow row 0 to stretch
        self.rowconfigure(1, weight=0)  # Allow row 0 to stretch
        self.rowconfigure(2, weight=1)  # Allow row 1 to stretch
        self.columnconfigure(0,weight=1)  # Allow column 0 to stretch

        self.createWidgets()


    def createWidgets(self):
        def random_number(photo_dice):
            random_int = random.randint(1, 6)
            self.image_dice = tk.PhotoImage(file=f"./image/{random_int}.png")
            self.output_text.set(f"Wylosowałeś: {random_int}")
            photo_dice.config(image=self.image_dice)

        # Create upper and lower frames
        upper_label = tk.Frame(self, height=50, bg="#262626")

        separator = tk.Frame(self, height=5,bg="#005580")

        lower_label = tk.Frame(self, bg="#262626", height=700, width=800)
        lower_label.rowconfigure(0,minsize=50, weight=1)
        lower_label.rowconfigure(1,minsize=500, weight=1)
        lower_label.rowconfigure(2, weight=1)
        lower_label.columnconfigure(0, weight=1)

        # Upper label widgets
        welcome_text = tk.Label(upper_label,text="Witam w symulatorze kostki 6 ściennej :)", fg="lightblue", bg="#262626", font=self.text_font)
        welcome_text.pack(expand=True, fill="both")

        # Lower label widgets
        play_button = tk.Button(
            lower_label,
            text="Rzuć kością",
            font=self.text_font,
            bg="black",  # Set background color
            fg="lightblue",  # Set text color
            activebackground="gray",  # Background when hovered
            activeforeground="black",  # Text color when hovered
            highlightthickness=0,  # Remove button border highlight
            borderwidth=0,  # Adjust border thickness
            command=lambda: random_number(photo_dice)
        )

        info_random = tk.Label(lower_label, textvariable=self.output_text, font=self.text_font, fg="lightblue", bg='#262626')
        photo_dice = tk.Label(lower_label,bg="#262626", image=self.image_dice)

        info_random.grid(row=0,column=0, sticky="nsew")
        photo_dice.grid(row=1, column=0, sticky="nsew")
        play_button.grid(row=2, column=0)

        # Setting up grid
        upper_label.grid(row=0, column=0, sticky="ew")
        separator.grid(row=1, column=0, sticky="ew")
        lower_label.grid(row=2, column=0, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
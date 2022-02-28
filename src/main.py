import tkinter as tk
from tkinter import *
from tkinter.font import Font
from utils import *


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bravo Tango Beta")
        self.geometry("512x512")
        self.build_menubar()
        self.create_attributes()

    def build_menubar(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        file_menu = Menu(menubar)
        file_menu.add_command(label="Open", command=lambda: open_file())
        menubar.add_cascade(label="File", menu=file_menu)

    def create_attributes(self):
        attrib_font = Font(size=16)
        # character name
        name_label = Label(self, text="Character Name:", font=attrib_font)
        name_entry = Entry(self, font=attrib_font)
        name_label.grid(column=0, row=0)
        name_entry.grid(column=1, row=0)
        # attributes
        str_label = Label(self, text="Strength:", font=attrib_font)
        str_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        dex_label = Label(self, text="Dexterity:", font=attrib_font)
        dex_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        agi_label = Label(self, text="Agility:", font=attrib_font)
        agi_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        will_label = Label(self, text="Willpower:", font=attrib_font)
        will_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        end_label = Label(self, text="Endurance:", font=attrib_font)
        end_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        str_label.grid(column=0, row=1)
        str_box.grid(column=1, row=1)
        dex_label.grid(column=0, row=2)
        dex_box.grid(column=1, row=2)
        agi_label.grid(column=0, row=3)
        agi_box.grid(column=1, row=3)
        will_label.grid(column=0, row=4)
        will_box.grid(column=1, row=4)
        end_label.grid(column=0, row=5)
        end_box.grid(column=1, row=5)
        # TODO: find a way to attach identifiers to these things, maybe parallel arrays?
        # Actually now that I think about it, it's a lot better to make a giant dict of strings to widgets
        # That'll streamline the cur_dict refresh to a simple sweep of the global dict
        config.all_widgets.extend([name_entry, dex_box, agi_box, will_box, end_box])
        # save
        save_button = Button(self, text="Save", font=attrib_font, command=lambda: save())
        save_button.grid(column=1, row=6)


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()

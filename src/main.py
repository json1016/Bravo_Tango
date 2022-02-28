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
        config.all_widgets["name"] = name_entry
        # attributes
        str_label = Label(self, text="Strength:", font=attrib_font)
        str_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        config.all_widgets["strength"] = str_box
        dex_label = Label(self, text="Dexterity:", font=attrib_font)
        dex_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        config.all_widgets["dexterity"] = dex_box
        agi_label = Label(self, text="Agility:", font=attrib_font)
        agi_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        config.all_widgets["agility"] = agi_box
        will_label = Label(self, text="Willpower:", font=attrib_font)
        will_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        config.all_widgets["willpower"] = will_box
        end_label = Label(self, text="Endurance:", font=attrib_font)
        end_box = Spinbox(self, from_=0, to=10, font=attrib_font)
        config.all_widgets["endurance"] = end_box
        # save
        save_button = Button(self, text="Save", font=attrib_font, command=lambda: save())
        # grid all widgets
        name_label.grid(column=0, row=0)
        name_entry.grid(column=1, row=0)
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
        save_button.grid(column=1, row=6)


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()

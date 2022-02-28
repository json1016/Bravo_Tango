import json
from tkinter import *
from tkinter import filedialog as fd

import config


def open_file():
    with fd.askopenfile(filetypes=((".json", "*.json"),)) as f:
        config.cur_dict = json.load(f)
        for k in config.all_widgets.keys():
            v = config.all_widgets[k]
            v.delete(0, END)
            v.insert(0, config.cur_dict[k])


def refresh():
    for k in config.all_widgets.keys():
        v = config.all_widgets[k].get()
        config.cur_dict[k] = v


def save():
    refresh()
    with fd.asksaveasfile(defaultextension=".json", filetypes=((".json", "*.json"),)) as f:
        json.dump(config.cur_dict, f)
        f.close()

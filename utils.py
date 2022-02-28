import json
from tkinter import filedialog as fd

import config


def open_file():
    with fd.askopenfile() as f:
        config.cur_dict = json.load(f)
        refresh()


def refresh():
    for w in config.all_widgets:
        print(w.get())


def save():
    refresh()
    with fd.asksaveasfile() as f:
        json.dump(config.cur_dict, f)
        f.close()

import tkinter as tk
from typing import cast, Dict

from services.tkinter_ui.menu import assemble_menu
from services.tkinter_ui.settings import assemble_settings

def frame_select(
    var: tk.StringVar,
    frames: Dict[str, tk.Frame]
):
    value = var.get()
    to_pos = (-10e2, -10e2)

    for name, frame in frames.items():
        if value == name:
            frame.place(x=0, y=0)
        else:
            frame.place(
                x=to_pos[0],
                y=to_pos[1]
            )


def make_frame_selectors(
        master: tk.Frame,
        frame_var: tk.StringVar,
        frames: Dict[str, tk.Frame]
):
    tk.Radiobutton(
        master=master,
        variable=frame_var,
        value="menu",
        text="Select menu",
        command=lambda: frame_select(frame_var, frames)
    ).pack()

    tk.Radiobutton(
        master=master,
        variable=frame_var,
        value="settings",
        text="Select settings",
        command=lambda: frame_select(frame_var, frames)
    ).pack()


def run(
    app: tk.Tk,
    whisper_module,
    llm_module
):
    frame_var = tk.StringVar(value="menu")

    menu = assemble_menu(
        master=cast(tk.Frame, app),
        whisper_module=whisper_module,
        llm_module=llm_module
    )
    settings = assemble_settings(master=cast(tk.Frame, app))

    frames = {
        "menu": menu,
        "settings": settings
    }
    frame_select(frame_var, frames)
    make_frame_selectors(cast(tk.Frame, app), frame_var, frames)

    app.mainloop()
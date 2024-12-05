import tkinter as tk

def assemble_settings(master: tk.Frame) -> tk.Frame:
    settings = tk.Frame(
        master=master,
        width=500,
        height=500
    )

    title = tk.Label(
        master=settings,
        text="This is the page for Settings",
        font="Arial 10"
    )

    settings.pack()
    title.pack()

    return settings

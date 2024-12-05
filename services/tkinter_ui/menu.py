import tkinter as tk

def assemble_menu(
        master: tk.Frame,
        whisper_module,
        llm_module,
) -> tk.Frame:
    menu = tk.Frame(
        master=master,
        width=500,
        height=500
    )

    title = tk.Label(
        master=menu,
        text="Main menu for the program",
        font="Arial 10",
    )

    title.pack()
    menu.pack()

    return menu
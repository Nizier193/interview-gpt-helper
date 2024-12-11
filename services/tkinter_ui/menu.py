import tkinter as tk

from services.whisper_code.main import WhisperTranscriber

def fill_vars(
        text: str,
        text_var: tk.StringVar, 
        all_text_var: tk.StringVar, 
        text_field: tk.Text
    ):
    text_var.set(text)
    all_text_var.set(all_text_var.get().strip() + " " + text_var.get())
    
    text_field.replace("0.0", tk.END, all_text_var.get())

def assemble_menu(master: tk.Frame) -> tk.Frame:
    text_var = tk.StringVar(value="")
    all_text_var = tk.StringVar(value="")

    whisper_transcriber = WhisperTranscriber(
        var_updater=lambda text: fill_vars(
            text=text,
            text_var=text_var,
            all_text_var=all_text_var,
            text_field=text_field
        )
    )

    start_recording_button = tk.Button(master=master, text="Start rec", command=whisper_transcriber.start)
    start_recording_button.pack()

    stop_recording_button = tk.Button(master=master, text="Stop rec", command=whisper_transcriber.stop)
    stop_recording_button.pack()

    text_label = tk.Label(
        master=master, 
        textvariable=text_var,
        wraplength=550,
        justify=tk.LEFT
    )
    text_label.pack()

    all_text_label = tk.Label(
        master=master, 
        textvariable=all_text_var,
        wraplength=550,
        justify=tk.LEFT
    )
    all_text_label.pack()

    text_field = tk.Text(
        width=100,
        height=10
    )
    text_field.pack()

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
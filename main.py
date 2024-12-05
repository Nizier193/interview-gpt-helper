import tkinter as tk

from services.llms.main import LLMModule
from services.whisper.main import WhisperModule
from services.tkinter_ui.base import run
# Based on tkinter
# Uses whisper to transcribe in stream mode
# Can work with multiple gpts
# Can generate graphs and other stuff

# Probably can be made into something better

# Scheme
# (Whisper Module)  (LLM Module)  (Tkinter Module)
#  Transcription > Help / Search >  Visualization

def main():
    # There is the mainloop for gpt-helper project
    app = tk.Tk()
    app.geometry("500x500")
    app.title("interview-gpt-helper")

    llm_module = LLMModule()
    whisper_module = WhisperModule()

    run(
        app=app,
        whisper_module=whisper_module,
        llm_module=llm_module
    )

if __name__ == "__main__":
    main()
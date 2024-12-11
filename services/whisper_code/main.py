from typing import Callable
import sounddevice as sd
import numpy as np
import whisper
import queue
import threading

from tkinter import StringVar

class WhisperTranscriber:
    def __init__(self, var_updater: Callable):
        self.model = whisper.load_model("small")
        self.audio_queue = queue.Queue()
        self.text_buffer = []

        self.var_updater = var_updater
        self.is_running = False
        self.sample_rate = 16000
        self.block_duration = 4
        
    def audio_callback(self, indata, frames, time, status):
        """Callback для захвата аудио"""
        self.audio_queue.put(indata.copy())
        
    def process_audio(self):
        """Обработка аудио и распознавание речи"""
        while True:
            audio_data = self.audio_queue.get()
            # Преобразование аудио в формат для Whisper
            audio_np = audio_data.flatten().astype(np.float32)
            
            # Распознавание речи
            result = self.model.transcribe(audio_np, language="ru")
            
            if result["text"].strip():
                self.var_updater(result["text"])
                self.text_buffer.append(result["text"])
                print(f"Распознано: {result['text']}")

            if self.is_running == False:
                break

        print("Ended processing.")

    def run_input(self):
        stream_device = sd.InputStream(
                callback=self.audio_callback,
                channels=1,
                samplerate=self.sample_rate,
                blocksize=int(self.sample_rate * self.block_duration)
            )
        stream_device.start()
        while True:
            sd.sleep(100)
            if self.is_running == False:
                break
        stream_device.close()

        print("Ended stream device.")

    def start(self):
        self.is_running = True

        processing_thread = threading.Thread(target=self.process_audio)
        processing_thread.start()

        input_thread = threading.Thread(target=self.run_input)
        input_thread.start()

        print("Started process and input.")
        
    def stop(self):
        """Остановка распознавания"""
        self.is_running = False
        print("\nЗапись остановлена")
        
    def get_transcription(self):
        """Получение всего распознанного текста"""
        return " ".join(self.text_buffer)

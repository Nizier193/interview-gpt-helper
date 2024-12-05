from random import sample
from string import ascii_letters

class WhisperModule():
    def get_transcription(self):
        return "".join(sample(ascii_letters, 20))

# currently implementing microphone streaming
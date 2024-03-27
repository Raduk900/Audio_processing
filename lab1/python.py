from tkinter import filedialog
from tkinter import Tk
from pydub import AudioSegment
import IPython.display as ipd
import tempfile
import os

def import_audio():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])

    if file_path:
        audio = AudioSegment.from_wav(file_path)
        return audio
    else:
        return None

audio = import_audio()
print(audio)

temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
audio.export(temp_file.name, format="wav")
temp_file.close()

ipd.Audio(temp_file.name)
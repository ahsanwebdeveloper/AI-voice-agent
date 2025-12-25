import av
import numpy as np
import tempfile
from scipy.io.wavfile import write

def save_audio_from_frames(frames, sample_rate=16000):
    pcm = []

    for frame in frames:
        if isinstance(frame, av.AudioFrame):   # 👈 now av is used
            pcm.append(frame.to_ndarray())

    audio = np.concatenate(pcm).astype(np.int16)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(tmp.name, sample_rate, audio)

    return tmp.name

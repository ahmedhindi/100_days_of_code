import sounddevice as sd
from scipy.io import wavfile
import numpy as np
from typing import List, Tuple
import sys


def clean_data(data):
    if data.shape[1] > 1:
        data = data[:, 0]
    return data[data > 0]


def calc_time(data: np.array, samplerate: int) -> int:
    """returns time of the audio file in seconds"""
    return len(data) // samplerate


def read_wav(file: str) -> Tuple[int, np.array]:
    "returns samplerate, data"
    return wavfile.read(file)


def create_wav_with_time(data: np.array, sample_time: float, play_time: int) -> np.array:
    multiples = (play_time) // sample_time
    return np.concatenate([data] * multiples)


def play(data: np.array, samplerate: int) -> None:
    sd.play(data, samplerate=samplerate, mapping=None, blocking=True)


def main():
    time = 2
    samplerate, data = read_wav("brown.wav")
    data = clean_data(data)
    sample_time = calc_time(data, samplerate)
    data = create_wav_with_time(data, sample_time, play_time=time)
    play(data, samplerate)
    sys.exit()


main()


# add tests
# add other noises https://www.zapsplat.com/sound-effect-category/ocean/
# use fire
# sum noises to see if works and normalize

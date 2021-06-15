import sounddevice as sd
from scipy.io import wavfile
import numpy as np
from typing import List, Tuple
import sys
import os
import time


def clean_data(data: np.array) -> np.array:
    if len(data.shape) > 1:
        data = data[:, 0]
    return np.trim_zeros(data)


def calc_time(data: np.array, samplerate: int) -> int:
    """returns time of the audio file in seconds"""
    return int(len(data) / samplerate)


def read_wav(file: str) -> Tuple[int, np.array]:
    "returns samplerate, data"
    return wavfile.read(file)


def create_wav_with_time(data: np.array, sample_time: float, play_time: int) -> np.array:
    multiples = int(play_time * 60 / sample_time)
    return np.concatenate([data] * multiples)


def play(data: np.array, samplerate: int) -> None:
    """plays a numpy array"""
    sd.play(data, samplerate=samplerate, mapping=None, blocking=True)


def list_available(dir: str):
    res = [">>> " + i.split(".")[0] for i in os.listdir(dir)]
    for i in res:
        print(i)


def main(total_time: int = 1, sound: str = "brown", sounds_dir: str = "sounds"):
    os.chdir(sound)
    samplerate, data = read_wav(f"{sound}.wav")
    data = clean_data(data)
    sample_time = calc_time(data, samplerate)
    data = create_wav_with_time(data, sample_time, play_time=total_time)
    play(data, samplerate)
    sys.exit()


if __name__ == "__main__":
    main()


# add tests
# add other noises https://www.zapsplat.com/sound-effect-category/ocean/
# use fire
# sum noises to see if works and normalize

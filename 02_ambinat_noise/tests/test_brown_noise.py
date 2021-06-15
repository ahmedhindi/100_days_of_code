import pytest
from tests.fixtures import *
from noise.brown_noise import *


def test_clean_data(dirty_data: np.array) -> np.array:
    res = clean_data(dirty_data)
    assert len(res) < len(dirty_data)
    assert (res[0] != 0) and res[-1] != 0


def test_calc_time(data_and_rate):
    data, rate = data_and_rate
    assert calc_time(data, rate) == 60


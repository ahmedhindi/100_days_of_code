import numpy as np
import pytest


@pytest.fixture
def dirty_data()-> np.array:
    return np.array([0,0,0,0,5,6,5,4,7,0,8,-1,6,3,2,8,0,0,0,0])
    



@pytest.fixture
def data_and_rate() :
    data  = np.random.uniform(-3,-3,60000)
    return data, 1000



import numpy as np
import pytest

from src import game_core_v3


@pytest.mark.parametrize("input", np.random.randint(1, 101, size=(1000)))
def test_game_core_v3(input):
    assert game_core_v3(input) < 20

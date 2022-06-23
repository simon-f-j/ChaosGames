import pytest
from chaos_game import ChaosGame


def test_ngon_number_of_corners():
    a = ChaosGame(3)
    b = ChaosGame(4)
    c = ChaosGame(99)
    assert len(a._generate_ngon()) == 3
    assert len(b._generate_ngon()) == 4
    assert len(c._generate_ngon()) == 99


def test_if_n_not_int():
    with pytest.raises(Exception):
        a = ChaosGame(3.0)


def test_if_r_not_float():
    with pytest.raises(Exception):
        a = ChaosGame(3, "a")


def test_n_in_valid_range():
    with pytest.raises(Exception):
        a = ChaosGame(2)
        b = ChaosGame(0)


def test_r_in_valid_range():
    with pytest.raises(Exception):
        a = ChaosGame(3, 1.1)
        b = ChaosGame(3, 0.0)

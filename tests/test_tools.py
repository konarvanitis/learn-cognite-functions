from math import log

from pytest import approx

from tools import thermal_resistance


def test_thermal_resistance():
    row = {"T_hot_IN": 100, "T_hot_OUT": 60, "T_cold_IN": 20, "T_cold_OUT": 50, "Flow_hot": 2}
    # dT1=50, dT2=40; F=0.8, A=1.0, Cp_hot=2.4
    expected = 0.8 * (50 - 40) / log(50 / 40) / (2 * 2.4 * (100 - 60))
    assert thermal_resistance(row) == approx(expected)

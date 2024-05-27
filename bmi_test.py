import pytest
from bmi import vypocitej_bmi

def test_bmi_normal():
    assert pytest.approx(vypocitej_bmi(70, 1.75), 0.01) == 22.86

def test_bmi_underweight():
    assert pytest.approx(vypocitej_bmi(50, 1.75), 0.01) == 16.33

def test_bmi_overweight():
    assert pytest.approx(vypocitej_bmi(90, 1.75), 0.01) == 29.39

def test_bmi_obese():
    assert pytest.approx(vypocitej_bmi(110, 1.75), 0.01) == 35.92

def test_zero_height():
    with pytest.raises(ValueError):
        vypocitej_bmi(70, 0)

def test_negative_height():
    with pytest.raises(ValueError):
        vypocitej_bmi(70, -1.75)
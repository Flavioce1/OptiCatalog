import pytest

from parse import Correction, EyeCorrection, parse_correction


def test_format_standard_avec_parentheses_et_slash():
    resultat = parse_correction(
        "OD -2.50 (-0.75) 90° Add 1.50 / OG -2.25 (-0.50) 85° Add 1.50"
    )
    assert resultat == Correction(
        od=EyeCorrection(sphere=-2.50, cylinder=-0.75, axis=90, addition=1.50),
        og=EyeCorrection(sphere=-2.25, cylinder=-0.50, axis=85, addition=1.50),
    )


def test_minuscules_et_virgule_decimale():
    resultat = parse_correction(
        "od -3,00 -1,25 180 add 2,00 og -2,75 -1,00 175 add 2,00"
    )
    assert resultat == Correction(
        od=EyeCorrection(sphere=-3.00, cylinder=-1.25, axis=180, addition=2.00),
        og=EyeCorrection(sphere=-2.75, cylinder=-1.00, axis=175, addition=2.00),
    )


def test_signe_positif_et_separateur_point_virgule():
    resultat = parse_correction(
        "OD: +1.25 (+0.50) 100 ADD +2.50 ; OG: +1.00 (+0.75) 95 ADD +2.50"
    )
    assert resultat == Correction(
        od=EyeCorrection(sphere=1.25, cylinder=0.50, axis=100, addition=2.50),
        og=EyeCorrection(sphere=1.00, cylinder=0.75, axis=95, addition=2.50),
    )


@pytest.mark.xfail(
    reason="Correction sans cylindre ni addition : edge case 'OG'/valeurs manquantes traité dans une prochaine PR",
    raises=IndexError,
    strict=True,
)
def test_correction_sans_cylindre_ni_addition():
    parse_correction("OD -1.50 OG -1.75")

import re
from typing import NamedTuple

import typer


class EyeCorrection(NamedTuple):
    """Correction d'un œil : sphère, cylindre, axe (degrés), addition."""

    sphere: float
    cylinder: float
    axis: int
    addition: float


class Correction(NamedTuple):
    """Correction complète : œil droit (OD) et œil gauche (OG)."""

    od: EyeCorrection
    og: EyeCorrection


NOMBRE = r"[+-]?\d+(?:[.,]\d+)?"


def normaliser(texte: str) -> str:
    """Uniformise la casse, le séparateur décimal et les espaces."""
    texte = texte.upper()
    texte = texte.replace(",", ".")
    texte = " ".join(texte.split())
    return texte


def _parse_oeil(valeurs: list[str]) -> EyeCorrection:
    """Construit une EyeCorrection à partir des 4 nombres extraits, dans l'ordre."""
    return EyeCorrection(
        sphere=float(valeurs[0]),
        cylinder=float(valeurs[1]),
        axis=int(valeurs[2]),
        addition=float(valeurs[3]),
    )


def parse_correction(texte: str) -> Correction:
    """Transforme une correction en texte libre en valeurs structurées.

    Gère le format standard où les 4 valeurs (sphère, cylindre, axe, addition)
    sont présentes pour chaque œil. Le cas des valeurs manquantes (ex. correction
    sans cylindre ni addition) est traité séparément.
    """
    t = normaliser(texte)
    partie_od, partie_og = t.split("OG")
    od = re.findall(NOMBRE, partie_od)
    og = re.findall(NOMBRE, partie_og)
    return Correction(od=_parse_oeil(od), og=_parse_oeil(og))


def main(
    correction: str = typer.Argument(
        ...,
        help='Correction à parser, ex : "OD -2.50 (-0.75) 90 Add 1.50 / OG -2.25 (-0.50) 85 Add 1.50"',
    ),
) -> None:
    """Parse une correction optique en texte libre vers des valeurs structurées."""
    typer.echo(parse_correction(correction))


if __name__ == "__main__":
    typer.run(main)

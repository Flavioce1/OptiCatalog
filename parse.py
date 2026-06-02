import re

# Exemples de corrections 
EXEMPLES = [
    "OD -2.50 (-0.75) 90° Add 1.50 / OG -2.25 (-0.50) 85° Add 1.50",
    "od -3,00 -1,25 180 add 2,00 og -2,75 -1,00 175 add 2,00",
    "OD -1.50 OG -1.75",
    "OD: +1.25 (+0.50) 100 ADD +2.50 ; OG: +1.00 (+0.75) 95 ADD +2.50",
]

NOMBRE = r"[+-]?\d+(?:[.,]\d+)?" 

def normaliser(texte: str) -> str:
    texte = texte.upper()
    texte = texte.replace(",", ".")
    texte = " ".join(texte.split())
    return texte

def parse_correction(texte: str) -> dict:
    t = normaliser(texte)
    partie_od, partie_og = t.split("OG")
    od = re.findall(NOMBRE, partie_od)
    og = re.findall(NOMBRE, partie_og)
    return {
        "od_sphere": float(od[0]), "od_cylinder": float(od[1]),
        "od_axis": int(od[2]), "od_addition": float(od[3]),
        "og_sphere": float(og[0]), "og_cylinder": float(og[1]),
        "og_axis": int(og[2]), "og_addition": float(og[3]),
    }

for i, ex in enumerate(EXEMPLES, start=1):
    try:
        print(f"Exemple {i} :", parse_correction(ex))
    except Exception as e:
        print(f"Exemple {i} : ECHEC -> {type(e).__name__}: {e}")
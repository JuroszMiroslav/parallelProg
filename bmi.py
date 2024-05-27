def vypocitej_bmi(vaha, vyska):
    """
    Vypočítá BMI na základě váhy (kg) a výšky (m).

    Args:
        vaha (float): Váha v kilogramech.
        vyska (float): Výška v metrech.

    Returns:
        float: BMI hodnota.
    """
    if vyska <= 0:
        raise ValueError("Výška musí být větší než nula")
    return vaha / (vyska ** 2)
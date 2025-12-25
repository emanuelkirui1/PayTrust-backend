def kra_paye(gross):
    bands = [
        (24000, 0.10),
        (32333, 0.25),
        (500000, 0.30),
    ]
    tax = 0
    for band, rate in bands:
        if gross > band:
            tax += band * rate
        else:
            tax += gross * rate
            break
    return round(tax, 2)


def ura_paye(gross):
    # Uganda PAYE
    if gross <= 235000:
        return 0
    elif gross <= 335000:
        return (gross - 235000) * 0.10
    elif gross <= 410000:
        return (100000 * 0.10) + ((gross - 335000) * 0.20)
    else:
        return (100000 * 0.10) + (75000 * 0.20) + ((gross - 410000) * 0.30)

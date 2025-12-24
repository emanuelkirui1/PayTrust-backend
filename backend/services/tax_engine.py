def kra_paye(gross):
    bands = [
        (24000, 0.10),
        (32333, 0.25),
        (float("inf"), 0.30)
    ]

    tax = 0
    remaining = gross
    lower = 0

    for limit, rate in bands:
        taxable = min(remaining, limit - lower)
        tax += taxable * rate
        remaining -= taxable
        lower = limit
        if remaining <= 0:
            break

    relief = 2400
    return max(tax - relief, 0)


def ura_paye(gross):
    bands = [
        (235000, 0.10),
        (335000, 0.20),
        (410000, 0.30),
        (10000000, 0.40)
    ]

    tax = 0
    remaining = gross
    lower = 0

    for limit, rate in bands:
        taxable = min(remaining, limit - lower)
        tax += taxable * rate
        remaining -= taxable
        lower = limit
        if remaining <= 0:
            break

    return tax


def calculate_paye(gross, country="KE"):
    if country == "KE":
        return kra_paye(gross)
    elif country == "UG":
        return ura_paye(gross)
    else:
        return 0

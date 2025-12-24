def kenya_nssf(gross):
    # Employee contribution capped
    return min(gross * 0.06, 2160)


def kenya_nhif(gross):
    bands = [
        (5999, 150),
        (7999, 300),
        (11999, 400),
        (14999, 500),
        (19999, 600),
        (24999, 750),
        (29999, 850),
        (34999, 900),
        (39999, 950),
        (44999, 1000),
        (49999, 1100),
        (59999, 1200),
        (69999, 1300),
        (79999, 1400),
        (89999, 1500),
        (99999, 1600),
        (float("inf"), 1700)
    ]

    for limit, amount in bands:
        if gross <= limit:
            return amount
    return 0


def uganda_nssf(gross):
    return gross * 0.05


def calculate_statutory(gross, country="KE"):
    if country == "KE":
        return {
            "nssf": kenya_nssf(gross),
            "nhif": kenya_nhif(gross)
        }
    elif country == "UG":
        return {
            "nssf": uganda_nssf(gross),
            "nhif": 0
        }
    return {"nssf": 0, "nhif": 0}

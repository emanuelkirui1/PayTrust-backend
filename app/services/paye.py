def calculate_paye(country, salary):
    kra = [(24000,0.1),(32333,0.25),(500000,0.30)]
    ura = [(235000,0.1),(335000,0.2),(410000,0.3)]

    bands = kra if country.lower()=="kenya" else ura
    tax = 0
    for limit, rate in bands:
        if salary > limit: tax += (salary-limit)*rate
    return max(tax,0)

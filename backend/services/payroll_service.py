PERSONAL_RELIEF = 2400

def calculate_paye(salary):
    tax = 0

    if salary <= 24000:
        tax = salary * 0.10
    elif salary <= 32333:
        tax = (24000 * 0.10) + ((salary - 24000) * 0.25)
    else:
        tax = (24000 * 0.10) + ((32333 - 24000) * 0.25) + ((salary - 32333) * 0.30)

    return max(tax - PERSONAL_RELIEF, 0)

def calculate_nssf(salary):
    return min(salary * 0.06, 1080)

def calculate_nhif(salary):
    if salary <= 5999:
        return 150
    elif salary <= 7999:
        return 300
    elif salary <= 11999:
        return 400
    return 1700

def calculate_ura(salary):
    # Optional statutory levy (example)
    return salary * 0.015

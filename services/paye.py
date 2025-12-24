def kra_paye(salary):
    if salary <= 24000:
        tax = salary * 0.1
    elif salary <= 32333:
        tax = 2400 + (salary - 24000) * 0.25
    else:
        tax = 2400 + 2083.25 + (salary - 32333) * 0.30
    return max(tax - 2400, 0)

def ura_paye(salary):
    if salary <= 235000:
        return 0
    elif salary <= 335000:
        return (salary - 235000) * 0.10
    elif salary <= 410000:
        return 10000 + (salary - 335000) * 0.20
    else:
        return 25000 + (salary - 410000) * 0.30

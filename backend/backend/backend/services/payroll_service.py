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

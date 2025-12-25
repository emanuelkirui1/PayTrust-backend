def calculate_payroll(basic, allowances=0, deductions=0):
    gross = basic + allowances
    paye = gross * 0.05
    nhif = 500
    nssf = 200
    net = gross - (paye + nhif + nssf + deductions)
    return {"gross":gross,"paye":paye,"nhif":nhif,"nssf":nssf,"net":net}

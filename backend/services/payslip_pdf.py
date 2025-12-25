from reportlab.pdfgen import canvas

def generate_payslip(filename, employee, payroll):
    c = canvas.Canvas(filename)
    c.drawString(100, 800, f"Payslip for: {employee}")
    c.drawString(100, 780, f"Gross Salary: {payroll['gross']}")
    c.drawString(100, 760, f"Net Salary: {payroll['net']}")
    c.save()
    return filename

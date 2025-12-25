from reportlab.pdfgen import canvas

def generate_payslip(employee, salary, tax):
    file = f"{employee}_payslip.pdf"
    c = canvas.Canvas(file)
    c.drawString(100,800,f"Payslip for {employee}")
    c.drawString(100,780,f"Salary: {salary}")
    c.drawString(100,760,f"TAX (PAYE): {tax}")
    c.save()
    return file

from reportlab.pdfgen import canvas

def generate_payslip(filename, employee, netpay):
    c = canvas.Canvas(filename)
    c.drawString(100, 800, f"Payslip for {employee}")
    c.drawString(100, 780, f"Net Pay: {netpay}")
    c.save()
    return filename

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def generate_payslip(employee, payroll):
    path = f"/tmp/payslip_{employee.id}.pdf"
    c = canvas.Canvas(path, pagesize=A4)

    c.drawString(50, 800, "PayTrust Payslip")
    c.drawString(50, 770, f"Name: {employee.name}")
    c.drawString(50, 750, f"Email: {employee.email}")
    c.drawString(50, 720, f"Gross: {payroll['gross']}")
    c.drawString(50, 700, f"PAYE: {payroll['paye']}")
    c.drawString(50, 680, f"Net Pay: {payroll['net']}")
c.drawString(50, 660, f"NSSF: {payroll.get(nssf, 0)}")
c.drawString(50, 640, f"NHIF: {payroll.get(nhif, 0)}")
c.drawString(50, 660, f"NSSF: {payroll.get(nssf, 0)}")
c.drawString(50, 640, f"NHIF: {payroll.get(nhif, 0)}")
c.drawString(50, 640, f"NHIF: {payroll.get(nhif, 0)}")

    c.save()
    return path

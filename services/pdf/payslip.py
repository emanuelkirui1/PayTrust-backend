from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

def generate_payslip(employee, payroll):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    pdf.drawString(50, 800, "PayTrust Payslip")
    pdf.drawString(50, 770, f"Employee: {employee.first_name} {employee.last_name}")
    pdf.drawString(50, 740, f"Gross Salary: {payroll['gross']}")
    pdf.drawString(50, 710, f"KRA PAYE: {payroll['kra_paye']}")
    pdf.drawString(50, 680, f"URA PAYE: {payroll['ura_paye']}")
    pdf.drawString(50, 650, f"Net Pay: {payroll['net']}")

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer

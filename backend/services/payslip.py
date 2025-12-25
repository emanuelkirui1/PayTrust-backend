from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import smtplib, ssl

def generate_payslip(name, gross, net, filename="payslip.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.drawString(100, 800, f"PAYTRUST PAYSLIP")
    c.drawString(100, 780, f"Employee: {name}")
    c.drawString(100, 760, f"Gross Salary: {gross}")
    c.drawString(100, 740, f"Net Salary: {net}")
    c.save()
    return filename


def email_payslip(to_email, pdf_path):
    smtp_server = "smtp.gmail.com"
    port = 465
    sender = "yourcompany@example.com"
    password = "APP_PASSWORD_HERE"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, to_email, f"Payslip attached", pdf_path)

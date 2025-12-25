from flask_mail import Mail, Message

mail = Mail()

def init_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = "yourcompany@gmail.com"
    app.config['MAIL_PASSWORD'] = "your-app-password"
    mail.init_app(app)

def send_payslip(email, pdf_path):
    from flask import current_app
    with current_app.app_context():
        msg = Message("Payslip", sender=current_app.config['MAIL_USERNAME'], recipients=[email])
        msg.body = "Attached is your monthly payslip."
        with open(pdf_path, "rb") as f:
            msg.attach("payslip.pdf", "application/pdf", f.read())
        mail.send(msg)

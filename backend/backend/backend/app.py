from flask import Flask
from routes.payroll import payroll_bp

app = Flask(__name__)

app.register_blueprint(payroll_bp, url_prefix="/api/payroll")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

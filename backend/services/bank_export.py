import csv
import os

def generate_bank_csv(employees):
    path = "/tmp/bank_export.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Employee", "Amount"])

        for e in employees:
            writer.writerow([e["employee"], e["net"]])

    return path

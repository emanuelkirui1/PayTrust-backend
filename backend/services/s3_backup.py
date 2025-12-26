import boto3, os

def upload_payslip_to_s3(file_path, file_name):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    bucket = os.getenv("S3_BUCKET")
    s3.upload_file(file_path, bucket, f"payslips/{file_name}")
    return f"https://{bucket}.s3.amazonaws.com/payslips/{file_name}"

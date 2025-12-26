import boto3, os

def upload_payslip_to_s3(file_path, file_name):
    bucket = os.getenv("S3_BUCKET")
    if not bucket:
        return "Missing S3_BUCKET env variable"

    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    s3.upload_file(file_path, bucket, f"payslips/{file_name}")
    return f"s3://{bucket}/payslips/{file_name}"

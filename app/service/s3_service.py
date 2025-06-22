import os

import boto3

bucket_name = os.getenv('BUCKET_NAME', "bridee-user-bucket")

def upload_image(file_path, destination_name):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket_name, destination_name)
    print("Upload realizado com sucesso")
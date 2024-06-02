# src/cosmic_pi_network/cloud/cloud_storage.py
import boto3

class CloudStorage:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_path, key):
        self.s3.upload_file(file_path, self.bucket_name, key)

    def download_file(self, key, file_path):
        self.s3.download_file(self.bucket_name, key, file_path)

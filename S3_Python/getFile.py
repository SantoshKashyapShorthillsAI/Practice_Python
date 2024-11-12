import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_file_url(bucket_name, object_name):
    """
    Returns the URL of an object in S3.
    """
    return f"https://{bucket_name}.s3.amazonaws.com/{object_name}"

bucket_name = 'pythontranning2024'
object_name = 'S3_Python/document.txt'
print(get_file_url(bucket_name, object_name))
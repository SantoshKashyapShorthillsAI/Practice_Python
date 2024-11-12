
import boto3
from botocore.exceptions import NoCredentialsError

def generate_presigned_url(bucket_name, object_name, expiration=3600):
    """
    Generates a presigned URL to access an S3 object.
    
    :param bucket_name: Name of the S3 bucket.
    :param object_name: S3 object name.
    :param expiration: Time in seconds for the presigned URL to remain valid (default is 1 hour).
    :return: Presigned URL as a string.
    """
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
        return response
    except NoCredentialsError:
        print("Credentials not available.")
        return None

url = generate_presigned_url('pythontranning2024', 'S3_Python/document.txt')
print("Presigned URL:", url)

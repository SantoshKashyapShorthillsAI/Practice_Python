import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_to_s3(file_name, bucket_name, object_name=None, public=False):
    """
    Uploads a file to an S3 bucket and optionally makes it publicly accessible.

    :param file_name: Path to the file to upload
    :param bucket_name: Name of the S3 bucket
    :param object_name: S3 object name. If not specified, file_name is used
    :param public: If True, sets the uploaded file to be publicly accessible
    :return: True if file was uploaded, else False
    """
    # If S3 object_name is not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Initialize S3 client
    s3_client = boto3.client('s3')
    # Set extra arguments if public access is required
    # extra_args = {'ACL': 'public-read'} if public else None

    try:
        # Upload the file
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded to '{bucket_name}/{object_name}' successfully.")
        if public:
            print(f"The file '{object_name}' is now publicly accessible.")
        return True
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
        return False

upload_to_s3('S3_Python/document.txt', 'pythontranning2024', public=True)


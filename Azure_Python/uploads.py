from azure.storage.blob import BlobClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def upload_file_to_blob(file_path):
    """
    Uploads a file to Azure Blob Storage using the SAS URL from the .env file.

    Args:
    file_path (str): Path to the local file to upload.
    """
    try:
        # Get the SAS URL from environment variables
        sas_url = os.getenv("AZURE_BLOB_SAS_URL")
        
        if not sas_url:
            raise ValueError("SAS URL not found. Check .env file.")
        
        # Initialize BlobClient with the SAS URL
        blob_client = BlobClient.from_blob_url(sas_url)
        
        # Upload the file
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        print(f"File '{file_path}' uploaded successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Usage
file_path = "Azure_Python/document.txt"
upload_file_to_blob(file_path)

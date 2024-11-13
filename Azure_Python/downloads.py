from azure.storage.blob import BlobClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def download_file_from_blob(download_path):
    """
    Downloads a file from Azure Blob Storage using the SAS URL from the .env file.

    Args:
    download_path (str): Path where the file will be saved locally.
    """
    try:
        # Get the SAS URL from environment variables
        sas_url = os.getenv("AZURE_BLOB_SAS_URL")
        
        if not sas_url:
            raise ValueError("SAS URL not found. Check .env file.")
        
        # Initialize BlobClient with the SAS URL
        blob_client = BlobClient.from_blob_url(sas_url)
        
        # Download the file
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        
        print(f"File downloaded successfully to '{download_path}'.")
    except Exception as e:
        print(f"Error downloading file: {e}")

download_path = "Azure_Python/downloaded_document.txt"
download_file_from_blob(download_path)

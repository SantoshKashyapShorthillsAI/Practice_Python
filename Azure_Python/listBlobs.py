import os
from azure.storage.blob import ContainerClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
container_sas_url = os.getenv("AZURE_SAS_URL")

if not container_sas_url:
    raise ValueError("AZURE_BLOB_SAS_URL is not defined in the .env file")

# Initialize ContainerClient using the container SAS URL
container_client = ContainerClient.from_container_url(container_sas_url)

def list_blobs_in_container():
    """
    List all blobs in the specified Azure Blob Storage container.
    """
    try:
        print("Blobs in container:")
        blobs_list = container_client.list_blobs()
        for blob in blobs_list:
            print(blob.name)
    except Exception as e:
        print(f"Error listing blobs: {e}")

# Call the function
list_blobs_in_container()

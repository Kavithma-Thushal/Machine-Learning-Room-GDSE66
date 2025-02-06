import os
import boto3

# Provide AWS Credentials
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = r'D:\IJSE\Workspace\4th Sem Repo\ML\AWS\Boto3\credentials'
s3 = boto3.resource('s3')

# Define the S3 bucket name
BUCKET_NAME = "gdse66-s3-bucket"

# Define the downloaded file name
s3_key = "wallpaper_uploaded.jpg"

# Define the local path for downloaded file
file_path = "wallpaper_downloaded.jpg"

# Download the file from the S3 bucket
s3.Bucket(BUCKET_NAME).download_file(s3_key, file_path)

# Print a success message
print("Image downloaded successfully!")

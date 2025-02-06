import os
import boto3

# Provide AWS Credentials
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = r'D:\IJSE\Workspace\4th Sem Repo\ML\AWS\Boto3\credentials'
s3 = boto3.resource('s3')

BUCKET_NAME = 'gdse66-s3-bucket'
folder_path = 'uploads/'
s3_folder = 'uploads/'

# Iterate over the files in the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        local_path = os.path.join(root, file)

        # Create the relative path for the S3 key
        s3_key = os.path.join(s3_folder, os.path.relpath(local_path, folder_path))

        # Read the file and upload to S3
        with open(local_path, 'rb') as f:
            s3.Bucket(BUCKET_NAME).put_object(Key=s3_key, Body=f)

        print(f"Image uploaded successfully! - {s3_key}")

print("Folder completely uploaded to bucket successfully!")

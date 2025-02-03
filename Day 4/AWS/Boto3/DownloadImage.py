import boto3

# Define the S3 bucket name
BUCKET_NAME = "gdse66-s3-bucket"

# Define the downloaded file name
s3_key = "Wallpaper.jpg"

# Define the local path for downloaded file
file_path = "Wallpaper-Downloaded.jpg"

# Download the file from the S3 bucket
s3.Bucket(BUCKET_NAME).download_file(s3_key, file_path)

# Print a success message
print("Image downloaded successfully!")

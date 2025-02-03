import boto3

# Define the S3 bucket name
BUCKET_NAME = "gdse66-s3-bucket"

# Define the local path of the file
file_path = "Wallpaper.jpg"

# Define the uploaded file name
s3_key = "Wallpaper-Uploaded.jpg"

# Upload the file to the S3 bucket
with open(file_path, 'rb') as file:
    s3.Bucket(BUCKET_NAME).put_object(Key=s3_key, Body=file)

# Print a success message
print("Image uploaded successfully!")

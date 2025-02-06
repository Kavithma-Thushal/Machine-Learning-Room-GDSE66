import os
import boto3

# Provide AWS Credentials
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = r'D:\IJSE\Workspace\4th Sem Repo\ML\AWS\Boto3\credentials'
s3 = boto3.resource('s3')

# Print the bucket name
for bucket in s3.buckets.all():
    print(bucket.name)

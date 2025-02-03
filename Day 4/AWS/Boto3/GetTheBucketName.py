import boto3

# Print the bucket name
for bucket in s3.buckets.all():
    print(bucket.name)

import boto3

# create an S3 client
s3 = boto3.client('s3')

# list all buckets
response = s3.list_buckets()

# print the name of each bucket
for bucket in response['Buckets']:
    print(bucket['Name'])

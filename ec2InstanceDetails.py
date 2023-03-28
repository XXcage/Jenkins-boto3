import boto3
import os

# Get the AWS access key ID and secret access key from environment variables.
access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Connect to AWS using the access key ID and secret access key.
ec2 = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Get a list of all EC2 instances.
instances = ec2.describe_instances()

# Loop over the instances and check if they are in a stopped state.
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'stopped':
            print(f"Instance ID: {instance['InstanceId']}")
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    print(f"Instance Name: {tag['Value']}")

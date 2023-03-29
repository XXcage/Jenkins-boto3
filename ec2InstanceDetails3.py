import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Retrieve all EC2 instances
response = ec2.describe_instances()

# Loop through all instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_state = instance['State']['Name']
        instance_name = ''
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
        # Check if the instance is in a stopped state
        if instance_state == 'stopped':
            print('Instance ID: {} | Instance Name: {}'.format(instance_id, instance_name))

import boto3

# Create a Boto3 EC2 client
ec2 = boto3.client('ec2')

# Get the list of running instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Loop through each instance and get its ID and name
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        # Get the instance ID
        instance_id = instance['InstanceId']

        # Get the instance name (if available)
        instance_name = ''
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break

        # Print the instance ID and name
        if instance_name:
            print(f"Instance {instance_id} ({instance_name}) is running")
        else:
            print(f"Instance {instance_id} is running")

import boto3

# create an EC2 client
ec2 = boto3.client('ec2')

# get all running instances
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# loop through instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        # check if there are any tags associated with the instance
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break
            else:
                instance_name = 'N/A'
        else:
            instance_name = 'N/A'
        
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        private_ip = instance['PrivateIpAddress']
        public_ip = instance.get('PublicIpAddress', 'N/A')
        
        print(f'Instance ID: {instance_id} | Instance Name: {instance_name} | Instance Type: {instance_type} | Private IP: {private_ip} | Public IP: {public_ip}')

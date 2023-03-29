import boto3
import json

# create an EC2 client
ec2 = boto3.client('ec2')

# get all instances and filter by stopped instances
instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

# check if there are no stopped instances
if len(instances['Reservations']) == 0:
    print('There are no stopped instances')
else:
    # extract details of each stopped instance and store in a list
    stopped_instances = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_name = ''
            rztag_value = ''
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                elif tag['Key'] == 'ec2forProj3':
                    tag_value = tag['Value']
            instance_details = {
                'InstanceId': instance_id,
                'InstanceName': instance_name,
                'ec2forProj3': tag_value,
                'State': instance['State']['Name'],
                'PrivateIpAddress': instance['PrivateIpAddress'],
                'LaunchTime': str(instance['LaunchTime'])
            }
            stopped_instances.append(instance_details)

    # output list of stopped instances in JSON format
    print(json.dumps(stopped_instances, indent=4))

import boto3

# create an EC2 client
ec2 = boto3.client('ec2')

# get all instances and filter by running instances
instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# check if there are no running instances
if len(instances['Reservations']) == 0:
    print('There are no running instances')
else:
    # print details of each running instance
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_name = ''
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
            print(f'Instance ID: {instance_id} | Instance Name: {instance_name}')

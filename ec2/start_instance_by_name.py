import boto3
import os
tag_key = 'tag:Name'
tag_value = 'ubuntu-20-tls'

ec2 = boto3.resource('ec2')

def get_instance_id(name, value):


    filters =[
        {
        'Name': name,
        'Values': [
            value,
            ]
        },
    ]


    instances = ec2.instances.filter(Filters = filters)

    for instance in instances:
        return instance.instance_id


instance_id = get_instance_id(tag_key, tag_value)

# print(instance_id)
instance = ec2.Instance(instance_id)
# instance.start()

os.environ["EC2_IP"] = instance.public_ip_address
# print(instance.public_ip_address)

# os.system(f'bash -c export EC2_IP="{instance.public_ip_address}"')

# print(os.environ["EC2_IP"])
os.system("echo $EC2_IP")
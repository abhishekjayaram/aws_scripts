import boto3

ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-07d5a54becbf0361a')

# response = instance.start()

for tags in instance.tags:
    if tags['Key'] == 'Name':
        print(tags['Value'])
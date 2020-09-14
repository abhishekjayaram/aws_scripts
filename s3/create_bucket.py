import boto3

s3_resource = boto3.resource('s3')

def createBucket(bucketname, region) :
    s3_resource.create_bucket(
        Bucket = bucketname, CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )

createBucket("testbucketpythonboto", "ap-south-1")
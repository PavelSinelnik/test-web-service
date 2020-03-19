import boto3
client = boto3.client('s3')
def create_s3(s3_name):
    client.create_bucket(
        ACL='public-read-write',
        Bucket=s3_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'
        }
    )
    client.put_bucket_versioning(
        Bucket=s3_name,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )
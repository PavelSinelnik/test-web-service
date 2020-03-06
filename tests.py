import boto3

l=boto3.client('lambda')


l.publish_version(FunctionName='get_device_data')

print(l)
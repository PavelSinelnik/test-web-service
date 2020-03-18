import boto3
import base64
import botocore.response
client= boto3.client('s3')
def lambda_handler(event, context):
    list_of_files = client.list_objects(
        Bucket='example141323'
    )
    for i in list_of_files['Contents']:
        if event['id'] == i["Key"]:
            s3 = boto3.client('s3')
            a =s3.get_object(Bucket="example141323", Key=event['id'],VersionId=event['VersionId'])
            return base64.b64decode(botocore.response.StreamingBody.read(a['Body']))


    return "Not found "
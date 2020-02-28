import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    get_file_content = event['content']
    object = s3.put_object(Bucket="example141323", Key=event['id'], Body=get_file_content)

    return {"VersionId": object["VersionId"]}

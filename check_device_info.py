import boto3

client= boto3.client('s3')
def lambda_handler(event, context):
    list_of_files = client.list_objects(
        Bucket='example141323'
    )
    for i in list_of_files['Contents']:
        if event['id'] == i["Key"]:
            return "Data is found "

    return "Not found"


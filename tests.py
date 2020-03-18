import boto3

s3=boto3.client('s3')
l=boto3.client('lambda')

#l.add_permission(
#  StatementId  = "AllowExecutionFromS3Bucket",
#  Action        = "lambda:InvokeFunction",
#  FunctionName = "trigtest",
#  Principal     = "s3.amazonaws.com",
#  SourceArn    = "arn:aws:s3:::forgit"
#)




response = client.update_function_code(
    FunctionName='string',
    S3Bucket='string',
    S3Key='string',

)



response3 = s3.put_bucket_notification_configuration(
                            Bucket='forgit',
                            NotificationConfiguration= {'LambdaFunctionConfigurations':[{'LambdaFunctionArn': 'arn:aws:lambda:us-east-2:301691100982:function:trigtest', 'Events': ['s3:ObjectCreated:*']}]})
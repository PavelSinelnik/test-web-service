import boto3
import json
import os


NAME_OF_JSON_FILE='cloud1.json'
StackName = 'TryStack'


with open(NAME_OF_JSON_FILE) as f:
    parameters = json.load(f)


s3 = boto3.client('s3')
cloud=boto3.client('cloudformation')
api_gateway=boto3.client('apigateway')

buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    if bucket['Name'] == parameters['Parameters']['NameForS3']['Default']:
        #s3.upload_file(parameters['Parameters']['LambdaSaveDeviceInfo']['Default'] + '.zip',parameters['Parameters']['NameForS3']['Default'],parameters['Parameters']['LambdaSaveDeviceInfo']['Default'] + '.zip')
        #s3.upload_file(parameters['Parameters']['LambdaGetDeviceData']['Default'] + '.zip',parameters['Parameters']['NameForS3']['Default'],parameters['Parameters']['LambdaGetDeviceData']['Default'] + '.zip')
        cloud.create_stack(StackName=StackName,TemplateURL="https://" + parameters['Parameters']['NameForS3']['Default'] + ".s3." +parameters['Parameters']['Region']['Default'] + ".amazonaws.com/" + NAME_OF_JSON_FILE,Capabilities=['CAPABILITY_NAMED_IAM'], )
        while 1:

            s = cloud.list_stacks(StackStatusFilter=['CREATE_COMPLETE'])
            for j in s['StackSummaries']:
                if j['StackName'] == StackName:
                    describe_stack = cloud.describe_stack_resources(
                        StackName=StackName
                    )

                    for i in describe_stack['StackResources']:
                        if i['LogicalResourceId'] == 'CreateRestAPi':
                            api_id = i["PhysicalResourceId"]
                        if i['LogicalResourceId'] == 'CreateApiKey':
                            api_key_id = i["PhysicalResourceId"]

                    api_key = api_gateway.get_api_key(apiKey=api_key_id, includeValue=True)
                    # print("https://" + api_id + ".execute-api." + parameters['Parameters']['Region']['Default'] + ".amazonaws.com/" + parameters['Parameters']['NameForStage']['Default']+'/' +parameters['Parameters']['LambdaSaveDeviceInfo']['Default'] + "/{id}")
                    # print("https://" + api_id + ".execute-api." + parameters['Parameters']['Region']['Default'] + ".amazonaws.com/" + parameters['Parameters']['NameForStage']['Default'] + '/' +parameters['Parameters']['LambdaCheckDeviceInfo']['Default'] + "/{id}")
                    # print("https://" + api_id + ".execute-api." + parameters['Parameters']['Region']['Default'] + ".amazonaws.com/" + parameters['Parameters']['NameForStage']['Default'] + '/' +parameters['Parameters']['LambdaGetDeviceData']['Default'] + "/{id}")
                    print(api_key['value'])
                    os.abort()
                else:
                    pass





s3.create_bucket(
        ACL='public-read-write',
        Bucket=parameters['Parameters']['NameForS3']['Default'],
        CreateBucketConfiguration={
            'LocationConstraint': parameters['Parameters']['Region']['Default']
        }
    )
s3.put_bucket_versioning(
        Bucket=parameters['Parameters']['NameForS3']['Default'],
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )


s3.upload_file(parameters['Parameters']['LambdaSaveDeviceInfo']['Default']+'.zip', parameters['Parameters']['NameForS3']['Default'],parameters['Parameters']['LambdaSaveDeviceInfo']['Default']+'.zip')
s3.upload_file(parameters['Parameters']['LambdaGetDeviceData']['Default']+'.zip', parameters['Parameters']['NameForS3']['Default'],parameters['Parameters']['LambdaGetDeviceData']['Default']+'.zip')
s3.upload_file(NAME_OF_JSON_FILE, parameters['Parameters']['NameForS3']['Default'],NAME_OF_JSON_FILE)
cloud.create_stack(StackName=StackName,TemplateURL="https://"+parameters['Parameters']['NameForS3']['Default']+ ".s3."+parameters['Parameters']['Region']['Default']+".amazonaws.com/"+NAME_OF_JSON_FILE,Capabilities=['CAPABILITY_NAMED_IAM'],)


while 1 :
    s = cloud.list_stacks(StackStatusFilter=['CREATE_COMPLETE'])
    for j in s['StackSummaries']:
        if j['StackName'] == StackName:
            describe_stack = cloud.describe_stack_resources(
                StackName=StackName
            )

            for i in describe_stack['StackResources']:
                if i['LogicalResourceId'] == 'CreateRestAPi':
                    api_id = i["PhysicalResourceId"]
                if i['LogicalResourceId'] == 'CreateApiKey':
                    api_key_id = i["PhysicalResourceId"]

            api_key = api_gateway.get_api_key(apiKey=api_key_id,includeValue=True)
            #print("https://" + api_id + ".execute-api." + parameters['Parameters']['Region']['Default'] + ".amazonaws.com/" + parameters['Parameters']['NameForStage']['Default']+'/' +parameters['Parameters']['LambdaSaveDeviceInfo']['Default'] + "/{id}")
            #print("https://" + api_id + ".execute-api." + parameters['Parameters']['Region']['Default'] + ".amazonaws.com/" + parameters['Parameters']['NameForStage']['Default'] + '/' +parameters['Parameters']['LambdaCheckDeviceInfo']['Default'] + "/{id}")
            #print("https://" + api_id + ".execute-api." + parameters['Parameters']['Region']['Default'] + ".amazonaws.com/" + parameters['Parameters']['NameForStage']['Default'] + '/' +parameters['Parameters']['LambdaGetDeviceData']['Default'] + "/{id}")
            print(api_key['value'])
            os.abort()
        else:
            pass


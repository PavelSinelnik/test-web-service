import boto3

client = boto3.client('dynamodb')
def create_table():
    table = client.create_table(
        TableName ='data_from_users',
        KeySchema =[

            {
                'AttributeName' : 'id',
                'KeyType' : 'HASH'
            }

        ],

        AttributeDefinitions =[

            {
                'AttributeName' : 'id',
                'AttributeType' : 'S'
            }


        ],
        BillingMode = 'PAY_PER_REQUEST'

    )


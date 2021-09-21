import json
import boto3

dynamodb = boto3.resource('dynamodb')
myTable = 'johnkoenig-ninja-counter'
table = dynamodb.Table(myTable)

# Update
def lambda_handler(event, context):
    myTable = table.update_item(
        Key={
            'site': 'johnkoenig.ninja'
        },
        UpdateExpression='SET hit_count = hit_count + :value',
        ExpressionAttributeValues={
            ':value':1
        },
        ReturnValues="UPDATED_NEW"
    )

# Read
    responseBody = json.dumps({"hit_count": int(myTable["Attributes"]["hit_count"])})
    print(responseBody)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(responseBody)
    }

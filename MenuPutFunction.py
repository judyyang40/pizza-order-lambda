from __future__ import print_function

import boto3
import json

def handler(event, context):
    
    dynamo = boto3.resource('dynamodb').Table('Menus')
    
    for key in event:
        if key != 'menu_id':
            k = key

    response = dynamo.update_item(
        Key={
            'menu_id': event['menu_id']
        },
        UpdateExpression="set "+k+" = :v",
        ExpressionAttributeValues={
            ':v': event[k]
        },
        ReturnValues="UPDATED_NEW"
    )
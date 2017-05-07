from __future__ import print_function

import boto3
import json

def handler(event, context):

    order_table = boto3.resource('dynamodb').Table('Orders')
    response = order_table.get_item(
        Key={
            'order_id': event['order_id']
        }
    )
    item = response['Item']
    return(item)
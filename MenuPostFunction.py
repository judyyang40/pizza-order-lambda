from __future__ import print_function

import boto3
import json

def handler(event, context):
    dynamo = boto3.resource('dynamodb').Table('Menus')

    response = dynamo.put_item(
        Item={
            'menu_id': event['menu_id'],
            'store_name': event['store_name'],
            'selection': event['selection'],
            'size': event['size'],
            'price': event['price'],
            'store_hours': event['store_hours']
        }
    )
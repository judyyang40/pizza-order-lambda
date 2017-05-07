from __future__ import print_function

import boto3
import json


def handler(event, context):
    dynamo = boto3.resource('dynamodb').Table('Menus')

    response = dynamo.delete_item(
        Key={
            'menu_id': event['menu_id']
        }
    )
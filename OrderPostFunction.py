from __future__ import print_function

import boto3
import json

def handler(event, context):
    order_table = boto3.resource('dynamodb').Table('Orders')

    response = order_table.put_item(
        Item={
            'menu_id': event['menu_id'],
            'order_id': event['order_id'],
            'customer_name': event['customer_name'],
            'customer_email': event['customer_email']
        }
    )
    
    menu_table = boto3.resource('dynamodb').Table('Menus')
    response = menu_table.get_item(
        Key={
            'menu_id': event['menu_id']
        }
    )
    item = response['Item']
    selectionstring = ""
    for i, val in enumerate(item['selection']):
        if i != 0:
            selectionstring += ", "
        selectionstring += str(i+1)+". "+val
        
    r={
        "Message": "Hi "+event['customer_name']+", please choose one of these selection:  "+selectionstring
    }
    return(r)
from __future__ import print_function

import boto3
import json
from time import strftime
from datetime import datetime, timedelta

def handler(event, context):
    
    order_table = boto3.resource('dynamodb').Table('Orders')
    response = order_table.get_item(
        Key={
            'order_id': event['order_id']
        }
    )
    order_item = response['Item']
    
    menu_table = boto3.resource('dynamodb').Table('Menus')
    response2 = menu_table.get_item(
        Key={
            'menu_id': order_item['menu_id']
        }
    )
    menu_item = response2['Item']
    
    if 'order' not in order_item:
        response3 = order_table.update_item(
            Key={ 'order_id': event['order_id'] },
            UpdateExpression="set #order = :s",
            ExpressionAttributeNames={ '#order': 'order' },
            ExpressionAttributeValues={ ':s': { "selection": menu_item['selection'][int(event['input'])-1] } },
            ReturnValues="UPDATED_NEW"
        )
        
        sizestring = ""
        for i, val in enumerate(menu_item['size']):
            if i != 0:
                sizestring += ", "
            sizestring += str(i+1)+". "+val
            
        r={
            "Message": "Which size do you want? "+sizestring
        }
        return(r)

    now = datetime.now()
    dt = now+timedelta(hours = -7)
    response4 = order_table.update_item(
        Key={ 'order_id': event['order_id'] },
        UpdateExpression="set order_status = :os, #order.size = :s, #order.costs = :c, #order.order_time = :d",
        ExpressionAttributeNames={ '#order': 'order' },
        ExpressionAttributeValues={
            ':os': 'processing',
            ':s': menu_item['size'][int(event['input'])-1],
            ':c': menu_item['price'][int(event['input'])-1],
            ':d': dt.strftime("%Y-%m-%d@%H:%M:%S")
        },
        ReturnValues="UPDATED_NEW"
    )
    r2={
        "Message": "Your order costs $"+menu_item['price'][int(event['input'])-1]+". We will email you when the order is ready. Thank you!"
    }
    return(r2)
    
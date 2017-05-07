# CMPE273 assignment2 -- pizza-order-lambda
Lambda functions written in python linked to Amazon Apigateway. Simulates menu management and customer orders.
https://github.com/sithu/cmpe273-spring17/tree/master/assignment2
Invoke URL: https://n1vzr0808c.execute-api.us-west-1.amazonaws.com/prod

1. POST /menu

_Request_

```json
{
    "menu_id": "pizzahut",
    "store_name": "Pizza Hut",
    "selection": [
        "Cheese",
        "Pepperoni"
    ],
    "size": [
        "Slide", "Small", "Medium", "Large", "X-Large"
    ],
    "price": [
        "3.50", "7.00", "10.00", "15.00", "20.00"
    ],
    "store_hours": {
        "Mon": "10am-10pm",
        "Tue": "10am-10pm",
        "Wed": "10am-10pm",
        "Thu": "10am-10pm",
        "Fri": "10am-10pm",
        "Sat": "11am-12pm",
        "Sun": "11am-12pm"
    }
}
```

_Response_

```sh
200 OK
```

2. DELETE /menu/{menu-id}

_Response_

```sh
200 OK
```

3. GET /menu/{menu-id}

_Response_

```json
{
    "menu_id": "pizzahut",
    "store_name": "Pizza Hut",
    "selection": [ 
        "Cheese",
        "Pepperoni"
    ],
    "size": [
        "Slide", "Small", "Medium", "Large", "X-Large"
    ],
    "price": [
        "3.50", "7.00", "10.00", "15.00", "20.00"
    ],
    "store_hours": {
        "Mon": "10am-10pm",
        "Tue": "10am-10pm",
        "Wed": "10am-10pm",
        "Thu": "10am-10pm",
        "Fri": "10am-10pm",
        "Sat": "11am-12pm",
        "Sun": "11am-12pm"
    }
}
```

4. PUT /menu/{menu-id}

Update the existing menu to add the "Vegetable" option.

_Request_

```json
{
    "menu_id": "pizzahut",
    "selection": [ 
        "Cheese",
        "Pepperoni",
        "Vegetable"
    ]   
}
```

_Response_

```sh
200 OK
```


1. POST /order

_Request_

```json
{   
    "menu_id": "pizzahut",
    "order_id": "johnsmith",
    "customer_name": "John Smith",
    "customer_email": "foobar@gmail.com"
}
```

_Response_

200 OK 

```sh
{
    "Message": "Hi {customer_name}, please choose one of these selection:  1. Cheese, 2. Pepperoni, 3.Vegetable"
}
```

2. PUT /order/{order_id}

_Request_

```json
{   
    "input": "1",
}
```

_Response_

200 OK 

```sh
{
    "Message": "Which size do you want? 1. Slide, 2. Small, 3. Medium, 4. Large, 5. X-Large"
}
```

2. PUT /order/{order_id}

_Request_

```json
{   
    "input": "4",
}
```

_Response_

200 OK 

```sh
{
    "Message": "Your order costs $15.00. We will email you when the order is ready. Thank you!"
}
```

3. GET /order/{order-id}

_Response_

```
{   
    "menu_id": "pizzahut",
    "order_id": "johnsmith",
    "customer_name": "John Smith",
    "customer_email": "foobar@gmail.com"
    "order_status": "processing"
    "order": {
        "selection": "Cheese",
        "size": "Large",
        "costs": "15.00",
        "order_time": "mm-dd-yyyy@hh:mm:ss"
    }
}
```

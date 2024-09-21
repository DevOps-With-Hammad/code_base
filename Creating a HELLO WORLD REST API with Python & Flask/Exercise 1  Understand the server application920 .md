 # Exercise 1: Understand the server application
In the Files Explorer open the jmgdo-microservices/CRUD folder and view products.py.

You first need to import the packages required to create REST APIs with Flask.

1
2
from flask import Flask, jsonify, request
import json
Copied!
You can then create the Flask application, which will service all the REST APIs for adding, retrieving, updating, and deleting products.
1
app = Flask("Product Server")
Copied!
The code has precreated products added to the list. These are defined in the following code.
1
2
3
4
products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]
Copied!
Now that the server is defined, you will create the REST API endpoints and define the routes or paths, one for each of the following operations.
Retrieve all the products - GET Request Method
Retrieve a product by its id - GET Request Method
Add a product - POST Request Method
Update a product by its id - PUT Request Method
Delete a product by its id - DELETE Request Method
Add the following code to products.py in the space provided.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
# Example request - http://localhost:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)
# Example request - http://localhost:5000/products/144 - with method GET
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)
# Example request - http://localhost:5000/products - with method POST
@app.route('/products', methods=['POST'])
def add_product():
    products.append(request.get_json())
    return '', 201
# Example request - http://localhost:5000/products/144 - with method PUT
@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    id = int(id)
    updated_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in updated_product.items():
        product[key] = value
    return '', 204
# Example request - http://localhost:5000/products/144 - with method DELETE
@app.route('/products/<id>', methods=['DELETE'])
def remove_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204

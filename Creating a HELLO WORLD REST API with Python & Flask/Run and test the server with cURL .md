# Run and test the server with cURL
In the terminal, run the python server using the following command.
1
python3 products.py
Copied!Executed!
The server starts running and listening at port 5000.

Server Running

Open another Terminal by clicking the Terminal menu and selecting New Terminal.

In the new terminal, run the following command to access the http://localhost:5000/products API endpoint. curl command stands for Client URL and is used as command line interfacing with the server serving REST API endpoints. It is, by default, a GET request.

1
curl http://localhost:5000/products
Copied!Executed!
This returns a JSON with the products that have been preloaded.

get products REST API

In the terminal, run the following command to add a product to the list. This will be a POST request to which you will pass the product parameter as a JSON.
1
2
3
curl -X POST -H "Content-Type: application/json" \
    -d '{"id": 145, "name": "Pen", "price": 2.5}' \
    http://localhost:5000/products
Copied!
This command will not return any output. It will add the product to the list of products.

Verify if the product is added by running the following command.
1
curl http://localhost:5000/products/145
Copied!
This should return the details of the product you just added with a POST request.

get product
Previous

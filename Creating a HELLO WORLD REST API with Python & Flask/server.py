from flask import Flask
app = Flask (" My hello World Application ")

@app.route ("/")
def hello():
    return "Hello World!"

if __name__=="__main__":
    app.run(debug=True)

    # when no port is specified , start at default port 5000

"""
python3 -m pip install flask 
python3 -m pip install flask 
python3 server.py 

"""
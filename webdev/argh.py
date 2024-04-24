from flask import Flask  # import the Flask class to create an app

app = Flask(__name__)  # invoke the Flask clas


@app.route('/')  # define the first route, the home route
def index():  # define the function that responds to the above route
    return 'Hello, World!'


@app.get("/posts")
def index():
    return {"response_code": 200, "data": "Hello from index"}


if __name__ == '__main__':
    app.run()  # Start the server listening for requests
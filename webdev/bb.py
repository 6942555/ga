from flask import Flask


app = Flask(__name__)  # invoke the Flask clas


@app.route('/')  # define the first route, the home route
def index():  # define the function that responds to the above route
    return 'Hello, World!'


if __name__ == '__main__':
    # Start the server listening for requests
    app.run(host="0.0.0.0", port=80, debug=True)

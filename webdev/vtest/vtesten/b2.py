from flask import Flask


app = Flask(__name__)


@app.route('/')  # define the first route, the home route
def index():  # define the function that responds to the above route
    return 'Hello, World!'
@app.get('/posts')
def posts():
	return {"response_code": 200, "data": "hello from index"}


if __name__ == '__main__':
    # Start the server listening for requests host="0.0.0.0", 
    app.run(port=80, debug=True)

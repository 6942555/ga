from flask import Flask, request  # import the Flask class to create an app

app = Flask(__name__)  # invoke the Flask clas


@app.route('/')  # define the first route, the home route
# def index():  # define the function that responds to the above route
#     return 'Hello, World!'


# @app.route("/posts")  #, methods=["GET"]
# def posts():
#     return {"response_code": 200, "data": "Hello from index"}


# @app.route("/posts/<post_id>", methods=["GET"])
# def posts_identified(post_id):
#     return {"response_code": 200, "data": f"Hello from {post_id}"}

#home page of reviews "/reviews"
@app.route("/reviews", methods=["GET"])
def index():
    return {"response_code": 200, "data": "reviews database - index page"}


#add new review "/reviews"
@app.route("/reviews", methods=["POST"])  # , methods=["POST"]
def create():
    return {"response_code": 200, "data": "add new review"}


#show details of specific review "/reviews/<id>"
@app.route("/reviews/<review_id>", methods=["GET"])  #
def show(review_id):
    return {"response_code": 200, "data": f"{review_id} plus the actual data"}


#update specific review "/reviews/<id>"
@app.route("/reviews/<review_id>", methods=["POST"])  #, methods=["POST"]
def update(review_id):
    return {"response_code": 200, "data": f"{review_id} is updated?"}


#delete review "/reviews/<id>"
@app.route("/reviews/<review_id>", methods=["DELETE"])  #
def delete(review_id):
	return {"response_code": 200, "data": f"{review_id} got deleted"}

#show new review form "/reviews/new"
@app.route("/reviews/new", methods=["GET"])
def new():
    return {"response_code": 200, "data": "new item form goes here"}

#show form for updating specific review "/reviews/<id>/edit"
@app.route("/reviews/<review_id>/edit", methods=["GET"])
def edit(review_id):
    return {"response_code": 200, "data": f"{review_id} editing form"}


if __name__ == '__main__':
    # Start the server listening for requests
    app.run(port=5000,debug=True)  #host="0.0.0.0",

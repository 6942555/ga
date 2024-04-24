from flask import Flask, render_template, request  # import what we need to use from the flask library


# To fake a database, the collection below will be our application's "data"
reviews = [
    {"book_title":"Confessions of a Python Programmer", "review_text":"A cautionary tale for all would-be programmers", "score":5, "id":"1"},
    {"book_title":"To Serve Man", "review_text":"Delicious recipes", "score":3, "id":"2"},
    {"book_title":"Pride and Prejudice", "review_text":"The pride is ok but the prejudice not so much", "score":4, "id":"3"},
]


app = Flask(__name__)  # invoke the Flask clas


#home page of reviews "/reviews"
@app.route("/reviews", methods=["GET"])
def index():
    return render_template("index.html", reviews=reviews)


#add new review "/reviews"
@app.route("/reviews", methods=["POST"])  # , methods=["POST"]
def create():
    #check dupes? append id?
    new_review_dict = request.get_json()
    reviews.append(new_review_dict)
    return {"response_code": 201, "data": f"{reviews}"}


#show details of specific review "/reviews/<id>"
@app.route("/reviews/<review_id>", methods=["GET"])  #
def show(review_id):
    for review in reviews:
        if review.get("id") == review_id:
          return render_template("show.html", review=review)  
    return {"response_code": 200, "data": "review by that id not found"}


#update specific review "/reviews/<id>"
@app.route("/reviews/<review_id>", methods=["POST"])  #, methods=["POST"]
def update(review_id,updated_review):
    #change data at id to new data
    return {"response_code": 201, "data": f"{reviews}"}


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

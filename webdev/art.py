from flask import Flask, render_template, request  # import the Flask class to create an app
import requests, json, time

app = Flask(__name__)  # invoke the Flask clas


 # main url bit    f"https://collectionapi.metmuseum.org/public/collection/v1/"

 #dept id         search?departmentId={dept_id}&q=cat       
 #object id         objects/{object_id}
 #str search        search?q=sunflowers


# @app.route('/')  # define the first route, the home route
# def index():  # define the function that responds to the above route
#     return 'Hello, World!'


# @app.route("/posts")  #, methods=["GET"]
# def posts():
#     return {"response_code": 200, "data": "Hello from index"}


# @app.route("/posts/<post_id>", methods=["GET"])
# def posts_identified(post_id):
#     return {"response_code": 200, "data": f"Hello from {post_id}"}

#departments - 'home page' kinda fake, hard to get anything from a list of art id
@app.route("/", methods=["GET"]) #departments
def index():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    depts = requests.get(url)
    deptlist = []
    for dept in depts.json().get('departments'):
        deptlist.append(dept)

    return render_template("departments.html", deptlist=deptlist)
    #return {"response_code": 200, "data": f"{depts.json()}"}



# #show details of department highlights "/reviews/<id>"
@app.route("/departments/<dept_id>", methods=["GET"])  #
def show(dept_id):
    results = []
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&departmentId={dept_id}&q=cat"
    dept_objects = requests.get(url)
    if dept_objects.status_code == 200:
        for object_id in dept_objects.json()['objectIDs']:
            url_id = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
            dept_object = requests.get(url_id)
            if dept_object.status_code == 200:
                results.append(dept_object.json())
                time.sleep(0.05) # so we don't get 500 errors from hitting the API too often
    return render_template("display.html", obj_data=results)


# #objects - empty, in case
@app.route("/objects", methods=["GET"])
def show_objects():
    return {"response_code": 200, "data": "nothing yet"}


#show details of specific object "/object/<id>"
@app.route("/objects/<object_id>", methods=["GET"])  #
#sanitize object id
def show_object(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    object_data = requests.get(url)
    obj_data = []
    obj_data.append(object_data.json())
    return render_template("display.html", obj_data=obj_data)
    #return {"response_code": 200, "data": f"{object_data}"}


@app.route("/search/<search>", methods=["GET"])  #
def get_data(search="sunflowers"):
    """
    Given a search term, will return all the info
    for met artworks on display that match
    If nothing matches, will return an empty list
    """
    obj_data = []
    # assume we're only interested in on display
    url_objects = f'https://collectionapi.metmuseum.org/public/collection/v1/search?q={search}&isOnView=true'
    
    r_objects = requests.get(url_objects)
    if r_objects.status_code == 200:
        for object_id in r_objects.json()['objectIDs']:
            url_id = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
            r_object = requests.get(url_id)
            if r_object.status_code == 200:
                obj_data.append(r_object.json())
                time.sleep(0.05) # so we don't get 500 errors from hitting the API too often
    return render_template("display.html", obj_data=obj_data) 
    #return {"response_code": 200, "data": f"{results}"}


if __name__ == '__main__':
    # Start the server listening for requests
    app.run(port=5000,debug=True)  #host="0.0.0.0",

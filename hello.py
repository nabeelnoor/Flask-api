from flask import Flask,jsonify,request
import numpy as np;
import pandas as pd;

app = Flask(__name__)

courseList=[
{"name":"Java",
"price":"1"},
{"name":"Python",
"price":"1"},
{"name":"Javascript",
"price":"1"},
]

@app.route("/getAllCourses",methods=['Get'])
def getCoursesList():
    return jsonify({'courses':courseList})

@app.route("/getCourseName/<int:course_id>",methods=['Get'])
def getCourse(course_id):
    a=courseList[course_id]
    print(a['name'])
    return jsonify({'courseName':a["name"]})

@app.route("/makeCourse",methods=['Post'])
def makeCourse():
    # temp=request.data
    # print(temp)
    sampleT=request.json
    courseList.append(sampleT)
    print(sampleT)
    return jsonify({'courseName':courseList})


@app.route("/then")
def hello_world():
    a=np.array([12,2,3,4,5])
    print(a)
    return "<p>Hello, World to then route @@@!</p>"

@app.route("/ok")
def hello_world2():
    return "<p>This is ok page</p>"

if __name__=="__main__":
    app.run(debug=True)

# ##some documentation on request
#link: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request

# request.data Contains the incoming request data as string in case it came with a mimetype Flask does not handle.

# request.args: the key/value pairs in the URL query string
# request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
# request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
# request.values: combined args and form, preferring args if keys overlap
# request.json: parsed JSON data. The request must have the application/json content type, or use request.get_json(force=True) to ignore the content type.
# All of these are MultiDict instances (except for json). You can access values using:

# request.form['name']: use indexing if you know the key exists
# request.form.get('name'): use get if the key might not exist
# request.form.getlist('name'): use getlist if the key is sent multiple times and you want a list of values. get only returns the first value.

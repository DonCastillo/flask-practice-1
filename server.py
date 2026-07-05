from flask import Flask, make_response
app = Flask("Hello, World")

@app.route('/')
def index():
    return {"message": "Hello, World!"}

@app.route('/no_content')
def no_content():
    return (dict(message="No content found"), 204)

@app.route('/exp')
def index_explicit():
    resp = make_response(dict(message="Hello World"))
    resp.status_code = 200
    return resp
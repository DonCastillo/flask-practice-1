from flask import Flask
app = Flask("Hello, World")

@app.route('/')
def index():
    return {"message": "Hello, World!"}
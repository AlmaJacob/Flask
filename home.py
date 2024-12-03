from flask import Flask

app=Flask(__name__)

@app.route('/')

def fun1():
    return " we want to study flask framework"
app.run()
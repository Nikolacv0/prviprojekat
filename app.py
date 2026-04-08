import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return render template

@app.route("/primer-string")
def string():
   return "Neki ne preterano dugacak tekst"

@app.route("/primer-broj")
def broj():
   return 265

@app.route("/primer-niz")
def niz():
    nekiNiz = [1,2,3,4,5]
    return nekiNiz

@app.route("/primer-json")
def primerJson():
    data = {
        "message": "This is a JSON response",
        "status": "success"
    }
    return (data)

@app.route("/primer-html")
def primerHTML():
    data = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF 8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible">
    """

if __name__=="__main__":
    app.run()

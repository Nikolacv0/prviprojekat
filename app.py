import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    nazivSpiska = "Spisak restorana"
    spisakRestorana = ["Pastica", "Pica tim, "HasHub", "Sahara"]
    return render_template("index.html", naziv=nazivSpiska, spisak=spisakRestorana)

@app.route("/restorani/1")
def meni():
    nazivMeni = "Meni Promenada"
    spisakMeni = ["Sendvici", "Burgeri", "Torte", "Paste"]
    return render_template("meni.html, naziv=nazivMeni, spisak=spisakMeni)

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

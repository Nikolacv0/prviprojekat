import os
import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    nazivSpiska = "Spisak restorana"
    #spisakRestorana = ["Pastica", "Pica tim", "HasHub", "Sahara"]
    con = sqlite3.connect("dostavaHrane.db")

    cur = con.cursor()
    cur.execute("SELECT id,naziv FROM restorani LIMIT 10")

    spisakRestorana=cur.fetchall()
   
    return render_template("index.html", naziv=nazivSpiska, spisak=spisakRestorana)

@app.route("/restoran/<id_rest>")
def meni():
    #nazivMeni = "Meni Promenada"
    #spisakMeni = ["Sendvici", "Burgeri", "Torte", "Paste"]
    con = sqlite3.connect("dostavaHrane.db")

    cur = con.cursor()
    query = f"SELECT naziv FROM meni where id_restorana == {id_rest}"
    cur.execute(query)

    menirestorana = cur.fetchall()
    return render_template("meni.html", naziv=nazivMeni, spisak=spisakMeni)

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

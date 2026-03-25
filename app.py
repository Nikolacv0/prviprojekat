import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return "Zdravo programeri"

if __name__=="__main__":
    app.run()

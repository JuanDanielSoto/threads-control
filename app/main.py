from flask import Flask, request, jsonify, redirect, url_for, render_template, flash
from datetime import datetime
from sharedTools import *
from flask_cors import CORS

app= Flask(__name__)
DB = database("db")
log = database("login")
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


#Actualizado

@app.route("/") #Actualizada
def all():
     return "Hola mundo"

@app.route("/new/<string:sen>") #Actualizado
def postNewSensor(sen):
      None

@app.route("/update", methods=["PUT"]) #Actualizado
def updateValues():
      """
      request - 
      {
        "name": "nombre",
        "site": "ubicación"
        "series": {
            "HUM": [],
            "PPM": [],
            "TEMP": []
          }
      }
      """
      return jsonify(post)

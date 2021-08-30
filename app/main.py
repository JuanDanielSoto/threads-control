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
      c

# @app.route("/update", methods=["PUT"]) #Actualizado
# def updateValues():
#       """
#       request - 
#       {
#         "name": "nombre",
#         "site": "ubicación"
#         "series": {
#             "HUM": [],
#             "PPM": [],
#             "TEMP": []
#           }
#       }
#       """
#       post = request.json
#       db = DB.load()
#       if exist(post["name"], db):
#             now = datetime.now()
#             db[post["name"]][post["site"]]["PPM"].append(post["series"]["PPM"])
#             db[post["name"]][post["site"]]["HUM"].append(post["series"]["HUM"])
#             db[post["name"]][post["site"]]["TEMP"].append(post["series"]["TEMP"])
#             db[post["name"]][post["site"]]["DATE"].append(str(now.date())+"/"+str(now.time()))
#             DB.update(db)
#             return jsonify({"sucess": "'"+post["name"]+"' fue falta actualizar correctamente"})
#       else:
#             return jsonify({"error": "'"+post["name"]+"' does not exists"})

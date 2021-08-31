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
     db = DB.load()
     return jsonify(db)

@app.route("/new/<string:sen>") #Actualizado
def postNewSensor(sen):
      None

@app.route("/update", methods=["POST"]) #Actualizado
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
      try:
            post = request.json
            db = DB.load()
            db.append(post)
            DB.update(db)
            # return jsonify({"status":"success"})
            return jsonify(post)
      except:
            return jsonify({"status":"403 Bad request"})

#Access login

@app.route("/login/validate", methods=["POST"])
def validate():
      """
      request - 
      {
            "user": "name",
            "pwd" : "password"
      }
      """
      post = request.json
      users = log.load()
      for user in users:
            if post["user"] == user["user"]:
                  if post["pwd"] == user["pwd"]:
                        return jsonify({"error": "Acceso concedido", "acess": True})
                  else:
                        return jsonify({"error": "Contraseña incorrecta", "acess": False})
      return jsonify({"error": "Usuario no existe", "acess": False})

@app.route("/login/add", methods=["POST"])
def addUser():
      """
      request - 
      {
            "user": "name"
      }
      """
      post = request.json
      users = log.load()
      for user in users:
            if post["user"] == user["user"]:
                  return jsonify({"error": "Usuario ya existe"})
      try:
            users.append({"user": post["user"], "pwd" : post["pwd"]})
            log.update(users)
            return jsonify({"success": "Usuario registrado exitosamente"})
      except Exception:
            return jsonify({"error": "Entrada inválida"})

@app.route("/login/delete", methods=["DELETE"])
def deleteUser():
      post = request.json
      users = log.load()
      for i, user in enumerate(users):
            if post["user"] == user["user"]:
                  users.pop(i)
                  log.update(users)
                  return jsonify({"success": "Usuario eliminado correctamente"})
      return jsonify({"error": "Este usuario no existe"})
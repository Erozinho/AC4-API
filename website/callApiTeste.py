from flask import Blueprint, jsonify, request
import random as r
import mysql.connector
import requests

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@",
    database="conselhoAluno",
)

conselhos = ("https://api.adviceslip.com/advice/")

mycursor = db.cursor()

insert = "INSERT INTO alunos (Nome, Idade, conselho) VALUES (%s,%s,%s)"
select = "SELECT * from alunos"

call = Blueprint('registrar', __name__)

@call.route('/call', methods=['GET'])
def pegar_registro():

    valor = r.randint(1,200)
    valor = str(valor)


    response = requests.get(f"{conselhos+valor}")

    if response.status_code == 200:
        print("sucessfully fetched the data")
        a = response.json()
        print(a['slip']['advice'])
        return '<h1>SUCESSO</h1>'
    else:
        return '<h1>FRACASSO</h1>'

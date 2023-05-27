from flask import Blueprint, request, render_template
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



add = Blueprint('add', __name__, template_folder="template")

@add.route('/add', methods=['GET'])
def pegar_registro():
    return render_template("registrar.html")

@add.route('/add', methods=['POST'])
def salvar_registro():
    n = request.form.get('nome')
    i = request.form.get('idade')
    c = request.form.get('conselho')
    i = int(i)
    c = int(c)

    val = (n,c,i)

    insert = "INSERT INTO alunos(Nome, Idade, Consellho) VALUES (%s,%s,%s)"

    mycursor.execute(insert, val)
    db.commit()
    return "<h1>Dados criado com sucesso!</h1>"
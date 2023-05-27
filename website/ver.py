from flask import Blueprint, jsonify, request, render_template
import mysql.connector
import requests

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@",
    database="conselhoAluno",
)


mycursor = db.cursor()

# Se comunica com o bd e puxa o conselho da api
ver = Blueprint('ver', __name__, template_folder="template")


@ver.route('/ver', methods=['GET'])
def carregar():
    return render_template("conselho.html")

@ver.route('/ver', methods=['POST'])
def ver_resultado():
    nome = request.form.get('nome')

    select = f"SELECT Consellho from alunos WHERE Nome='{nome}'"
    mycursor.execute(select)
    tabela = mycursor.fetchone()
    
    aluno_conselho = str(tabela[0])
        
    conselhos = ("https://api.adviceslip.com/advice/")
    response = requests.get(f"{conselhos+aluno_conselho}")

    if response.status_code == 200:
        print("sucesso na requisição")
        a = response.json()
        b = (a['slip']['advice'])
        return f"Conselho do Aluno {nome} é {b}"
    else:
        return "ERRO"
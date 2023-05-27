from flask import jsonify, Blueprint, request, render_template
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@",
    database="conselhoAluno",
)

conselhos = ("https://api.adviceslip.com/advice/")

mycursor = db.cursor()

excluir = Blueprint('excluir', __name__, template_folder="template")

@excluir.route('/del', methods=['GET'])
def carregar():
    return render_template('delete.html')

@excluir.route('/del', methods=['POST','DELETE'])
def apagar_registros():
    nome = request.form.get('nome')
    dele = f"DELETE FROM Alunos WHERE Nome='{nome}'"
    mycursor.execute(dele)
    db.commit()
    return "<h1>Dado apagado com sucesso.</h1>"
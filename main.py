#Vou importa a classe Flask do pacote flask

from flask import Flask,make_response,jsonify,request
from dados import Materias
import mysql.connector #importando o conector
#variável para conexão
#host - é o servidor
#user - usuário
#senha - root
#database - enem
mydb = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   password= 'root',
   database = 'enem',
)

#FIXME: Flask é um classe

app = Flask("__name__")#instância o objeto app / Assume o nome da aplicação como nome padrão
#NOTE: VAMOS DECORAR
#Decorators
#post(inserir),PUT()
@app.route('/materias', methods=["GET"])
def get_materias():
    return make_response(
        jsonify(
            Materias
        )
    )     
@app.route("/")
def index():
    return "Projeto Integrador Base (Enem)"

#request
#POST
@app.route('/materas', methods=['POST'])
def create_materia():
    materia = request.json
    return materia
#execultar a API
app.run()
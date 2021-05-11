from flask import Flask, jsonify, request
from cmd_bd import query, execute, insert, select, delete, update
from serializers import genero_from_db, genero_from_web, diretores_from_web, diretores_from_db
from models import get_genero, insert_genero, get_diretor, insert_diretor,update_diretor
from validacao import valida_genero, valida_diretores

app = Flask(__name__)


@app.route("/diretores", methods=["POST"])
def inserir_diretores():
    diretor = diretores_from_web(**request.json)
    if valida_diretores(**diretor):
        insert_diretor(**diretor)
        diretor_criado = get_diretor(diretor["nome_completo"])
        return jsonify(diretores_from_db(diretor_criado))
    else:
        return jsonify("erro", "diretor inválido")


@app.route("/diretores", methods=["GET"])
def get_diretores():
    return jsonify(select("diretores"))


@app.route("/diretores/<int:id>",methods=["PUT","PATCH"])
def update_diretores():
    diretor = diretores_from_web(**request.json)
    if valida_diretores(**diretor):
        update_diretor(id,**diretor)
        diretor_alterado = get_diretor(id)
        return jsonify(diretores_from_db(diretor_alterado))


@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        insert_genero(**genero)
        genero_criado = get_genero(genero["nome"])
        return jsonify(genero_from_db(genero_criado))
    else:
        return jsonify("erro", "genero inválido")


@app.route("/generos", methods=["GET"])
def get_generos():
    return jsonify(select("generos"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

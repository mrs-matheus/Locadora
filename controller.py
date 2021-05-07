from flask import Flask, jsonify, request
from cmd_bd import select
from serializers import diretores_from_db, usuario_from_web, usuario_from_db
from serializers import genero_from_db, genero_from_web, diretores_from_web, nome_usuario_from_web
from models import insert_diretor, update_diretor, delete_genero, update_usuario, delete_usuario,delete_diretor
from models import get_genero, insert_genero, get_diretor, get_usuario, insert_usuario, select_usuarios
from validacao import valida_genero, valida_diretores, valida_usuario

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


@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
def update_diretores():
    diretor = diretores_from_web(**request.json)
    if valida_diretores(**diretor):
        update_diretor(id, **diretor)
        diretor_alterado = get_diretor(id)
        return jsonify(diretores_from_db(diretor_alterado))


@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretores(id):
    try:
        delete_diretor(id)
        return None, 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/generos", methods=["POST"])
def inserir_generos():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_criado = get_genero(genero[id_genero])
        return jsonify(genero_from_db(genero_criado))
    else:
        return jsonify("erro", "genero inválido")


@app.route("/generos", methods=["GET"])
def get_generos():
    return jsonify(select("generos"))


@app.route("/generos", methods=["DELETE"])
def delete_generos():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        delete_genero(**genero)
        return jsonify(select("generos"))
    else:
        return jsonify("erros", "genero invalido")


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return None, 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

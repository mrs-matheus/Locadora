from cmd_bd import insert, select, update, delete, select_like


def insert_genero(nome):
    return insert("generos", ["nome"], [nome])


def get_genero(nome):
    select("generos", "nome", nome)


def update_genero(nome):
    update("generos", ["nome"], [nome])


def delete_genero(nome):
    delete("generos", ["nome"], [nome])


def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])


def get_diretor(nome_completo):
    select("diretores", "nome_completo", nome_completo)


def update_diretor(id, nome_completo):
    update("diretores", "id", id, ["nome_completo"], [nome_completo])


def delete_diretor(id, nome_completo):
    delete("diretores", "id", id, "nome_completo", nome_completo)


def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])


def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]


def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])


def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)


def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)

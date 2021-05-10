from cmd_bd import insert, select, update, delete, select_like


def insert_genero(nome):
    return insert("generos", ["nome"], [nome])


def get_genero(nome):
    return select("generos", "nome", nome)


def update_genero(id, nome):
    update("generos", "id", id, ["nome"], [nome])


def delete_genero(nome):
    delete("generos", ["nome"], [nome])


def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])


def get_diretor(nome_completo):
    return select("diretores", "nome_completo", nome_completo)


def update_diretor(id, nome_completo):
    update("diretores", "id", id, ["nome_completo"], [nome_completo])


def delete_diretor(id, nome_completo):
    delete("diretores", "id", id, "nome_completo", nome_completo)


def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])


def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]


def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario,
           ["nome_completo", "CPF"], [nome_completo, CPF])


def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)


def select_usuario(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)


def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes",
                  ["titulo,ano,classificacao,preco,diretores_id,generos_id"],
                  [titulo, ano, classificacao, preco, diretores_id, generos_id])


def get_filme(id):
    return select("filmes", "id", id)


def update_filme(id_filme, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id_filme,
           ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def delete_filme(id_filme):
    delete("filmes", "id", id_filme)


def insert_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    return insert("locacacoes",
                  ["data_inicio", "data_fim", "filmes_id", "usuarios_id"],
                  [data_inicio, data_fim, filmes_id, usuarios_id])


def get_locacao(id_locacao):
    return select("locacao", "id", id_locacao)


def update_locacao(id_locacao, data_inicio, data_fim, filmes_id, usuarios_id):
    update("locacoes", "id", id_locacao,
           ["data_inicio", "data_fim", "filmes", "filmes_id", "usuarios_id"],
           [data_inicio, data_fim, filmes_id, usuarios_id])


def delete_locacao(id_locacao):
    delete("locacacoes", "id", id_locacao)


def insert_pagamento(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    return insert("pagamento",
                  ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
                  [tipo, status, codigo_pagamento, valor, data, locacoes_id])


def get_pagamento(id_pagamento):
    return select("pagamento", "id", id_pagamento)


def update_pagamento(id_pagamento, tipo, status, codigo_pagamento, valor, data, locacoes_id):
    update("pagamento", "id", id_pagamento,
           ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
           [tipo, status, codigo_pagamento, valor, data, locacoes_id])

def delete_pagamento(id_pagamento):
    delete("pagamento","id",id_pagamento)

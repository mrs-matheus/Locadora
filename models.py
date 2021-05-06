from cmd_bd import insert,select,update,delete

def insert_genero(nome):
    insert("generos",["nome"],[nome])

def get_genero(nome):
    select("generos","nome",nome)

def insert_diretor(nome_completo):
    insert("diretores",["nome_completo"],[nome_completo])

def get_diretor(nome_completo):
    select("diretores","nome_completo",nome_completo)

def update_diretor(id,valor_chave,nome_completo):
    update("diretores",["id"],["valor_chave"],"nome_completo",["valores"],[id,valor_chave,nome_completo])
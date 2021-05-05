from main import insert,select

def insert_genero(nome):
    insert("generos",["nome"],[nome])

def get_genero(nome):
    select("locadora.generos","nome",nome)
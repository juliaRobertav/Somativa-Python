from conexao import conect


def leitura_marcas(marca):
    conexao, cursor = conect()
    ler = f"SELECT * FROM celular WHERE marca = '{marca}'"
    cursor.execute(ler)
    resultado = cursor.fetchall()
    return resultado

def leituratodos():
    conexao, cursor = conect()
    ler = f"SELECT * FROM celular"
    cursor.execute(ler)
    resultado = cursor.fetchall()
    return resultado
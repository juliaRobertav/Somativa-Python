from conexao import conect

def adeus_banco():
    """
    :return: método para deletar o banco de dados
    """
    conexao, cursor = conect()
    apagar = f"""DELETE FROM celular"""
    cursor.execute(apagar)
    conexao.commit()
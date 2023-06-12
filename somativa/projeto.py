from bs4 import BeautifulSoup
import requests
from conexao import conect


class Colombo:
    """
    classe criada para realização do webscraping utilizando BeautifulSoup
    """

    def __init__(self):
        self.sites()

    def sites(self):
        """
        :return:funçao onde captura os links do site Colombo, além de capturar os dados através das tags HTML
        """
        # dicionário contendo nomes das marcas como chaves e urls como valores
        marcas = {
            'samsung': 'https://www.colombo.com.br/produto/Smartphone-e-Celular/Samsung',
            'motorola': 'https://www.colombo.com.br/produto/Smartphone-e-Celular/Motorola',
            'apple': 'https://www.colombo.com.br/produto/Smartphone-e-Celular/Apple',
            'lg': 'https://www.colombo.com.br/produto/Smartphone-e-Celular/LG',
            'xiaomi': 'https://www.colombo.com.br/produto/Smartphone-e-Celular/Xiaomi'
        }

        # .items retorna tuplas de 'marcas' e 'marca,url' permite acessar cada link
        for marca, url in marcas.items():
            # envia uma solicitação GET para a URL e recebe a resposta
            resp = requests.get(url)
            # cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta
            scrap = BeautifulSoup(resp.content, 'html.parser')
            modelos = scrap.select('.product-list h2')
            preco = scrap.find_all(class_='price')
            for i in range(10):
                # extrai o conteúdo do nome do modelo em forma de texto, através do indíce de acordo com o loop
                model = modelos[i].text.strip()
                # mesma coisa que o anterior porém será o preço dos celulares
                total = preco[i].text.strip()
                print(model)
                print(total)

                conexao, cursor = conect()  # fazendo a conexão
                teste = f""" INSERT INTO celular (marca, modelo, preco)
                              VALUES ('{marca}', '{model}', '{total}') """
                cursor.execute(teste)
                conexao.commit()


Colombo()

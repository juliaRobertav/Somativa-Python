from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import projeto
from read import leitura_marcas, leituratodos
from delete import adeus_banco
import pandas as pd


class Tela():
    def __init__(self):
        self.janela = Tk()
        self.loja = projeto.Colombo()
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.listar_frame()
        self.listar_marcas()
        self.janela.mainloop()
        self.janela.update()
        # self.exportar_dados()

    def tela(self):
        """
        :return: dimensões da tela
        """
        self.janela.title('loja')
        self.janela.configure(background='#FDD2A3')
        self.janela.geometry('1000x800')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=1000, height=800)

    def frames(self):
        """
        :return: função para criação dos frames
        """
        self.frame0 = Frame(self.janela, bg='#FDD2A3')
        self.frame0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame1 = Frame(self.janela, bg='#FDD2A3')
        self.frame1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.10)

        self.frame2 = Frame(self.janela, bg='#FDD2A3')
        self.frame2.place(relx=0.03, rely=0.36, relwidth=0.94, relheight=0.60)

    def labels(self):
        """
        :return: função para a labels
        """
        self.lbTitulo = Label(self.frame0, text='COLOMBO', bg='#E6C387')
        self.lbTitulo.place(relx=0, rely=0, relwidth=1, relheight=0.30)

        self.lbMarca = Label(self.frame1, text='Marcas Disponíveis', bg='#E6C387')
        self.lbMarca.place(relx=0, rely=0, relwidth=1, relheight=0.30)

        self.lbConectaBanco = Label(self.frame2, text='Dados', bg='#E6C387')
        self.lbConectaBanco.place(relx=0, rely=0, relwidth=1, relheight=0.10)

    def botoes(self):
        """
        :return: função para os botões
        """
        self.bt = Button(self.frame0, text="Armazenar dados", command=self.dados)
        self.bt.place(relx=0.23, rely=0.35, relwidth=0.1, relheight=0.50)

        self.btRead = Button(self.frame0, text="Exibir dados", command=self.ler_banco)
        self.btRead.place(relx=0.43, rely=0.35, relwidth=0.1, relheight=0.50)

        self.btDelete = Button(self.frame0, text="Deletar dados", command=self.apagar_dados)
        self.btDelete.place(relx=0.60, rely=0.35, relwidth=0.1, relheight=0.50)

    def listar_marcas(self):
        """
        :return: função para DropDrown das marcas e dos formatos de arquivos no pandas
        """
        self.site = StringVar(self.frame1)
        self.marcas = ["Samsung", "Motorola", "Apple", "LG", "Xiaomi"]

        self.menu = OptionMenu(self.frame1, self.site, *self.marcas, command=lambda x: self.produtos(self.site.get()))
        self.menu.place(relx=0.55, rely=0.35, relwidth=0.30, relheight=0.55)

        self.planilha = StringVar(self.frame1)
        self.arquivos = ["csv", "xlsx"]

        self.panda = OptionMenu(self.frame1, self.planilha, *self.arquivos,
                                command=lambda x: self.exportar_dados(self.planilha.get()))
        self.panda.place(relx=0.15, rely=0.35, relwidth=0.30, relheight=0.55)

    def listar_frame(self):
        """
        :return: função para listar os dados
        """
        self.listaPro = ttk.Treeview(self.frame2, height=3,
                                     columns=('col0',
                                              'col1',
                                              'col2',
                                              'col3'))
        self.listaPro.heading('#0', text='ID', )
        self.listaPro.heading('#1', text='*')
        self.listaPro.heading('#2', text='Produto')
        self.listaPro.heading('#3', text='Valor')
        self.listaPro.heading('#4', text='Marca')

        self.listaPro.column('#0', width=0, stretch=NO)
        self.listaPro.column('#1', width=0, stretch=NO)
        self.listaPro.column('#2', width=550)
        self.listaPro.column('#3', width=188)
        self.listaPro.column('#4', width=188)

        self.listaPro.place(relx=0.01, rely=0.10, relwidth=0.95, relheight=0.88)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaPro.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.10, relwidth=0.030, relheight=0.88)

    def produtos(self, marca):
        """
        :param marca:  nome da marca
        :return: retorna os valores da função listar_frame para leitura das marcas
        """
        self.listaPro.delete(*self.listaPro.get_children())  # * (seleciona a lista toda)
        ler_marcas = leitura_marcas(marca)
        if ler_marcas is not None:  # incrementa todos os epaços vazios para mostrar o banco, caso não for ser ainserido na lista
            for i in ler_marcas:
                self.listaPro.insert(parent='', index=0, values=i)
        # for i in leitura_marcas(marca):
        #     self.listaPro.insert(parent='', index=0, values=i)

    def mostrar_banco(self):
        """
        :return: retorna os valores da função listar_frame para leitura de tudo, mostra os dados do banco
        """
        self.listaPro.delete(*self.listaPro.get_children())
        ler_tudo = leituratodos()
        if ler_tudo is not None:
            for i in ler_tudo:
                self.listaPro.insert(parent='', index=0, values=i)

    def ler_banco(self):
        """
        :return: leitura do banco de dados
        """
        mensagem1 = messagebox.askyesnocancel("Exibição do banco de dados.\n Deseja continuar?")
        if mensagem1:
            self.mostrar_banco()
            messagebox.showinfo("Exibição concluida")

    def dados(self):
        """
        :return: armazena no banco de dados
        """
        mensagem2 = messagebox.askyesnocancel("Todos os dados serão enviados para o banco de dados."
                                              "\nDeseja continuar?")
        if mensagem2:
            self.loja.sites()
            messagebox.showinfo("Dados armazenados com sucesso")

    def apagar_dados(self):
        """
        :return: deleta o banco de dados
        """
        mensagem3 = messagebox.askyesnocancel("Todos os dados serão apagados do banco de dados."
                                              "\nDeseja continuar?")
        if mensagem3:
            adeus_banco()
            messagebox.showinfo("Dados deletados com sucesso")

    def exportar_dados(self, plan):
        """
        :param plan: parâmetro para criação dos arquivos xlsx ou csv
        :return: exporta os dados nos arquivos tanto em formato csv ou xlsx
        """

        df = pd.DataFrame(self.mostrar_banco(), columns=["ID", "Marca", "Modelo", "Preço"])
        if plan == 'csv':
            df.to_csv("dados_colombo.csv", index=False, sep='\t')


        elif plan == 'xlsx':
            escreve = pd.ExcelWriter("./dados_colombo.xlsx")
            df.to_excel(escreve, sheet_name="Sheet1", index=False, header=False)
            escreve.close()

        messagebox.showinfo("Exportação concluída", f"Dados exportados como {plan.upper()}")  # mensagem


Tela()

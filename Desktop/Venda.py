from Pessoa import Pessoa
from Bebida import Bebida

class Venda:
    def __init__(self, codigoVenda : int, dataVenda, codCliente : int , codCerveja : int, qtdComprada : int):
        self.__codigoVenda = codigoVenda
        self.__dataVenda = dataVenda
        self.__cliente = codCliente
        self.__cerveja = codCerveja
        self.__qtdComprada = qtdComprada

    def getCodigoVenda(self):
        return self.__codigoVenda
    
    def getDataVenda(self):
        return self.__dataVenda

    def getCliente(self):
        return self.__cliente
    
    def getBebida(self):
        return self.__cerveja
    
    def getQtdComprada(self):
        return self.__qtdComprada

    def Apresentacao(self):
        return f'Codigo venda: {self.__codigoVenda} Data de venda: {self.__dataVenda} Codigo cliente: {self.__cliente} Codigo bebida: {self.__cerveja} Quantidade comprada: {self.__qtdComprada}'
import os
from Pessoa import Pessoa
from Bebida import Bebida
from Venda import Venda

class Arquivo:
    def GravarPessoa(pessoa : Pessoa):
        arquivo = f'{pessoa.getCodigo()},{pessoa.getCpf()},{pessoa.getNomeCompleto()},{pessoa.getDataNasc()},{pessoa.getEstado()},{pessoa.getCidade()},{pessoa.getEstado()},{pessoa.getCep()},{pessoa.getBairro()},{pessoa.getRua()},{pessoa.getNumeroCasa()},{pessoa.getComplemento()}\n'
        f = open('Dados/Pessoa.txt','a')
        f.write(arquivo)   
        f.close()

    def LerPessoas():
        f = open('Dados/Pessoa.txt', 'r')

        retorno = []

        for x in f:
            temp = x.strip().split(',')
            pessoa = Pessoa(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8], temp[9], temp[10]) 
            retorno.append(pessoa)

        f.close()

        return retorno 

    def GravarBebida(bebida : Bebida):
        arquivo = f'{bebida.getCodigo()},{bebida.getNomeBebida()},{bebida.getTipoBebida()},{bebida.getVolBebida()},{bebida.getPrecoUnitario()}'

        f = open('Dados/Bebida.txt', 'a')
        f.write(arquivo)
        f.close()

    def LerBebida():
        f = open('Dados/Bebida.txt', 'r')

        retorno = []

        for i in f:
            temp = i.strip().split(',')
            bebida = Bebida(temp[0], temp[1], temp[2], temp[3], temp[4])
            retorno.append(bebida)

        f.close()

        return retorno

    def GravarVenda(venda : Venda):
        arquivo = f'{venda.getCodigoVenda()},{venda.getDataVenda()},{venda.getCliente()},{venda.getBebida()},{venda.getQtdComprada()}\n'
        f = open('Dados/Compra.txt', 'a')
        f.write(arquivo)
        f.close()

    def LerVenda():
        f = open('Dados/Compra.txt', 'r')

        retorno = []

        for i in f:
            temp = i.strip().split(',')
            venda = Venda(temp[0],temp[1],temp[2],temp[3], temp[4])
            retorno.append(venda)

        f.close()

        return retorno

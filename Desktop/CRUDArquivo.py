import os
from Pessoa import Pessoa
from Bebida import Bebida

class Arquivo:
    def GravarPessoa(pessoa : Pessoa):
        if not os.path.isdir('Desktop/Dados'): 
            os.mkdir('Desktop/Dados')

        arquivo = f'{pessoa.getCodigo()},{pessoa.getCpf()},{pessoa.getNomeCompleto()},{pessoa.getDataNasc()},{pessoa.getEstado()},{pessoa.getCidade()},{pessoa.getEstado()},{pessoa.getCep()},{pessoa.getBairro()},{pessoa.getRua()},{pessoa.getNumeroCasa()},{pessoa.getComplemento()}\n'
        f = open('Desktop/Dados/Pessoa.txt','a')
        f.write(arquivo)   
        f.close()

    def LerPessoas():
        f = open('Desktop/Dados/Pessoa.txt', 'r')

        retorno = []

        for x in f:
            temp = x.strip().split(',')
            pessoa = Pessoa(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8], temp[9], temp[10]) 
            retorno.append(pessoa)

        f.close()

        return retorno 

    def GravarBebida(bebida : Bebida):
        if not os.path.isdir('Desktop/Dados'): 
            os.mkdir('Desktop/Dados')

        arquivo = f'{bebida.getCodigo()},{bebida.getNomeBebida()},{bebida.getTipoBebida()},{bebida.getVolBebida()},{bebida.getPrecoUnitario()}'

        f = open('Desktop/Dados/Bebida.txt', 'a')
        f.write(arquivo)
        f.close()

    def LerBebida():
        f = open('Desktop/Dados/Bebida.txt', 'r')

        retorno = []

        for i in f:
            temp = i.strip().split(',')
            bebida = Bebida(temp[0], temp[1], temp[2], temp[3], temp[4])
            retorno.append(temp)

        f.close()

        return retorno
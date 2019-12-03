from Pessoa import Pessoa
from Bebida import Bebida
from RWArquivo import Arquivo

class Auxiliar:
    def exibeMenu():
        print('*' * 50,'\n')
        print('1 - Cadastrar cliente\n2 - Ver clientes cadastrados\n3 - Cadastrar produto(s)\n4 - Ver produtos cadastrados\n5 - Vendas\n6 - Relatorio de vendas\n7 - Sair\n')
        print('*' * 50)
        return int(input('Digite a opção desejada: '))

    def cadastraPessoa():
        codigo = int(input('Digite o codigo: '))
        cpf =  input('Digite o cpf: ')
        nome = input('Digite o nome completo: ')
        dataNasc = input('Digite a data de nascimento: ')
        estado = input('Digite o estado: ')
        cidade = input('Digite a cidade: ')
        cep = input('Digite o cep: ')
        bairro = input('Digite o bairro: ')
        rua = input('Digite a rua: ')
        nCasa = int(input('Digite o numero da casa: '))
        complemento = input('Digite o complemento: ')

        pessoa = Pessoa(codigo, cpf, nome, dataNasc, estado, cidade, cep, bairro, rua, nCasa, complemento)

        Arquivo.GravarPessoa(pessoa)

    def cadastraBebida():
        codigo = int(input('Digite o codigo da bebida: '))
        nome = input('Digite o nome da bebida: ')
        tipo = input('Digite o tipo da bebida: ')
        vol = input('Digite o volume da bebida: ')
        preco = float(input('Digite o preco da bebida: '))

        bebida = Bebida(codigo, nome, tipo, vol, preco)

        Arquivo.GravarBebida(bebida)

    def listarPessoas():
        pessoas = Arquivo.LerPessoas()

        for i in pessoas:
            print(i.apresentacao())

    def listarBebidas():
        bebidas = Arquivo.LerBebida()

        for i in bebidas:
            print(i.Apresentacao())
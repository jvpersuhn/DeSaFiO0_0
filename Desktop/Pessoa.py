class Pessoa:
    def __init__(self, codigo : int, cpf, nomeCompleto, dataNasc, estado, cidade, cep, bairro, rua, numeroCasa : int, complemento):
        self.__codigo = codigo
        self.__cpf = cpf
        self.__nomeCompleto = nomeCompleto
        self.__dataNasc = dataNasc
        self.__estado = estado
        self.__cidade = cidade
        self.__cep = cep
        self.__bairro = bairro
        self.__rua = rua
        self.__numeroCasa = numeroCasa
        self.__complemento = complemento

    def getCodigo(self):
        return self.__codigo
    def getCpf(self):
        return self.__cpf
    def getNomeCompleto(self):
        return self.__nomeCompleto
    def getDataNasc(self):
        return self.__dataNasc
    def getEstado(self):
        return self.__estado
    def getCidade(self):
        return self.__cidade
    def getCep(self):
        return self.__cep
    def getBairro(self):
        return self.__bairro
    def getRua(self):
        return self.__rua
    def getNumeroCasa(self):
        return self.__numeroCasa
    def getComplemento(self):
        return self.__complemento

    def apresentacao(self):
        return f'Codigo: {self.__codigo} Nome: {self.__nomeCompleto} Cpf: {self.__cpf} Data Nasc: {self.__dataNasc} Estado: {self.__estado} Cidade: {self.__estado} Cep: {self.__cep} Bairro: {self.__bairro} Rua: {self.__rua} N° casa: {self.__numeroCasa} Complemento: {self.__complemento}\n'

    def getEndereco(self):
        return f'Rua: {self.__rua} Bairro: {self.__bairro} N°: {self.__numeroCasa}'
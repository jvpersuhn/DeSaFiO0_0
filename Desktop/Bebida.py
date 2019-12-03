class Bebida:
    def __init__(self, codigo : int, nomeBebida, tipoBebida, volBebida, precoUnitario : float):
        self.__codigo = codigo
        self.__nomeBebida = nomeBebida
        self.__tipoBebida = tipoBebida
        self.__volBebida = volBebida
        self.__precoUnitario = precoUnitario

    def getCodigo(self):
        return self.__codigo

    def getNomeBebida(self):
        return self.__nomeBebida

    def getTipoBebida(self):
        return self.__tipoBebida

    def getVolBebida(self):
        return self.__volBebida

    def getPrecoUnitario(self):
        return self.__precoUnitario

    def Apresentacao(self):
        return f'Codigo: {self.__codigo} Nome: {self.__nomeBebida} Tipo de bebida: {self.__tipoBebida} Volume bebida: {self.__volBebida} Preco Unitario: {self.__precoUnitario}'
class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construyendo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extracto(self):
        print("Saldo de {} del titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def retira(self, valor):
        self.__saldo -= valor

    def transfiere(self, valor, destino):
        self.retira(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
class Cuenta:
    def __init__(self,numero,titular,saldo,agencia,limite):
        print('Creando una cuenta bancaria... {}'.format(self))
        self.__numero = numero              #Para definir un atributo privado,es poner dos guines bajos antes del atributo
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.__limite = limite

    def retira(self,valor):
        self.__saldo -= valor              #Cuando se usan en un metodo igual se poner los dos guines bajos

    def deposita(self,valor):
        self.__saldo -= valor

    def extracto(self):
        print(f'El saldo de la cuenta de {self.__titular} es: {self.__saldo}')

    def transfiere(self, valor, destino):
        self.retira(valor)                  #se le aplica un metodo a la misma instacia
        destino.deposita(valor)

    #Getters
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    #Setters
    def set_limite(self, limite):
        self.__limite = limite
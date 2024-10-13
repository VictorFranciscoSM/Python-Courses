
class Cuenta:
    def __init__(self,numero,titular,saldo,agencia,limite):
        print('Creando una cuenta bancaria')
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

cuenta1 = Cuenta(123,'Victor',2000.0,'Nu',10000.0)
cuenta1._Cuenta__saldo = 20             #para acceder a variables privadas
cuenta1.extracto()

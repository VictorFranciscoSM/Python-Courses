
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

    def transfiere(self, valor, destino):
        self.retira(valor)                  #se le aplica un metodo a la misma instacia
        destino.deposita(valor)

cuenta1 = Cuenta(123,'Victor',2000.0,'Nu',10000.0)
cuenta2 = Cuenta(427,'Arturo',1200.0,'Nu',62000.0)

cuenta1.transfiere(100.0,cuenta2)
cuenta1.extracto()
cuenta2.extracto()

#El encapsulamiento consiste en organizar nuestro código de forma eficiente, 
#agrupando funcionalidades relacionadas dentro de una clase

#La cohesión se refiere a la relación entre los elementos de una clase. 
# Es importante que los elementos de una clase estén relacionados entre sí y que tengan un propósito común.
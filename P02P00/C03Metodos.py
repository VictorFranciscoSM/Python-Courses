
class Cuenta:
    def __init__(self,numero,titular,saldo,agencia,limite):
        print('Creando una cuenta bancaria')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia
        self.limite = limite

## Creacion de metodos

    def retira(self,valor):
        self.saldo -= valor

    def deposita(self,valor):
        self.saldo -= valor

    def extracto(self):
        print(f'El saldo de la cuenta de {self.titular} es: {self.saldo}')

#self es la instacia, la referencia. por eso es para referirse a la clase Cuenta

cuenta1 = Cuenta(123,'Victor',2000.0,'Nu',10000.0)
cuenta2 = Cuenta(427,'Arturo',1200.0,'Nu',62000.0)

##Para llamar un metodo, es el Objeto.NombreDelMetodo(atributos)
cuenta1.deposita(100)
cuenta1.extracto()
cuenta1.retira(852)
cuenta1.extracto()


'''
analogia de clases y metodos
La receta es como una clase, y cada paso de la receta es como un método.
Por ejemplo, un método podría ser "mezclar los ingredientes". Este método tiene instrucciones 
específicas sobre cómo mezclar los ingredientes, como qué ingredientes usar, en qué orden y por cuánto tiempo

Para llamar a un método, simplemente lo "ejecutas" como si fuera una función. Por ejemplo, para llamar al
método "mezclar los ingredientes", escribirías algo como esto:
pastel.mezclar_ingredientes()

En Python, los métodos siempre se definen dentro de una clase y siempre toman self como primer argumento. 
self representa la instancia actual de la clase, es decir, el objeto específico al que se está aplicando el método.

NONE
En el contexto de las clases, None se utiliza para romper la conexión entre una variable y un objeto en la memoria.

Por ejemplo, si tienes una variable cuenta_1 que apunta a un objeto Cuenta en la memoria, 
y luego asignas None a cuenta_1, la variable ya no estará conectada al objeto.

cuenta_1 = Cuenta(1000) # Crea un objeto Cuenta
print(cuenta_1) # Imprime el objeto Cuenta

cuenta_1 = None # Asigna None a la variable
print(cuenta_1) # Imprime None

En este caso, el objeto Cuenta sigue existiendo en la memoria, pero ya no se puede acceder a él a través 
de la variable cuenta_1.
'''
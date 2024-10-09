class Cuenta:
    def __init__(self,numero,titular,saldo,agencia,limite):          #Creacion del constructor, al momento de construirlo esta toma el espacio de memoria donde va a quedar almacenado el objeto resultante de este llamado
        print('Creando una cuenta bancaria ')
        #atributos
        self.numero = numero                        #self espacio de memoria que va ser ocupado por la instancia donde va a quedar alamacenado el objeto o la clase
        self.titular = titular
        self.agencia = agencia
        self.limite = limite

cuenta1 = Cuenta(123,'Victor',100.0,'001',1000.0)
print(cuenta1)

print(cuenta1.numero)
print(cuenta1.titular)

'''
Constructor (__init__):

El constructor es una función especial que se ejecuta automáticamente cuando se crea una instancia de la clase.
Se utiliza para inicializar los atributos de la instancia.
Recibe como argumento self, que es una referencia a la instancia actual.
Recibe también los valores para los atributos de la cuenta (número, titular, saldo, límite y agencia).
Asigna los valores recibidos a los atributos correspondientes de la instancia.

Cuando creas una instancia de una clase, Python automáticamente crea un objeto self que apunta a esa instancia específica.

Por ejemplo, si creas una instancia de la clase Cuenta llamada cuenta_1, Python crea un objeto self que apunta a cuenta_1.
'''
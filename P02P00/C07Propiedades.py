class Cliente:
    def __init__(self, nombre, limite):
        self.__nombre = nombre
        self.__limite = limite

    @property
    def nombre(self):                   #en vez de get_nombre se pone nombre
        return self.__nombre.title()
    
    @property           # Python automáticamente llama a este método cada vez que accedemos al atributo.
    def limite(self):
        return self.__limite
    
    @nombre.setter      #antes del método setter nos permite modificar el valor del atributo.
    def nombre(self, nombre):
        self.__nombre = nombre

    @limite.setter          
    def limite(self, limite):           ##en vez de set_limite se poner limite
        self.__limite = limite

cliente = Cliente('victor', 10000)
print(cliente.nombre)
cliente.nombre = 'francisco'
print(cliente.nombre)
print(cliente.limite)
cliente.limite = 15000.0
print(cliente.limite)



'''
Al usar @property antes del método getter, Python automáticamente llama a 
este método cada vez que accedemos al atributo. De manera similar, @nombre.setter 
antes del método setter nos permite modificar el valor del atributo.

Piensa en el decorador @property como un portero de un club exclusivo. 
Tú quieres entrar al club (acceder al atributo privado), pero el portero 
(el decorador) te pide tu identificación (ejecuta el método getter) antes 
de dejarte pasar. El portero puede revisar tu identificación, hacer 
algunas verificaciones y luego decidir si te deja entrar o no.

En el caso del decorador @property, el método getter puede realizar algunas 
operaciones con el valor del atributo privado antes de devolvértelo.
'''



class Cuenta:       #Se crea una clase y la convencion en CamellCase para para los nombres
    print('La receta esta esperando a resivir instrucciones')

cuenta = Cuenta()
print(cuenta)           #es un objeto main y muesta en que espacio de la memoria esta almacena #Salida <__main__.Cuenta object at 0x000001AE9BFE5D30>
print(type(cuenta))     #es un objeto cuenta #Salida: <class '__main__.Cuenta'>

cuenta_1 = cuenta       #sera la misma instancia por lo que ocupara el mismo espacio de memoria
print(cuenta_1)

cuenta = Cuenta()

'''
 una clase es como una receta para crear un objeto. 
 La clase define las características y funcionalidades que tendrá el objeto.

En Python, creamos una clase usando la palabra reservada class 
y el nombre de la clase en CamelCase. Por ejemplo, class Cuenta:

Una instancia es un objeto creado a partir de una clase. 
Podemos crear una instancia de una clase usando el nombre de la 
clase seguido de paréntesis. Por ejemplo, cuenta = Cuenta().

Una instancia es como una galleta que se crea usando ese molde. 
Cada galleta tiene la misma forma y tamaño, pero puede tener diferentes decoraciones o sabores.

En el caso de la clase Cuenta, podemos crear varias instancias, 
cada una representando una cuenta bancaria diferente. Cada instancia 
tendrá las mismas características y funcionalidades definidas en la clase, 
pero puede tener diferentes valores para esas características (como el saldo, el titular, etc.).
Por ejemplo, podríamos crear dos instancias de la clase Cuenta:

cuenta1 = Cuenta()
cuenta2 = Cuenta()
Ambas instancias son objetos Cuenta, pero cada una tiene su propio espacio 
de memoria y sus propios valores para las características.

Cada instancia de una clase ocupa un espacio único en la memoria del ordenador.

Imagina que la memoria del ordenador es como un gran almacén con muchos estantes. 
Cada estante representa un espacio de memoria.

'''
def agregar_elemento(lista, elemento):
    lista.append(elemento)

mi_lista = [1, 2, 3]

agregar_elemento(mi_lista, 4)

print(mi_lista)  # Imprime [1, 2, 3, 4]

#estamos modificando la lista letras_acertadas directamente dentro de la función. 
# En Python, las listas son mutables, lo que significa que su contenido puede ser modificado.

#En este ejemplo, la función agregar_elemento() recibe una lista y un elemento como argumentos. 
#Dentro de la función, se utiliza el método append() para agregar el elemento a la lista.

#Aunque la función no devuelve nada explícitamente, la lista original mi_lista se modifica 
# porque se está trabajando con la referencia a la lista original.

def incrementar_errores(errores):
    return errores + 1
#En esta función, se recibe el valor actual de errores como argumento y se retorna el valor incrementado en 1.
#Luego, en tu código principal, podrías usar la función de esta manera:

errores = 0
errores = incrementar_errores(errores)
#De esta forma, la variable errores se actualiza con el nuevo valor retornado por la función.

#diferencia de las listas que son mutables, las variables simples como los números o las cadenas de texto son inmutables. 
# Esto significa que no puedes modificarlas directamente dentro de una función.


#Las variables mutables en Python, como las listas, diccionarios y conjuntos, no necesitan ser retornadas explícitamente por una función porque trabajan con referencias.

#Cuando pasas una variable mutable a una función, en realidad estás pasando una referencia a la ubicación 
# de la variable en la memoria. Cualquier cambio que hagas a la variable dentro de la función se reflejará 
# en la variable original.

#as variables inmutables, como los números, cadenas de texto y tuplas, no funcionan de esta manera. Si necesitas modificar una variable inmutable dentro de una función, 
# debes retornar el nuevo valor para que se actualice la variable original.
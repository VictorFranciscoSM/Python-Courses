
frutas = ['Manzana', 'Banana', 'Uva', 'Fresa']

print(frutas)
print(frutas[1])                #Accedes al elemto del indice
frutas[3] = 'Mango'             #modificas el elemento en el indice indicado
print(frutas)  
frutas.append("Banana")         #se agrega un elmento al final de la lista
print(frutas)
frutas.remove('Banana')         #elimana la primera aparicion del elemento 
print(frutas)
for fruta in frutas:            #la lista es iterable por lo que se puede poner en un for
    print(fruta)
frutas.insert(2,'Pera')         #inseta el elmeneto en el posicion 2
print(frutas)
print(frutas.pop())             #elimina el elemento de la posicion indicada, el default es la ultima posicion
print(frutas.index('Uva'))      #retorna en que posicion esta el elemento
print(frutas.count('Banana'))   #cuanta cuantas veces esta el elemento en la lista

numeros1 = [5,8,7,9,2]
numeros = [5, 2, 8, 1, 9]
numeros.sort()                  #modifica la lista original en orden,pero no regresa nada por eso el comando va en una linea
print(numeros)

numeros.reverse()               #modifica la lista original en orden,pero no regresa nada por eso el comando va en una linea
print(numeros) 

numeros.extend(numeros1)        #agrega la lista2 iterable a la primera lista, pero no regresa nada poer eso el comando va en una linea
print(numeros) 

print(frutas.clear())

num = [1, 4, 5, 6]
reversed_num = list(reversed(num))      #retorna una lista modifica de la lista num
print(reversed_num)  # Salida: [6, 5, 4, 1]
print(num)  # Salida: [1, 4, 5, 6]


frutas = ['Manzana', 'Banana', 'Uva', 'Fresa']
lista= []
for fruta in frutas:
    lista.append('_')
print(lista)
lista1 = ['_' for letra in frutas]      #se pueden crear una lista con otra lista por medio del for in
print(lista1)

enteros = [1,3,4,5,7,8]
cuadrado = [n*n for n in enteros]
print(cuadrado)

enteros = [1,3,4,5,7,8,9]
pares = []
for numero in enteros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

pares.clear()
pares = [x for x in enteros if x % 2 == 0]
print(pares)
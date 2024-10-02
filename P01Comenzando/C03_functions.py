#Function range ciclo de lazo con for

for numero in range(5):
    print(numero)

for numero in range(1,6):
    print(numero)

for numero in range(1,10,2):
    print(numero)

print("Intento {} de {}".format(1,3))
print("Intento {1} de {0}".format(1,3))             #Para decidir en que espacio ira cada varible se hara por su posicion dentro de .format
"Intento {1} de {0}".format(1,3)                    #No es necesario tener la funcion print para imprimir un str usando el .format
"$ {:f}".format(5.56)

print("Intento {1} de {0}".format(1,3))
print("$ {:f}".format(5.5645))              #para mostrar el valor como un tipo flotante
print("$ {:.2f}".format(5.5645))            #para indicar cuantas numeros decimales se mostraran
print("$ {:5.2f}".format(5.5645))           #para indicar que se mostraran un espacios en blanco y 4 digitos depues
print("$ {:7.2f}".format(5.5645))           #para indicar que se mostraran tres espacios en blanco y 4 digitos depues
print("$ {:07.2f}".format(5.5645))          #para indicar que se mostraran 3 ceros al imicio y 4 digitos depues

print("El numero {:7d}".format(46))         #Muestra 7 espacios, 5 en blanco y los dos numeros
print("El numero {:07d}".format(46))         #Muestra 7 espacios, 5 en 0 y los dos numeros
print("Fecha:{:2d}/{:2d}".format(5,5))
print("Fecha:{:02d}/{:02d}/20{:2d}".format(5,5,24))        




#Tuplas Secuencia inmuables
dias = ('l','m','m','j','v','s','d')
type(dias)

print(len(dias))
print(dias[1])
print(dias.count("m"))
print(dias.index('s'))
#   dias.pop()      no tiene este atributo y no pueden ser modificadas las tuplas

punto1 = (3,5)
punto2 = (4,5)
punto3 = (4,8)
instructor1 = ('Victor', 26)
instructor2 = ('Nicole', 27)
instructores = [instructor1,instructor2]

lista = [punto1,punto2,punto3]          # se pueden almacenar tuplas en una lista
print(lista[1])         
print(lista[1][1])                      #pedemos acceder a los valores de la tupla podiendo [indice] que quieras 

print(instructores[1][0])

print(type(instructor1))
instructor1= list(instructor1)          #se convierte una tupla a una lista
print(type(instructor1))
instructores = tuple(instructores)      #Convierte la lista a tupla
print(type(instructores))               

print("**********")
print("Adivina el numero")
print("**********")

#la funcion input("str") muestra un string en la terminal y se almacena lo introducido en la asocioado
guess = 25
valor_str = input("introduce un numero: ")  #sera un valor str
valor_int = int(valor_str)
print("Tu numero fue: ", valor_int)

acierto = guess == valor_int
mayor = valor_int > guess
menor = valor_int < guess

#La identacion en python es omportante ya que si no se usa, marca error
if(acierto):
    print("Adivinaste")
else:
    if(mayor):
        print("El numero es mayoy")
    elif(menor):
        print("El numero es menor")
    print("Intentalo de nuevo")

print("El juego a concluido")
print(type(valor_int), type(valor_str))






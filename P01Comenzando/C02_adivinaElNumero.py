
print("**********")
print("Adivina el numero")
print("**********")

#la funcion input("str") muestra un string en la terminal y se almacena lo introducido en la asocioado
guess = 25
valor_str = input("introduce un numero: ")  #sera un valor str
valor_int = int(valor_str)
print("Tu numero fue: ", valor_int)

#La identacion en python es omportante ya que si no se usa, marca error
if(guess == valor_int):
    print("Adivinaste")
else:
    print("Intentalo de nuevo")

print("El juego a concluido")
print(type(valor_int), type(valor_str))






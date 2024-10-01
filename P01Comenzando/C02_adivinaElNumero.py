
print("**********")
print("Adivina el numero")
print("**********")

#la funcion input("str") muestra un string en la terminal y se almacena lo introducido en la asocioado
guess = 25
total_intentos = 3
intento = 1
valor_int = 0

for intento in range(1,4):
    #print("Intento {} de {}".format(intento, total_intentos))
    print(f"Intento {intento} de {total_intentos}")
    valor_str = input("introduce un numero: ")  #sera un valor str
    valor_int = int(valor_str)

    if (valor_int <1 or valor_int >100):
        print("Digita un nnumero mayor que 0 y menor que 100")
        continue    #se salta a la siguiente iteration cuando entra, ya que no sirve que evalue lo siguiente

    print("Tu numero fue: ", valor_int)

    acierto = guess == valor_int
    mayor = valor_int > guess
    menor = valor_int < guess

    #La identacion en python es omportante ya que si no se usa, marca error
    if(acierto):
        print("Adivinaste")
        break   #una vez que se ejectura se rompe el ciclo donde se encuentre
    else:
        if(mayor):
            print("El numero es mayor")
        elif(menor):
            print("El numero es menor")
        print("Intentalo de nuevo")

print("El juego a concluido")








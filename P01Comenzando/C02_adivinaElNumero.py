import random

intento = 1
valor_int = 0

print("***********************************")
print("*********Adivina el numero*********")
print("***********************************")
print("Elige el nivel de dificultad")
print("(1)Novato (2)Intermedio (3)Avanzado")

dificultad = 0
while(dificultad > 3 or dificultad < 1):
 dificultad = int(input("Introduce la difultad "))
 if(dificultad > 3 or dificultad < 1) == True:
     print("Ingresa una dificultad valida")

if dificultad == 1:
    total_intentos = 20
elif dificultad == 2:
    total_intentos = 10
else:
    total_intentos = 5

#guess = round(random.random() * 100)    #primero nos da unnuemro del 0 al 1 y despues la redondea
guess = random.randint(1,100)
print("El nuemro secreto es: ", guess)
puntos = 1000

for intento in range(1,total_intentos + 1):                       #range genera un rangp de numeros secuenciales
    #print("Intento {} de {}".format(intento, total_intentos))
    print(f"Intento {intento} de {total_intentos}")
    valor_str = input("introduce un numero: ")  #sera un valor str
    valor_int = int(valor_str)

    if (valor_int <1 or valor_int >100):
        print("Digita un numero mayor que 0 y menor que 100")
        continue    #se salta a la siguiente iteration cuando entra, ya que no sirve que evalue lo siguiente

    print("Tu numero fue: ", valor_int)

    acierto = guess == valor_int
    mayor = valor_int > guess
    menor = valor_int < guess

    #La identacion en python es omportante ya que si no se usa, marca error
    if(acierto):
        print("Adivinaste")
        print(f"Has acertado el numero es {guess}, tu puntaje es {puntos}")
        break   #una vez que se ejectura se rompe el ciclo donde se encuentre
    else:
        if(mayor):
            print("El numero es mayor")
        elif(menor):
            print("El numero es menor")
        print("Intentalo de nuevo")
        puntosPerdidos = abs(valor_int - guess)
        puntos = puntos - puntosPerdidos

print("El juego a concluido")








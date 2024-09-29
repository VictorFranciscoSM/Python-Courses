#Para subirlo al repo se necesitan los comando de git
print("**********")
print("Adivina el numero")
print("**********")

guess = 25
valor = input("intriduce un numero")
print("Tu numero fue: ", valor)

if(guess == int(valor)):
    print("Adivinaste")
else:
    print("Intentalo de nuevo")

edad1 = 10
edad2 = "20"
print(edad1, edad2, edad1 + int(edad2))
producto = edad1 * edad2
print(producto)
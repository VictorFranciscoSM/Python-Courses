def jugar():
    print("***********************************")
    print("************El Ahorcado************")
    print("***********************************")
    print("Biemvemido al juego el Ahorcado")

    secretWord = "banana" 
    ahorco = False
    acerto = False
    tamano = len(secretWord)
    lista_vacia = [None]*tamano

    i=0
    longitud = 2
    while (not ahorco and not acerto) and i < tamano:
        while longitud > 1:
            intento = input("Digita una letra: ")
            longitud = len(intento)
            if(longitud != 1):
                print("Ingresa solo una letra")
        indice = 0
        for letra in secretWord:
            print(letra)
            if letra == intento:
                print(f"Entoncre la letra '{letra}', en la posicion {indice}")
                lista_vacia[indice] = letra
            indice +=1
        i += 1    


if(__name__ == "__main__"):
    jugar()
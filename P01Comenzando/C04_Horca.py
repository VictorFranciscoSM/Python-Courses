def jugar():
    print("***********************************")
    print("************El Ahorcado************")
    print("***********************************")
    print("Biemvemido al juego el Ahorcado\n")

    secretWord = "banana" 
    secretWord = secretWord.strip()               #Elimana todos los espacios dentro del string
    ahorco = False
    acerto = False
    tamano = len(secretWord)
    lista_vacia = ["_"]*tamano                   #Multiplica la lista ["_"] por un cierto valor y regresa la lista con ese valor en los elemntos
    print(lista_vacia)

    i=0
    while (not ahorco and not acerto) and i < tamano:
        longitud = 2
        while longitud > 1:
            intento = input("\nDigita una letra: ")
            intento = intento.strip()               #Elimina todos los espacios dentro del string
            #intento = intento.lower()               #Covierte todos los caracteres a minusculas
            #intento = intento.upper()               #Covierte todos los caracteres a mayusculas
            longitud = len(intento)
            if(longitud != 1):
                print("Ingresa solo una letra")

        indice = 0
        for letra in secretWord:
            #print(letra)
            if letra.upper() == intento.upper():
                #print(f"Entoncre la letra '{letra}', en la posicion {indice}")
                lista_vacia[indice] = letra.upper()
            indice +=1
        print(lista_vacia)
        i += 1  
        if("_" not in lista_vacia):
            i = len(secretWord)
    if("_" in lista_vacia):
        print("Perdiste")
    else:
        print("Has completado el juego")
    print(lista_vacia)

if(__name__ == "__main__"):
    jugar()

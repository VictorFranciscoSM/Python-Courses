def jugar():
    print("***********************************")
    print("************El Ahorcado************")
    print("***********************************")
    print("Bienvenido al juego del Ahorcado adivina la siguiente palabra\n")

    secretWord = "banana".upper()
    secretWord = secretWord.strip()               #Elimana todos los espacios dentro del string
    ahorco = False
    acerto = False
    tamano = len(secretWord)
    lista_vacia = ["_"]*tamano                   #Multiplica la lista ["_"] por un cierto valor y regresa la lista con ese valor en los elemntos
    print(lista_vacia,"\n")

    errores=0
    while not ahorco and not acerto:
        print(f"\nIntento {errores+1}")
        longitud = 2
        while longitud > 1:
            intento = input("\nDigita una letra: ")
            intento = intento.strip()               #Elimina todos los espacios dentro del string
            #intento = intento.lower()               #Covierte todos los caracteres a minusculas
            intento = intento.upper()               #Covierte todos los caracteres a mayusculas
            longitud = len(intento)
            if(longitud != 1):
                print("Ingresa solo una letra")

        if intento in secretWord:
            indice = 0
            for letra in secretWord:
                #print(letra)
                if letra == intento:
                    #print(f"Entoncre la letra '{letra}', en la posicion {indice}")
                    lista_vacia[indice] = letra
                indice +=1
        else:
            errores += 1
            print("\nHas fallado, quedan {} intentos." .format(tamano-errores))
            ahorco = errores == tamano       

        print("\n",lista_vacia)    
        letras_faltantes = str(lista_vacia.count('_'))
        acerto = "_" not in lista_vacia
        if ahorco:
            print("\nPerdiste el juego")
            print("\nFaltantan acertar {} letras" .format(letras_faltantes))
        elif acerto:
            print("\nHas completado el juego")

if(__name__ == "__main__"):
    jugar()

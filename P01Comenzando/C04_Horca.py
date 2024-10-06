import random
def jugar():
    print("***********************************")
    print("************El Ahorcado************")
    print("***********************************")
    print("Bienvenido al juego del Ahorcado adivina la siguiente palabra\n")

    #archivo = open("C:/Users/VictorFSM/Desktop/Cursos One/Python-Courses/P01Comenzando/palabra.txt", 'r')   #Las comillas dobles (" ") son necesarias para indicar a Python que la ruta completa es un 
                                                        #solo string, incluso si contiene espacios.
                                                        #Si no se usan las comillas dobles, Python interpretará cada espacio como el final de un string,
                                                        # lo que genera un error.

    #palabras = [linea.strip() for linea in archivo]     #crea una lista tomando como valor cada linea, con el strip evitamos el caracter \n
    #archivo.close()
    with open("C:/Users/VictorFSM/Desktop/Cursos One/Python-Courses/P01Comenzando/palabra.txt", 'r') as archivo:
        palabras = [linea.strip() for linea in archivo]     #crea una lista tomando como valor cada linea, con el strip evitamos el caracter \n

    i = random.randrange(0,len(palabras))
    secretWord = palabras[i].upper()
    secretWord = secretWord.strip()               #Elimana todos los espacios dentro del string
    ahorco = False
    acerto = False
    tamano = len(secretWord)
    #lista_vacia = ["_"]*tamano                   #Multiplica la lista ["_"] por un cierto valor y regresa la lista con ese valor en los elemntos
    lista_vacia = ["_" for letra in secretWord]
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

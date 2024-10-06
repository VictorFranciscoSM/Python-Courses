import random
def jugar():

    imprime_presentacion()    
    secretWord = cargar_palabra()
    lista_vacia = inicializa_lista(secretWord)
    print(lista_vacia,"\n")

    ahorco = False
    acerto = False
    tamano = len(secretWord) 
    errores=0

    while not ahorco and not acerto:
        print(f"\nIntento {errores+1}")
        intento = pide_intento()
        if intento in secretWord:
            marca_intento_correcto(intento,secretWord,lista_vacia)
        else:
            errores = marca_intento_incorrecto(tamano,errores)

        print("\n",lista_vacia)    
        letras_faltantes = str(lista_vacia.count('_'))
        ahorco = errores == tamano
        acerto = "_" not in lista_vacia
        if ahorco:
            print("\nPerdiste el juego")
            print("\nFaltantan acertar {} letras" .format(letras_faltantes))
        elif acerto:
            print("\nHas completado el juego")


def imprime_presentacion():
        print("***********************************")
        print("************El Ahorcado************")
        print("***********************************")
        print("Bienvenido al juego del Ahorcado adivina la siguiente palabra\n")

def cargar_palabra():     
    #archivo = open("C:/Users/VictorFSM/Desktop/Cursos One/Python-Courses/P01Comenzando/palabra.txt", 'r')   #Las comillas dobles (" ") son necesarias para indicar a Python que la ruta completa es un 
                                                            #solo string, incluso si contiene espacios.
                                                            #Si no se usan las comillas dobles, Python interpretará cada espacio como el final de un string,
                                                            # lo que genera un error.

    #palabras = [linea.strip() for linea in archivo]     #crea una lista tomando como valor cada linea, con el strip evitamos el caracter \n
    #archivo.close()
    with open("C:/Users/VictorFSM/Desktop/Cursos One/Python-Courses/P01Comenzando/palabra.txt", 'r') as archivo:
        palabras = [linea.strip() for linea in archivo]     #crea una lista tomando como valor cada linea, con el strip evitamos el caracter \n
    i = random.randrange(0,len(palabras))
    secretWord = palabras[i].upper().strip()
    return secretWord

def inicializa_lista(palabra):
    #lista_vacia = ["_"]*tamano                   #Multiplica la lista ["_"] por un cierto valor y regresa la lista con ese valor en los elemntos
    lista_vacia = ["_" for letra in palabra]
    return lista_vacia

def pide_intento():
    longitud = 2
    while longitud > 1:
        intento = input("\nDigita una letra: ")
        #intento = intento.strip()               #Elimina todos los espacios dentro del string
        #intento = intento.lower()               #Covierte todos los caracteres a minusculas
        #intento = intento.upper()               #Covierte todos los caracteres a mayusculas
        intento = intento.strip().upper()
        longitud = len(intento)
        if(longitud != 1):
            print("Ingresa solo una letra")
    return intento

#Cuando pasamos lista_vacia como argumento a la función, 
#en realidad estamos pasando una referencia a la lista original. 
#Dentro de la función, cuando agregamos un nuevo elemento a 
#lista_vacia, estamos modificando la lista original, no creando una copia.
#por eso no es necesario que la retornemos
def marca_intento_correcto(intento,secretWord,lista_vacia):
    indice = 0
    for letra in secretWord:
        #print(letra)
        if letra == intento:
            #print(f"Entoncre la letra '{letra}', en la posicion {indice}")
            lista_vacia[indice] = letra
        indice +=1


def marca_intento_incorrecto(tamano,errores):
    errores += 1
    print("\nHas fallado, quedan {} intentos." .format(tamano-errores))
    return errores

if(__name__ == "__main__"):
    jugar()

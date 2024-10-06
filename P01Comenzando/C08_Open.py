#archivo = open('palabra.txt', 'w')      #Si el arhivo no esta creado lo crea y en formato de escritura
                                        #w es de write
                                        #a es de append 
                                        #r es de read
#imagen('logo.png', 'rb')               #b  para trabajar en modo binario, para abrir imagen
                                    


#archivo.write('uva\n')                    #metodo para escribir dentro del archivo
#archivo.write('banana\n')
#archivo.close()                         #Cierra el archivo guardando las modifaciones, si no se cierra no se podra usar en el futuro

#archivo = open('palabra.txt', 'a')
#archivo.write('fresa\n')
#archivo.write('manzana\n')
#archivo.close() 

archivo = open('P01Comenzando\palabra.txt', 'r')
#print(archivo.read())               #si se usa la terminal con arhivo.read() mostraria todo junto y mostrando los \n
#linea = archivo.readline()          #extrar la primara linea del arhivo, por lo que se extrae 'uva\n'
#print(linea)

for linea in archivo:               #toma liena por linea hasta que llegue al final ej. "uva\n"
    print(linea)

print(linea.strip())                #como tambien toma el salto de linea tenemos que poner strip apra quitarselo

archivo.close() 

#Con with, Python se encarga de cerrar el archivo automáticamente, incluso si ocurre un error
with open("palabra.txt") as archivo:    #Esto significa que estamos abriendo el archivo "palabras.txt" y asignándolo a la variable archivo
  for linea in archivo:
    print(linea)

#with open("palabras.txt", 'w') as archivo:
'''
open(nombre_archivo, modo): Esta función es la base para trabajar con archivos.

nombre_archivo: Es el nombre del archivo que quieres abrir.
modo: Indica cómo quieres trabajar con el archivo:
"r": Lectura (solo lectura).
"w": Escritura (sobreescribe el archivo si existe o lo crea si no existe).
"a": Añadir (agrega contenido al final del archivo).
"x": Creación (crea un archivo nuevo, si ya existe, lanza un error).
"b": Binario (para archivos binarios).
"t": Texto (para archivos de texto).
"r+": Lectura y escritura (abre el archivo para lectura y escritura).
"w+": Escritura y lectura (sobreescribe el archivo si existe o lo crea si no existe).
"a+": Añadir y lectura (agrega contenido al final del archivo).
read(): Lee todo el contenido del archivo como una única cadena de texto.
        La función read() lee todo el archivo de una vez, colocando el puntero 
        de lectura al final del mismo. Si llamamos a la función read() nuevamente, 
        como el puntero de lectura está al final, no se leerá nada.
        Si deseamos leer el archivo nuevamente, debemos cerrarlo con el comando close(), 
        abrirlo nuevamente con el comando open() y luego podremos leerlo completo nuevamente.

readline(): Lee una sola línea del archivo.

readlines(): Lee todas las líneas del archivo y las devuelve como una lista.

write(contenido): Escribe el contenido especificado en el archivo.

close(): Cierra el archivo. Es importante cerrar los archivos después de usarlos para liberar recursos.

seek(posición): Mueve el puntero de lectura o escritura a una posición específica dentro del archivo.

tell(): Devuelve la posición actual del puntero de lectura o escritura.

truncate(tamaño): Trunca el archivo a un tamaño específico.

import os

os.remove(nombre_archivo): Elimina un archivo.

os.rename(nombre_archivo_original, nuevo_nombre_archivo): Renombra un archivo.

os.path.exists(nombre_archivo): Verifica si un archivo existe.

os.path.isfile(nombre_archivo): Verifica si un archivo es un archivo regular (no un directorio).

os.path.isdir(nombre_archivo): Verifica si un archivo es un directorio.

os.path.getsize(nombre_archivo): Devuelve el tamaño del archivo en bytes.

os.path.abspath(nombre_archivo): Devuelve la ruta absoluta del archivo.

os.path.join(ruta, nombre_archivo): Une una ruta y un nombre de archivo para crear una ruta completa.

# Solicita al usuario que ingrese la ruta del archivo
path = input("Ingresa la ruta del archivo: ")

# Verifica si la ruta es válida
if os.path.exists(path):
    # Abre el archivo
    archivo = open(path, "r")
    # Procesa el archivo
    # ...
    archivo.close()
else:
    print("La ruta ingresada no es válida.")
'''
import C04_Horca                        #para importar arhivos a otro archivo se sa el import coon el nombre del archivo
import C02_adivinaElNumero

print("***********************************")
print("*********Juegos de python**********")
print("***********************************")
print("(1)La Horca (2)Adivinanza")
juego = 0
while juego > 2 or juego < 1:
    juego= int(input("Selecciona el juego que deseas: "))
    if juego > 2 or juego < 1:
        print("Introduce un juego valido")

if juego == 1:
    print("Juego de la Horca")
    C04_Horca.jugar()
elif juego == 2:
    print("Juego de adivinanza")
    C02_adivinaElNumero.jugar()

#from fechas import Fecha

class Fechas:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def fromatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')


f = Fechas(21,11,2022)
f.fromatada()

'''
from fechas import Fecha: Esta línea importa la clase Fecha del módulo fechas.
from: Esta palabra clave indica que estás importando algo de otro archivo.
fechas: Este es el nombre del archivo o módulo que contiene la clase Fecha.
import Fecha: Esta parte indica que estás importando específicamente la clase Fecha del módulo fechas.
'''
class Cliente:
    def __init__(self, nombre, limite):
        self.__nombre = nombre
        self.__limite = limite

    @property
    def nombre(self):
        return self.__nombre.title()
    
    @property
    def limite(self):
        return self.__limite
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
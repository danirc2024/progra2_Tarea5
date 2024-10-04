class Asignatura:
    __contador_asignaturas=0

    def __init__(self, nombre, codigos, creditos):
        self.__nombre= nombre
        self.__codigos= codigos
        self.__creditos= creditos
        Asignatura.__contador_asignaturas+=1

    def __str__(self):
        mostrar_info= f"La asignatura {self.__nombre} {self.__codigos}, con una cantidad de {self.__creditos} créditos" 
        return mostrar_info
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def codigos(self):
        return self.__codigos
    
    @property
    def creditos(self):
        return self.__creditos
    
materia1= Asignatura("Topicos", 1001, 6)
print(materia1)

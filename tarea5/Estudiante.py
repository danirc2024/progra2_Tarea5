from Persona import Persona

class Estudiante(Persona):
    __contador_estudiante= 0

    def __init__(self, nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__matricula= matricula
        self.__carrera= carrera
        self.__semestre= semestre
        Estudiante.__contador_estudiante+=1

    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def carrera(self):
        return self.__carrera
    
    @property
    def semestre(self):
        return self.__semestre
    
    def estudiar(self, materia, horas):
        return f"El estudiante ha estudiado {materia} durante {horas} horas"
     
    def __str__(self):
        presentacion = (f"Yo soy {self.nombre} {self.apellido}, nací el {self.fecha_nacimiento}, "
                        f"con matrícula {self.__matricula}, en la carrera de {self.__carrera} y en el semestre {self.__semestre}")
        return presentacion
    
    @classmethod
    def get_cantidad_estudiantes(cls):
        return cls.__contador_estudiante
    
est1 = Estudiante("Juan", "Pérez", "01-01-2000", "123456", "Ingeniería", 3)

resultado = est1.estudiar("mate", 2)
print(resultado)  
print(est1)

print(f"Cantidad de estudiantes: {Estudiante.get_cantidad_estudiantes()}")
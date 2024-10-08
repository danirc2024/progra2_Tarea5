from Persona import Persona

class Profesor(Persona):
    __contador_profesores=0
    def __init__(self, nombre, apellido, fecha_nacimiento, numero_empleado, departamento):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__numero_empleado= numero_empleado
        self.__departamento= departamento
        Profesor.__contador_profesores+=1

    def ensenar(self,materia):
        return f"El profesor {self.nombre} {self.apellido} enseña {materia}"
    
    def __str__(self):
        presentación= (f"Profesor {self.nombre} {self.apellido}, nacido el {self.fecha_nacimiento}."
                       f"Empleado número {self.__numero_empleado} y del departamento de {self.__departamento}")
        return presentación
    
    @property
    def numero_empleado(self):
        return self.__numero_empleado
    
    @property
    def departamento(self):
        return self.__departamento
    
    @classmethod
    def get_cantidad_profesores(cls):
        return cls.__contador_profesores
    

profesor1= Profesor("Christopher", "Morgan", "30-09-1990", 4, "Matematicas")
print(profesor1)
print(profesor1.ensenar("Algebra"))
print(f"Cantidad de profesores: {Profesor.get_cantidad_profesores()}")

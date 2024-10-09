from Asignatura import Asignatura
from Profesor import Profesor
from Estudiante import Estudiante

class Grupo:
    __contador_grupos=0

    def __init__(self, numero_grupo, asignatura, profesor):
        self.__numero_grupo= numero_grupo
        self.__asignatura= asignatura
        self.__profesor= profesor
        self.__estudiantes= []
        Grupo.__contador_grupos+=1

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
            print(f"Estudiante {estudiante} agregado correctamente.")
        else:
            print( f"El estudiante {estudiante} ya está en el grupo")

    def eliminar_estudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.matricula == matricula:
                self.__estudiantes.remove(estudiante)
                print(f"Estudiante {matricula} eliminado correctamente.")
                return 
        print(f"No se encontró un estudiante con matrícula {matricula} en la sección")

    def __str__(self):
        mostrar_grupo = (f"Grupo número: {self.__numero_grupo}\n"
                         f"La asignatura: {self.__asignatura}\n"
                         f"Profesor: {self.__profesor}\n"
                         f"Estudiantes:\n" + "\n".join(str(estudiante) for estudiante in self.__estudiantes))
        return mostrar_grupo


    @property
    def numero_grupo(self):
        return self.__numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, numero_grupo):
        self.__numero_grupo = numero_grupo

    @property
    def asignatura(self):
        return self.__asignatura

    @asignatura.setter
    def asignatura(self, asignatura):
        self.__asignatura = asignatura

    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    @property
    def estudiantes(self):
        return self.__estudiantes

asignatura = Asignatura("Matemáticas", "MAT101", 3)
profesor = Profesor("Juan", "Pérez","10-10-1990", 32, "Matemáticas")
grupo1 = Grupo(1, asignatura, profesor)

estudiante1 = Estudiante("Maria","Gonzales","01-01-2001", "2023-123", "Ingeniería", 1)
estudiante2 = Estudiante("Carlos", "Vazques", "21-12-2000", "2023-456", "Ingeniería", 2)

# Agregar estudiantes
grupo1.agregar_estudiante(estudiante1)
grupo1.agregar_estudiante(estudiante2)
print(grupo1)

# Eliminar un estudiante
grupo1.eliminar_estudiante("2023-123")

print(grupo1)

from Grupo import Grupo

class ProgramaAcademico:
    __contador_programas=0

    def __init__(self, nombre, codigo):
        self.__nombre= nombre
        self.__codigo= codigo
        self.__grupos= []
        ProgramaAcademico.__contador_programas+=1

    def agregar_grupo(self, grupo):
        # Validación para evitar grupos duplicados
        for g in self.__grupos:
            if g.numero_grupo == grupo.numero_grupo:
                print(f"El grupo número {grupo.numero_grupo} ya está en el programa.")
                return
        self.__grupos.append(grupo)
        print(f"Grupo número {grupo.numero_grupo} agregado correctamente al programa.")

    def eliminar_grupo(self, numero_grupo):
        # Verificación de existencia del grupo
        for grupo in self.__grupos:
            if grupo.numero_grupo == numero_grupo:
                self.__grupos.remove(grupo)
                print(f"Grupo número {numero_grupo} eliminado correctamente.")
                return
        print(f"No se encontró el grupo número {numero_grupo} en el programa.")

    def mostrar_programa(self):
        # Muestra la información completa del programa, incluyendo los grupos
        print(f"Programa Académico: {self.__nombre} ({self.__codigo})")
        if not self.__grupos:
            print("No hay grupos registrados en este programa.")
        else:
            for grupo in self.__grupos:
                print(grupo)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def grupos(self):
        return self.__grupos
    
# Creación del programa académico
programa = ProgramaAcademico("Ingeniería Informática", "INF-2024")

# Creación de grupos
grupo1 = Grupo(101, "Programación II", "Prof. García")
grupo2 = Grupo(102, "Bases de Datos", "Prof. Pérez")

# Agregar grupos al programa
programa.agregar_grupo(grupo1)
programa.agregar_grupo(grupo2)

# Mostrar información del programa
programa.mostrar_programa()

# Eliminar un grupo
programa.eliminar_grupo(101)

# Mostrar nuevamente la información del programa
programa.mostrar_programa()


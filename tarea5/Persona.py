class Persona:
    __contador_personas= 0

    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.__nombre= nombre
        self.__apellido= apellido
        self.__fecha_nacimiento= fecha_nacimiento
        Persona.__contador_personas+=1

    def __str__(self):
        presentacion= f"Yo soy {self.__nombre} {self.__apellido} nací el {self.__fecha_nacimiento}"
        return presentacion
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    
    @classmethod
    def get_cantidad_personas(cls):
        return cls.__contador_personas

    

persona1= Persona("Daniela", "Romero", "19-10-2005" )
print(persona1)
persona2=Persona("Meliza", "Salas", "14-11-2004")
print(persona2)
persona3= Persona("Maycool", "Arevalo", "05-11-2005")
print(persona3)
        
print(f"Cantidad de personas: {Persona.get_cantidad_personas()}")        
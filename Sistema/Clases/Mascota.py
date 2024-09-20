class Mascota():
    """Clase de  mascota"""

    def __init__(
            self, nombre:str, tipo:str, edad:int, estado_salud:str, raza:str, disponible:bool
        ):
        """Constructor de la clase"""
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.raza = raza
        self.estado_salud = estado_salud
        self.disponible = disponible

    def __str__(self):
        texto = (
            f"Nombre: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad}, "
            f"Estado de Salud: {self.estado_salud}, Disponible: {self.disponible}"
        )
        return texto

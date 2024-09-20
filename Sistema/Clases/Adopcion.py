
from datetime import datetime
from Clases.Persona import Persona
from Clases.Mascota import Mascota

class Adopcion():
    """Clase de adopcion"""

    def __init__(self, persona:Persona, mascota:Mascota)->None:
        """Constructor de la clase"""
        self.fecha_adopcion = datetime.now().strftime("%d/%m/%Y")
        self.persona = persona
        self.mascota = mascota

    def realizar_adopcion(self)->None:
        """Metodo para realizar adopcion"""
        if self.mascota.disponible:
            self.mascota.disponible = False
            self.persona.nmascotas += 1
            print(f"{self.persona.nombre} ha adoptado a {self.mascota.nombre} el {self.fecha_adopcion}")
        else:
            print(f"{self.mascota.nombre} ya ha sido adoptada.")

    def __str__(self):
        return f"{self.persona.nombre} adoptó a {self.mascota.nombre} el {self.fecha_adopcion}"
    
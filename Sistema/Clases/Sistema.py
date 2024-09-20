from Clases.Adopcion import Adopcion
from Clases.Persona import Persona
from Clases.Mascota import Mascota
import csv


class Sistema():

    def __init__(self):
        self.personas = {}
        self.mascotas = {}
        self.adopciones = {}

    def registrar_persona(self, persona:Persona)->None:
        """Metodo para registrar a persona en un diccionario"""
        self.personas[persona.nombre]=persona
        print(f"Persona {persona.nombre} registrada exitosamente.")

    def listar_personas(self):
        """Metodo para listas a las personas registradas"""
        for persona in self.personas.values():
            print(persona)

    def agregar_mascota(self, mascota:Mascota):
        """Metodo  para  gregar a las mascotas"""
        self.mascotas[mascota.nombre] = mascota
        print(f"Mascota {mascota.nombre} añadida exitosamente.")

    def eliminar_mascota(self, nombre_mascota:str):
        """Metodo para  eliminar a  la mascota de el diccionario"""
        if nombre_mascota in self.mascotas:
            del self.mascotas[nombre_mascota]
            print(f"Mascota {nombre_mascota} eliminada.")
        else:
            print(f"Mascota {nombre_mascota} no encontrada.")

    def eliminar_persona(self, nombre_persona:str):
        """Metodo para  eliminar a las personas de el diccionario"""
        if nombre_persona in self.personas:
            del self.personas[nombre_persona]
            print(f"Persona {nombre_persona} eliminada.")
        else:
            print(f"Persona {nombre_persona} no encontrada.")

    def listar_mascotas_disponibles(self):
        """Metodo que enlista a las mascotas cuando su estado es True"""
        for mascota in self.mascotas.values():
            if mascota.disponible:
                print(mascota)

    def realizar_adopcion(self, nombre_persona:str, nombre_mascota:str):
        """Metodo para realizar adopcion haciendo uso de una clase Adopcion"""
        if nombre_persona in self.personas.keys() and nombre_mascota in self.mascotas.keys():
            adopcion = Adopcion(self.personas[nombre_persona], self.mascotas[nombre_mascota])
            adopcion.realizar_adopcion()
            self.adopciones[adopcion.fecha_adopcion] = adopcion  # diccionario con clave de fecha
        else:
            print('No existe la persona o la mascota')


    def generar_reporte_adopciones(self):
        """Metodo que muestra en consola un reporte de las adopciones realizadas y tambien genera un archivo .csv"""
        print("Reporte de Adopciones Realizadas:")
        
        
        for adopcion in self.adopciones.values():  # Iteramos sobre los valores, que son objetos 'Adopcion'
            print(f"{adopcion.persona.nombre} adoptó a {adopcion.mascota.nombre} el {adopcion.fecha_adopcion}")
        
        # Generar el archivo CSV
        with open('reporte_adopciones.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            
            
            writer.writerow(['Nombre Persona', 'Nombre Mascota', 'Fecha de Adopción'])
            
            
            for adopcion in self.adopciones.values():  # Asegúrate de iterar sobre los valores
                writer.writerow([adopcion.persona.nombre, adopcion.mascota.nombre, adopcion.fecha_adopcion])
        
        print("Reporte generado exitosamente en 'reporte_adopciones.csv'")
        
        
        

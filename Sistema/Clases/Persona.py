class Persona():
    """Clase del cliente"""
    
    def __init__(
                self, nombre: str, edad: int, direccion: str, telefono: str, nmascotas: int
        ) -> None:
        """Constructor de la clase"""
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.nmascotas = nmascotas

    def __str__(self):
        texto = (f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono: {self.telefono}, "
                 f"Dirección: {self.direccion}, Mascotas Adoptadas: {self.nmascotas}")
        return texto
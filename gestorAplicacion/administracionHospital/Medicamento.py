import Serializable

class Medicamneto:
#inicializador y atributos
    def __init__(self, nombre, enfermedad, descripcion, cantidad, precio):
        self.nombre = nombre
        self.enfermedad = enfermedad
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    #metodos

    def eliminar_cantidad(self):
        self.cantidad -= 1

    #setters y getters
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre
    
    def set_enfermedad(self, enfermedad):
        self.enfermedad = enfermedad

    def get_enfermedad(self):
        return self.enfermedad
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad
    
    def set_precio(self, precio):
        self.precio = precio

    def get_precio(self):
        return self.precio
    
    #str

    def __str__(self):

        return f'Nombre: {self.nombre}\nEnfermedad: {self.enfermedad.nombre} {self.enfermedad.tipologia}\n Descripcion: {self.descripcion}"
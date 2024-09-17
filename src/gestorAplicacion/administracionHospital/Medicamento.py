#Elaborado por Jeronimo

class Medicamento:
#inicializador y atributos
    def __init__(self, nombre, descripcion, enfermedad, cantidad, precio):
        self.nombre = nombre
        self.enfermedad = enfermedad
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    #metodos
    def eliminarCantidad(self):
        self.cantidad -= 1

    # Muestra la informacion del medicamento sin la cantidad
    def mostrarInfo(self):
        return f"Nombre: {self.nombre} | Trata la enfermedad: {self.enfermedad} | Descripcion: {self.descripcion} | Precio: {self.precio}"

    def __str__(self):
        return f"Nombre: {self.nombre} | Trata la enfermedad: {self.enfermedad} | Descripcion: {self.descripcion} | Precio: {self.precio} | Cantidad: {self.cantidad}"

#setters y getters
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setEnfermedad(self, enfermedad):
        self.enfermedad = enfermedad

    def getEnfermedad(self):
        return self.enfermedad
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getCantidad(self):
        return self.cantidad
    
    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio

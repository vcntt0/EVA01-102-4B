class Vendedor:
    def __init__(self, nombre, rut, telefono):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
    
    def mostrarDatos(self):
        print("===============VENDEDOR===============")
        print(f"EL nombre del vendedor es: {self.nombre}")
        print(f"El rut del vendedor es {self.rut}")
        print(f"El telefono del vendedor es {self.telefono}")

    # def calcularComision(self, montoVenta):
    #     if montoVenta >= 5000000:
    #         return montoVenta * self.precio //100
    #     else:
    #         return montoVenta * self.precio //50
         
        
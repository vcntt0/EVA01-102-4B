class Vehiculo:
    def __init__(self, patente, marca, modelo, año, precio):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrarInfo(self):
        print("===============VEHICULO===============")
        print(f"La patente del vehiculo es: {self.patente}")
        print(f"La marca del vehiculo es: {self.marca}")
        print(f"El modelo del vehiculo es: {self.modelo}")
        print(f"El año del vehiculo es: {self.año}")
        print(f"El precio del vehiculo es: {self.precio}")

    def calcularAñosUso(self, añoActual):
        añoActual = 2026
        añoActual = añoActual - self.año
        return añoActual
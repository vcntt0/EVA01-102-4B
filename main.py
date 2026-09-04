from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():

    # Crear automotora
    automotora_1 = Automotora("Don pepito")

    # Crear 2 automóviles
    auto_1 = Auto("HJCV03", "ferrari", "California", 2003, 7000000,2,95)
    auto_2 = Auto("HOLA12", "Volkswagen", "Golf", 2014, 4000000,4,93)
    

    # Crear motocicleta
    moto_1 = Motocicleta("E2SR17","suzuki", "Hayabusa", 2026, 9000000, 700,"carrera")

    # Agregar vehículos a la automotora
    automotora_1.agregarVehiculo(auto_1)
    automotora_1.agregarVehiculo(moto_1)
    automotora_1.agregarVehiculo(auto_2)

    # Mostrar vehículos
    print("===== VEHÍCULOS DE LA AUTOMOTORA =====")
    automotora_1.mostrarVehiculos()



    # Probar métodos de un Auto
    print("\n===== AUTO =====")
    auto_1.abrirMaletero()
    print(auto_2.tieneAireAcondicionado())

    # Calcular años de uso del auto
    print(auto_1.calcularAñosUso(2022))
    print(auto_2.calcularAñosUso(2010))
    # Probar métodos de Motocicleta
    print("\n===== MOTOCICLETA =====")
    moto_1.encenderMotor()
    print(moto_1.esDeAltaCilindrada())
    # Calcular años de uso de la motocicleta
    print(moto_1.calcularAñosUso(2026))

    # Crear vendedor
    vendedor1 = Vendedor(
         "cristobal macaya",
         "12.345.678-9",
         "987654321"
     )

    print("\n===== VENDEDOR =====")
    vendedor1.mostrarDatos()
    #print(vendedor1.calcularComision(auto_1))


#link github : https://github.com/vcntt0/EVA01-102-4B.git

if __name__ == "__main__":
    main()
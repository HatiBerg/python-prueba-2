def main():
    mensaje = """
Seleccione una de las siguientes opciones:
1) Kilómetros -> Millas
2) Millas -> Kilómetros
3) Kilogramos -> Libras
4) Libras -> Kilogramos
5) Celsius -> Fahrenheit
6) Fahrenheit -> Celsius
7) Salir
"""
    print(mensaje)
    opcion = int(input("Ingrese una opción: "))

    while(opcion != 7):
        numero = float(input("Ingrese la cantidad a convertir: "))
        if opcion == 1:
            resultado = numero * 0.621371
            print(f"{numero} Kilómetros son {resultado} Millas")
        elif opcion == 2:
            resultado = numero * 1.60934
            print(f"{numero} Millas son {resultado} Kilómetros")
        elif opcion == 3:
            resultado = numero * 2.20462
            print(f"{numero} Kilogramos son {resultado} Libras")
        elif opcion == 4:
            resultado = numero * 0.453592
            print(f"{numero} Libras son {resultado} Kilogramos")
        elif opcion == 5:
            resultado = (numero * (9/5)) + 32
            print(f"{numero} Celsius son {resultado} Fahrenheit")
        elif opcion == 6:
            resultado = (numero - 32) * (5/9)
            print(f"{numero} Fahrenheit son {resultado} Celsius")
        else:
            print("Opción no valida, intente de nuevo")
        print("")
        opcion = int(input("Ingrese una opción: "))
    print("Programa Terminado")

if __name__ == "__main__":
    main()
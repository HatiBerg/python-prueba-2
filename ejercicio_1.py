def es_primo(numero):
    if numero == 1:
        return False
    else:
        for i in range(2,numero):
            if numero % i == 0:
                return False
        return True

def main():
    numero = int(input("Ingrese un número: "))

    if es_primo(numero):
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")

if __name__ == "__main__":
    main()
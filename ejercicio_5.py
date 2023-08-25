def main():
    palabra = input("Ingrese una palabra: ")
    letra = input("Ingrese una letra: ")
    cont = 0

    for i in palabra.lower():
        if letra == i:
            cont+=1

    print(f"Veces que aparece la letra {letra} en la palabra {palabra}: {cont}")

if __name__ == "__main__":
    main()
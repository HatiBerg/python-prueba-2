def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

def main():
    palabra = input("Ingrese una palabra: ")
    if len(palabra) > 2:
        if es_palindromo(palabra):
            print(f"La palabra {palabra} es palíndromo")
        else:
            print(f"La palabra {palabra} no es palíndromo")
    else:
        print("La palabra tiene que tener más de 3 caracteres")

if __name__ == "__main__":
    main()
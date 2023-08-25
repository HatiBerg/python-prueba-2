def main():
    cesta = {}
    total = 0
    articulo = input("Ingrese un artículo: ")

    while(articulo.lower() != "terminar"):
        precio = int(input("Ingrese el precio del artículo: "))
        cesta[articulo] = precio
        articulo = input("Ingrese un artículo: ")

    print("Lista de compra:")
    print("")
    for i in cesta:
        print(f"{i}    {cesta[i]}")
        total+=cesta[i]
    print(f"Total    {total}")

if __name__ == "__main__":
    main()
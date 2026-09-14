km = int(input("Kilómetros recorridos: "))
consumo = int(input("Consumo (litros cada 100km): "))
precioL = int(input("Precio litro: "))


print("El costetotal es de :", km / 100 * consumo * precioL, "€")
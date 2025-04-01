#Ejercicio 4 - LISTA
tamaño = int(input("Ingrese el tamaño de la lista: "))
compañias = list(map(lambda _: input("Ingrese una compañía: "), range(tamaño)))
compañias_repetidas = compañias + list(map(lambda _: input("Ingrese una compañía repetida: "), range(2)))
compañias_sin_repetidos = list(set(compañias_repetidas))

print("Lista inicial:", compañias)
print("Lista sin repetidos:", compañias_sin_repetidos)
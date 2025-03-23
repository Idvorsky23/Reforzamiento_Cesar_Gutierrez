# Ejercicio 8
paises = input("Ingrese 8 países separados por coma: ").split(",")
copia = paises[:]
del copia[0]
del copia[-2]
print("Lista original:", paises)
print("Lista modificada:", copia)
print("Tamaño lista modificada:", len(copia))


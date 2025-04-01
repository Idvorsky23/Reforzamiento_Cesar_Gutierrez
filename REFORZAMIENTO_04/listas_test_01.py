#Ejercicio 1
tamaño = int(input("Ingrese el tamaño de la lista: "))
nombres = list(map(lambda _: input("Ingrese un nombre: "), range(tamaño)))
print("______________________________")
print(f"Tamaño de la lista: {len(nombres)}")
print("Nombres ingresados:", nombres)
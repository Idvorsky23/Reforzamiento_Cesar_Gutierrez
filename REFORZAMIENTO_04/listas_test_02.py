#Ejercicio 2 - LISTA
departamentos = ["Lima", "Cusco", "Arequipa", "Piura", "Trujillo"]
print("Lista actual:", departamentos)

dep1 = input("Ingrese el departamento a reemplazar: ")
dep2 = input("Ingrese el nuevo departamento: ")

if dep1 in departamentos:
    index = departamentos.index(dep1)
    departamentos[index] = dep2
    print("Lista actualizada:", departamentos)
else:
    print("El departamento no está en la lista.")
#Ejercicio 3
estudiantes = ["Juan", "Maria", "Carlos", "Ana", "Luis"]
nombre = input("Ingrese un nombre: ")

if nombre in estudiantes:
    estudiantes.remove(nombre)
    print(f"{nombre} fue eliminado.")
else:
    estudiantes.append(nombre)
    print(f"{nombre} no estaba en la lista y ha sido agregado.")

print("Lista actualizada:", estudiantes)
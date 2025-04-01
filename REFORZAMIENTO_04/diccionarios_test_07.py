#Ejercicio 7: Notas de alumnos
# Diccionario de alumnos y sus notas
alumnos = {"Cesar": 13, "Diego": 15, "Elinor": 18, "Jaime": 10}
# Solicitar el nombre del alumno
nombre = input("Ingrese el nombre del alumno: ")
# Obtener la nota si el alumno existe, de lo contrario mostrar un mensaje
nota = alumnos.get(nombre, "Alumno no encontrado")
# Mostrar la nota en consola
print("La nota de {} es {}" .format(nombre, nota))
# Agenda telefónica
agenda = {"Cesar": 960909775, "Diego": 960102839, "Elinor": 965124756, "Jaime": 914935124}
# Solicitar el nombre
nombre = input("Ingrese el nombre: ")
# Obtener la nota si el alumno existe, de lo contrario mostrar un mensaje
telefono = agenda.get(nombre, "No encontrado")
# Mostrar en la consola
if nombre in agenda:
    print("El múmero telefónico de {} es {}" .format(nombre, telefono))
else:
    print("No se encuentra registrado en la agenda")
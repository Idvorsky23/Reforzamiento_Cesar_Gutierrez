#Ejercicio 2: Modificación de diccionario
persona = {"nombre": "Cesar", "edad": 24, "salario": 2000}
persona["dni"] = "72449657"
print(f"Salario: {persona['salario']}, DNI: {persona['dni']}")

del persona["edad"]
print("Diccionario actualizado:", persona)
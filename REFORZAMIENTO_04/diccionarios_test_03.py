#Ejercicio 3: Conversión de diccionario a lista y verificación de tipo
persona = {"nombre": "Cesar", "edad": 24, "salario": 2000}
lista_diccionario = list(persona.items())
print("Tipo de datos final:", type(lista_diccionario))
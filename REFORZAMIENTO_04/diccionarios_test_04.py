#Ejercicio 4: Modificación de diccionario de departamentos
departamentos = {"1": "Lima", "2": "Cusco", "3": "Arequipa", "4": "Piura", "5": "Trujillo", "6": "Tacna"}

del departamentos["3"]  # Eliminando Arequipa
departamentos["5"] = "Huancayo"  # Actualizando penúltimo departamento

print("¿Arequipa sigue en el diccionario?", "Arequipa" in departamentos.values())
print("Diccionario actualizado:", departamentos)
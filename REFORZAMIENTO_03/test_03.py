#Ejercicio 3
# Crear la primera lista vacía
lista1 = []

# Definir variables con diferentes tipos de datos
float1, float2, float3 = 1.1, 2.2, 3.3
int1, int2, int3 = 10, 20, 30
str1, str2, str3 = "uno", "dos", "tres"

# Agregar las variables a la lista usando append
lista1.append(float1)
lista1.append(float2)
lista1.append(float3)
lista1.append(int1)
lista1.append(int2)
lista1.append(int3)
lista1.append(str1)
lista1.append(str2)
lista1.append(str3)

# Crear la segunda lista vacía
lista2 = []

# Definir otras variables con los mismos tipos de datos
float4, float5, float6 = 4.4, 5.5, 6.6
int4, int5, int6 = 40, 50, 60
str4, str5, str6 = "cuatro", "cinco", "seis"

# Agregar las variables a la segunda lista usando append
lista2.append(float4)
lista2.append(float5)
lista2.append(float6)
lista2.append(int4)
lista2.append(int5)
lista2.append(int6)
lista2.append(str4)
lista2.append(str5)
lista2.append(str6)

# Sumar ambas listas
lista_total = lista1 + lista2

# Mostrar el resultado en consola
print(lista_total)
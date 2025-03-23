# Ejercicio 1
lista = ["a", "b", "c", "d", "e"]
lista.extend(["f", "g", "h", "i", "j"])
lista.remove("b")
lista.remove("d")
lista.append(len(lista))
print("Lista final:", lista)

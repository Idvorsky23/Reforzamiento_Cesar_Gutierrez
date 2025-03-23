# Ejercicio 10
bd_relacionales = ["MySQL", "PostgreSQL", "Oracle", "MySQL", "SQL Server", "SQLite", "Oracle", "PostgreSQL"]
bd_relacionales.remove("MySQL")
del bd_relacionales[bd_relacionales.index("Oracle")]
print("Lista actualizada:", bd_relacionales)
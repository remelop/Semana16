# Escribir notas
with open("my_notes.txt", "w") as archivo:
    # Escribir líneas de notas
    archivo.write("Ronny Eduardo.\n")
    archivo.write("Melo Penaherrera.\n")
    archivo.write("35.\n\n")

# Leer notas
with open("my_notes.txt", "r") as archivo:
    # Leer cada línea y mostrarla
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()

# Escribir notas
with open("my_notes.txt", "a") as archivo:
        archivo.write("Quito, Pichincha, Norte.\n\n")

# Leer notas
with open("my_notes.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()
# Cerrar el archivo
archivo.close()


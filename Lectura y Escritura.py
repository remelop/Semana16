# Escribir notas
with open("my_notes.txt", "w") as archivo:
    # Escribir líneas de notas
    archivo.write("Ronny Eduardo.\n")
    archivo.write("Melo Peñaherrera.\n")
    archivo.write("35 años.\n\n")

# Leer notas
with open("my_notes.txt", "r") as archivo:
    # Leer cada línea y mostrarla
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()

# Escribir notas
with open("my_notes.txt", "w") as archivo:
    archivo.write("Quito, Pichincha, Norte.\n\n")

# Leer notas
with open("my_notes.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()

with open("my_notes.txt", "w") as archivo:
    archivo.write("Gracias.\n")
with open("my_notes.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()


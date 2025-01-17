from io import open

texto = "una linea con a"

# Crea un archivo en modo de escritura
archivo = open("archivo.txt",'w')

# Escribe el texto en el archivo
archivo.write(texto)

archivo.close()
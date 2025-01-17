from io import open

texto = ""
archivo = open("archivo.txt","r")

texto = archivo.readline()
print(texto)

#rchivo.seek(0)



archivo.close()
from io import open
import os


class diccionario: 
    archivo = ''

    def __init__(self,archivo):
        self.archivo = archivo
 
    
    # método para crear o iniciar con el archivo de texto
    def iniciar_archivo(self):
        archivo = open(self.archivo,'w')
        archivo.close()    
    
    # método para capturar palabras en el diccionario 
    def capturar_palabra(self, palabra, traduccion):
        archivo = open(self.archivo,'a')
        archivo.write("{}: {}\n".format(palabra,traduccion))
        archivo.close()

    # método para buscar palabras en ingles y español
    def buscar_palabra(self,opcion):
        # leer palabras del archivo
        archivo = open(self.archivo,'r')
        palabras = archivo.readlines()
        archivo.close()
        # cambiar formato de la lista
        palabras_list = "".join(palabras).strip().replace("\n"," , ").replace(": "," , ").split(" , ")
        busqueda = input("Palabra a buscar: ")
        if opcion == 1:
            # validar que la palabra este en la lista
            if busqueda in palabras_list:
                # si la palabra esta, encontrar la traducción a ingles imprimiendo la siguiente posición. 
                for i in range(len(palabras_list)):
                    if palabras_list[i] == busqueda:
                        print("Traducción al ingles: " + palabras_list[i + 1])
            if busqueda not in palabras_list:
                print("Palabra no encontrada. ")
        if opcion == 2:
            # validar que la palabra este en la lista
            if busqueda in palabras_list:
                # si la palabra esta, encontrar la traducción a español imprimiendo la posición anterior
                for i in range(len(palabras_list)):
                    if palabras_list[i] == busqueda:
                        print("Traducción al español: " + palabras_list[i - 1])
            if busqueda not in palabras_list:
                print("Palabra no encontrada. ")

# método inicial 
def run(): 
    # instancia de la clase diccionario 
    dic = diccionario('diccionario.txt')
    dic.iniciar_archivo()
    while True:
        print("\nMenú de opciones: ")
        print("1. Capturar palabra")
        print("2. Buscar palabra")
        print("3. Salir")
        opcion = int(input("\nIngrese la opción seleccionada: "))
        os.system('cls')
        if opcion == 1: 
            palabra = input("Ingrese la palabra en español: ")
            traduccion = input("Ingrese su traducción en ingles: ")
            dic.capturar_palabra(palabra,traduccion)
        if opcion == 2:
            print("1. Buscar a partir su palabra en español")
            print("2. Buscar a partir su palabra en ingles")
            idioma = int(input("\nIngrese la opción seleccionada: "))
            dic.buscar_palabra(idioma)
        if opcion == 3: 
            break

if __name__=="__main__":
    run()
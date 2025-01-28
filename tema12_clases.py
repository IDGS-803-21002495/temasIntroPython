# palabra reservada class para crear la clase
class OperasBas: 
    # declaración de propiedades 
    num1 = 0
    num2 = 0
    res = 0
    # declaración de constructor de la clase: inicializa las propiedades de la clase
    # en este caso se pasan dos parametros para la instancia de la clase 
    def __init__(self,a,b): #self = this hace referencia a las propiedades de la clase
        self.num1 = a
        self.num2 = b
        
    # declaración de métodos de la clase
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))

# método fuera de la clase
def main():
    # instancia de la clase
    obj = OperasBas(3,5) 
    obj.suma() # Llamo al método
    
if __name__=="__main__":
    main()
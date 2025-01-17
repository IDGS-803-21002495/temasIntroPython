# Listas: Definir una serie de elementos
# Se declaran por medio de []

lista1 = [] # Lista vacia
lista2 = [1,22,13,2,15] # Lista de enteros
lista3 = [6.3,7.4,8.2,9.3,10.9] # Lista de
lista4 = ["Mario", "Pedro","Dario"] # Lista de strings
lista5 = [1,3,4.3,2.3, "Veronica"]
print(type(lista1)) 
print(lista2)
#print(len(lista2))

# Asignar elementos a una lista 
lista2[2] = 7
print(lista2)

lista1.append(10)
lista1.append(1)
lista1.append(11)
print(lista1)
# Quita ultimo elemento de la lista
lista1.pop()
print(lista1)

print(lista2)
# Organizar elementos 
lista2.sort()
print(lista2)
lista = [7 , 6, 5 , 4 , 3 ,2 ]
print(len(lista))
#agregar elementos hay 2 maneras
lista.append(9)
print(lista)
lista.insert(1,8)
print(lista)

#quitar elementos 
del lista[3]
print(lista)
lista.remove(4)
print(lista)

#info de elementos
print(lista.index(9))

lista[0]=1
print(lista)


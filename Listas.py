def separaEntDec(n: float):
    return int(n), n - int(n)


lista = ["Leonel", 20, 1.77, True]

#destructuracion
print(lista[0])
print (lista[3])
print(lista [len(lista)-1])
print(lista [-1])
print(lista [-4])
print()
print(lista[1:3])
print(lista[:3])
print(lista[:])

nom = lista[0]
edad = lista [1]
altura = lista[2]
essoltero = lista [3]

nom, edad, altura, essoltero = lista

a =10
b =20
c,d=a,b
print(f"c{c} f{d}")

b,a=a,b
print(f"a{a} b{b}")

print (separaEntDec(8.3))

print(1.77 in lista)
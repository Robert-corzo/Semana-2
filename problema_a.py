"""
Haz un progrma en Python que te muestre un menu con la primera pcion
que te permita crear persona con nombre y DNI y la aguegué a una lista de personas.
El menu tendrá una segunda opcion donde mostrará todas las personas.
El menú tendra una tercera opcion que pedirá un DNI  eliminará a la persona con ese DNI. 
"""

class Persona:
    def __init__(self,_dni=0, _nombre=""):
        self.nombre = _nombre
        self.dni = dni

    def __str__(self):
        return f"DNI: {self.dni} {self.nombre}"
    
lista= []
opc = 0

while opc != 9:
   opc = int(input("seleccione opcion: \n1-crear\n2-listar\n3-eliminar\n9-fin"))
   if opc ==1:
       dni = input ("Ingrese dni:\n")
       nombre = input ("Ingrese nombre:\n")
       nuevo = Persona(dni, nombre)
       lista.append(nuevo)

   elif opc ==2:
       for p in lista:
           print(p)
       
   elif opc == 3:
       dniB = input ("Ingrese dni a borrar:\n")
       idx = 0
       for idx, p in enumerate(lista):
           if p.dni == dniB:
              del lista[idx]
              break

   elif opc == 4:
       break


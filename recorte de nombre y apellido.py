def NombreApellido (nom, ape):
    C1= nom [0:3]
    C2=ape [-3:]
    suma=C1+C2
    return suma
nom=input("Dame tu nombre")
ape=input("Dame tu apellido")
r= NombreApellido (nom,ape)
    print (r)
           


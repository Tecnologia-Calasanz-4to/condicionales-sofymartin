

valor1=int(input("Ingrese el primer valor"))
valor2=int(input("Ingrese el segundo valor"))
valor3=int(input("Ingrese el tercer valor"))
valor4=int(input("Ingrese el cuarto valor"))
valor5=int(input("Ingrese el quinto valor"))

def op1 ():
        print ("LOS MEJORES")
        return

def op2 ():
        print ("Muy ricos o muy feos dependiendo del lugar")
        return

def op3 ():
        print ("HORRIBLE ")
        return
    
def op4 ():
        print ("Los mejores para una comida rápida")
        return
    
def op5 ():
        print ("Ricos para cada tanto")
        return


def main ( ):
    print ("Elegí una de las opciones")
    print ("1. Mostrar un Promedio")
    print ("2. Mostrar el valor mas bajo")
    print ("3. Mostrar el valor mas alto")



    opcion = input("Elegí una pasta")

    if (opcion == 1):
        op1 ()
    if (opcion == 2):
        op2 ()
    if (opcion == 3):
        op3 ()
    if (opcion == 4): 
        op4 ()
    if (opcion == 5): 
        op5 ()

    

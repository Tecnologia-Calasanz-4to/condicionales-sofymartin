def rectangulo (base, altura):
    cuentarec= base * altura
    return cuentarec

def triangulo (base, altura):
    cuentatriang= base * altura // 2
    return cuentatriang

b= int(input("Base:"))
a= int(input("Altura:"))
arearec= rectangulo(b,a)
areatr= triangulo (b,a)
print ("El area del rectangulo es: ", arearec)
print ("El area del triangulo es: ", areatr)

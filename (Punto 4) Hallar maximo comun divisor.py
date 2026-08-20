print("Introduzca dos numeros a los que desea hallar su maximo comun denominador")
m=int(input("Primer Numero: "))
while m<0:
    m=int(input("El numero debe ser positivo, vuelva a intentar: "))
n=int(input("Segundo numero: "))
while n<0:
    n=int(input("El numero debe ser positivo, vuelva a intentar: "))
resultado = 0
g=m
p=n
lim=n
if m<n:
    lim=m
for i in range(1, lim+1):
    r1=m%i
    r2=n%i
    if r1 ==0 and r2==0:
        resultado=i
print("El maximo comun divisor de " + str(g)+ " y " + str(p)+ " es: "+ str(resultado))
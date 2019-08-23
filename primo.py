a=int(input("El numero a probar es: "))
divisores=0
i=1
while divisores<=2 and i<=a//2:
    if a%i==0:
        divisores=divisores+1
        i=i+1
    else:
        i=i+1
    

if divisores<=1:
    print("el numero es primo")
else:
    print("el numero no es primo")

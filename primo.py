a=int(input("El numero a probar es: "))
divisores=0
mitadE=a//2
for i in range(1, mitadE):
    if a%i==0:
        divisores=divisores+1
        if divisores==3:
            break
    

if divisores<=2:
    print("el numero es primo")
else:
    print("el numero no es primo")
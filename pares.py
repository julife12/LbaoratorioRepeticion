a=int(input("digite la cantidad de numeros que desea probar: "))
print("cuando un numero sea impar se detendra el proceso")
cant_par=0
cant_impar=0

for i in range(1, a+1):
    num=int(input("digite el numero: "))
    if num==0:
        break


    if num%2==0:
        cant_par=cant_par+1        
    else:
        cant_impar=cant_impar+1
    


print("la cantidad de numeros pares es: ", cant_par, "la cantidad de numeros impares es: ", cant_impar)

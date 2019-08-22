a=int(input("digite el numero: "))
if a>0:
    print("es mayor a cero")
else:
    print("es menor a cero")

cant_mas=0
cant_menos=0
cant_cero=0
for i in range(1, 11):
    num=int(input("digite el numero: "))
    if num>0:
        cant_mas=cant_mas+1
    else:
        if num==0:
            cant_cero=cant_cero+1
        else:
            cant_menos=cant_menos+1


print("la cantidad de numeros positivos fueron: ", cant_mas, "la cantidad de numeros negativos es: ", cant_menos, "la cantidad de ceros que inscribio fueron: ", cant_cero)

Diccionario={"norte":["fecha",400],"centro":["",300],"sur":["",700],"sambo":["",1000],"daule":["",200]}
seguir=True
while(seguir!=False):
    print("Desea ingresar una surcursal?(Y/N):")
    opcion=input()
    if opcion=="Y" :
        nombre=input("Ingrese el nombre de la sucursal: ")
        fecha=input("Ingrese la fecha de inauguracion: ")
        dinero=input("Ingrese la ganancia fija anual: ")
        lista=[fecha, int(dinero)]
        Diccionario[nombre]=lista
    else :
         seguir=False
print("Calcular promedio anual")
acumulador=0
cantidad=0
for key in Diccionario:
    list=Diccionario[key]
    acumulador+=list[1]
    cantidad+=1
    print(Diccionario[key])
promedio=acumulador/cantidad
print("El promedio es %d",promedio)
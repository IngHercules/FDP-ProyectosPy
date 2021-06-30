#import os
import math
def Menu():
     #os.system('cls')
     print("1.- Calcular IMC ")
     print("2.- Identificar numero mayor ")
     print("3.- Suma secuencial")
     print("4.- Numero primo")
     print("5.- Area de un triangulo")
     print("6.- Salir del programa ")
opcion=1
while (opcion !=0 ):
    Menu()
    opcion=int(input("Seleccione una opcion: "))
    
    if(opcion==1):
        peso=float(input("Ingrese el peso en Kilogramos: "))
        estatura=float(input("Ingrese la estatura en metros: "))
        IMC=peso/estatura**2
        if(IMC<18.5):
            print("IMC= ",IMC,"Estado: Desnutrido")
        elif (18.5<=IMC<=25.5):
            print("IMC= ",IMC,"Estado: Peso Normal")
        else:
            print("IMC= ",IMC,"Estado: Sobrepeso")
    elif (opcion==2):
        valor=int(input("Cuantos valores ingresara: "))
        numMayor=0
        for i in range(valor):
            num=int(input("Ingrese un valor entero: "))
            if num>numMayor:
                numMayor=num
        print("El numero mayor ingresado es: ",numMayor)
    elif (opcion==3):
         num=int(input("Ingrese el limite de la suma: "))
         Suma=0
         for i in range(1, num+1):
            Suma=Suma+i
         print("Total de la suma: ",Suma)
    elif (opcion==4):
        num=int(input("Ingrese un valor entero: "))
        valor=0
        for div in range(1,num+1):
            if(num%div==0):
                valor=valor+1
        if(valor>2):
            print("No es primo")
        else:
            print("Es primo")
    elif (opcion==5):
        Cat_A=float(input("Ingrese el valor del cateto A: "))
        Cat_B=float(input("Ingrese el valor del cateto B: "))
        Cat_C=float(input("Ingrese el valor del cateto C: "))
        SubArea=float(Cat_A+Cat_B+Cat_C)/2
        Area=float(SubArea*(SubArea - Cat_A)*(SubArea - Cat_B)*(SubArea - Cat_C))**0.5
       # Area= float(prod**0.5)
        print("El area del triangulo es: ", Area)     
    elif (opcion==6):
        opcion=0
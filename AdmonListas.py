miLista = []
while True:
    print("1- Insertar un registro")
    print("2- Modificar un registro")
    print("3- Eliminar un registro")
    print("4- Listar registros")
    print("5- Salir del programa")
    opc = int(input("Seleccione una opcion: "))
    
    if opc == 1:
        nombre = input("Ingrese el nombre a registrar: ")
        miLista.append(nombre)
    elif opc == 2:
        indice = int(input("Ingrese el indice del registro: "))
        if indice < len(miLista) :
            nNombre = input("Ingrese el nuevo nombre: ")
            miLista[indice] = nNombre
        else:
            print("Indice incorrecto")
    elif opc == 3:
        indice = int(input("Ingrese el indice del registro a eliminar: "))
        if indice < len(miLista):
            miLista[indice]=[]
        else:
            print("Indice incorrecto")
    elif  opc == 4:
        print(miLista)
    elif opc == 5:
        break
    else:
        print("Opcion seleccionada no es valida")
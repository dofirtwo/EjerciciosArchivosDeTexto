import os
verificacion=False
try:    
    archivo= open("carros.txt","a", encoding="UTF-8")
    archivolectura= open("carros.txt","r", encoding="UTF-8")
    placas=archivolectura.readlines()
    archivolectura.close()
    placa=input("Ingrese la placa del carro: ")
    for p in placas:
        todasPlacas=p.strip("\n").split(",")
        for td in todasPlacas:
            if td==placa:
                verificacion=True
                break
        if (verificacion):
            print(f"La placa {placa} ya existe")
            break
    if verificacion==False:
            marca=input("Ingrese la marca del carro: ")
            color=input("Ingrese el color del carro: ")
            archivo.write(f"{placa},")
            archivo.write(f"{marca},")
            archivo.write(f"{color}\n")
            archivo.close
except IOError as error:
    print(error)
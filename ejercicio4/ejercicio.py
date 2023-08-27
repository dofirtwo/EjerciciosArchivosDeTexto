import os
verificacion=False
try:
    nombre=input("Ingrese el nombre del archivo: ")
    if os.path.exists(nombre):
        archivo= open(nombre,"r", encoding="UTF-8")
        palabras=archivo.readlines()
        archivo.close()
        lineas=0
        for p in palabras:
            lineas=lineas+1
            saber=p.strip("\n")
            print(f"la palabra: {saber} se encuetra en la linea: {lineas}")
        print()
    else:
        print("Ese archivo de texto no existe")
except IOError as error:
    print(error)
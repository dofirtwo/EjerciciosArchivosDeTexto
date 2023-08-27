import os
verificacion=False
try:
    nombre=input("Ingrese el nombre del archivo: ")
    if os.path.exists(nombre):
        archivo= open(nombre,"r", encoding="UTF-8")
        palabras=archivo.readlines()
        archivo.close()
        palabra=input("Ingrese una palabra: ")
        for p in palabras:
            todaspalabras=p.strip("\n").split(" ")
            for td in todaspalabras:
                if td==palabra:
                    print()
                    print(f"la palabra {p} se encuentra en el archivo {nombre}")
                    print()
                    verificacion=True
                    break
            if(verificacion):
                break
            
        if verificacion==False:
            print()
            print("No Existe esa palabra")
            
        else:
            print("Ese archivo de texto no existe")
        
except IOError as error:
    print(error)
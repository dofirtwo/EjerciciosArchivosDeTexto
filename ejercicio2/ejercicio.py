try:
    archivo= open("lineas.txt","w", encoding="UTF-8")
    linea=int(input("Ingrese cuantas lineas quiere guardar: "))
    for x in range(1,linea+1):
        archivo.write(f"Linea de Texto {x}\n")
    archivo.close
except IOError as error:
    print(error)
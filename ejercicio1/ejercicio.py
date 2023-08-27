try:
    archivo= open("personas.txt","a", encoding="UTF-8")
    persona=input("Ingrese el nombre de una persona ")
    archivo.write(f"{persona}\n")
    archivo.close
except IOError as error:
    print(error)
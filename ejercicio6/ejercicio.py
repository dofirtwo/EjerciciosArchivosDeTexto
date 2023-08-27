x=0
def crearContactos():
    """_summary_: crea el archivo contactos.txt 
    y agrega datos a ese archivo verificando 
    su existencia por la identificacion
    """
    verificacion=False
    try:
        archivo= open("contactos.txt","a", encoding="UTF-8")
        archivolectura= open("contactos.txt","r", encoding="UTF-8")
        idetificaciones=archivolectura.readlines()
        archivolectura.close()
        id=input("Ingrese la Identificacion: ")
        for i in idetificaciones:
            todasId=i.strip("\n").split(",")
            for ti in todasId:
                if ti==id:
                    verificacion=True
                    break
            if (verificacion):
                print(f"La Identificacion {id} ya existe")
                break
        if verificacion==False:
            nombre=input("Ingrese el Nombre ")
            apellido=input("Ingrese el Apellido: ")
            correo=input("Ingrese el Correo: ")
            while(True):
                genero=input("Ingrese el Genero (Masculino/Femenino): ").lower()
                if (genero=="femenino" or genero=="masculino"):
                    break
                else:
                    print("debe volver a ingresar el genero :o")
            archivo.write(f"{id},")
            archivo.write(f"{nombre},")
            archivo.write(f"{apellido},")
            archivo.write(f"{correo},")
            archivo.write(f"{genero}\n")
            archivo.close
    except IOError as error:
        print(error)
 
def listarContactos():
    """_summary_:lista los contactos 
    guardados en el archivo contactos.txt
    """
    archivo = open("contactos.txt","r", encoding="UTF-8")
    contactos = archivo.readlines()
    archivo.close()
    for c in contactos:
        print(c.strip("\n"))
    
           
while x!=4:
    print("\t\Gestion de Contactos")
    print("\t1. Agregar")
    print("\t2. Cosnultar por Identificacion")
    print("\t3. Listar Contactos")
    print("\t4. Salir")
    x=int(input("Ingrese Opción (1-4): "))
    
    if x == 1:
        crearContactos()
            
    if x == 2:
        verificacion=False
        try:
            archivo = open("contactos.txt","r", encoding="UTF-8")
            contactos = archivo.readlines()
            archivo.close()
            id=input("Ingrese la Identificacion: ")
            for i in contactos:
                todasId=i.strip("\n").split(",")
                for ti in todasId:
                    if ti==id:
                        print(todasId)
                        verificacion=True
                        break
                if (verificacion):
                    break
            if verificacion==False:
                print("Esa identificacion no Existe")
            
        except IOError as error:
            print(error)
    if x == 3: 
        listarContactos()
print("vuelva pronto :D")
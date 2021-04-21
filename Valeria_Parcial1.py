'''
        PARCIAL 1 BIOINGENIERIA

Valeria Giraldo Agudelo
Grupo 2

Universidad de Antioquia
Medellin - Antioquia
Abril 2021

'''
def clearScreen():
    # Esta funcion dara la ilucion de que la consola fue limpiada
    print("\n"*20) # Se imprimen 20 saltos de linea

def Menu():
    # Esta funcion se encarga de imprimir un menu de opciones
    print("Menu:\n",
          "1. Ingresar informacion de una pipeta.\n",
          "2. Consultar informacion de una pipeta.\n",
          "3. Estadisticos.\n",
          "4. Salir.")
def Marca():
        # Esta funcion se encarga de imprimir un menu de marcas
    print("Marcas:\n",
          "1. Brand.\n",
          "2. 3M.\n",
          "3. Rainin.\n",
          "4. PipeteLine.")

lab_metrologia = [] # lab_metrologia es la lista que almacenara los datos de todas las pipetas ingresadas.
marcas = ["Brand", "3M", "Rainin", "PipeteLine"] # marcas contine los nombres de las cuatro marcas de pipetas.
contadorMarcas = [0,0,0,0] # contadorMarcas almacenara la cantidad de pipetas de cada marca.

for h in range(0,99999999999):
    
    MCUL = [] # Mediciones de 100uL
    MMUL = [] # Mediciones de 1000uL
       
    Menu() # Se imprime en consola el menu de opciones
    option = input("Opcion: ") # option es la variable que almacenara la opcion escogida por el usuario
    clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
    
    # Este ciclo se encarga de verficar si la opcion escogida por el usuario es valida
    while(option.isnumeric() == False or int(option)<1 or int(option)>4):
        print("Opcion invalida.\n") # Se advierte al usuario que la opcion ingresada es invalida
        Menu() # Se imprime en consola el menu de opciones
        option = input("Opcion: ") # Se le pide al usuario que ingrese una nueva opcion
        clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
    
    # Se verifica si la opcion escogida por el usuario es la numero uno
    if(int(option) == 1):
        Marca() # Se imprime en consola el menu de las marcas disponibles.
        marca = input("Marca: ")
        clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
        
        # este ciclo se encarga de verificar si la marca escogida por el usuario es valida
        while(marca.isnumeric() == False or int(marca)<1 or int(marca)>4):
            print("Marca no existente.\n") # Se advierte al usuario que la opcion ingresada es invalida
            Marca() # Se imprime en consola el menu de las marcas disponibles.
            marca = input("Opcion: ") # Se le pide al usuario que ingrese una nueva opcion
            clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
            
        contadorMarcas[int(marca)-1] += 1 # Se aumenta el contador de la marca escogida.
        marca = marcas[int(marca)-1] # Se le asigna a la variable 'marca' el nombre de la marca escogida.
        
        serial = input("Ingrese el serial: ") # Se pide al usuario que ingrese el serial de la pipeta que va a ingresar a la base de datos.
        clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
        
        media = 0 # media es la variable que almacenara el promedio de las mediones de cada pipeta.
        print("Ingrese los resultados para 100uL")
        # Este ciclo se encarga de pedir las tres mediciones que se realizaron para el volumen de 10%
        for i in range(0,3):
            aux=float(input("Resultado "+str(i+1)+": ")) # Se pide al usuario ingresar el resultado de la i-esima medicion.
            clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
            
            #Este ciclo se encarga de verificar si la medida ingresada para el volumen de 10% cumple con el rango establecido de 90<=V<=110
            while(aux<90 or aux >110):
                print("¡ALERTA! de La medicion de 100uL esta fuera del rango aceptable.") # En caso de que se ingrese una medida no valida se mostrara el mensaje correspondiente.
                aux=float(input("Resultado "+str(i+1)+": ")) # Se pide al usuario ingresar de nuevo el resultado de la i-esima medicion.
                clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
            
            media += aux; # Se le asigna a media el valor que ya tenia mas el resultado de la i-esima medicion.            
            MCUL.append(aux) # Se añade la medicion ingresada a la lista que las almacenara.
        
        MCUL.append(media/3) # se añade el promedio de las mediciones a la lista que almacena las mediciones para un volumen de 10%.
        
        media = 0 # Se restablece el valor de media para poder calcular un nuevo promedio.  
        print("Ingrese los resultados para 1000uL")
        # Este ciclo se encarga de pedir las tres mediciones que se realizaron para el volumen de 100%
        for i in range(0,3):
            aux=float(input("Resultado "+str(i+1)+": ")) # Se pide al usuario ingresar el resultado de la i-esima medicion.
            clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
            
            #Este ciclo se encarga de verificar si la medida ingresada para el volumen de 10% cumple con el rango establecido de 900<=V<=1100
            while(aux<900 or aux >1100):
                print("¡ALERTA! de La medicion de 1000uL esta fuera del rango aceptable.") # En caso de que se ingrese una medida no valida se mostrara el mensaje correspondiente.
                aux=float(input("Resultado "+str(i+1)+": ")) # Se pide al usuario ingresar de nuevo el resultado de la i-esima medicion.
                clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
            
            media += aux # Se le asigna a media el valor que ya tenia mas el resultado de la i-esima medicion.  
            MMUL.append(aux)  # Se añade la medicion ingresada a la lista que las almacenara.
            
        MMUL.append(media/3) # se añade el promedio de las mediciones a la lista que almacena las mediciones para un volumen de 100%.
        
        # Se añaden todos los datos de la pipeta ingresada a la lista lab_metrologia siguiento el siguiente formato [marca, serial,[v1,v2,v3,media],[v1,v2,v3,media]], 
        # siendo la posicion 2 las mediciones realizadas con un volumen de 10% y la posicion 3 las realizadas para un volumen de 100% 
        lab_metrologia.append([marca, serial, MCUL, MMUL])      
    
    # Se verifica si la opcion escogida por el usuario es la numero dos
    elif(int(option) == 2):
        existeSerial = False # esxisteSerial es la variable que le dira al programa si el serial consultado esta en la base de datos.
        serial = input("Ingrese serial a consultar: ") # Se pide al usuario ingresar el serial a consultar.
        clearScreen() # Se imprimen 20 saltos de linea, dando la ilucion de que la consola es limpiada.
        
        # Este ciclo se encarga de imprmir todos los datos correspondientes a la pipeta de numero serial 'serial'
        for i in lab_metrologia:
            # Se verifica si el serial consultado existe
            if(i[1] == serial):
                existeSerial = True # En caso de que se encuentre el serial consultado el estado de esta variable es cambiado a True
                print("Informacion de la pipeta numero", serial)
                print("Marca:", i[0]) # Se imprime la marca de la pipeta correspondiente al serial consultado
                
                print("Las medidas para 100uL(10%) fueron: ")
                # Este ciclo se encarga de imprimir todas la mediciones que se ingresaron pra un volumen de 10%
                for j in range(0,3):
                    print("Medida "+str(j+1)+":", i[2][j], "uL") # Se imprime la medicion j-esima de la base de datos para 10% 
                print("Con una media de", i[2][3]) # Se imprime el promedio de las mediciones correspondientes a un volumen de 10%
                
                print("Las medidas para 1000uL(100%) fueron:")
                # Este ciclo se encarga de imprimir todas la mediciones que se ingresaron pra un volumen de 10%
                for j in range(0,3):
                    print("Medida "+str(j+1)+":", i[3][j], "uL") # Se imprime la medicion j-esima de la base de datos para 100% 
                print("Con una media de", i[3][3], "\n") #Se imprime el promedio de las mediciones correspondientes a un volumen de 10%
         
        # Se verifica si el serial consultado existe
        if(not(existeSerial)):
            print("La pipeta numero", serial, "no esta en la base de datos.\n") # En caso de que el sereial consultado no exista se imprime el mensaje correspondiente
    
    # Se verifica si la opcion escogida por el usuario es la numero tres
    elif(int(option) == 3):
        print("             Estadisticos")
        print("El numero de pipetas de la marca Brand es de:", contadorMarcas[0]) # Se imprime el numero de pipetas de la marca Brand que hay en la base de datos.
        print("El numero de pipetas de la marca 3M es de:", contadorMarcas[1]) # Se imprime el numero de pipetas de la marca 3M que hay en la base de datos.
        print("El numero de pipetas de la marca Rainin es de:", contadorMarcas[2]) # Se imprime el numero de pipetas de la Rainin Brand que hay en la base de datos.
        print("El numero de pipetas de la marca PipeteLine es de:", contadorMarcas[3]) # Se imprime el numero de pipetas de la marca PipeteLine que hay en la base de datos.
    
    # En caso de que el usuario escoja la opcion cuatro se cerrara el programa
    else:
        break; #Se rompe el ciclo infinito
  
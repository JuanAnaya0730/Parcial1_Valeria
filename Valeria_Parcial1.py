'''
        PARCIAL 1 BIOINGENIERIA

Valeria Giraldo Agudelo
Grupo 2

Universidad de Antioquia
Medellin - Antioquia
Abril 2021

'''
def clearScreen():
    print("\n"*20)

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

lab_metrologia = []
marcas = ["Brand", "3M", "Rainin", "PipeteLine"]
contadorMarcas = [0,0,0,0]

while True:
    
    MCUL = [] # Mediciones de 100uL
    MMUL = [] # Mediciones de 1000uL
       
    Menu() # Se imprime en consola el menu de opciones
    option = input("Opcion: ") # option es la variable que almacenara la opcion escogida por el usuario
    clearScreen()
    
    # Este ciclo se encarga de verficar si la opcion escogida por el usuario es valida
    while(option.isnumeric() == False or int(option)<1 or int(option)>4):
        print("Opcion invalida.\n") # Se advierte al usuario que la opcion ingresada es invalida
        Menu() # Se imprime en consola el menu de opciones
        option = input("Opcion: ") # Se le pide al usuario que ingrese una nueva opcion
        clearScreen()
       
    if(int(option) == 1):
        Marca()
        marca = input("Marca: ")
        clearScreen()
        
        while(marca.isnumeric() == False or int(marca)<1 or int(marca)>4):
            print("Marca no existente.\n") # Se advierte al usuario que la opcion ingresada es invalida
            Marca() # Se imprime en consola el menu de opciones
            marca = input("Opcion: ") # Se le pide al usuario que ingrese una nueva opcion
            clearScreen()
        
        contadorMarcas[int(marca)-1] += 1
        marca = marcas[int(marca)-1]
        
        serial = input("Ingrese el serial: ") 
        clearScreen()
        
        media = 0
        print("Ingrese los resultados para 100uL")
        for i in range(0,3):
            aux=float(input("Resultado "+str(i+1)+": "))
            clearScreen()
            
            while(aux<90 or aux >110):
                print("¡ALERTA! de La medicion de 100uL esta fuera del rango aceptable.")
                aux=float(input("Resultado "+str(i+1)+": "))
                clearScreen()
            
            media += aux;            
            MCUL.append(aux)
        
        MCUL.append(media/3)
        
        media = 0        
        print("Ingrese los resultados para 1000uL")
        for i in range(0,3):
            aux=float(input("Resultado "+str(i+1)+": "))
            clearScreen()
            
            while(aux<900 or aux >1100):
                print("¡ALERTA! de La medicion de 1000uL esta fuera del rango aceptable.")
                aux=float(input("Resultado "+str(i+1)+": "))
                clearScreen()
            
            media += aux
            MMUL.append(aux)
            
        MMUL.append(media/3)
        
        lab_metrologia.append([marca, serial, MCUL, MMUL])      
                      
    elif(int(option) == 2):
        existeSerial = False
        serial = input("Ingrese serial a consultar: ")
        clearScreen()
        
        for i in lab_metrologia:
            if(i[1] == serial):
                existeSerial = True
                print("Informacion de la pipeta numero", serial)
                print("Marca:", i[0])
                
                print("Las medidas para 100uL(10%) fueron: ")
                for j in range(0,3):
                    print("Medida "+str(j+1)+":", i[2][j], "uL")
                print("Con una media de", i[2][3])
                
                print("Las medidas para 1000uL(100%) fueron:")
                for j in range(0,3):
                    print("Medida "+str(j+1)+":", i[3][j], "uL")
                print("Con una media de", i[3][3], "\n")
                
        if(not(existeSerial)):
            print("La pipeta numero", serial, "no esta en la base de datos.\n")
    
    elif(int(option) == 3):
        print("             Estadisticos")
        print("El numero de pipetas de la marca Brand es de:", contadorMarcas[0])
        print("El numero de pipetas de la marca 3M es de:", contadorMarcas[1])
        print("El numero de pipetas de la marca Rainin es de:", contadorMarcas[2])
        print("El numero de pipetas de la marca PipeteLine es de:", contadorMarcas[3])
    
    else:
        break;
    
    
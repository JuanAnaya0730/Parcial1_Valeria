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
MCUL = [] # Mediciones de 100uL
MMUL = [] # Mediciones de 1000uL
marcas = ["Brand", "3M", "Rainin", "PipeteLine"]

while True:
    
    clearScreen()
    
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
        
        marca = marcas[int(marca)-1]
        
        serial = input("Ingrese el serial: ") 
        clearScreen()
        
        print("Ingrese los resultados para 100uL")
        for i in range(0,3):
            aux=int(input("Resultado "+str(i+1)+": "))
            clearScreen()
            
            while(aux<90 or aux >110):
                print("¡ALERTA! de La medicion de 100uL esta fuera del rango aceptable.")
                aux=int(input("Resultado "+str(i+1)+": "))
                clearScreen()
                
            MCUL.append(aux)
        
        print("Ingrese los resultados para 1000uL")
        for i in range(0,3):
            aux=int(input("Resultado "+str(i+1)+": "))
            clearScreen()
            
            while(aux<900 or aux >1100):
                print("¡ALERTA! de La medicion de 100uL esta fuera del rango aceptable.")
                aux=int(input("Resultado "+str(i+1)+": "))
                clearScreen()
                
            MMUL.append(aux)
        
        lab_metrologia.append([marca, serial, MCUL, MMUL])
        print(lab_metrologia)        
                      
    elif(int(option) == 2):
        print("El usuario va a consultar informacion.")
    
    elif(int(option) == 3):
        print("El usuario quiere ver estadisticas.")
    
    elif(int(option) == 4):
        break;
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
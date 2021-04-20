'''
        PARCIAL 1 BIOINGENIERIA

Valeria Giraldo Agudelo
Grupo 2

Universidad de Antioquia
Medellin - Antioquia
Abril 2021

'''

def Menu():
    # Esta funcion se encarga de imprimir un menu de opciones
    print("Menu:\n",
          "1. Ingresar informacion de una pipeta.\n",
          "2. Consultar informacion de una pipeta.\n",
          "3. Estadisticos.\n",
          "4. Salir.")

while True:
    
    Menu() # Se imprime en consola el menu de opciones
    option = input("Opcion: ") # option es la variable que almacenara la opcion escogida por el usuario
    
    # Este ciclo se encarga de verficar si la opcion escogida por el usuario es valida
    while(option.isnumeric() == False or int(option)<1 or int(option)>4):
        print("Opcion invalida.\n") # Se advierte al usuario que la opcion ingresada es invalida
        Menu() # Se imprime en consola el menu de opciones
        option = input("Opcion: ") # Se le pide al usuario que ingrese una nueva opcion
       
    if(int(option) == 1):
        print("El usuario debe ingresar informacion de una pipeta.")
        
    elif(int(option) == 2):
        print("El usuario va a consultar informacion.")
    
    elif(int(option) == 3):
        print("El usuario quiere ver estadisticas.")
    
    elif(int(option) == 4):
        print("El usuario quiere salir.")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
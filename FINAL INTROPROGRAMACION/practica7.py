#Hacer un programa en el que ingresas 
# un número que representa cierta cantidad de una fruta y divides esa cantidad por 3 chicos.
# Mostrar por pantalla el resultado
# Pedir al usuario su edad y mostrar si es mayor o no de edad
def dividir_frutas_entre_ninos():
    try:
        # Solicitar al usuario que ingrese la cantidad de frutas
        cantidad_frutas = int(input("Ingresa la cantidad de frutas: "))
        
        # Calcular la cantidad de frutas por niño (división entre tres)
        frutas_por_nino = cantidad_frutas / 3
        
        # Mostrar el resultado
        print(f"Cada niño recibirá {frutas_por_nino} frutas.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar la primera parte del programa
dividir_frutas_entre_ninos()
##############parte 2 VERIFICAR SI EL USUARIO ES MAYOR DE EDAD ###########################
def verificar_edad():
    try:
        # Solicitar al usuario que ingrese su edad
        edad = int(input("Ingresa tu edad: "))
        
        # Verificar si es mayor de edad (mayor o igual a 18 años)
        if edad >= 18:
            print("Eres mayor de edad.")
        else:
            print("Eres menor de edad.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar la segunda parte del programa
verificar_edad()

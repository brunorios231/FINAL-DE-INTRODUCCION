#Diseñar un algoritmo que calcule la superficie de un triángulo 
# a partir del ingreso de su base y altura y muestre por pantalla el resultado, 
# con el mensaje “La superficie del triángulo es:.”.
def calcular_superficie_triangulo():
    try:
        # Solicitar al usuario que ingrese la base y la altura del triángulo
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        
        # Calcular la superficie del triángulo
        superficie = (base * altura) / 2
        
        # Mostrar el resultado por pantalla
        print(f"La superficie del triángulo es: {superficie}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa números decimales para la base y la altura.")

# Llamar a la función para ejecutar el programa
calcular_superficie_triangulo()


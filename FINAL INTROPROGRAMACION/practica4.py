#Hacer un programa que ingresas la edad de una persona 
# y calcula cuántos años va a tener dentro de 23 años.
# Mostrar el resultado por pantalla.
def calcular_edad_futura():
    try:
        # Pedir al usuario que ingrese su edad actual
        edad_actual = int(input("Ingresa tu edad actual: "))
        
        # Calcular la edad futura dentro de 23 años
        edad_futura = edad_actual + 23
        
        # Mostrar el resultado
        print(f"En 23 años, tendrás {edad_futura} años.")
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar el programa
calcular_edad_futura()


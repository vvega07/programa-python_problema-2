# =============================================================================
# FASE 5 - EVALUACIÓN FINAL - FUNDAMENTOS DE PROGRAMACIÓN
# PROGRAMA: PEDIDOS CON COMAS (VERSION SIMPLIFICADA)
# ESTUDIANTE: VÍCTOR VEGA DELGADO
# CÉDULA: C.C. 1005967518
# =============================================================================

# 1. MATRICES / LISTAS: Menú con los datos base
matriz_productos = [
    ["Hamburguesa Sencilla", "Plato Fuerte", 15000],
    ["Pizza Familiar", "Plato Fuerte", 35000],
    ["Gaseosa 350ml", "Bebida", 4000],
    ["Cerveza Artesanal", "Bebida", 12000],
    ["Helado de Vainilla", "Postre", 8000],
    ["Tiramisú de la Casa", "Postre", 14000]
]

# 2. FUNCIONES / MÓDULOS: Operación matemática básica
def calcular_precio_final_cuenta(total_acumulado):
    """
    Recibe la suma total. Si pasa de 35000, resta el 15%.
    Si no, deja el precio normal.
    """
    if total_acumulado > 35000:
        descuento = total_acumulado * 0.15
        precio_con_descuento = total_acumulado - descuento
        return precio_con_descuento
    
    return total_acumulado


# 3. MENÚ INTERACTIVO Y CICLOS REPETITIVOS
def iniciar_sistema_restaurante():
    # Variables globales de la sesión para acumular los datos
    total_cuenta_base = 0.0
    productos_seleccionados = []
    
    # Ciclo repetitivo 'while' para el menú principal
    while True:
        print("\n=== MENÚ INTERACTIVO ===")
        print("1. Hacer pedido (Separado por comas)")
        print("2. Ver mi cuenta total y promoción")
        print("3. Reiniciar cuenta a $0")
        print("4. Salir del programa")
        print("========================")
        
        opcion = input("Escriba el número de la opción (1-4): ")
        
        if opcion == "1":
            print("\n--- PLATOS DISPONIBLES ---")
            
            # Ciclo 'for' para mostrar el menú de forma sencilla
            numero = 1
            for prod in matriz_productos:
                nombre = prod[0]
                precio = prod[2]
                print(str(numero) + ". " + nombre + " = $" + str(precio))
                numero = numero + 1
            
            print("\nEjemplo para pedir: 1,2,5")
            entrada = input("Escriba los números de su pedido separados por comas: ")
            
            # Convertimos el texto en una lista de números cortando por las comas
            lista_numeros = entrada.split(",")
            
            # Ciclo 'for' para procesar cada número que escribió el usuario
            for num in lista_numeros:
                indice = int(num) # Convertimos el texto a número entero
                
                # Buscamos el producto en la matriz usando el número
                producto_elegido = matriz_productos[indice - 1]
                
                # Guardamos el nombre y sumamos el precio al acumulador
                productos_seleccionados.append(producto_elegido[0])
                total_cuenta_base = total_cuenta_base + producto_elegido[2]
                
                print("-> Agregado: " + producto_elegido[0])
                
            print("\nSubtotal guardado. Revise su cuenta en la opción 2.")
            
        elif opcion == "2":
            print("\n--- RESUMEN DE SU CUENTA ---")
            
            if total_cuenta_base == 0.0:
                print("No ha pedido nada todavía.")
            else:
                print("Productos pedidos:")
                for item in productos_seleccionados:
                    print(" * " + item)
                
                print("----------------------------")
                # Llamamos a nuestra función pasándole la suma acumulada
                total_final = calcular_precio_final_cuenta(total_cuenta_base)
                
                print("SUMA TOTAL PRECIOS BASE: $" + str(total_cuenta_base))
                
                # Revisamos si hubo descuento comparando los totales
                if total_final < total_cuenta_base:
                    ahorro = total_cuenta_base - total_final
                    print("DESCUENTO DEL 15% APLICADO: -$" + str(ahorro))
                    print("TOTAL FINAL CON PROMO: $" + str(total_final))
                    print("¡Se aplicó el descuento por pasar los $35.000!")
                else:
                    print("DESCUENTO DEL 15% APLICADO: $0.0")
                    print("TOTAL FINAL A PAGAR: $" + str(total_final))
                    print("No alcanzó el umbral de $35.000 para la promoción.")
                    
        elif opcion == "3":
            total_cuenta_base = 0.0
            productos_seleccionados = []
            print("\nCuenta reiniciada a cero.")
            
        elif opcion == "4":
            print("\n¡Gracias por usar el programa! Saliendo...")
            break # Termina el ciclo while
            
        else:
            print("\nOpción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    iniciar_sistema_restaurante()
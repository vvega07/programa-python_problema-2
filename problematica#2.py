# =============================================================================
# FASE 5 - EVALUACIÓN FINAL POA - FUNDAMENTOS DE PROGRAMACIÓN
# PROGRAMA: SISTEMA DE GESTIÓN DE PRECIOS Y PROMOCIONES DE UN RESTAURANTE
# ESTUDIANTE: VÍCTOR VEGA DELGADO
# GRUPO: 213022A_2201
# CURSO: FUNDAMENTOS DE LA PROGRAMACIÓN
# =============================================================================

# 1. MATRICES / LISTAS (Almacenamiento de productos, categorías y precios base)
matriz_productos = [
    ["Hamburguesa Sencilla", "Plato Fuerte", 15000],
    ["Pizza Familiar", "Plato Fuerte", 35000],
    ["Gaseosa 350ml", "Bebida", 4000],
    ["Cerveza Artesanal", "Bebida", 12000],
    ["Helado de Vainilla", "Postre", 8000],
    ["Tiramisú de la Casa", "Postre", 14000],
    ["Ensalada César", "Plato Fuerte", 18000],
    ["Limonada Natural", "Bebida", 5000],
    ["Brownie con Helado", "Postre", 10000],
    ["bistec a la parrilla", "Plato Fuerte", 22000],
    ["Agua Mineral 500ml", "Bebida", 3000],
    ["Cheesecake de Fresa", "Postre", 12000],
]

# 2. FUNCIONES / MÓDULOS (Descuento general del 15% si supera el umbral de $35.000)
def calcular_precio_final_cuenta(total_acumulado, umbral_precio=35000):
    if total_acumulado > umbral_precio:
        descuento = total_acumulado * 0.15
        return total_acumulado - descuento
    return total_acumulado

# 3. CICLOS REPETITIVOS (Menú interactivo para realizar pedidos, ver cuenta y reiniciar)
def iniciar_sistema_restaurante():
    total_cuenta_base = 0.0
    productos_seleccionados = []
    umbral_promocion = 35000
    
    while True:
        print("\n" + "="*55)
        print(" SISTEMA DE PEDIDOS EXPRESS RESTAURANTE")
        print("="*55)
        print("1. Ver menú y escoge tu pedido ")
        print("2. Ver mi cuenta actual")
        print("3. Reiniciar mi cuenta ")
        print("4. Salir del programa")
        print("="*55)
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            print("\n" + "-"*15 + " PRODUCTOS EN EL MENÚ " + "-"*15)
            
            # Mostramos el menú de productos con su número, nombre, categoría y precio
            numero = 1
            for prod in matriz_productos:
                print(f"{numero}. {prod[0]:<22} | {prod[1]:<12} | Precio: ${prod[2]:,.2f}")
                numero = numero + 1
            
            print("-" * 52)
            print("para agregar productos a tu cuenta, estan numerados del 1 al 12.")
            entrada_usuario = input("Ingrese los números de sus productos separados por COMAS: ")
            
            #  usamos el método split para dividir la entrada del usuario en partes individuales basadas en las comas
            partes = entrada_usuario.split(',')
            
            print("\n--- PROCESANDO TU PEDIDO ---")
            
            # Recorremos cada parte ingresada por el usuario para validar y agregar a la cuenta
            for parte in partes:
                if parte.strip().isnumeric():
                    indice = int(parte) # Convertimos la parte a número entero para usarlo como índice
                    
                    if 1 <= indice <= len(matriz_productos):
                        prod_elegido = matriz_productos[indice - 1]
                        
                        productos_seleccionados.append(prod_elegido[0])
                        total_cuenta_base += prod_elegido[2]
                        
                        print(f"[OK] se añadió tu pedido {prod_elegido[0]} (${prod_elegido[2]:,.2f})")
                    else:
                        print(f"[ERROR] El número '{indice}' no está en el menú. vuelve a intentarlo.")
                else:
                    # Si ingresamos una letra o lo dejamos vacío mostramos un error simple
                    if parte.strip() != "":
                        print(f"[ERROR] '{parte}' no es un número válido. vuelve a intentarlo.")
            
            print(f"\nSubtotal acumulado de tu cuenta: ${total_cuenta_base:,.2f}")
            
        elif opcion == '2':
            print("\n" + "-"*15 + " RESUMEN DE TU FACTURA " + "-"*15)
            if not productos_seleccionados:
                print("No has agregado ningún producto. Ve a la Opción 1.")
            else:
                print("productos seleccionados de tu cuenta:")
                for item in productos_seleccionados:
                    print(f" * {item}")
                print("-"*52)
                
                total_cuenta_final = calcular_precio_final_cuenta(total_cuenta_base, umbral_promocion)
                
                print(f"SUMA TOTAL PRECIOS BASE:          ${total_cuenta_base:,.2f}")
                
                if total_cuenta_final < total_cuenta_base:
                    ahorro = total_cuenta_base - total_cuenta_final
                    print(f"DESCUENTO GENERAL (15% APLICADO): -${ahorro:,.2f}")
                    print(f"TOTAL FINAL CON PROMO A PAGAR:    ${total_cuenta_final:,.2f}")
                    print("\n¡Genial! Tu cuenta superó los $35.000 y se aplicó la promoción.")
                else:
                    print(f"DESCUENTO GENERAL (15% APLICADO): $0.00")
                    print(f"TOTAL FINAL A PAGAR:              ${total_cuenta_final:,.2f}")
                    print(f"\nNota: Te faltan ${umbral_promocion - total_cuenta_base:,.2f} para activar el descuento.")
                    print("Agrega más productos a tu cuenta para aprovechar la promoción.")
            print("-" * 52)
            
        elif opcion == '3':
            productos_seleccionados = []
            total_cuenta_base = 0.0
            print("\n[INFO] Cuenta vaciada. Puedes iniciar un nuevo pedido múltiple.")
            
        elif opcion == '4':
            print("\n¡Gracias por tu compra! Cerrando el sistema...")
            break
        else:
            print("\n[ERROR] Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    iniciar_sistema_restaurante()
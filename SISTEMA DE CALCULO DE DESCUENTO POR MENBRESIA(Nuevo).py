# Pedimos al usuario el valor de la compra con validación
while True:
    try:
        valor_compra = float(input("Ingrese el valor de la compra: "))
        if valor_compra < 0:
            print("Error: El valor no puede ser negativo.")
            continue
        break  # sale del bucle si todo está bien
    except ValueError:
        print("Error: Debes ingresar un número válido.")

# Pedimos el tipo de cliente (normal o premium) con validación
while True:
    tipo_cliente = input("Ingrese el tipo de cliente (normal/premium): ").lower()
    if tipo_cliente in ["normal", "premium"]:
        break
    else:
        print("Error: Debes escribir 'normal' o 'premium'.")

# Calculamos el descuento
if tipo_cliente == "premium":
    descuento = valor_compra * 0.15  # 15% de descuento
else:
    descuento = 0  # No hay descuento

# Calculamos el total a pagar
total_pagar = valor_compra - descuento

# Mostramos los resultados
print("\n--- Resumen de la compra ---")
print("Valor de la compra:", valor_compra)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)
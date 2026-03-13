# Pedimos al usuario el valor de la compra
valor_compra = float(input("Ingrese el valor de la compra: "))

# Pedimos el tipo de cliente (normal o premium)
tipo_cliente = input("Ingrese el tipo de cliente (normal/premium): ")

# Verificamos si el cliente es premium
if tipo_cliente.lower() == "premium":
    descuento = valor_compra * 0.15  # Calculamos el 15% de descuento
else:
    descuento = 0  # Si no es premium, no hay descuento

# Calculamos el total a pagar
total_pagar = valor_compra - descuento

# Mostramos el resultado final
print("El total a pagar es:", total_pagar)
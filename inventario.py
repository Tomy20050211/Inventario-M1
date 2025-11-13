# Bucle que se repite hasta que todos los datos sean válidos
while True:
    print("Welcome to the inventory \n---------------------")
    
    # Pedir el nombre del producto
    name = input("Enter the product name: ")
    # Validar que el nombre solo tenga letras
    if not name.isalpha():
        print("Error: Name must contain only letters. Please try again...")
        continue  
    
    # Pedir el precio del producto
    priceInput = input("Enter the product price: ")
    # Validar que el precio sea un número
    if not priceInput.replace('.', '', 1).isdigit():
        print("Error: Price must be a number. Please try again...")
        continue
    # Convertir el precio a decimal
    price = float(priceInput)
    
    # Pedir la cantidad del producto
    quantityInput = input("Enter the quantity: ")
    # Validar que la cantidad sea un número entero
    if not quantityInput.isdigit():
        print("Error: Quantity must be a number. Please try again...")
        continue
    # Convertir la cantidad a número entero
    quantity = int(quantityInput)
    
    # Salir del bucle si todo es correcto
    break  

# Calcular el precio total
totalPrice = price * quantity

# Mostrar el resumen del inventario
print(f"YOUR INVENTORY\n"
      f"-----------\n"
      f"Name product: {name}\n"
      f"Price product: {price}\n"
      f"Quantity product: {quantity}\n"
      f"Total price: {totalPrice}")

"""
RESUMEN:
Este programa gestiona un inventario básico. Pide al usuario el nombre, precio y 
cantidad de un producto. Valida que los datos sean correctos y calcula el precio 
total. Al final muestra toda la información del producto ingresado.
"""
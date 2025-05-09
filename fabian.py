# Presentacion
print("/////////////////////////////////////")
print("           Tienda Ara               ")
print("/////////////////////////////////////")

# Ingreso de credenciales de la tienda
# El usuario: Ara----- Contraseña es: Ara123
tiendaCorrecto = ""
tiendaUsuario = "Ara"
contraseñaCorrecta = "Ara123"
contraseñaTienda = ""

while tiendaCorrecto != tiendaUsuario:
    tiendaCorrecto = str(input("Ingresa el usuario de la tienda=> "))
else:
    print("Usuario correcto!")
    print()

while contraseñaTienda != contraseñaCorrecta:
    contraseñaTienda = str(input("Ingresa contraseña de la tienda=> "))
else:
    print("Contraseña correcta! ")
print("Bienvenido a Tiendas Riwi!")


# lista de inventario vacia
inventario = []


# funciones para añadir los productos
def Añadir_productos(nombre, precio, cantidad):
    # Añade un nuevo producto al inventario.
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print("Error, el producto ya exite en el inventario")
            return
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Has añadido un producto!")


# funcion para buscar productos
def Busca_productos(nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto


# funcion para actulializar lista
def actualizar_lista(nombre, nuevo_precio):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["precio"] = nuevo_precio
            print("Precio actualizado!")
            return
    print("Error, producto no encotrado!")


# funcion para eliminar productos
def eliminar_productos(nombre):
    for i in range(len(inventario)):
        if inventario[i]["nombre"].lower() == nombre.lower():
            del inventario[i]
            print("Producto eliminado!")
            return
    print("Error, producto no encontrado")


# funcion para mostrar el inventario
"""def productos_inventario(inventario):
    for producto_inventarios in inventario:
        if producto_inventarios
   """

# Funcion lambda para calcular el valor total


def calcular_valor_total():
    return sum(p["precio"] * p["cantidad"] for p in inventario)


# Funcion para validar numeros
def validar_numero(mensaje, tipo=float):
    while True:
        entrada = input(mensaje)
        try:
            valor = tipo(entrada)
            if valor < 0:
                print("Error, el valor no debe ser negativo")
                continue
            return valor
        except ValueError:
            print(f"Error, debes ingresar un numero valido ({tipo.__name__})")


# Colecciones:
def main():
    # funcion para interactuar con el menu
    while True:
        print("\n--  Menu de inventario---")
        print("1. Añadir nuevos productos 🛒")
        print("2. Buscar productos 🔎")
        print("3. Actulizar precios💸")
        print("4. Eliminar productos🆑🛒")
        print("5. Mostrar inventario📦")
        print("6. Valor total del inventario💵")
        print("7. Salir ⏻")

        opcion = input("Selecciona una opcion (1-6): ")

        if opcion == "1":
            print("\nNuevo producto")
            nombre = input("Nombre del producto: ").strip()

            if not nombre:
                print("Error, el nombre no puede estar vacio.")
                continue

            precio = validar_numero("Precio del producto: ", float)
            cantidad = validar_numero("Cantidad en stock: ", int)
            Añadir_productos(nombre, precio, cantidad)

        if opcion == "2":
            print("\nBuscar producto")
            nombre = input("nombre del producto a buscar: ").strip()
            productos = Busca_productos(nombre)

            if productos:
                print("\nDatos del producto:")
                print(f"nombre: {productos['nombre']}")
                print(f"precio: ${productos['precio']:.2f}")
                print(f"cantidad: {productos['cantidad']}")
            else:
                print("Producto no encontrado en el inventario")

        if opcion == "3":
            print("\nActualizar precio")
            nombre = input("nombre del producto: ").strip()

            if Busca_productos(nombre):
                nuevo_precio = validar_numero("nuevo precio: ", float)
                actualizar_lista(nombre, nuevo_precio)
            else:
                print("Producto no encontrado")

        if opcion == "4":
            print("\nEliminar productos")
            nombre = input("nombre del producto al que quieres eliminar: ").strip()
            eliminar_productos(nombre)

        if opcion == "5":
            print(f"Este es tu inventario {inventario}")

        if opcion == "6":
            total = calcular_valor_total()
            print(f"\nValor total del inventario: ${total:.2f}")

        elif opcion == "7":
            print("\nExit...")
            break
        else:
            print()


# Ejecutar el programa
if __name__ == "__main__":
    main()

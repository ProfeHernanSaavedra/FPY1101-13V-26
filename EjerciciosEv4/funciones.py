
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre == "" :
        print("El nombre no puede ser vacío")
        return

    if nombre in productos:
        print("El producto ya existe")
        return

    stock = int(input("Ingrese stock del producto: "))
    while True:
        try:
            precio = int(input("Ingrese precio $:"))
            if precio > 0 :
                break
        except ValueError:
            print("Deber ser un número, por favor vuelva a intentar")
    
    productos[nombre] = [stock,precio]
    #productos[teclado] = [2,11500]
    print("Dato agregado correctamente!")

def mostrar_productos(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return
    for nombre in productos:
        print(f"- {nombre}  - {productos[nombre][0]} - ${productos[nombre][1]}")


def buscar_producto(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return
    
    nombre = input("Nombre producto a buscar: ").strip()

    if nombre in productos:
        print("Producto encontrado")
        print("Stock : ",productos[nombre][0])
        print("Precio : $",productos[nombre][1])
    else:
        print("Producto no existe o agotado")

def producto_mas_caro(productos):
    
    if len(productos) == 0 :
        print("No existen productos")
        return
    
    mayor = 0
    mayorNombre = ""
    for nombre in productos:
        precio = productos[nombre][1]

        if precio > mayor :
            mayor = precio
            mayorNombre = nombre
    print(f"Producto mas caro es: {mayorNombre}")
    print(f"Su precio es: ${mayor}")

print("FIN")

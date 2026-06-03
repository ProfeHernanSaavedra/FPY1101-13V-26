'''productos = {
    "Mouse" : [10,15000],
    "Teclado" : [5,25000],
    "Monitor" : [3,180000]
}'''
import funciones as fn
#codigo ppal
productos = {}

while True:
    print("---MENU---")
    print("1. Agregar Producto")
    print("2. Mostrar Producto")
    print("3. Buscar Producto")
    print("4. Producto más caro")
    print("5. Salir")

    while True:
        try:
            op = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("La opción debe ser un número")
    if op == 1 :
        fn.agregar_producto(productos)
        #print("Agregar")
    elif op == 2 :
        fn.mostrar_productos(productos)
        #print(productos)
    elif op == 3 :
        fn.buscar_producto(productos)
        #print("Buscar")
    elif op == 4:
        fn.producto_mas_caro(productos)
        #print("Mas caro")
    elif op == 5:
        print("Saliendo del sistema..")
        break
    else:
        print("Opción no válida, debe estar entre 1 y 5")



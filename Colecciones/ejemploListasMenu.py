def ingresar() :
    print("Ingresando datos")
    dato = input("Ingrese su nombre: ")
    nombres.append(dato)

def eliminar() :
    print("Eliminando datos...")
    print("Los datos de la lista son: ")
    print(nombres)
    dato = input("Ingrese dato a eliminar: ")
    nombres.remove(dato)

def mostrar():
    print("Mostrar Lista")
    for elemento in nombres:
        print(elemento)

#Ingrese nombres usando menus
nombres = []
while True:
    print("---- MENU -----")
    print("1. Ingrese nombre")
    print("2. Eliminar nombre")
    print("3. Mostrar lista")
    print("4. Salir")
    while True:

        try:
            op = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Debe ingresar un valor numerico, Intente nuevamente!!")

    if op == 1 :
        ingresar()
    elif op == 2 :
        eliminar()

    elif op == 3 :
        mostrar()
    elif op == 4:
        print("Saliendo...")
        break
    else:
        print("Opción no válida")

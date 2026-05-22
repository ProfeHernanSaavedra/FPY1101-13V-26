#creando funciones
def sumarFijo():
    '''este es um ejemplo de funcion, que suma dos numeros
        n1:3
        n2: 4
    '''
    n1 = 3
    n2 = 4
    sumar = n1 + n2 
    print(sumar)

def sumar(num1,num2):
    '''Esta función sirve para sumar dos números que se 
        se ingresan por parámetros, num1, num2
        '''
    suma = num1 + num2
    return suma

def resta(n1,n2):

    resta = n1 - n2
    return resta

sumarFijo()
print("SUMANDO")
nu1 = int(input("Ingrese número 1: "))
nu2 = int(input("Ingrese número 2: "))
resultado = sumar(nu1,nu2)
print(resultado)
print("RESTANDO")
n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
result = resta(n1,n2)
print(result)

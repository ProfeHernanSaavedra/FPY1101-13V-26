#creando funciones
from math import pi

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

def areaCirculo(radio):
    area = pi*(radio**2)
    return area

def perimetroCirculo(radio):
    per = 2*pi*radio
    return per

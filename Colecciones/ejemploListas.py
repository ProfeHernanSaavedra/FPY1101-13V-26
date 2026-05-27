nombres = [] # declaro lista

nombres = ["juan","pedro","diego"]
#        i    0     1      2
# J U A N
# 0 1 2 3

print(nombres[2])
print(nombres) # imprimo toda la lista

for i in range(3):
    print(nombres[i])
print()
for elemento in nombres:
    print(elemento)

nombres.append("Francisca")
nombres.append(24)

print(nombres)

nombres.remove(24)

print(nombres)

nombres.insert(2,"Maria")
print(nombres)

nombres.reverse()
print(nombres)

nombres.sort() # ordenar de menor a mayor, pero solo numeros o solo letras/palabras
print(nombres)


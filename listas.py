#2.Crea una lista vacía llamada departamentos Colombia, pida al usuario la cantidad de departamentos a ingresar, a través de un ciclo for pida al usuario que ingrese el departamento de Colombia que desee, agregue esta información a la lista y luego esta sea ordenada en orden descendente.
#a. Se debe imprimir la lista con los valores organizados de forma descendentes.
#b. Debe imprimir además los 2 últimos departamentos ingresados

departamentos_colombia = []

cantidad_departamentos = int(input("Ingrese la cantidad de departamentos que desea ingresar: "))

for i in range(cantidad_departamentos):
    departamento = input(f"Ingrese el departamento {i+1}: ")
    departamentos_colombia.append(departamento)

departamentos_colombia.sort(reverse=True)

print("La lista de departamentos ordenada en orden descendente es:")
print(departamentos_colombia)

print(f"Los dos últimos departamentos ingresados son: {departamentos_colombia[-2:]}")

#3.crea una lista vacía llamada números, a través de un bucle for o while pide al usuario que ingrese números enteros, agrega los números a la lista y luego ordena esta de forma ascendente y descendente. Mostrar ambas listas (ascendente y descendente)

numeros = []

while True:
    numero = input("Ingrese un número entero (o 'fin' para terminar): ")
    if numero.lower() == 'fin':
        break
    try:
        numero_entero = int(numero)
        numeros.append(numero_entero)
    except ValueError:
        print("Debe ingresar un número entero válido.")

numeros_ascendente = sorted(numeros)

numeros_descendente = sorted(numeros, reverse=True)

print("La lista de números en orden ascendente es:")
print(numeros_ascendente)
print("La lista de números en orden descendente es:")
print(numeros_descendente)
#1.Crear una tupla con números que usted desee, crear dos tuplas vacías llamadas par y la otra impar. A través de un ciclo for recorrer la tupla numérica si el numero evaluado es para ingresar el valor a la tupla par, de lo contrario insertar a la tupla impar
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
par = ()
impar = ()

for num in numeros:
    if num % 2 == 0:
        par += (num,)
    else:
        impar += (num,)

print("Tupla par:", par)
print("Tupla impar:", impar)

#2.Crear una tupla con diferentes valores numéricos o cadenas de texto, crear un programa que muestre el elemento mayor y menor de la tupla usando la función correspondiente
tupla = (10, 5, 20, 30, 15, 25)

mayor = max(tupla)
print("El elemento mayor es:", mayor)

menor = min(tupla)
print("El elemento menor es:", menor)

#3.Crea una tupla numérica, pide al usuario que ingrese un número y crea un programa que cuente cuantas veces está el numero ingresado en la tupla, de lo contrario muestre que el número no se encuentra
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero = int(input("Ingrese un número: "))
contador = 0

for num in tupla:
    if num == numero:
        contador += 1

if contador == 0:
    print("El número no se encuentra en la tupla.")
else:
    print(f"El número {numero} se encuentra {contador} veces en la tupla.")

#4.Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono. Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar más. No se podrán meter nombres repetidos. Debe imprimir el diccionario creado
contactos = {}
while True:
    nombre = input("Ingrese el nombre del contacto (o 'no' para terminar): ")
    if nombre == "no":
        break
    if nombre in contactos:
        print("El nombre ya existe en la lista de contactos. Por favor, ingrese otro nombre.")
        continue
    telefono = input("Ingrese el número de teléfono del contacto: ")
    contactos[nombre] = telefono

print("Lista de contactos:")
print(contactos)


#5.Teniendo en cuenta el punto anterior, crea un programa que solicite al usuario la clave(usuario) y muestre el teléfono correspondiente
clave = input("Ingrese el nombre del contacto para mostrar su teléfono: ")
if clave in contactos:
    print("El número de teléfono de", clave, "es:", contactos[clave])
else:
    print("El nombre no se encuentra en la lista de contactos.")

#6.Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla.
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

indice = int(input("Ingrese un índice para mostrar el valor correspondiente de la tupla: "))

if indice < 0 or indice >= len(tupla):
    print("El índice ingresado está fuera de rango.")
else:
    valor = tupla[indice]
    print(f"El valor correspondiente al índice {indice} es: {valor}.")
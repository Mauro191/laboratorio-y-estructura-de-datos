lista= ['a','b','c']

for letra in lista:
    numero_de_letra= lista.index(letra) + 1
    print("Letra : " + letra+f" su posion en la lista es: {numero_de_letra}")

lista_nombres = ["laura","fernando","cristina","sergio","manuel","alejandra"]

for nombre in lista_nombres:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f"El nombre que comieza con el L es {nombre}")


numeros= [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor +numero

print(mi_valor)


for numero in [1,2,3,4]:
    print(numero)

for lista in [[1,2],[3,4]]:
    print()

for a,b in [[1,2],[3,4]]:
    print(a)
    print(b)

dic = {"clave1":1,"clave2":2, "clave3":3}

for clave in dic.keys():
    print(clave)

for valor in dic.values():
    print(valor)

for a,b in dic.items():
    print(a,b)




# Práctica Loop For 1
# Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

# Por ejemplo: "Hola María"

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f"hola {alumno}.")


# Práctica Loop For 2
# Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros= 0
for numero in lista_numeros:
    suma_numeros=suma_numeros+numero
    print(suma_numeros)

# Práctica Loop For 3
# Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:
suma_pares=list()
suma_impares=list()
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares.append(numero)
    else :
        suma_impares.append(numero)



# *Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar

# num % 2 == 0 (valores pares)

# num % 2 == 1 (valores impares)

moneda = 0
while moneda != 10 :
    print(moneda)
    moneda = moneda+ 1
else:
    print("termino ")




# Práctica Loop While 1
# Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.

numero = 10



# Práctica Loop While 2
# Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:

# - Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

# - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).

numero = 50






# Práctica Interrupción de Flujo
# Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# No debes cambiar el orden de la lista.




for numero in range(0,20,2):
    print(numero)

lista = list(range(0,100))


# Práctica Rango 1
# Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.


# Práctica Rango 2
# Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.



# Práctica Rango 3
# Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.

# Para ello:

# Crea un rango de valores que puedas recorrer en un loop

# Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).

# Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.


lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)
for indice,item in enumerate(range(50,55)):
    print(indice,item)



# Práctica Enumerador 1
# Imprime en pantalla frases como la siguiente:

# '{nombre} se encuentra en el índice {indice}'

# Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().

# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.

# Tip: utiliza loops!




# Práctica Enumerador 2
# Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

# Llama a la lista obtenida con el nombre de variable lista_indices .




# Práctica Enumerador 3
# Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

# Loops

# Condicionales if

# El método enumerate()

# Métodos de strings o indexado

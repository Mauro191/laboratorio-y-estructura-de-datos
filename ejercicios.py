#1Declara dos variables, llamadas nombre y edad.
#Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.

nombre="Tony Soprano"
edad=51

#2 Crea tres variables:
    #nombre
    #apellido
    #nombrecompleto
# A nombre, asígnale el valor "Julia", y en apellido, 
#asigna el valor "Roberts". Finalmente, 
#construye la variable nombrecompleto concatenando 
#las variables (recuerda sumar un espacio intermedio).

nombre="Julia"
apellido="Roberts"
nombrecompleto=(f"{nombre} {apellido}")
print(nombrecompleto)

# 3) Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:
#Estás tomando un curso de curso
#Para ello deberás concatenar la primera parte de la 
# frase con el valor que asumirá la variable. 
# Recuerda agregar un espacio antes de concatenar la 
# variable al resto del texto.

curso="Python"
print(str(f"estas tomando un curso de {curso}"))

# 4)Práctica con Integers
# Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.

num_entero=24
print(num_entero)

# 5)Práctica con Floats
# Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.

# Imprime el tipo de dato de dicha variable.

num_decimal=float(10)
print(num_decimal)

# 6)Práctica con Tipos de Datos Numéricos
# ¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.

# Para ello, crea dos variables:

# num1 = 7.5

# num2 = 2.5

# A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.

num1 = 7.5
num2 = 2.5
print(num1+num2)

# 7) Práctica con Conversiones 1
# Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
# num1 = 7.5

num1 = 7.5
print(float(num1))

# 8)Práctica con Conversiones 2
# Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
# num2 = 10

num2 = 10
num2=float(num2)
print(num2)

# 9) Práctica con Conversiones 3
# Suma los valores de num1 y num2.
# No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().

print(float(num1)+float(num2))

# 10) Práctica Formatear Cadenas 1
# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.

# nombre_asociado = "Jesse Pinkman"
# numero_asociado = 399058

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

# 11) Práctica Formatear Cadenas 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto
# puntos_nuevos = 350
# puntos_totales = 1225

puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

# 12)Práctica Formatear Cadenas 3
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos


puntos_totales=puntos_totales+puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

# 13)Práctica Operadores Matemáticos 1
# Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.
# Debes mostrar solo el valor numérico que resulta de esta operación.

numero1=874/27
print(numero1)

# 14) Práctica Operadores Matemáticos 2
# Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.

# Debes mostrar solo el valor numérico que resulta de esta operación.

numero2=456%33
print(numero2)

# 15)Práctica Operadores Matemáticos 3
# Calcula y muestra en pantalla la raíz cuadrada de 783.

# Debes mostrar solo el valor numérico que resulta de esta operación.

resultadoRaiz=783**0.5

# 16) Práctica Redondeo 1
# Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.

resultadoDivision=round(10/3,2)
print(resultadoDivision)

# 17) Práctica Redondeo 2
# Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.

print(round(10.676767,0))

# 18) Práctica Redondeo 3
# Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.

raiz=5**0.5
print(round(raiz,4))


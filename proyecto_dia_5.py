from random import choice

def mostrar_mensaje_inicial(palabra, cantidad):
    print(f"""
          JUEGO DEL AHORCADO

        Palabra secreta: "{" ".join(palabra)}" (contiene {cantidad} caracteres).

          Tienes que ingresar una letra para verificar si la misma se encuentra
          en la palabra secreta. Tienes 8 intentos para descubrirla.
          """)

def juego_del_ahorcado():
    palabras = ["perro", "gato", "serpiente", "oso"]
    palabra_seleccionada = choice(palabras)
    lista_caracteres = ["_" for _ in palabra_seleccionada]
    cantidad_caracteres = len(lista_caracteres)

    mostrar_mensaje_inicial(lista_caracteres, cantidad_caracteres)

    intentos = 8
    intentos_1 = 0

    while intentos > 0:
        pregunta = input("""
           A continuación, ingresa la letra: 
           
                         """).lower()
        
        if pregunta in palabra_seleccionada:
            for i, caracter in enumerate(palabra_seleccionada):
                if pregunta == caracter:
                    lista_caracteres[i] = pregunta
            print(f"""
                  La letra '{pregunta}' sí se encuentra en la palabra.""")
        else:
            intentos -= 1
            intentos_1 += 1
            print(f"""
                  La letra '{pregunta}' no se encuentra en la palabra.""")

        print(f"""
              Palabra secreta: {' '.join(lista_caracteres)}
              Intentos restantes: {intentos}""")
        
        if "_" not in lista_caracteres:
            print(f"¡Has encontrado la palabra secreta! : {''.join(lista_caracteres)} , y lo has logrado en {intentos_1} intentos.")
            break
        
        if intentos == 0:
            print(f"Te has quedado sin intentos. La palabra era: {palabra_seleccionada}")


juego_del_ahorcado()
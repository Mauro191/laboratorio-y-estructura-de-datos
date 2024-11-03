# Proyecto del Día 6

# Llegó el momento de poner todo lo que hemos aprendido en un proyecto del mundo real. Y el de hoy sí que nos va a tomar tiempo, porque a pesar de ser relativamente simple, implica mucho código, muchas funciones y es imprescindible llevar una especie de orden mental de lo que necesitas hacer. Hoy vas a crear un administrador de recetas. Básicamente esto es un programa a través del cual un usuario puede leer, crear y eliminar recetas que se encuentren en una base de datos.

# Entonces, antes de comenzar, es necesario que crees en tu ordenador un directorio en la carpeta base de tu ordenador, con una carpeta llamada Recetas, que contiene cuatro carpetas y cada una de ellas contiene dos archivos de texto. Dentro de los archivos puedes escribir lo que quieras, puede ser la receta en sí misma o no, pero eso no es importante para este ejercicio. Lo importante es que escribas algo para poder leerlas cuando haga falta o, si prefieres, también puedes directamente descargar y descomprimir el archivo adjunto a esta elección y ubicarlo en tu directorio raíz si no tienes ganas de crearlo tú mismo.

# Este programa tiene algunas cuestiones importantes a considerar:

# Cada vez que el usuario realice exitosamente cualquiera de sus opciones, el programa le va a pedir que presione alguna letra para poder volver al inicio, por lo que el código se va a repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se cumpla la condición de que la elección del usuario sea 6.

#  Sería genial que cada vez que el usuario vuelva al menú inicial, la consola limpie la pantalla para que no se acumulen las ejecuciones anteriores. Recuerda que cuentas con system para poder reiniciar la pantalla y comenzar a mostrar todo desde cero.

#  Si bien te he enseñado muchos métodos para administrar archivos, para este ejercicio vas a necesitar algunos que aún no has visto, pero que están incluidos en los objetos con los que hemos estado trabajando, por lo que en ocasiones deberás buscar entre los métodos que trae Path, por ejemplo, leer la documentación y aprender a implementarlo.

# Yo sé que sería mucho más fácil que yo te enseñe todo acerca de cada uno de los métodos, pero recuerda que también es importante que a medida que avanzamos vayas aprendiendo a gestionar tu propio aprendizaje. Es parte de la vida real y cotidiana del programador en el mundo en que vivimos.

from pathlib import Path  # importamos el modulo pathlib para poder crear objetos del tipo ruta.

path_recetas = Path('C:/Users/Estudio/recetas')# Devuelve un objeto Path representando el directorio base del usuario.

# Tu código le va a dar primero la bienvenida al usuario, le va a informar la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar cuántas recetas hay en total dentro de esa carpeta.

def bienvenida():
    """saludar e informar al usuario"""
    print(f"Bienvenido ¡, la ruta de acceso a la carpeta de recetas es: {path_recetas}")
    recetas = list(path_recetas.glob('**/*'))
    recetas = [r for r in recetas if r.is_file()]
    numero_recetas = len(recetas)
    print(f'Existen {numero_recetas} recetas a disposicion.')

def lista_de_categorias():
    return [p.name for p in path_recetas.iterdir() if p.is_dir()]

def elegir_categoria(categorias):
    print("Categorías disponibles:")
    for idx, categoria in enumerate(categorias, start=1):
        print(f"{idx}. {categoria}")

    while True:
        try:
            seleccion = int(input("Selecciona una categoría (número): ")) - 1
            if 0 <= seleccion < len(categorias):
                return categorias[seleccion]
            else:
                print("Número fuera de rango. Por favor, elige un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

# 1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.

def opc_1():
    categorias = lista_de_categorias()
    if not categorias:
        print("No hay categorías disponibles.")
        return

    categoria = elegir_categoria(categorias)
    recetas_categoria = list((path_recetas / categoria).iterdir())

    if not recetas_categoria:
        print(f"En esta categoria no existen recetas disponibles '{categoria}.")
        return

    print("Recetas a disposicion:")
    for idx, receta in enumerate(recetas_categoria, start=1):
        print(f"{idx}. {receta.name}")

    while True:
        try:
            seleccion = int(input("Selecciona una receta para leer (número): ")) - 1
            if 0 <= seleccion < len(recetas_categoria):
                with open(recetas_categoria[seleccion], 'r') as f:
                    contenido = f.read()
                print("Contenido de la receta:")
                print(contenido)
                break
            else:
                print("Número fuera de rango. Por favor, elige un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

# 2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va a crear ese archivo en el lugar correcto.

def opc_2():
    categorias = lista_de_categorias()
    if not categorias:
        print("No hay categorías disponibles. Crea una nueva categoría primero.")
        return

    categoria = elegir_categoria(categorias)
    nombre_receta = input("Escribe el nombre de la nueva receta: ")
    contenido_receta = input("Escribe el contenido de la receta: ")

    with open(path_recetas / categoria / nombre_receta, 'w') as f:
        f.write(contenido_receta)
    print("Receta creada con éxito.")

# 3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar una carpeta nueva con ese nombre.

def opc_3():
    nueva_categoria = input("Escribe el nombre de la nueva categoría: ")
    (path_recetas / nueva_categoria).mkdir(exist_ok=True)
    print("Categoría creada con éxito.")

# 4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va a eliminar

def opc_4():
    categorias = lista_de_categorias()
    if not categorias:
        print("No hay categorías disponibles.")
        return

    categoria = elegir_categoria(categorias)
    recetas_categoria = list((path_recetas / categoria).iterdir())

    if not recetas_categoria:
        print(f"No hay recetas disponibles en la categoría '{categoria}'.")
        return

    print("Recetas disponibles:")
    for idx, receta in enumerate(recetas_categoria, start=1):
        print(f"{idx}. {receta.name}")

    while True:
        try:
            seleccion = int(input("Selecciona una receta para eliminar : ")) - 1
            if 0 <= seleccion < len(recetas_categoria):
                recetas_categoria[seleccion].unlink()
                print("Receta eliminada exitosamente.")
                break
            else:
                print("Número fuera de rango. Por favor, elige un número válido.")
        except ValueError:
            print("Error , por favor, ingresa un número.")

# 5. La opción 5, le va a preguntar qué categoría quiere eliminar.

def opc_5():
    categorias = lista_de_categorias()
    if not categorias:
        print("No hay categorías disponibles.")
        return

    categoria = elegir_categoria(categorias)
    (path_recetas / categoria).rmdir()
    print("Categoría eliminada con éxito.")

# 6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.

def menu():

    while True:
        
        print("\nOpciones : ")
        print(" 1 . Leer la receta.")
        print(" 2 . Crear una nueva receta.")
        print(" 3 . Crear una nueva categoría.")
        print(" 4 . Eliminar la receta.")
        print(" 5 . Eliminar la categoría.")
        print(" 6 . Salirdel sistema.")

        opcion = input("Por favor , selecciona una opción : ")

        match opcion:
            case '1':
                opc_1()
            case '2':
                opc_2()
            case '3':
                opc_3()
            case '4':
                opc_4()
            case '5':
                opc_5()
            case '6':
                print("Salir del programa...")
                break
            case _:
                print("Error , por favor, selecciona una opción válida.")
                

bienvenida()
menu()
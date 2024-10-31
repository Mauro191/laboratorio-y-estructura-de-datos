from pathlib import Path

ruta_recetas = Path('C:/Users/Estudio/recetas')

def bienvenida():
    """saludar e informar al usuario"""
    print("¡Bienvenido al sistema de recetas!")
    print(f"La ruta de acceso a la carpeta de recetas es: {ruta_recetas}")
    recetas = list(ruta_recetas.glob('**/*'))
    recetas = [r for r in recetas if r.is_file()]
    numero_recetas = len(recetas)
    print(f'Existen {numero_recetas} recetas a disposicion.')

def listar_categorias():
    return [p.name for p in ruta_recetas.iterdir() if p.is_dir()]

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

def opcion_1():
    categorias = listar_categorias()
    if not categorias:
        print("No hay categorías disponibles.")
        return

    categoria = elegir_categoria(categorias)
    recetas_categoria = list((ruta_recetas / categoria).iterdir())

    if not recetas_categoria:
        print(f"En esta categoria no existen recetas disponibles '{categoria}'.")
        return

    print("Recetas disponibles:")
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

def opcion_2():
    categorias = listar_categorias()
    if not categorias:
        print("No hay categorías disponibles. Crea una nueva categoría primero.")
        return

    categoria = elegir_categoria(categorias)
    nombre_receta = input("Escribe el nombre de la nueva receta: ")
    contenido_receta = input("Escribe el contenido de la receta: ")

    # Crear el archivo de la nueva receta
    with open(ruta_recetas / categoria / nombre_receta, 'w') as f:
        f.write(contenido_receta)
    print("Receta creada con éxito.")

def opcion_3():
    nueva_categoria = input("Escribe el nombre de la nueva categoría: ")
    (ruta_recetas / nueva_categoria).mkdir(exist_ok=True)
    print("Categoría creada con éxito.")

def opcion_4():
    categorias = listar_categorias()
    if not categorias:
        print("No hay categorías disponibles.")
        return

    categoria = elegir_categoria(categorias)
    recetas_categoria = list((ruta_recetas / categoria).iterdir())

    if not recetas_categoria:
        print(f"No hay recetas disponibles en la categoría '{categoria}'.")
        return

    print("Recetas disponibles:")
    for idx, receta in enumerate(recetas_categoria, start=1):
        print(f"{idx}. {receta.name}")

    while True:
        try:
            seleccion = int(input("Selecciona una receta para eliminar (número): ")) - 1
            if 0 <= seleccion < len(recetas_categoria):
                recetas_categoria[seleccion].unlink()
                print("Receta eliminada con éxito.")
                break
            else:
                print("Número fuera de rango. Por favor, elige un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def opcion_5():
    categorias = listar_categorias()
    if not categorias:
        print("No hay categorías disponibles.")
        return

    categoria = elegir_categoria(categorias)
    (ruta_recetas / categoria).rmdir()
    print("Categoría eliminada con éxito.")

def menu():
    while True:
        print("\nOpciones:")
        print("1. Leer receta")
        print("2. Crear receta")
        print("3. Crear categoría")
        print("4. Eliminar receta")
        print("5. Eliminar categoría")
        print("6. Salir")
        opcion = input("Selecciona una opción (número): ")

        if opcion == '1':
            opcion_1()
        elif opcion == '2':
            opcion_2()
        elif opcion == '3':
            opcion_3()
        elif opcion == '4':
            opcion_4()
        elif opcion == '5':
            opcion_5()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar la bienvenida y el menú
bienvenida()
menu()
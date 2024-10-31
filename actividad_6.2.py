
# Práctica Archivos y Funciones 1

# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).

ruta_archivo = "C:/Users/Estudio/clase 6/carnes.txt"

def abrir(archivo_receta):
    with open (archivo_receta, "r") as archivo:
        mostrar_contenido= archivo.read()
        print(mostrar_contenido)

        
abrir(ruta_archivo)

# Práctica Archivos y Funciones 2

# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"


ruta_eliminar = "C:/Users/Estudio/clase 6/carnes.txt"
def eliminar(contenido):
    with open(contenido, 'w') as eliminar:
       eliminar.write("El contenido se ha eliminado")
    with open(contenido, 'r') as mostrar:
       mostrar_mensaje = mostrar.read()
       print(mostrar_mensaje) 
       
eliminar(ruta_eliminar)

# Práctica Archivos y Funciones 3

# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
# Finalmente, debe cerrar el archivo abierto.

def registro_error(error):
    with open(error,'a') as mensaje_error:
        mensaje_error.write("\nexiste un error en la ejecucion.")
    with open(error, 'r') as archivo:
        print(archivo.read())
        
registro_error(ruta_eliminar)
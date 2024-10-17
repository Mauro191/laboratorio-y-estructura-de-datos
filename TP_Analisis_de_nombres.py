# Trabajo Practico Evaluativo: Análisis de Nombres de Estudiantes

nombres_alumnos=[]
print("""A continuacion ingrese los nombres de los alumnos :
    Escriba "fin" para finalizar la carga de nombres.
    Escriba "repetir" para observar la lista de nombres. """)
while True : 
    consulta=input("Nombre :").lower()

    if (consulta.isalpha()) or (consulta!=""):
        if consulta=="fin":
           break
        elif consulta=="repetir": 
           print(nombres_alumnos)
        else:
           nombres_alumnos.append(consulta)
    else:
        print("""El nombre ingresado no es valido , por favor , ingrese un nombre nuevamente (verificar que el nombre a ingresar no este vacio , o contenga caracteres especiales). """)

# Menú de opciones:

while True:

    opcion=input("""
                 menu de opciones :

    1 - Nombres ingresados.
    2 - Nombres ordenados alfabéticamente.
    3 - Longitud de nombres ingresados.
    4 - Cantidad de vocales y consonantes.
    5 - Cantidad de palabras en cada nombre.
    6 - Mostrar los nombres invertidos.
    7 - Mostrar solo los nombres que empiezan con una letra especifica.
    8 - Buscar si un nombre está en la lista.
    9 - Mostrar los nombres con mas de 5 caracteres.
    10 - Convertir los nombres a mayúsculas o minúsculas.
    11 - Eliminar un determinado nombre.            
    12 - Salir del programa.

Por favor , ingrese una opcion : 
                 """)

    match opcion: 

        case "1" : #### Mostrar nombres ingresados.
    
            print(nombres_alumnos)

        case "2" : #### Nombres ordenados alfabéticamente.

            orden_alfabetico=nombres_alumnos.sort()
            print(f"A continuacion se muestra la lista de nombres, ordenada alfabeticamente : {", ".join(nombres_alumnos)}.")

        case "3" : #### Longitud de nombres.

            nombre_max_longitud=max(nombres_alumnos,key=len)
            nombre_min_longitud=min(nombres_alumnos,key=len)
            print(f"El nombre con mayor cantidad de caracteres es : {nombre_max_longitud} , y el nombre con menor cantidad de caracteres es : {nombre_min_longitud}")

        case "4" : #### Conteo de vocales y consonantes.

            conversion_a_cadena="".join(nombres_alumnos)
            vocales=["a","e","i","o","u"]
            cantidad_vocales=0
            cantidad_consonantes=0
            for caracter in conversion_a_cadena:
                if caracter.lower() in vocales:
                    cantidad_vocales=cantidad_vocales+1
                else:
                    cantidad_consonantes=cantidad_consonantes+1
            print(f"En el listado de nombres , existen {cantidad_vocales} vocales , y {cantidad_consonantes} consonantes.")

        case "5" : #### Conteo de palabras por nombre.
        
            for nombre in nombres_alumnos:
                cantidad_palabras=len(nombre.split())   
                variable_dependiente="palabra"
                if cantidad_palabras>1 :
                    variable_dependiente="palabras"    
                print(f"El nombre {nombre} , tiene {cantidad_palabras} {variable_dependiente}.")   

        case "6" : #### Mostrar nombres invertidos.

            for nombre in nombres_alumnos:
                print(nombre[::-1])

        case "7" : #### Mostrar nombres que inician con determinada letra.

            solicitud_caracter=input("A continuacion , ingrese el caracter , para observar los nombres que comienzan con el mismo : ").lower()
            for nombre in nombres_alumnos:
                if nombre.startswith(solicitud_caracter) :
                    print(f"{nombre} inicia con : {solicitud_caracter}")
                else:
                    continue
         
        case "8" : #### verificar si un nombre está en la lista.

            verificar_nombre=input("Ingrese un nombre para verificar si se encuentra en la lista : ")
            if verificar_nombre in nombres_alumnos:
                print(f"El nombre {verificar_nombre} , esta presente en la lista.")
            else:
                print(f"El nombre {verificar_nombre} , no se encuentra en la lista.")

        case "9" : #### Mostrar los nombres con mas de 5 caracteres.
            
            variable_dependiente="palabra"
            variable_dependiente2="existe"
            variable_dependiente3="tiene"
            # estas tres "variables dependientes" modifican las palabras del mensaje final de la seleccion para darle coherencia al mensaje.
            palabras_may_a_5_caracteres=0
            for nombre in nombres_alumnos:
                cantidad_caracteres=len(nombre)
                if cantidad_caracteres>5 :
                    palabras_may_a_5_caracteres += 1                  
            if palabras_may_a_5_caracteres!=1:
                variable_dependiente="palabras"
                variable_dependiente2="existen"
                variable_dependiente3="tienen"
            print(f"{variable_dependiente2} {palabras_may_a_5_caracteres} {variable_dependiente} que {variable_dependiente3} mas de 5 caracteres.")

        case "10" : #### Convertir los nombres a mayúsculas o minúsculas.
    
            nombres_en_mayuscula=[]
            nombres_en_minuscula=[]
            consulta=input("""
                           
        1 - Mostrar nombres en mayúsculas. 
        2 - Mostrar nombres en minusculas.
            
            Seleccione una opcion : """)
            match consulta: 
                case "1" :
                    for nombre in nombres_alumnos:
                        nombre_mayuscula=nombre.upper()
                        nombres_en_mayuscula=[]
                        nombres_en_mayuscula.append(nombre_mayuscula)
                        print(nombres_en_mayuscula)
                case "2" :
                    for nombre in nombres_alumnos:
                        nombre_minuscula=nombre.lower() 
                        nombres_en_minuscula=[]
                        nombres_en_minuscula.append(nombre_minuscula)
                        print(nombres_en_minuscula)

        case "11" : #### Salida del programa

            print("saliendo del programa...")
            break
        
        case "12" : #### Eliminar un nombre determinado.

            nombre_a_eliminar=input("Por favor , ingrese el nombre a eliminar :")
            nombres_alumnos.remove(nombre_a_eliminar)
            print(f"la lista , actualizada , queda de la siguiente manera : {nombres_alumnos}")

        case "_" : 
            
            print("Seleccione una opcion nuevamente : ")
        













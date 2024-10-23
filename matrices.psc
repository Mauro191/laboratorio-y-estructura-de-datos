Algoritmo matriz
	
    Dimension matrizFrutas[2,5] 
    Definir OP Como Entero
    Definir i, j Como Entero
    Definir encontrado Como Logico
    Definir  nombreFruta Como Caracter
	
    // Inicializamos la matriz:
	
    Para i Desde 1 Hasta 2 Hacer
        Para j Desde 1 Hasta 5 Hacer
            matrizFrutas[i,j] <- ""
        FinPara
    FinPara

    Mientras OP <> 3 Hacer
		
        Escribir  "Menú:"
        Escribir  "0 - Ingresar un artículo"
        Escribir  "1 - Buscar un artículo"
        Escribir  "2 - Imprimir todos los artículos"
        Escribir  "3 - Salir"
        Leer OP
		
        Segun OP hacer
		
			Caso 0:
				
		                Para i Desde 1 Hasta 1 Con Paso 1 Hacer
					Para j Desde 1 Hasta 5 Con Paso 1 Hacer
						Escribir "ingrese la fruta"
						Leer matrizFrutas[i,j] 
					FinPara
				FinPara
				Para i Desde 1 Hasta 2 Con Paso 1 Hacer
					Para j Desde 1 Hasta 5 Con Paso 1 Hacer
						Escribir "ingrese la cantidad"
						Leer matrizFrutas[i,j] 
					FinPara
				FinPara
		
			Caso 1:
		
				Escribir "ingrese el articulo a buscar"
		        Leer  nombreFruta
				encontrado <- Falso
		        Para i = 1 hasta 2 con paso 1 Hacer
					Para j = 1 hasta 5 con paso 1 Hacer
						si matrizFrutas[i,j] = nombreFruta Entonces
						    Escribir  "Artículo: ", matrizFrutas[1,j], ", Cantidad: ", matrizFrutas[2,j]
					        encontrado <- Verdadero
				        FinSi
			        FinPara
				FinPara
				si encontrado = Falso Entonces
			        Escribir "Artículo no encontrado."
		        FinSi
		
	        Caso  2:
		
		        Escribir  "Artículos cargados:"
				Para j Desde 1 Hasta 5 Hacer
					si matrizFrutas[1,j] <> "" Entonces
					Escribir matrizFrutas[1,j], ": ", matrizFrutas[2,j]
					Fin si
				Fin para
		
	        Caso  3:
		
				Escribir "Salir del programa."
		
			De Otro Modo:
		
				Escribir  "Opción inválida. Intente nuevamente."
		
		Fin segun
	    
    fin mientras
	
FinAlgoritmo

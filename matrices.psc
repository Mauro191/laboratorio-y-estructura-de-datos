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

	matrizFrutas[1,1] <- "Banana"
    matrizFrutas[2,1] <- "3"
    matrizFrutas[1,2] <- "Manzana"
    matrizFrutas[2,2] <- "4"
    matrizFrutas[1,3] <- "Pera"
    matrizFrutas[2,3] <- "5"
    matrizFrutas[1,4] <- "Kiwi"
    matrizFrutas[2,4] <- "5"
    matrizFrutas[1,5] <- "Melon"
    matrizFrutas[2,5] <- "3"

    Mientras OP <> 3 Hacer
		
        Escribir  "Men�:"
        Escribir  "0 - Ingresar un art�culo"
        Escribir  "1 - Buscar un art�culo"
        Escribir  "2 - Imprimir todos los art�culos"
        Escribir  "3 - Salir"
        Leer OP
		
        Segun OP hacer
		
			Caso 0:
				
		        Escribir "Ingrese el nombre del art�culo: "
		        Leer nombreFruta
				Escribir "Ingrese la cantidad del art�culo: "
		        Leer cantidadFruta
		        matrizFrutas[1,1] <- nombreFruta
				matrizFrutas[2,1] <- cantidadFruta
		
			Caso 1:
		
				Escribir "ingrese el articulo a buscar"
		        Leer  nombreFruta
				encontrado <- Falso
		        Para i = 1 hasta 2 con paso 1 Hacer
					Para j = 1 hasta 5 con paso 1 Hacer
						si matrizFrutas[i,j] = nombreFruta Entonces
						    Escribir  "Art�culo: ", matrizFrutas[1,j], ", Cantidad: ", matrizFrutas[2,j]
					        encontrado <- Verdadero
				        FinSi
			        FinPara
				FinPara
				si encontrado = Falso Entonces
			        Escribir "Art�culo no encontrado."
		        FinSi
		
	        Caso  2:
		
		        Escribir  "Art�culos cargados:"
				Para j Desde 1 Hasta 5 Hacer
					si matrizFrutas[1,j] <> "" Entonces
					Escribir matrizFrutas[1,j], ": ", matrizFrutas[2,j]
					Fin si
				Fin para
		
	        Caso  3:
		
				Escribir "Salir del programa."
		
			De Otro Modo:
		
				Escribir  "Opci�n inv�lida. Intente nuevamente."
		
		Fin segun
	    
    fin mientras
	
FinAlgoritmo

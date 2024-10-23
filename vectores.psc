
Algoritmo vectores
	
	Definir cantidad_numeros_mayores_a_5,sumatoria,cantidad,numero_mayor,numero_menor Como Real                        
	cantidad_numeros_mayores_a_5=0
	sumatoria=0
	cantidad=0

	//Iteramos el vector para ingreso de datos(lectura de numeros):
	
	Escribir "Cuantos números va a ingresar?"
	Leer cantidad
	Dimension num[cantidad]
	Para i=1 Hasta cantidad Hacer
		Escribir "Ingresar el número " , i , ":"
		Leer num[i]
	FinPara
	
	numero_mayor = num[1]
	numero_menor = num[1]
	
	//Iteramos el vector para evaluar datos ingresados:
	
	Para i=1 Hasta cantidad Hacer
		
	    //Evaluar el mayor y el menor numero ingresado:
	
		Si num[i] > numero_mayor Entonces
			numero_mayor = num[i]
		FinSi
		Si num[i] < numero_menor Entonces
			numero_menor = num[i]
		FinSi
		
	    //Evaluar la cantidad de numeros ingresados que son mayores a 5:
		
		Si num[i] > 5 Entonces
			cantidad_numeros_mayores_a_5=cantidad_numeros_mayores_a_5+1
        FinSi
		
	    //Sumatoria de todos los numeros ingresados en el vector:
		
		sumatoria=sumatoria+num[i]
		
	FinPara
	
	Escribir ""
	Escribir "El mayor número ingresado es: " , numero_mayor
	Escribir "El menor número ingresado es: " , numero_menor
	Escribir "Se ingresaron ", cantidad_numeros_mayores_a_5 ," numeros mayores a 5."
	Escribir "La sumatoria de todos los numeros ingresados es : ", sumatoria
	
FinAlgoritmo

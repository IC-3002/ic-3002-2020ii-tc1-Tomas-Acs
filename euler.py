import math



def e_cuadratica(n):
	suma = 1
	for i in range(1, n+1):
		suma = suma+(1/math.factorial(i))
	return suma



def e_lineal(n):
	factorial = 1
	euler = 2
	for x in range(2, n):
		factorial *= x
		euler += (1)/(factorial)
	return euler


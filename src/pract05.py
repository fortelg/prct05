#!/usr/bin/python
#!encoding: UTF-8
import sys

#Utilizacion de una funcion calcular_xi para obtener los xi
def calcular_xi (n, i):
	xi = (i - 1.0/2.0) / n
	return xi

#Utilizacion de una funcion calcular_fxi para obtener los f(xi)
def calcular_fxi (xi):
	fxi = 4.0 / (1.0 + xi*xi)
	return fxi

#Utilizacion de una funcion arccot para calcular la arcotangente
def arccot(x, unity):
	sum = xpower = unity // x
	n = 3
	sign = -1
	while 1:
		xpower = xpower // (x*x)
		term = xpower // n
		if not term:
			break
		sum += sign * term
		sign = -sign
		n += 2
	return sum

#Esta funcion es para calcular los 35 decimales, a su vez llama a la funcion arccot
def decimales_pi(digits):
	unity = 10**(digits + 10)
	decimal_pi = 4 * (4*arccot(5, unity) - arccot(239, unity))
	return (float(decimal_pi // 10**10) / 10**digits)


#Programa principal
#Ojo, para hacer uso de la funcion sys, debemos incluirla al principio del programa
argumentos = sys.argv[1:]
if (len(argumentos) == 1):
	n = int (argumentos[0])
else:
	print "Introduzca el numero de intervalos (n > 0):"
	n = int (raw_input ());
if (n > 0):
	ini = 0
	intervalo = 1.0 / float (n);
	sumatorio = 0.0
	for i in range(n):
		xi = calcular_xi(n, i+1)
		fxi = calcular_fxi (xi)
		print "Subintervalo: [", ini , ",", ini+intervalo, "]", "x_i:", xi, "fx_i:", fxi
		ini += intervalo
		sumatorio += fxi
	valor_pi = sumatorio / n;
	print "El valor aproximado de PI es:", valor_pi
	print "El valor de PI con 35 decimales: %10.35f" % decimales_pi (35)
else:
	print "El valor de los intervalos debe ser mayor que 0"





from sympy.stats import FiniteRV, E, variance,density
from sympy import Rational, exp, diff, symbols

"""
    Primero debemos calcular la Varialbe Aleatoria X
    Para esto tenemos que definir sus probabilidades.
    Tenemos los siguientes casos:
    Ganamos 5 cuando sale 3 veces seguidas cara o 3 veces seguidas cruz
    Por lo tanto tenemos {(CCC),(XXX)}
    La probabilidad de que esto pase es:
        La probabilidad de que salga cara: 1/2
        Por ende: 1/2 * 1/2 * 1/2 + (Puede ser cruz tambien) 1/2 * 1/2 * 1/2 = 1/4
        La probabilidad de este evento es 1/4
    
    Perdemos 3 cuando no sale 3 veces seguidas cara o 3 veces seguidas cruz
    Por lo tanto tenemos {(CXC),(XCC),(CCX),(XCX),(CXX),(XXC)}
    La probabilidad de que esto pase es:
        Podemos calcular la probabilidad de que no ocurra el evento anterior obteniendo su complemento
        Por ende: 1 - 1/4 = 3/4
        La probabilidad de este evento es 3/4
        
    La funcion de probabilidad es:
    P(X = 5) = 1/4
    P(X = 3) = 3/4
    
"""

#Se define la variable aleatoria X
X = FiniteRV('X', {5:1/4, -3: 3/4})
print(density(X).dict)

#Podemos calcular el valor esperado de X y la varianza de X de dos maneras distintas
#Utilizando funciones de sympy o utilizando la funcion generadora de momentos de la variable aleatoria

#Utilizando funciones de sympy

#Varianza
print("Varianza:", variance(X).evalf())

#Valor esperado
print("Valor esperado:", E(X).evalf())

#Utilizando la funcion generadora de momentos

#Debemos definir la funcion generadora de momentos de X

#Se define la constante
s = symbols('s')

#Se defina la funcion generadora de momentos
funGeneradoraMomentos = E(exp(s*X))

#El valor esperado de X es la primera derivada de la funcion generadora de momentos evaluada en 0
valorEsperado = funGeneradoraMomentos.diff(s).subs(s, 0)

#La varianza de X es la segunda derivada de la funcion generadora de momentos evaluada en 0 menos el valor esperado al cuadrado
varianza = funGeneradoraMomentos.diff(s, 2).subs(s, 0) - valorEsperado**2

#Resultados
print("Varianza, funcion generadora:", varianza.evalf())
print("Valor esperado, funcion generadora:", valorEsperado.evalf())

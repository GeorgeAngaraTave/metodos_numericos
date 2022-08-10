# from ast import Lambda
# import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np
from modulos.graficar import graficar
from modulos.met_biseccion import biseccion


#f = lambda x: np.e**x - 3*np.sin(x) - 3*x
# f = lambda x: np.sin(3*x) - np.cos(2*x) -1
# f = lambda x: 2**x * ( x - 6) - x
# f = lambda x: np.sin(3*x) - np.cos(2*x) -1
# f = lambda x: np.e**x/(x-3) + 2*x


def options():
    while True:
        
        print('\n*********************************')
        print('******* MÉTODOS NÚMERICOS *******')
        print('*********************************\n')
        
        print('1. - Gracificar función' )
        print('2. - Método de bisección' )
        print('3. - Salir' )
        
        option = input()
        print()

        if option.isnumeric() == False:
            print('Tiene que ingresar un número')
        else:
            option = int(option) 
        # Fubcióna  calcular        
        if option != 3:
            f = lambda x: 4*x*np.cos(x) + (2*np.sin(x))**2 -3
            print('límite inferior del intervalo')
            x_i = float(input())
            print('límite superior del intervalo')
            x_f = float(input())
            
            print()
            print('Intervalo inicial: ({}, {})'.format(x_i, x_f))
        if option == 1:
            #f = lambda x: (1/x)               
            graficar(f, x_i, x_f)
        
        if option == 2:     
            print('toleracia, criterio de parada')      
            tol = float(input())
            print()
            biseccion(f, x_i, x_f, tol)    
            
        elif option == 3:
            exit()
        else:      
            print('Opción no permitida')
        



if __name__ == '__main__':    
    options()
from lib2to3.pygram import Symbols
import numpy as np
from sympy import *
from app.funtions.Equations_one_variable import EquationsOneVariable

#f = lambda x: np.e**x - 3*np.sin(x) - 3*x
# f = lambda x: np.sin(3*x) - np.cos(2*x) -1
# f = lambda x: 2**x * ( x - 6) - x
# f = lambda x: np.sin(3*x) - np.cos(2*x) -1
# f = lambda x: np.e**x/(x-3) + 2*x
# f = lambda x: 4*x*np.cos(x) + (2*np.sin(x))**2 -3
# 1e-4


def options():
    while True:
        
        print('\n*********************************')
        print('******* MÉTODOS NÚMERICOS *******')
        print('*********************************\n')
        
        print('1. - Gracificar función' )
        print('2. - Método de bisección' )
        print('3. - Método regular falsi' )
        print('4. - Método newton raphson' )
        print('5. - Método secante' )
        print('6. - Método punto fijo' )
        print('7. - Salir' )
        
        option = input()
        print()

        if option.isnumeric() == False:
            print('Tiene que ingresar un número')
        else:
            option = int(option) 
        # Fubcióna  calcular        
        if option != 7:
            
            f = lambda x: np.sin(3*x) - np.cos(2*x) -1
            #print('Para la función : {f}')
            if option != 4:
                print('límite inferior del intervalo')
                x_i = float(input())
                print('límite superior del intervalo')
                x_f = float(input())      
                print()
                print('Intervalo inicial: ({}, {})'.format(x_i, x_f))
                        
            if option != 1:
                print('toleracia, criterio de parada')      
                tol = float(input())
            
        if option == 1:
            #f = lambda x: (1/x)               
            EquationsOneVariable.graficar(f, x_i, x_f)
        
        elif option == 2:     
            EquationsOneVariable.met_biseccion(f, x_i, x_f, tol)    
            
        elif option == 3:     
            EquationsOneVariable.met_regula_falsi(f, x_i, x_f, tol)        
            
        elif option == 4:
            # Método  newton raphson            
            print('semilla (punto inicial)')
            p_0 = float(input())
            print()
            #Averiguar la derivada
            x = Symbol('x')
            dff = diff(sin(3*x) - cos(2*x) -1, x)
            print('La dericada es:', dff)
            df = lambda x: 2*np.sin(2*x) + 3*np.cos(3*x)
            EquationsOneVariable.met_newton_raphson(f, df, p_0, tol)

        elif option == 5:
            # Método Secante 
            print('semilla1 (punto inicial 1)')
            p_n = float(input())
            print('semilla2 (punto inicial)')
            p_m = float(input())
            print()
            
            x = Symbol('x')
            dff = diff(sin(3*x) - cos(2*x) -1, x)
            print('La dericada es:', dff)
            df = lambda x: 2*np.sin(2*x) + 3*np.cos(3*x)
            EquationsOneVariable.met_secante(f, p_n, p_m, tol)
            
        elif option == 6:
            # Método punto jofo 
            print('semilla (punto inicial)')
            p_0 = float(input())
            print()            

            x = Symbol('x')
            dff = diff(sin(3*x) - cos(2*x) -1, x)
            print('La dericada es:', dff)
            df = lambda x: 2*np.sin(2*x) + 3*np.cos(3*x)
            EquationsOneVariable.met_puntofijo(f, df, p_0, tol)            
            
        elif option == 7:
            exit()
        else:      
            print('Opción no permitida')




def biseccion(f, a, b, tol):
    
    """
    Método de bisección
    :param f: Funcion a la que se le intenta encontrar una solucion 
    para la ecuacion f(x)=0, previamente definida
    :param a: límite inferior
    :param b: límite superior
    :param tol: toleracia, criterio de parada
    :return: solución exacta o aproximada, si tiene.
    """
    # Sea f(x) contínua sobre [a, b]
    # f(a) - f(b) < 0
    if not f(a)*f(b)<0:
        print('El intervalo no funciona: f({})={:.2f}, f({})={:.2f}'.format(a, f(a), b, f(b)))
        return None
    
    # Número de intervalos
    i = 1   
    
    while(abs(b - a)>=tol):
        p_i = (b + a)/2  # punto medio
        print('ite {:<2}: a_{:<2} = {:.4f}, b_{:<2} = {:.4f}, p_{:<2} = {:.5f}'.format(i, i-1, a, i-1, b, i, p_i))
        if f(p_i) == 0:
            print('solución exacta encontrada: {}'.format(p_i))
            return p_i
        # Se evalua f(a), f(b), f(m)
        if f(a)*f(p_i) < 0:
            b = p_i
        else:
            a = p_i
        i += 1
    
    print('solución encontrada: {:.5f}'.format(p_i))    
    print('error abs: abs({} - {})>={}'.format(b, a, tol), abs(b - a)>=tol) 
    print('solución no encontrada, iteraciones agotadas')
    return None
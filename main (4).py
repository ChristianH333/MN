def fixed_point_iteration(g, p0, tol, N0):
    i = 1
    
    while i <= N0:
        p = g(p0)
        
        if abs(p - p0) < tol:
            print("SALIDA (p):", p)
            return p  # El procedimiento fue exitoso
        
        i += 1
        p0 = p
        
    print("SALIDA: El método falló después de", N0, "iteraciones, N0 =", N0)
    # El procedimiento no fue exitoso

# Ejemplo de uso:
def g(x):
    return x**2 - 3

aproximacion_inicial = 1.5
tolerancia = 0.0001
numero_iteraciones = 100

fixed_point_iteration(g, aproximacion_inicial, tolerancia, numero_iteraciones)



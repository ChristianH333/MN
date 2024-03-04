def f(x):
    # Define la función f(x) que deseas encontrar su raíz
    return x**2 - 4

def secant_method(p0, p1, tol, N0):
    q0 = f(p0)
    q1 = f(p1)
    i = 2
    
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        
        if abs(p - p1) < tol:
            print("SALIDA (p):", p)
            return p  # El procedimiento fue exitoso
        
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
        
    print("SALIDA: El método falló después de", N0, "iteraciones, N0 =", N0)
    # El procedimiento no fue exitoso

# Ejemplo de uso:
aproximacion_inicial_1 = 3  # Primera aproximación inicial
aproximacion_inicial_2 = 2  # Segunda aproximación inicial
tolerancia = 0.0001  # Tolerancia
numero_iteraciones = 100  # N0

secant_method(aproximacion_inicial_1, aproximacion_inicial_2, tolerancia, numero_iteraciones)


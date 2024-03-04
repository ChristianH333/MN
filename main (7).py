def f(x):
    # Define la función f(x) que deseas encontrar su raíz
    return x**2 - 4

def f_prime(x):
    # Define la derivada de la función f(x)
    return 2 * x

def newton_method(p0, tol, N0):
    i = 1
    
    while i <= N0:
        p = p0 - f(p0) / f_prime(p0)
        
        if abs(p - p0) < tol:
            print("SALIDA (p):", p)
            return p  # El procedimiento fue exitoso
        
        i += 1
        p0 = p
        
    print("SALIDA: El método falló después de", N0, "iteraciones, N0 =", N0)
    # El procedimiento no fue exitoso

# Ejemplo de uso:
aproximacion_inicial = 3  # Aproximación inicial
tolerancia = 0.0001  # Tolerancia
numero_iteraciones = 100  # N0

newton_method(aproximacion_inicial, tolerancia, numero_iteraciones)


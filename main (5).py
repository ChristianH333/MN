def f(x):
    # Define la función f(x) que deseas encontrar su raíz
    return x**2 - 4

def secant_method(a, b, tol, N0):
    # Determinar p0 y q0, q1 según las condiciones dadas
    if f(a) > 0:
        p0 = b
        q0 = f(a)
        q1 = f(b)
    else:
        p0 = a
        q0 = f(b)
        q1 = f(a)
    
    i = 2
    
    while i <= N0:
        # Calcular p
        if f(a) > 0:
            p = p0 - q1 / (q1 - q0) * (p0 - a)
        else:
            p = p0 - q1 / (q0 - q1) * (b - p0)
        
        if abs(p - p0) < tol:
            print("SALIDA (p):", p)
            return p  # El procedimiento fue exitoso
        
        i += 1
        p0 = p
        q1 = f(p)
        
    print("SALIDA: El método fracasó después de", N0, "iteraciones, N0 =", N0)
    # El procedimiento no fue exitoso

# Ejemplo de uso:
a = 1  # Extremo a
b = 3  # Extremo b
tolerancia = 0.0001  # Tolerancia
numero_iteraciones = 100  # N0

secant_method(a, b, tolerancia, numero_iteraciones)


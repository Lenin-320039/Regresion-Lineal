from sumatorias import calcular_sumatorias
from pendiente import calcular_m
from interseccion import calcular_b

# Empresa en Manhattan
# x = NOMINA (Cientos de millones)
# y = VENTAS (Cientos de miles)
x = [1, 3, 4, 2, 1, 7]
y = [2, 3, 2.5, 2, 2, 3.5]

# MODULOS
n, s_x, s_y, s_xy, s_x2 = calcular_sumatorias(x, y)
m = calcular_m(n, s_x, s_y, s_xy, s_x2)
b = calcular_b(s_x, s_y, m, n)

print("--- RESULTADOS REGRESIÓN LINEAL: MANHATTAN ---")
print(f"Suma de x: {s_x}, Suma de y: {s_y}")
print(f"Suma de xy: {s_xy}, Suma de x^2: {s_x2}")
print(f"Pendiente (m): {m}")
print(f"Intersección (b): {b}")
print(f"Ecuación del modelo: y = {m}x + {b}")

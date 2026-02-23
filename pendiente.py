def calcular_m(n, sum_x, sum_y, sum_xy, sum_x2):
    numerador = (n * sum_xy) - (sum_x * sum_y)
    denominador = (n * sum_x2) - (sum_x)**2
    return numerador / denominador

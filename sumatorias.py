def calcular_sumatorias(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi**2 for xi in x)
    n = len(x)
    return n, sum_x, sum_y, sum_xy, sum_x2

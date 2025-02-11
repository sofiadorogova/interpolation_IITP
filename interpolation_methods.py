import numpy as np
import matplotlib.pyplot as plt

def linear_interpolation(x, y, x_new):
    """
    Линейная интерполяция.

    Параметры:
    -------
    x : array_like
        Одномерный массив узлов интерполяции (отсортирован по возрастанию).
    y : array_like
        Одномерный массив значений функции в узлах (x, y).
    x_new : float или array_like
        Точки, в которых нужно вычислить интерполированное значение.

    Возвращает:
    -------
    float или numpy.ndarray
        Значение(я) интерполяционного полинома в точках x_new.
        Если x_new — скаляр, возвращает скаляр; если массив, то numpy.ndarray.

    Примечание:
    Если x_new выходит за пределы x, результат будет экстраполирован,
    опираясь на крайние интервалы.
    """
    x_new_arr = np.array(x_new, ndmin=1, copy=False)
    y_new_arr = np.zeros_like(x_new_arr, dtype=float)

    for i, x_val in enumerate(x_new_arr):
        if x_val <= x[0]:
            y_new_arr[i] = y[0]
            continue

        if x_val >= x[-1]:
            y_new_arr[i] = y[-1]
            continue

        # Линейный поиск интервала [x[k], x[k+1]]
        for k in range(len(x) - 1):
            if x[k] <= x_val < x[k + 1]:
                t = (x_val - x[k]) / (x[k + 1] - x[k])
                y_new_arr[i] = y[k] + t * (y[k + 1] - y[k])
                break

    return y_new_arr[0] if np.isscalar(x_new) else y_new_arr


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


def nearest_neighbor_interpolation(x, y, x_new):
    """
    Интерполяция методом ближайшего соседа.

    Параметры
    ----------
    x : array_like
        Одномерный массив узлов интерполяции.
    y : array_like
        Одномерный массив значений функции в узлах (x, y).
    x_new : float или array_like
        Точки, в которых нужно вычислить интерполированное значение.

    Возвращает
    -------
    float или numpy.ndarray
        Значение(я) функции в ближайшем узле к точке(ам) x_new.
    """
    x_new_arr = np.array(x_new, ndmin=1, copy=False)
    y_new_arr = np.zeros_like(x_new_arr, dtype=float)

    for i, x_val in enumerate(x_new_arr):
        distances = np.abs(x - x_val)
        k = np.argmin(distances)
        y_new_arr[i] = y[k]

    return y_new_arr[0] if np.isscalar(x_new) else y_new_arr


def lagrange_interpolation(x, y, x_new):
    """
    Интерполяция методом Лагранжа.

    Параметры
    ----------
    x : array_like
        Одномерный массив узлов интерполяции (не должно быть повторяющихся значений).
    y : array_like
        Одномерный массив значений функции в узлах (x, y).
    x_new : float или array_like
        Точки, в которых нужно вычислить интерполированное значение.

    Возвращает
    -------
    float или numpy.ndarray
        Значение(я) интерполяционного многочлена в точках x_new.

    Формула
    -------
    L(x) = sum_{j=0}^{n-1} [ y_j * l_j(x) ],
    где:
        l_j(x) = product_{m=0, m != j}^{n-1} [ (x - x_m) / (x_j - x_m) ].
    """
    x_new_arr = np.array(x_new, ndmin=1, copy=False)
    n = len(x)

    y_new_arr = np.zeros_like(x_new_arr, dtype=float)

    for i, x_val in enumerate(x_new_arr):
        Lx = 0.0
        for j in range(n):
            lj = 1.0
            for m in range(n):
                if m != j:
                    lj *= (x_val - x[m]) / (x[j] - x[m])
            Lx += y[j] * lj
        y_new_arr[i] = Lx

    return y_new_arr[0] if np.isscalar(x_new) else y_new_arr


import numpy as np


def linear_interpolation(x, y, x_new):
    """
    Линейная интерполяция.

    Параметры:
    -------
    x : array_like
        Одномерный массив узлов интерполяции (отсортирован по возрастанию).
    y : array_like
        Значения функции в узлах (x, y).
    x_new : float или array_like
        Точки, в которых нужно вычислить интерполированное значение.

    Возвращает:
    -------
    float или numpy.ndarray
        Интерполированные значения в точках x_new.
    """
    x_new_arr = np.atleast_1d(x_new)
    y_new_arr = np.empty_like(x_new_arr, dtype=float)

    # Определяем интервалы с помощью np.searchsorted
    indices = np.searchsorted(x, x_new_arr, side="right") - 1
    indices = np.clip(indices, 0, len(x) - 2)

    x0, x1 = x[indices], x[indices + 1]
    y0, y1 = y[indices], y[indices + 1]

    # Предотвращаем деление на ноль, если x0 == x1
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(x1 != x0, (x_new_arr - x0) / (x1 - x0), 0.0)

    y_new_arr = y0 + t * (y1 - y0)

    # Корректируем граничные значения явно
    y_new_arr[x_new_arr <= x[0]] = y[0]
    y_new_arr[x_new_arr >= x[-1]] = y[-1]

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

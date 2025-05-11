import coverage
import numpy as np
import pytest

from interpolation_package.interpolation_methods import linear_interpolation


def test_linear_basic():
    """
    Проверяем, что на участке [0, 10], где y = x,
    линейная интерполяция даёт верное значение в середине.
    """
    x_vals = np.array([0, 10], dtype=float)
    y_vals = np.array([0, 10], dtype=float)
    assert linear_interpolation(x_vals, y_vals, 5) == 5


def test_linear_multiple_points():
    """
    Проверяем интерполяцию для массива x_new
    """
    x_vals = np.array([0, 10], dtype=float)
    y_vals = np.array([0, 20], dtype=float)
    x_new = np.array([2, 4, 6, 8], dtype=float)
    expected = np.array([4, 8, 12, 16], dtype=float)

    result = linear_interpolation(x_vals, y_vals, x_new)
    assert np.allclose(result, expected)


def test_linear_out_of_bounds_left():
    """
    Если x_new < x_vals[0], наша реализация берёт y = y_vals[0].
    """
    x_vals = np.array([2, 4], dtype=float)
    y_vals = np.array([2, 4], dtype=float)
    assert linear_interpolation(x_vals, y_vals, 0) == 2


def test_linear_out_of_bounds_right():
    """
    Если x_new > x_vals[-1], берём y = y_vals[-1].
    """
    x_vals = np.array([2, 4], dtype=float)
    y_vals = np.array([2, 4], dtype=float)
    assert linear_interpolation(x_vals, y_vals, 10) == 4


def test_linear_in_the_middle():
    """
    Дополнительно проверяем интерполяцию где x_new внутри промежутка,
    но не ровно посередине.
    """
    x_vals = np.array([0, 2], dtype=float)
    y_vals = np.array([0, 10], dtype=float)
    # Участок [0,2], y меняется от 0 до 10 => y = 5 * x
    x_new = 1
    expected = 5
    assert linear_interpolation(x_vals, y_vals, x_new) == pytest.approx(
        expected, 0.0001
    )

def test_linear_interpolation_middle_interval():
    x = np.array([0, 10, 20, 30])
    y = np.array([0, 100, 200, 300])

    # Выбираем точку, лежащую во втором или третьем интервале, 
    # например между 10 и 20
    x_val = 15  # Это гарантирует проход первой итерации (0->10 не подходит), 
                # и попадание на второй итерации (10->20 подходит)

    result = linear_interpolation(x, y, x_val)

    expected_result = 150  # так как это ровно середина между 100 и 200
    assert result == expected_result


import coverage
import numpy as np
import pytest

from interpolation_package.interpolation_methods import lagrange_interpolation


def test_lagrange_two_points():
    """
    Если у нас всего 2 точки, лагранжев многочлен -
    это просто прямая между этими точками.
    """
    x = np.array([0, 10], dtype=float)
    y = np.array([0, 10], dtype=float)

    assert lagrange_interpolation(x, y, 5) == pytest.approx(5.0)
    assert lagrange_interpolation(x, y, 0) == pytest.approx(0.0)
    assert lagrange_interpolation(x, y, 10) == pytest.approx(10.0)


def test_lagrange_three_points():
    """
    Проверка с 3 точками. Допустим, функция y = x^2
    в точках x = [0, 1, 2].
    """
    x = np.array([0, 1, 2], dtype=float)
    y = np.array([0, 1, 4], dtype=float)

    # Для x=1.5 (между 1 и 2) y=2.25 (1.5^2)
    result = lagrange_interpolation(x, y, 1.5)
    assert result == pytest.approx(2.25, 0.0001)


def test_lagrange_array_input():
    """
    Проверяем подачу массива x_new (несколько точек).
    Допустим, синус в 5 точках. Функция должна пройти точно через эти точки.
    """
    x = np.array([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi], dtype=float)
    y = np.sin(x)
    x_new = np.array([0, np.pi / 2, np.pi], dtype=float)

    # Так как x_new - подмножество исходных точек,
    # результат должен быть идентичен sin(x).
    result = lagrange_interpolation(x, y, x_new)
    expected = np.sin(x_new)
    assert np.allclose(result, expected)


def test_lagrange_out_of_bounds():
    """
    Лагранжева интерполяция не имеет встроенного механизма 'краевых значений',
    но мы можем проверить, что она экстраполирует по полиному.
    """
    x = np.array([0, 1, 2], dtype=float)
    y = np.array([1, 2, 3], dtype=float)
    # Это фактически прямая y = x + 1, т.к. точки (0,1), (1,2), (2,3).

    # Точка -1: по формуле получится y=0
    result_neg1 = lagrange_interpolation(x, y, -1)
    assert result_neg1 == pytest.approx(0.0, 0.0001)

    # Точка  3: должно получиться y=4 (по той же прямой)
    result_3 = lagrange_interpolation(x, y, 3)
    assert result_3 == pytest.approx(4.0, 0.0001)

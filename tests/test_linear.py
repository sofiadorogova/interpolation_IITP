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
    """
    Проверяем линейную интерполяцию, когда x_new попадает в середину массива узлов.

    Здесь мы специально выбираем значение x_new=15, которое:
      - Не подходит под первый интервал [0, 10], так как 15 > 10.
      - Подходит под второй интервал [10, 20], так как 10 <= 15 < 20.

    Это позволяет протестировать корректность внутреннего цикла поиска интервала,
    убедиться, что он корректно пропускает неподходящие интервалы и останавливается
    ровно на подходящем.

    Так как в выбранном интервале [10, 20] значения функции y меняются от 100 до 200,
    значение в середине интервала (в точке 15) должно быть ровно посередине,
    то есть 150.
    """
    x = np.array([0, 10, 20, 30])
    y = np.array([0, 100, 200, 300])

    x_val = 15

    result = linear_interpolation(x, y, x_val)

    expected_result = 150
    assert result == expected_result


def test_linear_interpolation_invalid_interval():
    """
    Проверяем поведение при некорректном массиве x (повторяющиеся значения).
    Ожидаем, что цикл завершится без нахождения интервала.
    """
    x_vals = np.array([0, 0, 10], dtype=float)  # повторяющийся узел 0
    y_vals = np.array([0, 0, 10], dtype=float)
    x_new = (
        0  # это значение точно попадает в узел, но проверка "< x[k + 1]" не срабатывает
    )
    result = linear_interpolation(x_vals, y_vals, x_new)
    assert result == 0

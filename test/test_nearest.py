import pytest
import numpy as np
from interpolation_package.interpolation_methods import nearest_neighbor_interpolation

def test_nearest_basic():
    """
    Проверка в простом случае из 2х точек.
    """
    x = np.array([0, 10], dtype=float)
    y = np.array([0, 100], dtype=float)
    
    # Точка 4 ближе к 0, значит y должно быть 0
    assert nearest_neighbor_interpolation(x, y, 4) == 0
    # Точка 6 ближе к 10, значит y должно быть 100
    assert nearest_neighbor_interpolation(x, y, 6) == 100

def test_nearest_on_exact_points():
    """
    Если x_new совпадает ровно с одной из исходных точек,
    то результат должен быть y этой точки.
    """
    x = np.array([0, 5, 10], dtype=float)
    y = np.array([0, 50, 100], dtype=float)
    
    assert nearest_neighbor_interpolation(x, y, 0) == 0
    assert nearest_neighbor_interpolation(x, y, 5) == 50
    assert nearest_neighbor_interpolation(x, y, 10) == 100

def test_nearest_array_input():
    """
    Проверяем работу с массивом x_new (несколько точек).
    """
    x = np.array([0, 10], dtype=float)
    y = np.array([0, 10], dtype=float)
    x_new = np.array([1, 8, 9], dtype=float)

    # Точка 1 ближе к 0 => y=0
    # Точка 8 ближе к 10 => y=10
    # Точка 9 тоже ближе к 10 => y=10
    expected = np.array([0, 10, 10], dtype=float)

    result = nearest_neighbor_interpolation(x, y, x_new)
    assert np.allclose(result, expected)

def test_nearest_more_points():
    """
    Больше точек в x, проверяем 'ступенчатость' результата.
    """
    x = np.array([0, 2, 5, 10], dtype=float)
    y = np.array([10, 20, 50, 100], dtype=float)
    
    # Точка 3 ближе к 2 => y=20
    # Точка 4 ближе к 5 => y=50 (или, если одинаково, см. реализацию,
    # но обычно argmin() возвращает первую)
    x_new = np.array([3, 4], dtype=float)
    result = nearest_neighbor_interpolation(x, y, x_new)
    # Тут придётся смотреть вашу реализацию; предположим, 3 ближе к 2, 4 ближе к 5
    expected = np.array([20, 50], dtype=float)
    assert np.allclose(result, expected)

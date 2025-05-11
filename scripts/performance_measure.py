import numpy as np
import timeit
import matplotlib.pyplot as plt
import os
from interpolation_package.interpolation_methods import (
    linear_interpolation,
    nearest_neighbor_interpolation,
    lagrange_interpolation,
)


def measure_time(method, x, y, x_new, repeats=3, number=5):
    stmt = lambda: method(x, y, x_new)
    times = timeit.repeat(stmt, repeat=repeats, number=number)
    return np.mean(times)


def main():
    print("Текущий каталог:", os.getcwd())

    sizes_linear = np.arange(10, 1010, 50)
    sizes_lagrange = np.arange(10, 210, 20)  # меньше точек для Лагранжа

    times_linear = []
    times_nearest = []
    times_lagrange = []

    # Измерение Linear и Nearest neighbor interpolation
    for size in sizes_linear:
        x = np.linspace(0, 10, size)
        y = np.sin(x)
        x_new = np.linspace(0, 10, size * 2)

        t_linear = measure_time(linear_interpolation, x, y, x_new)
        t_nearest = measure_time(nearest_neighbor_interpolation, x, y, x_new)

        times_linear.append(t_linear)
        times_nearest.append(t_nearest)

    # Измерение Lagrange interpolation отдельно с меньшими размерами
    for size in sizes_lagrange:
        x = np.linspace(0, 10, size)
        y = np.sin(x)
        x_new = np.linspace(0, 10, size * 2)

        t_lagrange = measure_time(lagrange_interpolation, x, y, x_new)
        times_lagrange.append(t_lagrange)

    output_dir = os.path.abspath("docs/source/images")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "performance_metrics.png")

    print("Сохраняем файл в:", output_path)

    # Строим график
    plt.figure(figsize=(12, 6))

    plt.plot(sizes_linear, times_linear, '-o', label='Linear interpolation')
    plt.plot(sizes_linear, times_nearest, '-o', label='Nearest neighbor interpolation')
    plt.plot(sizes_lagrange, times_lagrange, '-o', label='Lagrange interpolation')

    plt.xlabel('Number of data points')
    plt.ylabel('Execution time (s)')
    plt.title('Performance comparison of interpolation methods')
    plt.grid(True)
    plt.legend()

    # Сохраняем график
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
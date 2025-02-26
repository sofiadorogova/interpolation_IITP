import argparse
import numpy as np
import matplotlib.pyplot as plt

from interpolation_methods import (
    linear_interpolation,
    nearest_neighbor_interpolation,
    lagrange_interpolation
)


def main():
    """Пример CLI для запуска различных методов интерполяции."""
    parser = argparse.ArgumentParser(
        description="CLI для методов интерполяции (linear, nearest, lagrange)."
    )
    parser.add_argument(
        "--method", 
        choices=["linear", "nearest", "lagrange"], 
        default="linear",
        help="Выбор метода интерполяции."
    )
    parser.add_argument(
        "--n_points", 
        type=int, 
        default=50,
        help="Количество точек, на которых будем вычислять интерполяцию."
    )
    parser.add_argument(
        "--output",
        default="images/interpolation_cli_result.png",
        help="Путь для сохранения результирующего графика."
    )

    args = parser.parse_args()

    # Пример исходных данных
    x_vals = np.array([0, 2, 4, 6, 8, 10], dtype=float)
    y_vals = np.sin(x_vals)

    # Генерируем точки для интерполяции
    x_new = np.linspace(0, 10, args.n_points)

    # Вызываем нужный метод
    if args.method == "linear":
        y_new = linear_interpolation(x_vals, y_vals, x_new)
        label = "Линейная"
    elif args.method == "nearest":
        y_new = nearest_neighbor_interpolation(x_vals, y_vals, x_new)
        label = "Ближайший сосед"
    else:
        y_new = lagrange_interpolation(x_vals, y_vals, x_new)
        label = "Лагранжева"

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, "o", label="Исходные точки")
    plt.plot(x_new, y_new, "-", label=label)
    plt.title(f"Интерполяция методом: {label}")
    plt.legend()
    plt.grid(True)

    plt.savefig(args.output, dpi=300, bbox_inches="tight")
    print(f"График сохранён в файл: {args.output}")
    plt.show()


if __name__ == "__main__":
    main()

#python interpolation_package\cli_interpolation.py --method nearest --n_points 100 --output images/nearest.png
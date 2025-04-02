import click
import matplotlib.pyplot as plt
import numpy as np

from interpolation_package.interpolation_methods import (
    lagrange_interpolation,
    linear_interpolation,
    nearest_neighbor_interpolation,
)


@click.command()
@click.option(
    "--method",
    type=click.Choice(["linear", "nearest", "lagrange"], case_sensitive=False),
    default="linear",
    help="Выбор метода интерполяции (linear, nearest или lagrange).",
)
@click.option(
    "--n_points",
    type=int,
    default=50,
    help="Количество точек, на которых будем вычислять интерполяцию.",
)
@click.option(
    "--output",
    default="images/interpolation_cli_result.png",
    help="Путь для сохранения результирующего графика.",
)
def main(method, n_points, output):
    """
    Пример CLI для запуска различных методов интерполяции.
    Используется библиотека Click вместо argparse.
    """

    x_vals = np.array([0, 2, 4, 6, 8, 10], dtype=float)
    y_vals = np.sin(x_vals)

    x_new = np.linspace(0, 10, n_points)

    method_lower = method.lower()
    if method_lower == "linear":
        y_new = linear_interpolation(x_vals, y_vals, x_new)
        label = "Линейная"
    elif method_lower == "nearest":
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

    plt.savefig(output, dpi=300, bbox_inches="tight")
    click.echo(f"График сохранён в файл: {output}")

    plt.show()


if __name__ == "__main__":
    main()

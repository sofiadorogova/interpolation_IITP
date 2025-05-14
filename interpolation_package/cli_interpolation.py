import os

import click
import matplotlib

if os.environ.get("TESTING", "0") == "1":
    matplotlib.use("Agg")

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
    help="Interpolation method to use (linear, nearest, or lagrange).",
)
@click.option(
    "--n_points",
    type=int,
    default=50,
    help="Number of points to evaluate the interpolation at.",
)
@click.option(
    "--output",
    default="images/interpolation_cli_result.png",
    help="File path to save the resulting plot.",
)
def main(method, n_points, output):
    x_vals = np.array([0, 2, 4, 6, 8, 10], dtype=float)
    y_vals = np.sin(x_vals)

    x_new = np.linspace(0, 10, n_points)

    method_lower = method.lower()
    if method_lower == "linear":
        y_new = linear_interpolation(x_vals, y_vals, x_new)
        label = "Linear"
    elif method_lower == "nearest":
        y_new = nearest_neighbor_interpolation(x_vals, y_vals, x_new)
        label = "Nearest Neighbor"
    else:
        y_new = lagrange_interpolation(x_vals, y_vals, x_new)
        label = "Lagrange"

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, "o", label="Original points")
    plt.plot(x_new, y_new, "-", label=label)
    plt.title(f"Interpolation method: {label}")
    plt.legend()
    plt.grid(True)

    plt.savefig(output, dpi=300, bbox_inches="tight")
    click.echo(f"Plot saved to file: {output}")

    if matplotlib.get_backend() != "Agg":
        plt.show()


if __name__ == "__main__":
    main()

import os

os.environ["TESTING"] = "1"

from click.testing import CliRunner

from interpolation_package.cli_interpolation import main


def test_cli_linear() -> None:
    runner = CliRunner()
    output_path = "tests/test_linear_output.png"
    result = runner.invoke(
        main, ["--method", "linear", "--n_points", "20", "--output", output_path]
    )

    # Проверка что программа завершилась успешно
    assert result.exit_code == 0
    assert "Plot saved to file" in result.output

    # Проверка, что график создан
    assert os.path.exists(output_path)

    # Удаление тестового файла после теста
    os.remove(output_path)


def test_cli_lagrange() -> None:
    runner = CliRunner()
    output_path = "tests/test_lagrange_output.png"
    result = runner.invoke(
        main, ["--method", "lagrange", "--n_points", "20", "--output", output_path]
    )

    assert result.exit_code == 0
    assert "Plot saved to file" in result.output
    assert os.path.exists(output_path)
    os.remove(output_path)


def test_cli_nearest() -> None:
    runner = CliRunner()
    output_path = "tests/test_nearest_output.png"
    result = runner.invoke(
        main, ["--method", "nearest", "--n_points", "20", "--output", output_path]
    )

    assert result.exit_code == 0
    assert "Plot saved to file" in result.output
    assert os.path.exists(output_path)

    os.remove(output_path)

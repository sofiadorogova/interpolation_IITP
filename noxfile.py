import nox
from nox_poetry import Session, session

# Название пакета
PACKAGE = "interpolation_package"

# Сессии, которые будут запускаться по умолчанию при вводе "nox"
nox.options.sessions = ["format", "lint", "tests"]

# Список файлов, где хотим проверять стиль или форматировать
LOCATIONS = [
    "interpolation_package",
    "test",
    "noxfile.py",
]


@session(python="3.10")
def format(session: Session) -> None:
    """
    Запуск автоформатирования Ruff для заданных локаций.
    """
    session.install("ruff")
    # Запуск команды Ruff в режиме форматирования (экспериментальная фича Ruff)
    session.run("ruff", "format", *LOCATIONS)


@session(python="3.10")
def lint(session: Session) -> None:
    """
    Запуск Ruff в режиме линтинга (проверка стиля, unused imports и т.д.).
    """
    session.install("ruff")
    session.run("ruff", "check", *LOCATIONS)


@session(python="3.10")
def tests(session: Session) -> None:
    """
    Запуск тестов через pytest (с установкой зависимостей из Poetry).
    """
    # Устанавливаем проект (локально) и dev-зависимости (pytest и т.п.)
    # nox_poetry автоматически подтянет зависимости из pyproject.toml
    session.install("pytest", "pytest-cov")
    session.install(".")  # Установка текущего пакета (.)

    # Запускаем pytest
    # --cov=PACKAGE  для покрытия, --cov-report=term-missing выводит непокрытые строки
    session.run(
        "pytest",
        "--cov",
        "--cov=interpolation_package",
        "--cov-report=term-missing",
        *session.posargs,  # Позволяет передавать доп. аргументы, если захотим
    )

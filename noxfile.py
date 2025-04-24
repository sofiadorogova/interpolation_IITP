import nox
from nox_poetry import Session, session

PACKAGE = "interpolation_package"

nox.options.sessions = ["format", "lint", "tests", "docs"]

LOCATIONS = [
    PACKAGE,
    "tests",
    "noxfile.py",
]

DOCS_LOCATIONS = ["docs/source"]  # Локации для документов

@session(python="3.10")
def format(session: Session) -> None:
    """Запуск автоформатирования Ruff."""
    session.install("ruff")
    session.run("ruff", "format", *LOCATIONS)

@session(python="3.10")
def lint(session: Session) -> None:
    """Проверка стиля кода и импорта."""
    session.install("ruff")
    session.run("ruff", "check", *LOCATIONS)

@session(python="3.10")
def tests(session: Session) -> None:
    """Запуск тестов через PyTest."""
    session.install(".", "pytest", "pytest-cov")
    session.run("pytest", "--cov", PACKAGE, "--cov-report=term-missing", *session.posargs)

@session(name="docs", python="3.10")
def docs(session: Session) -> None:
    """Сборка документации с помощью Sphinx."""
    session.chdir("docs/")
    session.run("sphinx-build", "-b", "html", "./source", "./build")
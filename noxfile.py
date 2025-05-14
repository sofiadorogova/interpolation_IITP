import nox
from nox_poetry import Session, session

DOCS_DIR = "docs"
TEST_DIR = "tests"
COVERAGE_FILE = ".coverage"

PACKAGE = "interpolation_package"

nox.options.sessions = ["format", "lint", "tests", "docs", "typechecks"]

LOCATIONS = [
    PACKAGE,
    "tests",
    "noxfile.py",
]

DOCS_LOCATIONS = ["docs/source"]


@session(python="3.10")
def format(session: Session) -> None:
    """Запуск автоформатирования Ruff."""
    session.install("ruff")
    session.run("ruff", "format", *LOCATIONS)


@session(python="3.10")
def lint(session: Session) -> None:
    """Проверка и автоматическое исправление стиля кода."""
    session.install("ruff")
    session.run("ruff", "check", "--fix", *LOCATIONS)


@session(python="3.10")
def tests(session):
    """Запуск всех тестов"""
    session.run(
        "pytest",
        TEST_DIR,
        f"--cov={PACKAGE}",
        "--cov-report=term-missing",
        "--cov-report=html",
        "-v",
        env={"COVERAGE_FILE": COVERAGE_FILE},
    )


@nox.session(python="3.10")
def coverage_report(session):
    """Генерация отчета по покрытию тестов"""
    session.install("coverage[toml]")
    session.run("coverage", "report", "-m")
    session.run("coverage", "html", "-d", "htmlcov")


@session(name="docs", python="3.10")
def docs(session: Session) -> None:
    """Сборка документации с помощью Sphinx."""
    session.install("sphinx", "myst-parser", "sphinx-click", "furo")
    session.install(".")
    session.chdir("docs/")
    session.run("sphinx-build", "-b", "html", "./source", "./build")


@session(python="3.10")
def typechecks(session: Session) -> None:
    """Запуск статической проверки типов с помощью mypy."""
    session.install("mypy")
    session.install(".")
    session.run("mypy", "--explicit-package-bases", PACKAGE)

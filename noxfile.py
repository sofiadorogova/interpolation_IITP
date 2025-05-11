import nox
from nox_poetry import Session, session

DOCS_DIR = "docs"
TEST_DIR = "tests"
COVERAGE_FILE = ".coverage"

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
def tests(session):
    """Запуск всех тестов"""
    session.run(
        "pytest",
        TEST_DIR,
        f"--cov={PACKAGE}",
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
    session.chdir("docs/")
    session.run("sphinx-build", "-b", "html", "./source", "./build")

#!/bin/bash
set -euxo pipefail

# Активируем виртуальное окружение Poetry
poetry shell

# Собираем документацию с помощью Nox
nox -s docs
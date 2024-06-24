#!/bin/sh

GO_VERSION=1.22
PYTHON_VERSION=3.12

# brew upgrade allure go

source update.env
cd ..

go mod edit --go="${GO_VERSION}"
go mod tidy

npm update
npm audit fix
npm audit fix --force

pipenv --venv
pipenv --rm
pipenv --venv
rm Pipfile*
pipenv install --python "${PYTHON_VERSION}" &&
    pipenv install pytest allure-pytest pytest-xdist typing-extensions pytest-test-groups --pre &&
    pipenv install python-dotenv pytest-tagging pyhamcrest parameterized --pre &&
    pipenv install --dev pycodestyle pylint pyflakes flake8 yapf autopep8 --pre &&
    pipenv install --dev black isort autoformat autoflake --pre
pipenv lock

dart pub remove test
dart pub remove lints
dart pub upgrade
dart pub add dev:lints
dart pub add dev:test

#!/bin/sh

GO_VERSION=1.22
PYTHON_VERSION=3.12

# brew upgrade allure go

. update.env
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
    pipenv install pytest allure-pytest pytest-xdist typing-extensions pytest-test-gorups --pre &&
    pipenv install python-dotenv pytest-tagging pyhamcrest --pre &&
    pipenv install --dev black autoformat autoflake --pre
pipenv lock

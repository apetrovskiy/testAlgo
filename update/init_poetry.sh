#!/bin/sh

PACKAGE_NAME=main
PACKAGE_FOLDER_NAME=${PROJECT_NAME}
PYTHON_VERSION=3.12

. ./update.env
cd ..

rm -rf ~/Library/Caches/pypoetry/cache
rm -rf ~/.cache/pypoetry/cache/
rm -rf ~/.cache/pypoetry/artifacts/
poetry env remove "python${PYTHON_VERSION}"
poetry env use python3.12
# https://github.com/python-poetry/poetry/issues/1422
# run
# poetry new --src ${PACKAGE_FOLDER_NAME} --name ${PACKAGE_FOLDER_NAME}
# cd ${PACKAGE_FOLDER_NAME} || exit
# then rename ${PACKAGE_FOLDER_NAME} and run
# poetry init --name ${PACKAGE_FOLDER_NAME} --quiet
# finally, merge ${PACKAGE_FOLDER_NAME}/pyproject.toml into ./pyproject.toml,
# namely copy-paste the following:
# packages = [{include = "main", from = "src"}]
# instead of
# packages = [{include = "testalgo", from = "src"}]

poetry add structlog
poetry add --group test pytest allure-pytest pytest-xdist typing-extensions pytest-test-groups --allow-prereleases &&
    poetry add --group test python-dotenv pyhamcrest parameterized --allow-prereleases &&
    poetry add --group dev pycodestyle pylint pyflakes flake8 yapf autopep8 --allow-prereleases &&
    poetry add --group dev black autoformat autoflake --allow-prereleases &&
    poetry add --group dev isort

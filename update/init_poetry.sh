#!/bin/sh

PACKAGE_NAME=main
PACKAGE_FOLDER_NAME=testAlgo
PYTHON_VERSION=3.12

. ./update.env
cd ..

poetry env remove "python${PYTHON_VERSION}"
rm -rf ~/Library/Caches/pypoetry/cache
poetry env use python3.12
# https://github.com/python-poetry/poetry/issues/1422
# run
# poetry new --src ${PACKAGE_FOLDER_NAME} --name ${PACKAGE_NAME}
# cd ${PACKAGE_FOLDER_NAME} || exit
# then rename ${PACKAGE_FOLDER_NAME} and run
# poetry init --name ${PACKAGE_NAME} --quiet
# finally, merge ${PACKAGE_FOLDER_NAME}/pyproject.toml into ./pyproject.toml,
# namely copy-paste the following:
# packages = [{include = "main", from = "src"}]

poetry add structlog
poetry add --group test pytest allure-pytest pytest-xdist typing-extensions pytest-test-groups --allow-prereleases &&
    poetry add --group test python-dotenv pyhamcrest parameterized --allow-prereleases &&
    poetry add --group dev pycodestyle pylint pyflakes flake8 yapf autopep8 --allow-prereleases &&
    poetry add --group dev black autoformat autoflake --allow-prereleases &&
    poetry add --group dev isort

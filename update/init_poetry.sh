#!/bin/sh

PACKAGE_NAME=app
PACKAGE_FOLDER_NAME=testAlgo

. ./update.env
cd ..

poetry new --src ${PACKAGE_FOLDER_NAME} --name ${PACKAGE_NAME}
cd ${PACKAGE_FOLDER_NAME} || exit

poetry add structlog
poetry add --group dev black flake8 isort mypy pylint
poetry add --group test pytest

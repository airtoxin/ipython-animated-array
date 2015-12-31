#!/usr/bin/env bash

pandoc -f markdown -t rst README.md > README.rst

python setup.py sdist # create compressed source file
python setup.py bdist_wheel # create wheel file

# test pypi upload
python setup.py register -r https://testpypi.python.org/pypi
python setup.py sdist upload -r https://testpypi.python.org/pypi

# install from test pypi
# pip install --index-url https://testpypi.python.org/simple/ pysqldf

# pypi upload
# python setup.py register
# twine upload dist/*

#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='ipython-array-animation',
    version='0.0.1',
    description='',
    long_description=long_description,
    author='Ryoji Ishii',
    author_email='airtoxin@icloud.com',
    url='https://github.com/airtoxin/ipython-array-animation',
    packages=['ipython-array-animation'],
    package_dir={'ipython-array-animation': 'src'}
    classifiers=[],
    install_requires=[]
)

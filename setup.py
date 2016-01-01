#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='ipython-array-animation',
    version='0.0.1',
    description='animated array rendering on ipython-notebook (jupyter)',
    long_description=long_description,
    author='Ryoji Ishii',
    author_email='airtoxin@icloud.com',
    url='https://github.com/airtoxin/ipython-array-animation',
    packages=['ipython-array-animation'],
    package_dir={'ipython-array-animation': 'src'}
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: IPython',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    install_requires=[
        'jinja2'
        'vizarray',
        'ipythonblocks', # vizarray dependency
        'numpy', # vizarray dependency
        'matplotlib<1.5', # vizarray dependency
    ]
)

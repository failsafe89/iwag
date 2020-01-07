#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='iwag',
    version=0.1,
    scripts=[],
    author='failsafe89',
    author_email='',
    description='(I Want A Gui) Cross platform, pure python GUI library built on top of pydish',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/failsafe89/iwag',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Natural Language :: English",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script"""

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

test_requirements = [
    'codecov',
    'pytest',
    'pytest-cov',
]

setup(
    name='neural_net_cell_segmenter',
    version='0.0.1',
    url='https://github.com/NilaiVemula/neural_net_cell_segmenter',
    license='MIT',
    author='Nilai Vemula',
    author_email='nilai.r.vemula@vanderbilt.edu',
    description='https://github.com/NilaiVemula/neural_net_cell_segmenter',
    long_description=readme,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    package_data={'neural_net_cell_segmenter': ['*', '*/*', '*/*/*', '*/*/*/*', '*/*/*/*/*']},  # find some other way
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Natural Language :: English"
    ],
    test_suite='tests',
    tests_require=test_requirements,
)

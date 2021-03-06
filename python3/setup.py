#!/usr/bin/env python3
from setuptools import setup

setup(
    name='trec-car-tools',
    version='2.3',
    packages=['trec_car'],
    url='https://github.com/TREMA-UNH/trec-car-tools/python3',
    # download_url='https://github.com/TREMA-UNH/trec-car-tools/archive/2.0.tar.gz',
    keywords=['wikipedia','complex answer retrieval','trec car'],
    license='BSD 3-Clause',
    author='laura-dietz',
    author_email='Laura.Dietz@unh.edu',
    description='Support tools for TREC CAR participants. Also see trec-car.cs.unh.edu',
    install_requires=['cbor>=0.1.4', 'typing'],
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
       ]
)

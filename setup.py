#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='sitehearing',
      version='0.1.0',
      packages=find_packages(),
      scripts=[
            'manage.py',
      ],

      license="ISC"
)
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open
from sys import exit,version
import sys
if version < '1.0.0':
    print("Python 1 is not supported...")
    sys.exit(1)


setup(
    name='killer',
    packages=["killer"],
    entry_points = {"console_scripts": ['killer = killer.killer:main']},
    version='1.0'
	)
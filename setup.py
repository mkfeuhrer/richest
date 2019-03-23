try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

from codecs import open
from os import path

if sys.version < '3.5.1':
    print("Supports only Python >= 3.5.1")
    sys.exit(1)

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='richest',
      version='1.0.1',
      description='A Python package for getting list of Richest people in the world',
      url='https://github.com/mkfeuhrer/richest',
      entry_points={'console_scripts': ['richest = richest.__main__:main']},
      keywords=['richest', 'programming language ranking', 'index', 'programming language','forbes'],
      author='Mohit Khare (mkfeuhrer)',
      author_email='mohitfeuhrer@gmail.com',
      license='MIT',
      packages=['richest'],
      install_requires=[
          'requests',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown')

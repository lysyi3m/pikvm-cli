from setuptools import setup, find_packages
from io import open
from os import path

import pathlib

with open(path.join(pathlib.Path(__file__).parent, 'README.md'), 'r', encoding='utf-8') as f:
  long_description = f.read()

with open(path.join(pathlib.Path(__file__).parent, 'requirements.txt'), 'r', encoding='utf-8') as f:
  install_requires = f.read().splitlines()

setup(
  name='pikvm-cli',
  version='1.0.1',
  author='Emil Kashkevich',
  author_email='emil.kashkevich@gmail.com',
  description='CLI tool for managing PIKVM device',
  long_description=long_description,
  long_description_content_type='text/markdown',
  license='MIT',
  url='https://github.com/lysyi3m/pikvm-cli',
  packages=find_packages(),
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
  install_requires=install_requires,
  entry_points={
    'console_scripts': [
      'pikvm-cli=pikvm_cli.__main__:main',
    ]
  },
)

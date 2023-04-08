from setuptools import setup, find_packages
from io import open

with open('README.md', 'r') as f:
  long_description = f.read()

with open('requirements.txt') as f:
  install_requires = f.read().splitlines()

setup(
  name='pikvm-cli',
  version='1.0.0',
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

# Python wrapper for Allure framework

This python module contains wrapper that allows to automatically install last version of [Allure 2](https://github.com/allure-framework/allure2) framework and make reports.

### Installation
With pip:

`$ pip install git+https://github.com/grmmvv/allure-commandline-python.git`

Or with [pipenv](https://pipenv.kennethreitz.org/en/latest/):

`$ pipenv install -e git+https://github.com/grmmvv/allure-commandline-python.git@master#egg=allure-commandline-python`

### Usage

```python

from allure_commandline_python import AllureCLI

if __name__ == '__main__':
    AllureCLI().generate()

```

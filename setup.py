from setuptools import setup

PACKAGE = 'allure-commandline-python'
VERSION = '0.0.3'

install_requires = [
    'requests>=2.22.0'
]

setup(
    name=PACKAGE,
    version=VERSION,
    packages=['allure_commandline_python'],
    package_dir={'allure_commandline_python': 'src'},
    install_requires=install_requires,
    url='https://github.com/grmmvv/allure-commandline-python',
    license='unlicense',
    author='Max Gribennikov',
    author_email='grmmvv@gmail.com',
    description='Wrapper around allure-commandline'
)
